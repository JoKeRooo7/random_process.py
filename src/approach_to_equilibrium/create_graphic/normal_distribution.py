import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import gaussian_kde


def plot_normal_distribution(data, columns, title):
    fig, axes = plt.subplots(nrows=1, ncols=len(columns), figsize=(15, 5))
    
    for i, column in enumerate(columns):
        ax = axes[i] if len(columns) > 1 else axes
        mean = data[column].mean()
        std = data[column].std()
        std_err = std / np.sqrt(len(data[column]))  # Стандартная ошибка
        x = np.linspace(mean - 3 * std, mean + 3*std, 50)  # Задаем диапазон значений по оси x
        ax.plot(x, norm.pdf(x, mean, std), 'r-', lw=2)  # Строим график нормального распределения
        ax.set_title(column)
    
    fig.suptitle(title)
    plt.tight_layout()
    plt.show()

def plot_frequency_distribution(data, title):
    fig, axes = plt.subplots(nrows=1, ncols=data.shape[1], figsize=(15, 5))
    
    for i, column in enumerate(data.columns):
        ax = axes[i] if data.shape[1] > 1 else axes
        values = data[column]
        kde = gaussian_kde(values)
        x = np.linspace(values.min(), values.max(), 1000)
        ax.plot(x, kde(x), 'r-', lw=2)  # Plot kernel density estimate
        ax.set_title(column)
    
    fig.suptitle(title)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    data = pd.read_csv("../../../datasets/unstable_equilibrium_data_2.csv")
    plot_normal_distribution(data, data.columns[:3], "Нормальное распределение для 8, 16 и 64")
    plot_normal_distribution(data, data.columns[3:], "Нормальное распределение для 400, 800 и 3600")
    # plot_frequency_distribution(data, 'Распределение частоты встречаемости значений')
