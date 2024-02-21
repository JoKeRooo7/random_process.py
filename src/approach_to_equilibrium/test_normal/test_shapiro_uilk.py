import pandas as pd
from scipy.stats import shapiro

data = pd.read_csv('../../../datasets/unstable_equilibrium_data_1.csv')

# Проверка нормальности данных для каждой колонки
for column in data.columns:
    stat, p = shapiro(data[column])
    print(f'Для колонки {column}:')
    print(f'Статистика теста: {stat}')
    print(f'p-значение: {p}')
    if p > 0.05:
        print('Распределение данных не отличается от нормального')
    else:
        print('Распределение данных отличается от нормального')
    print()

