import numpy as np
import matplotlib.pyplot as plt

# Ваши данные
particles = [8, 16, 64, 400, 800, 3600]
mean_steps = [23.775, 33.343, 57.681, 158.296, 249.423, 708.722]

# Построение полиномиальной регрессии
degree = 2  # Степень полинома

# Подготовка данных
x = np.array(particles)
y = np.array(mean_steps)

# Вычисление коэффициентов полинома
coefficients = np.polyfit(x, y, degree)

# Создание модели полиномиальной регрессии
poly_model = np.poly1d(coefficients)

# Построение графика данных и аппроксимированной кривой
plt.scatter(x, y, label='Данные')
plt.plot(x, poly_model(x), color='red', label='Полиномиальная аппроксимация')
plt.xlabel('Количество частиц')
plt.ylabel('Среднее количество шагов')
plt.title('Аппроксимация зависимости количества шагов от числа частиц')
plt.legend()
plt.show()

