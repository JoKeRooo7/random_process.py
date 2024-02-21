import pandas as pd
from scipy.stats import ks_2samp

data = pd.read_csv('../../../datasets/unstable_equilibrium_data_1.csv')

# Проверка нормальности данных для каждой колонки
for column in data.columns:
    for other_column in data.columns:
        if other_column != column:
            stat_ks, p_ks = ks_2samp(data[column], data[other_column])
            print(f'Для колонок {column} и {other_column}:')
            print(f'Статистика теста Колмогорова-Смирнова: {stat_ks}')
            print(f'p-значение Колмогорова-Смирнова: {p_ks}')
            if p_ks > 0.05:
                print('Распределения данных не отличаются')
            else:
                print('Распределения данных отличаются')
            print()

