from table import Table
from converter import Converter

table = Table()
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

def __main__():
    conveter.setTargets(targets)
    if not conveter.convert_targets():
        print("target is not converted")
        exit(-1)
    ## 탐색적 데이터 분석 과정 ##
    # 표를 이용한 분석 과정
    # 1. 대륙별 ipv6 가능 비율 / 2. 대륙 하위 지역별 ipv6가능 비율 (ex : 동아시아와, 서유럽) / 3.국가별 ipv6가능 비율
    # 1. 대륙별 ipv6 가능 비율
    
    

__main__()