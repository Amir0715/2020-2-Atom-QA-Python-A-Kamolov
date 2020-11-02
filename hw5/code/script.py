import argparse
import pandas as pd
from pandas.core.frame import DataFrame
from tqdm import tqdm
from code.postgre_client.orm_client import PostgreOrmClient
from code.builders.posgre_orm_builder import PostgreOrmBuilder

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-p' , '--path', required=True, type=argparse.FileType(mode='r'))
    
    parser.add_argument ('-h' , '--host', default='127.0.0.1')
    parser.add_argument ('-p' , '--port', default=5432)
    parser.add_argument ('-d' , '--dbname' , default='logs')

    parser.add_argument ('-u' , '--username', default='postgres')
    parser.add_argument ('-P' , '--password' , required=True)
    return parser

def count_url(df, req : str) -> int:
    return len(df[df['req'] == req])

def count_req(df):
    req_post = len(df[df['req'].str.contains("POST")])
    req_get = len(df[df['req'].str.contains('GET')])
    return req_get , req_post , req_get+req_post

def top_ten(df, col:str) -> DataFrame:
    sorted_10_by_col = df.sort_values(col, ascending=False).head(10)
    return sorted_10_by_col

def code_eq(df, code_min : int, code_max: int) -> DataFrame:
    result = df[(df['code'] >= code_min ) & ( df['code'] < code_max ) ]
    return result

def unq(df, col:str):
    return df[col].unique()

def get_url(req: str) -> str:
    return req.split(sep=' ')[1]




if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()
    
    
    logs = namespace.path
    host = namespace.host
    port = namespace.port
    username = namespace.username
    password = namespace.password
    dbname = namespace.dbname


    client = PostgreOrmClient(username,password,dbname,host,password)
    builder = PostgreOrmBuilder(client)

    df = pd.read_csv(logs, sep=' ', header=None , names=['ip', '1', '2' , 'time', 'utc', 'req', 'code', 'size', '3', 'user-agent', '4' ])
    conver_dict = {'ip' : str, 'req' : str, 'code' : int, 'size' : int}
    df = df[df['size'] != '-']
    df = df.astype(conver_dict)

    get , post , sum = count_req(df)

    builder.add_CountOfReq(get,post,sum)

    top_ten_size = top_ten(df, 'size')
    
    for row in top_ten_size:
        str = row[['req', 'code', 'size']].to_string()
        builder.add_TopTenSize(row['req'], row['code'],row['size'])
        print(str)

    code_error = code_eq(df,400, 500)
    r = unq(code_error,'req')
    theard = DataFrame(columns=['count','req'])
    for u in tqdm(r):
        theard.loc[len(theard)] = [count_url(df,u),u]

    top_ten_with_user_error = top_ten(theard, 'count')


    for row in top_ten_with_user_error:
        str = row.to_string
        builder.add_TopTenCountWithUserError(row['req'],row['count'])
        print(str)

    top_ten_size_with_server_error = top_ten(code_eq(df,500, 600),'size')

    for row in top_ten_size_with_server_error:
        builder.add_TopTenSizeWithServerError(row['req'],row['code'],row['size'])
