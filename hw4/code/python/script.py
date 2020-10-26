from enum import unique
from re import split
from pandas.core.frame import DataFrame
import pyparsing
import sys
import argparse
import re
import pandas as pd
import numpy as np

from pyparsing import line

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-p' , '--path', required=True, type=argparse.FileType(mode='r'))
    parser.add_argument ('-o' , '--out' , type=argparse.FileType(mode='w'))
    return parser    

# TODO: Переделать на регулярку если получиться
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



def unq(df, col:str) -> list:
    return df[col].unique()

def get_url(req: str) -> str:
    return req.split(sep=' ')[1]

if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()

    logs = namespace.path

    df = pd.read_csv(logs, sep=' ', header=None , names=['ip', '1', '2' , 'time', 'utc', 'req', 'code', 'size', '3', 'user-agent', '4' ])
    conver_dict = {'ip' : str, 'req' : str, 'code' : int, 'size' : int}
    df = df[df['size'] != '-']
    df = df.astype(conver_dict)
    print(df.dtypes)
    print(len(df))
    print(df)
    # print(df['ip'].to_list())

    # print(df[df['code'] == 200])

    print(count_req(df))
    print(top_ten(df, 'size'))

    c = code_eq(df,300, 400)
    r = unq(c,'req')
    theard = DataFrame(columns=['count','req'])

    for u in r:
        theard.loc[len(theard)] = [count_url(df,u),u]

    print(top_ten(theard, 'count'))
    print(unq(df,'size'))
    print(df)
    print(df.sort_values('size', ascending=False))

    s = code_eq(df,400, 500)
    print(top_ten(s,'size'))
    # TODO: Доделать скрипт, базовые функции вроде готовы