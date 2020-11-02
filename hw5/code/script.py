import argparse
import pandas as pd
from pandas.core.frame import DataFrame
from tqdm import tqdm

from builders.posgre_orm_builder import PostgreOrmBuilder
from postgre_client.orm_client import PostgreOrmClient


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inpath', required=True, type=argparse.FileType(mode='r'))

    parser.add_argument('-H', '--host', default='127.0.0.1')
    parser.add_argument('-p', '--port', default=5432)
    parser.add_argument('-d', '--dbname', default='logs')

    parser.add_argument('-u', '--username', default='postgres')
    parser.add_argument('-P', '--password', required=True)
    return parser


def count_url(df, req: str) -> int:
    return len(df[df['req'] == req])


def count_req(df):
    req_post = len(df[df['req'].str.contains("POST")])
    req_get = len(df[df['req'].str.contains('GET')])
    return req_get, req_post, req_get + req_post


def top_ten(df, col: str) -> DataFrame:
    sorted_10_by_col = df.sort_values(col, ascending=False).head(10)
    return sorted_10_by_col


def code_eq(df, code_min: int, code_max: int) -> DataFrame:
    result = df[(df['code'] >= code_min) & (df['code'] < code_max)]
    return result


def unq(df, col: str):
    return df[col].unique()


def get_url(req: str) -> str:
    return req.split(sep=' ')[1]


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()

    logs = namespace.inpath
    host = namespace.host
    port = namespace.port
    username = namespace.username
    password = namespace.password
    dbname = namespace.dbname

    client = PostgreOrmClient(username, password, dbname, host, port)
    builder = PostgreOrmBuilder(client)

    df = pd.read_csv(logs, sep=' ', header=None,
                     names=['ip', '1', '2', 'time', 'utc', 'req', 'code', 'size', '3', 'user-agent', '4'])
    convert_dict = {'ip': str, 'req': str, 'code': int, 'size': int}
    df = df[df['size'] != '-']
    df = df.astype(convert_dict)

    get, post, sum = count_req(df)

    builder.add_CountOfReq(get, post, sum)

    top_ten_size = top_ten(df, 'size')
    req_and_trash = top_ten_size[['req', 'code', 'size']].to_string().split('\n')
    req_and_trash.pop(0)
    req = []
    for row in req_and_trash:
        req.append(row.split('  ')[1:])

    for row in req:
        builder.add_TopTenSize(row[0], int(row[1]), int(row[2]))

    code_error = code_eq(df, 400, 500)
    r = unq(code_error, 'req')
    third = DataFrame(columns=['count', 'req'])
    for u in tqdm(r):
        third.loc[len(third)] = [count_url(df, u), u]

    top_ten_with_user_error_tmp = top_ten(third, 'count')

    top_ten_tmp = top_ten_with_user_error_tmp[['count', 'req']].to_string().split('\n')
    top_ten_tmp.pop(0)
    top_ten_with_user_error = []

    for row in top_ten_tmp:
        res = " ".join(row.split(maxsplit=2))
        top_ten_with_user_error.append(res.split(maxsplit=2)[1:])

    for row in top_ten_with_user_error:
        builder.add_TopTenCountWithUserError(row[1], row[0])

    top_ten_size_with_server_error = top_ten(code_eq(df, 500, 600), 'size')
    req_top_ten_tmp = top_ten_size_with_server_error['req'].to_list()
    code_top_ten_tmp = top_ten_size_with_server_error['code'].to_list()
    size_top_ten_tmp = top_ten_size_with_server_error['size'].to_list()

    for req, code, size in zip(req_top_ten_tmp, code_top_ten_tmp, size_top_ten_tmp):
        builder.add_TopTenSizeWithServerError(req, int(code), int(size))
