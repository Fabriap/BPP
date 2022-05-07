import  pandas as pd
import re

def abrirArchivo():
    df = pd.read_csv('finanzas2020.csv',sep='\t',dtype=str)
    return df

def validarColumnas(df):
    return list(df.columns)

def validarNumeroColumnas(df,n):
    assert len(df.columns) == n
    return True

def validarCampos(df,columns,ex=0):
    validar = True
    count = 0
    while True:
        for n,c in enumerate(columns):
            if re.search(r'^([0-9]|-)',str(df.iloc[count,n])):
                df.iloc[count,n] =float(str(df.iloc[count,n]).replace("'",''))
            else:
                if ex==0:
                    df.iloc[count,n] = 0
                else: validar = False
        count += 1
        if count == df.shape[0]:break
    return validar

