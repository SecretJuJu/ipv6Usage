from converter import Converter
import pandas as pd
import os

conveter = Converter()

DATAFOLDER="./datas"
HTMLFOLDER=DATAFOLDER+"/htmls"
CSVFOLDER=DATAFOLDER+"/csvs"

targets = [
    {
    "input": HTMLFOLDER+"/국가별_ipv6_가능_비율.html",
    "output": CSVFOLDER+"/국가별_ipv6_가능_비율.csv"
    }
]

def align_center(value):
    # value : string
    return value.center(os.get_terminal_size().columns)

def display_CSV(csv_path,sort=None):
    data = pd.read_csv(csv_path)
    if sort is not None:
        data = data.sort_values(by=sort["column"] ,ascending=sort["ascending"])
    print(data.to_string(justify="center"))


def __main__():
    conveter.setTargets(targets)
    if not conveter.convert_targets():
        print("target is not converted")
        exit(-1)
    ## 탐색적 데이터 분석 과정 ##
    # 표를 이용한 분석 과정
    # 1. 대륙별 ipv6 가능 비율 / 2. 대륙 하위 지역별 ipv6가능 비율 (ex : 동아시아와, 서유럽) / 3.국가별 ipv6가능 비율
    table_names = ["대륙별 ipv6 가능 비율","대륙 하위 지역별 ipv6가능 비율","국가별 ipv6가능 비율"]
    # 1. 대륙별 ipv6 가능 비율
    # get csv list from csv directory
    i = 0
    for csv_name  in os.listdir(CSVFOLDER):
        path = CSVFOLDER+"/"+csv_name
        print(align_center("========== {} ==========".format(table_names[i])) )
        display_CSV(csv_path=path,sort={"column":"IPv6 Capable","ascending":False})
        i+=1



__main__()