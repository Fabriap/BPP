import plotly.express as px
import pandas as pd
from tqdm import tqdm
import operator


def comprobacion(row):
    for month in months:
        if row[month] == '':
            print('Hay una elemento que no tiene contenido')
    return row

def clean(row):
    try:
        row['Enero'] = float(row['Enero'].replace("'",''))
    except ValueError:
        row['Enero'] = 0
    try:
        row['Febrero'] = float(row['Febrero'].replace("'",''))
    except ValueError:
        row['Febrero'] = 0
    try: 
        row['Marzo'] = float(row['Marzo'].replace("'",''))
    except ValueError:
        row['Marzon'] = 0
    try: 
        row['Abril'] = float(row['Abril'].replace("'",''))
    except ValueError:
        row['Abril'] = 0
    try: 
        row['Mayo'] = float(row['Mayo'].replace("'",''))
    except ValueError:
        row['Mayo'] = 0
    try: 
        row['Junio'] = float(row['Junio'].replace("'",''))
    except ValueError:
        row['Junio'] = 0
    try: 
        row['Julio'] = float(row['Julio'].replace("'",''))
    except ValueError:
        row['Julio'] = 0
    try: 
        row['Agosto'] = float(row['Agosto'].replace("'",''))
    except ValueError:
        row['Agosto'] = 0
    try: 
        row['Septiembre'] = float(row['Septiembre'].replace("'",''))
    except ValueError:
        row['Septiembre'] = 0
    try: 
        row['Octubre'] = float(row['Octubre'].replace("'",''))
    except ValueError:
        row['Octubre'] = 0
    try: 
        row['Noviembre'] = float(row['Noviembre'].replace("'",''))
    except ValueError:
        row['Noviembre'] = 0
    try: 
        row['Diciembre'] = float(row['Diciembre'].replace("'",''))
    except ValueError:
        row['Diciembre'] = 0
    
    return row

def create_dictionaries():
    dictionary = {}
    for month in months:
        dictionary[month] = 0
    return dictionary

def gastos(row):
    for month in months:
        if row[month] < 0:
            gastos_dictionary[month] += row[month]
    return row

def ahorros(row):
    for month in months:
        ahorro_dictionary[month] += row[month]
    return row

def gastosMedia():
    contador = 0
    for month in months:
        contador += gastos_dictionary[month]
    return ((contador/12)*(-1)),contador

def ingresos(row):
    for month in months:
        if row[month] > 0:
            ingresos_dictionary[month] += row[month]
            
    return row

def ingresosTotales():
    contador = 0
    for month in months:
        contador += ingresos_dictionary[month]
    return contador


df = pd.read_csv('finanzas2020.csv',sep='\t',dtype=str)

assert(len(df.columns)==12)

months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio',
         'Agosto','Septiembre','Octubre','Noviembre','Diciembre']
df = df.apply(lambda x:comprobacion(x),axis = 1)

tqdm.pandas(ncols=100,desc='NORMALIZING: ')
df = df.progress_apply(lambda x: clean(x),axis = 1)

gastos_dictionary = create_dictionaries()
ahorro_dictionary = create_dictionaries()
ingresos_dictionary = create_dictionaries()

df = df.apply(lambda x: gastos(x),axis = 1)

key = min(gastos_dictionary.items(), key=operator.itemgetter(1))[0]
print('Mes con mas gastos:',key)

df = df.apply(lambda x: ahorros(x),axis = 1)
key = max(ahorro_dictionary.items(), key=operator.itemgetter(1))[0]
print('Mes con mas Ahorros:',key)

media,gastos_anuales = gastosMedia()

print('Media de gastos anuales:',media)
print('Gastos anuales:',gastos_anuales)


df = df.apply(lambda x: ingresos(x),axis = 1)
ingresos_totales = ingresosTotales()

print('Ingresos Totales:',ingresos_totales)

df_new = pd.DataFrame({
    'meses': months, 'ingresos':list(ingresos_dictionary.values())
})

fig = px.line(df_new, x='meses', y="ingresos", title = 'INGRESOS TOTALES')
fig.show()