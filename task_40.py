'''
Работать с файлом california_housing_train.csv, который находится в папке
sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
'''

import pandas as pd
df = pd.read_csv('sample_data/california_housing_train.csv')
avg = df[(df['population'] < 500)&
         (df['population'] > 0)]['medianHouseValue'].mean()
print(avg)
