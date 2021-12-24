#Сколько образцов разных видов стекла в таблице?
import pandas as pd
import numpy as np
df = pd.read_csv('glass.csv')

q = df['Type'].value_counts()
print(q)

#Найдите средние значения химических параметров для каждого типа стекла
df.groupby('Type').mean()
print(df.groupby('Type').mean())

#Найдите максимальную разницу между содержанием Si разных типов стекла. Постройте квадратную таблицу, в которой столбцы и строки - типы стекла, а в ячейках будут находиться значения абсолютной разницы.
x = df.groupby('Type').max().Si
y = df.groupby('Type').min().Si
print(x-y)

df1 = pd.DataFrame([['buildingwindowsfloatprocessed', 2.35],
                    ['buildingwindowsnonfloatprocessed', 4.64],
                    ['containers', 3.99],
                    ['headlamps', 4.92],
                    ['tableware', 3.04],
                    ['ehiclewindowsfloatprocessed', 1.65]],
                    columns = ['Type_new','Si_difference'])
print(df1)

#Как часто Барий(Ba) используется(>0) вместе с Магнием(Mg)(>0)?
z = df[(df['Ba'] > 0) & (df['Mg'] > 0)]
print('Барий используется вместе с магнием:', len(z))

#Правда ли, что в стекле, которое используют для посуды(tableware), в среднем меньше кальция(Ca), чем в стекле для окон(Тип начинается с building window)?
t = df[df['Type'] == 'tableware']
w = pd.concat([df[df['Type'] == 'buildingwindowsfloatprocessed'], df[df['Type'] == 'buildingwindowsnonfloatprocessed']], ignore_index=True)
if t['Ca'].mean()>w['Ca'].mean():
    print('Кальция больше в')
    print('Tableware')
else:
    print('Windows')
 
#Ri - Refractive index - коэффициент преломления. Расположите другие химические параметры по убыванию корреляции с Ri.
n = df['RI'].corr(df['Na'])
m = df['RI'].corr(df['Mg'])
a = df['RI'].corr(df['Al'])
s = df['RI'].corr(df['Si'])
k = df['RI'].corr(df['K'])
c = df['RI'].corr(df['Ca'])
b = df['RI'].corr(df['Ba'])
f = df['RI'].corr(df['Fe'])
correlation = [n, m, a, s, k, c, b, f]
correlation.sort(reverse = True)
print('Корреляция RI и химических параметров поубыванию:', correlation)

#Сколько образцов одновременно имеют Ri и Na больше медианной?
RIM = df['RI'].median()
NaM = df['Na'].median()
med = df[(df['RI'] > RIM) & (df['Na'] > NaM)]

print('количество образцов одновременно:', len(med))

#Разделите типы стекол windows по подтипам, каждый отдельный подтип вынесите в отдельную колонку в виде индикатора. Например, если в столбце Type есть building, то добавить столбец building и для таких значений поставить 1, в иных случаях - 0.

df.loc[:, 'vehicle'] = 0
df.loc[:, 'building'] = 0
for i in range(len(df)):
    if df.Type[i] == 'vehiclewindowsfloatprocessed':
        df.loc[i, 'vehicle'] = 1
    if df.Type[i] == 'buildingwindowsfloatprocessed' or df.Type[i] == 'buildingwindowsnonfloatprocessed':
        df.loc[i, 'building'] = 1
print(df)
