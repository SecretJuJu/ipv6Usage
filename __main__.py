from table import Table

table = Table()

DATAFOLDER="./datas"
HTMLFOLDER=DATAFOLDER+"/htmls"
CSVFOLDER=DATAFOLDER+"/csvs"

targets = [
    {
    "input": HTMLFOLDER+"/국가별_ipv6_가능_비율.html",
    "output": CSVFOLDER+"/국가별_ipv6_가능_비율.csv"
    }
]


data = pd.read_csv("./datas/csvs/국가별_ipv6_가능_비율(대륙별).csv")
print(data)