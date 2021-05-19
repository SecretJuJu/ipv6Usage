import pandas as pd

class TableConverter():
    def convert_percent_to_float(self,df,columnName):
        df[columnName] = df[columnName].str.rstrip('%').astype('float') / 100.0
    def convert_float_to_percent(self,df,columnName):
        df[columnName] = pd.to_numeric(df[columnName], errors='coerce').fillna(0).map("{:.2%}".format)
