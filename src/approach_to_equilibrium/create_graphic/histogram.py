import pandas as pd
import matplotlib.pyplot as plt

# Считываем данные из CSV файла
data = pd.read_csv('../../../datasets/unstable_equilibrium_data_2.csv')

# Создаем общий график с 6 подграфиками
fig, axs = plt.subplots(2, 3, figsize=(18, 10))

# Проходимся по каждой колонке и строим гистограмму на соответствующем подграфике
for i, column in enumerate(data.columns):
    ax = axs[i // 3, i % 3]  # Получаем нужный подграфик
    ax.hist(data[column], bins=20, alpha=0.5)
    ax.set_xlabel('Количество шагов')
    ax.set_ylabel('Частота')
    ax.set_title(f'Гистограмма количества шагов для {column}')

# Добавляем расстояние между графиками
plt.tight_layout()

# Показываем график
plt.show()
