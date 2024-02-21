import pandas as pd
from scipy.stats import anderson

data = pd.read_csv('../../../datasets/unstable_equilibrium_data_1.csv')

# Проверка нормальности данных для каждой колонки
for column in data.columns:
    result_anderson = anderson(data[column])
    print(f'Для колонки {column}:')
    print(f'Статистика теста Андерсона-Дарлинга: {result_anderson.statistic}')
    print(f'Критические значения: {result_anderson.critical_values}')
    print(f'Уровни значимости: {result_anderson.significance_level}')
    if result_anderson.statistic < result_anderson.critical_values[2]:
        print("Распределение данных не отличается от нормального на уровне значимости 5% по Андерсону-Дарлингу")
    else:
        print("Распределение данных отличается от нормального на уровне значимости 5% по Андерсону-Дарлингу")
    print()

