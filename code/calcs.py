import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 1. Задаем параметры функции (можете менять их для проверки)
a = 1.5
b = 0.5

# 2. Аналитическое задание функций
# Сигнал во временной области: f(t) = a * e^(-bt^2)
def f_t(t, a, b):
    return a * np.exp(-b * t**2)

# Фурье-образ (Спектр): F(w) = a * sqrt(pi/b) * e^(-w^2 / 4b)
def F_w(w, a, b):
    return a * np.sqrt(np.pi / b) * np.exp(-(w**2) / (4 * b))

# 3. Численное интегрирование для проверки равенства Парсеваля
# Энергия во времени: интеграл от -inf до +inf |f(t)|^2 dt
energy_time, error_t = quad(lambda t: f_t(t, a, b)**2, -np.inf, np.inf)

# Энергия в частоте: (1 / 2*pi) * интеграл от -inf до +inf |F(w)|^2 dw
energy_freq, error_w = quad(lambda w: (1 / (2 * np.pi)) * F_w(w, a, b)**2, -np.inf, np.inf)

# 4. Вывод результатов в консоль
print(f"--- Результаты (a={a}, b={b}) ---")
print(f"Энергия во временной области: {energy_time:.10f}")
print(f"Энергия в частотной области:  {energy_freq:.10f}")
print(f"Разница (погрешность):        {abs(energy_time - energy_freq):.2e}")

# 5. Визуализация для наглядности
t_vals = np.linspace(-5, 5, 500)
w_vals = np.linspace(-10, 10, 500)

plt.figure(figsize=(12, 5))

# График во времени
plt.subplot(1, 2, 1)
plt.plot(t_vals, f_t(t_vals, a, b), 'b', label='$f(t)$')
plt.fill_between(t_vals, f_t(t_vals, a, b)**2, alpha=0.2, color='blue', label='$|f(t)|^2$ (энергия)')
plt.title('Сигнал во временной области')
plt.legend()
plt.grid(True)

# График в частоте
plt.subplot(1, 2, 2)
plt.plot(w_vals, F_w(w_vals, a, b), 'r', label='$F(\omega)$')
plt.fill_between(w_vals, (1/(2*np.pi))*F_w(w_vals, a, b)**2, alpha=0.2, color='red', label='Спектр энергии')
plt.title('Спектр в частотной области')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()