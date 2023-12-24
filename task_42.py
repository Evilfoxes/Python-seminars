'''
Узнать какая максимальная households в зоне минимального значения population
'''

import pandas as pd

df = pd.read_csv('california_housing_train.csv')
max_households_in_min_population = df[df['population']==df['population'].min()]['households'].max()