# import pandas as pd
# import matplotlib.pyplot as plt

# # Считываем данные из CSV файла
# data = pd.read_csv('../../../datasets/stable_equilibrium_data_1.csv')

# # Построение графика
# plt.figure(figsize=(10, 6))

# for column in data.columns:
#     plt.plot(data.index, data[column], label=f'{column} particles')

# plt.xlabel('Эксперименты')
# plt.ylabel('Количество шагов')
# plt.title('График количества шагов в зависимости от числа экспериментов и частиц')
# plt.legend()
# plt.grid(True)

# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Считываем данные из CSV файла
data = pd.read_csv('../../../datasets/unstable_equilibrium_data_1.csv')

# Построение графиков
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

columns_groups = [data.columns[:2], data.columns[2:4], data.columns[4:6], data.columns[6:]]

for i, columns in enumerate(columns_groups[:3]):  # Изменено на columns_groups[:3]
    for column in columns:
        axs[i].plot(data.index, data[column], label=f'{column} particles')
    axs[i].set_xlabel('Эксперименты')
    axs[i].set_ylabel('Количество шагов')
    axs[i].set_title(f'График количества шагов для 1000 экспериментов')
    axs[i].legend()
    axs[i].grid(True)

plt.tight_layout()
plt.show()
