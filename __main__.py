from TableConverter import TableConverter
from converter import Converter
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import platform

if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic') 
elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic') 
elif platform.system() == 'Linux': #리눅스
        plt.rc('font', family='Malgun Gothic') 


conveter = Converter()
tableConverter = TableConverter()

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
    csvs = os.listdir(CSVFOLDER)
    csvs.sort()
    
    i = 0
    tables = []
    
    
    sort_key = "IPv6 Capable"
    for csv_name  in csvs:
        path = CSVFOLDER+"/"+csv_name
        print(align_center("========== {} ==========".format(table_names[i])) )
        data = pd.read_csv(path)
        tableConverter.convert_percent_to_float(data,sort_key)
        tables.append(data)

        pd.to_numeric(data[sort_key])
        
        data = data.sort_values(by=sort_key ,ascending=False)
        tableConverter.convert_float_to_percent(data,sort_key)
        print(data)
        i+=1
        
    # 그래프를 이용한 분석 과정
    # World column 제거
    regions = tables[0]['Region'].tolist()
    i = 0
    for region in regions:
        if region == "World":
            regions.pop(i)
            break
        i+=1
        
    capables = tables[0]['IPv6 Capable'].tolist()
    capables.pop(i)
    x = np.arange(len(regions))
    plt.bar(x, capables)
    plt.xticks(x, regions)
    plt.yticks(capables)
    plt.grid(True)
    plt.title('대륙별 IPv6도입률')
    plt.show()

    # 대륙 하위 지역별 ipv6가능 비율
    
    subRegions_Dict = {
        "Asia" : [],
        "Europe" : [],
        "Americas" : [],
        "Africa" : [],
        "Oceania" : []
    }
    
    subRegions = tables[1]['SubRegion'].tolist()
    subRegion_per_samples = tables[1]['Samples'].tolist()
    i = 0
    for subRegion in subRegions:
        subRegions_Dict[subRegion.split(",")[1]].append({
            "samples": int(subRegion_per_samples[i].replace(",", "")),
            "subRegion": subRegion
        })
        i+=1

    
    x = []
    samples = []
    sample_max = 0
    i = 0
    for r in subRegions_Dict.keys():
        for sr in subRegions_Dict[r]:
            samples.append(sr["samples"])
            if (sr["samples"] > sample_max) : sample_max = sr["samples"]
            x.append(sr["subRegion"])
            plt.text(i,sr["samples"],sr["samples"],
                fontsize = 10, 
                color='black',
                horizontalalignment='center',  # horizontalalignment (left, center, right)
                ) 
            i+=1
    y = np.arange(0,len(x))
    
    plt.title("대륙 하위 지역별 Ipv6 보급 개수")
    plt.grid(True)
    # plt.axis([0, len(x),-1,len(y)])
    plt.xticks(rotation=90)
    plt.bar(x, samples,width=0.5)
    
    plt.show()

    # IPv6 사용 가능 비율 비교 ( 한국, 인도 )    
    Korea = tables[2][tables[2]["CC"]=="KR"].to_dict()
    India = tables[2][tables[2]["CC"]=="IN"].to_dict()
    labels = ["ipv6 가능","ipv6 불가능"]
    
    
    plt.subplot(2,1,1)
    plt.title("IPv6 도입률 비교 ( 한국 )")
    _, v = Korea["IPv6 Capable"].popitem()
    plt.pie([v,1-v], labels=labels, autopct='%.1f%%')

    plt.subplot(2,1,2)
    plt.title("IPv6 도입률 비교 ( 인도 )")
    _, v = India["IPv6 Capable"].popitem()
    plt.pie([v,1-v], labels=labels, autopct='%.1f%%')
    plt.show()

__main__()