import numpy as np
from scipy import integrate
import warnings

warnings.filterwarnings("ignore")

def equation(f_t, bounds_t, f_w, bounds_w):
    fun_t = integrate.quad(f_t, bounds_t[0], bounds_t[1], limit=2000, epsabs=1e-10, epsrel=1e-10)
    fun_w = integrate.quad(f_w, bounds_w[0], bounds_w[1], limit=2000, epsabs=1e-10, epsrel=1e-10)
    
    integral_t = fun_t[0]
    integral_w = fun_w[0]
    
    if np.isnan(integral_t) or np.isnan(integral_w):
        return None, None
    
    return round(integral_t, 6), round(integral_w, 6)

def f_t_rectangle(t, a, b):
    return a if abs(t) <= b else 0

def f_w_rectangle(w, a, b):
    # np.sinc(x) = sin(pi*x)/(pi*x), поэтому (sin(w*b)/w) = b * np.sinc(w*b/pi)
    if w == 0:
        return (1/np.sqrt(2 * np.pi)) * 2 * a * b
    return (1/np.sqrt(2 * np.pi)) * 2 * a * np.sin(w * b) / w

def f_t_triangle(t, a, b):
    if abs(t) <= b:
        return a - abs(a * t / b)
    return 0

def f_w_triangle(w, a, b):
    if w == 0:
        return (1/np.sqrt(2 * np.pi)) * a * b
    return (1/np.sqrt(2 * np.pi)) * (4 * a * np.sin(w * b / 2)**2) / (b * w**2)

def f_t_sinc(t, a, b):
    if t == 0:
        return a
    return a * np.sin(b * t) / (b * t)

def f_w_sinc(w, a, b):
    if abs(w) <= b:
        return (a / b) * np.sqrt(np.pi / 2)
    return 0

def f_t_gauss(t, a, b):
    return a * np.exp(-b * t**2)

def f_w_gauss(w, a, b):
    return (a / np.sqrt(2 * b)) * np.exp(-(w**2) / (4 * b))

def f_t_exp(t, a, b):
    return a * np.exp(-b * abs(t))

def f_w_exp(w, a, b):
    return a * np.sqrt(2 / np.pi) * (b / (b**2 + w**2))

a_b = [[1, 1], [3, 1], [1, 3]]
inf = np.inf

print("Прямоугольная функция")
for a, b in a_b:
    # Оригинал ограничен [-b, b], образ бесконечен
    int_t, int_w = equation(lambda t: f_t_rectangle(t, a, b)**2, (-b, b), 
                            lambda w: f_w_rectangle(w, a, b)**2, (-inf, inf))
    print(f"({a}, {b}): {int_t:.6f} == {int_w:.6f}")

print("\nТреугольная функция")
for a, b in a_b:
    # Оригинал ограничен [-b, b], образ бесконечен
    int_t, int_w = equation(lambda t: f_t_triangle(t, a, b)**2, (-b, b), 
                            lambda w: f_w_triangle(w, a, b)**2, (-inf, inf))
    print(f"({a}, {b}): {int_t:.6f} == {int_w:.6f}")

print("\nКардинальный синус")
for a, b in a_b:
    # Оригинал бесконечен, образ ограничен [-b, b]
    int_t, int_w = equation(lambda t: f_t_sinc(t, a, b)**2, (-inf, inf), 
                            lambda w: f_w_sinc(w, a, b)**2, (-b, b))
    print(f"({a}, {b}): {int_t:.6f} == {int_w:.6f}")

print("\nФункция Гаусса")
for a, b in a_b:
    # Обе функции бесконечны
    int_t, int_w = equation(lambda t: f_t_gauss(t, a, b)**2, (-inf, inf), 
                            lambda w: f_w_gauss(w, a, b)**2, (-inf, inf))
    print(f"({a}, {b}): {int_t:.6f} == {int_w:.6f}")

print("\nДвустороннее затухание")
for a, b in a_b:
    # Обе функции бесконечны
    int_t, int_w = equation(lambda t: f_t_exp(t, a, b)**2, (-inf, inf), 
                            lambda w: f_w_exp(w, a, b)**2, (-inf, inf))
    print(f"({a}, {b}): {int_t:.6f} == {int_w:.6f}")