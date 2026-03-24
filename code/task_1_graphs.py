import numpy as np
import matplotlib.pyplot as plt

# Параметры из таблицы: (a, b, цвет, название)
data_points = [
    (1.0, 1.0, 'blue',   'Базовый'),
    (1.5, 0.5, 'orange', 'Высокий и узкий'),
    (0.5, 2.0, 'red',    'Низкий и широкий'),
    (1.2, 1.5, 'green',  'Средний'),
    (0.8, 0.8, 'purple', 'Уменьшенный')
]

t = np.linspace(-10, 10, 1000)
w = np.linspace(-20, 20, 1000)

def create_plot(title, original_func, fourier_func):
    plt.figure(figsize=(12, 6))
    plt.suptitle(title, fontsize=16)
    
    # Левый график - Оригинал
    ax1 = plt.subplot(1, 2, 1)
    for a, b, col, lbl in data_points:
        ax1.plot(t, original_func(t, a, b), color=col, label=f'a={a}, b={b} ({lbl})')
    ax1.set_title("Оригинал f(t)")
    ax1.grid(True)
    ax1.legend(prop={'size': 8})

    # Правый график - Фурье-образ
    ax2 = plt.subplot(1, 2, 2)
    for a, b, col, lbl in data_points:
        ax2.plot(w, fourier_func(w, a, b), color=col)
    ax2.set_title("Фурье-образ f_hat(w)")
    ax2.grid(True)

# --- Определение функций ---

# 1. Прямоугольная
rect_orig = lambda t, a, b: np.where(np.abs(t) <= b, a, 0)
rect_four = lambda w, a, b: (1/np.sqrt(2*np.pi)) * (2*a*np.sin(w*b) / (w + 1e-9))

# 2. Треугольная
tri_orig = lambda t, a, b: np.where(np.abs(t) <= b, a - np.abs(a*t/b), 0)
tri_four = lambda w, a, b: (1/np.sqrt(2*np.pi)) * (4*a*np.sin(w*b/2)**2 / (b * w**2 + 1e-9))

# 3. Кардинальный синус (sinc)
# В numpy sinc(x) = sin(pi*x)/(pi*x), поэтому нормируем аргумент
sinc_orig = lambda t, a, b: a * np.sinc(b * t / np.pi)
sinc_four = lambda w, a, b: np.where(np.abs(w) <= b, (a/b) * np.sqrt(np.pi/2), 0)

# 4. Функция Гаусса
gauss_orig = lambda t, a, b: a * np.exp(-b * t**2)
gauss_four = lambda w, a, b: (a / np.sqrt(2*b)) * np.exp(-w**2 / (4*b))

# 5. Двустороннее затухание (экспоненциальное)
exp_orig = lambda t, a, b: a * np.exp(-b * np.abs(t))
exp_four = lambda w, a, b: a * np.sqrt(2/np.pi) * (b / (b**2 + w**2))

# --- Построение ---

create_plot("1. Прямоугольная функция", rect_orig, rect_four)
create_plot("2. Треугольная функция", tri_orig, tri_four)
create_plot("3. Кардинальный синус", sinc_orig, sinc_four)
create_plot("4. Функция Гаусса", gauss_orig, gauss_four)
create_plot("5. Двустороннее затухание", exp_orig, exp_four)

plt.show()