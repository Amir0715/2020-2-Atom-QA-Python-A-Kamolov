#! /usr/bin/python3.8
import json
import argparse
import pandas as pd
from pandas.core.frame import DataFrame
from tqdm import tqdm

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-p' , '--path', required=True, type=argparse.FileType(mode='r'))
    parser.add_argument ('-o' , '--out' , type=argparse.FileType(mode='w'), default='result')
    parser.add_argument ('-j' , '--jsonFlag' , type=bool, default=False)
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
    result = namespace.out
    jsonFlag = namespace.jsonFlag

    df = pd.read_csv(logs, sep=' ', header=None , names=['ip', '1', '2' , 'time', 'utc', 'req', 'code', 'size', '3', 'user-agent', '4' ])
    conver_dict = {'ip' : str, 'req' : str, 'code' : int, 'size' : int}
    df = df[df['size'] != '-']
    df = df.astype(conver_dict)

    get , post , sum = count_req(df)

    if not jsonFlag:
        result.write('Count of get req: {} \n'.format(get))
        result.write('\n===')
        result.write('Count of post req: {} \n'.format(post))
        result.write('\n===')
        result.write('Count of all req: {} \n'.format(sum))
        result.write('\n===')
    else:
        count_of_req = {
                "count" : 
                    {
                    "get" : get,
                    "post" : post,
                    "all" : sum
                    }
                }
        with open("count_of_req.json", "w") as write_file:
            json.dump(count_of_req, write_file)

    top_ten_size = top_ten(df, 'size')

    if not jsonFlag:
        result.write(top_ten_size[['req', 'code', 'size']].to_string())
        result.write('\n===')
    else:
        top_ten_size_json = top_ten_size[['req', 'code', 'size']].to_json(orient="records")
        with open("top_ten_size.json", "w") as write_file:
            json.dump(top_ten_size_json, write_file)

    code_error = code_eq(df,400, 500)
    r = unq(code_error,'req')
    theard = DataFrame(columns=['count','req'])
    for u in tqdm(r):
        theard.loc[len(theard)] = [count_url(df,u),u]

    if not jsonFlag:
        result.write(top_ten(theard, 'count').to_string())
        result.write('\n===')
    else:
        top_ten_count_json = top_ten(theard, 'count').to_json(orient="records")
        with open("top_ten_count.json", "w") as write_file:
            json.dump(top_ten_count_json, write_file)

    s = code_eq(df,500, 600)

    if not jsonFlag:
        result.write(top_ten(s,'size')[['req','size','code']].to_string())
        result.write('\n===')
    else:
        top_ten_size_and_server_error = top_ten(s,'size')[['req','size','code']].to_json(orient="records")
        with open("top_ten_size_and_server_error.json", "w") as write_file:
            json.dump(top_ten_size_and_server_error, write_file)