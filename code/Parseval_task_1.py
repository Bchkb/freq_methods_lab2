from scipy import integrate
import numpy as np

def equation(f_t, f_w):
    fun_t = integrate.quad(f_t, -np.inf, np.inf, limit=1000)
    fun_w = integrate.quad(f_w, -np.inf, np.inf, limit=1000)
    
    integral_t = fun_t[0]
    integral_w = fun_w[0]
    
    if np.isnan(integral_t) or np.isnan(integral_w):
        return None, None
    
    return round(integral_t, 6), round(integral_w, 6)

def f_t_rect(t, a, b):
    return a if abs(t) <= b else 0

def f_w_rect(w, a, b):
    if abs(w) < 1e-10:
        return (1/np.sqrt(2 * np.pi)) * 2 * a * b
    return (1/np.sqrt(2 * np.pi)) * 2 * a * np.sin(w * b) / w

def f_t_triangle(t, a, b):
    if abs(t) <= b:
        return a - abs(a * t / b)
    return 0

def f_w_triangle(w, a, b):
    if abs(w) < 1e-10:
        return (1/np.sqrt(2 * np.pi)) * a * b
    return (1/np.sqrt(2 * np.pi)) * (4 * a * np.sin(w * b / 2)**2) / (b * w**2)

def f_t_sinc(t, a, b):
    if abs(t) < 1e-10:
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

test_params = [[1, 1], [3, 1], [1, 3]]

print("Прямоугольная функция")
for a, b in test_params:
    int_t, int_w = equation(lambda t: f_t_rect(t, a, b)**2, lambda w: f_w_rect(w, a, b)**2)
    print(f"({a}, {b}): {int_t} {int_w}")

print("\nТреугольная функция")
for a, b in test_params:
    int_t, int_w = equation(lambda t: f_t_triangle(t, a, b)**2, lambda w: f_w_triangle(w, a, b)**2)
    print(f"({a}, {b}): {int_t} {int_w}")

print("\nКардинальный синус")
for a, b in test_params:
    int_t, int_w = equation(lambda t: f_t_sinc(t, a, b)**2, lambda w: f_w_sinc(w, a, b)**2)
    print(f"({a}, {b}): {int_t} {int_w}")

print("\nФункция Гаусса")
for a, b in test_params:
    int_t, int_w = equation(lambda t: f_t_gauss(t, a, b)**2, lambda w: f_w_gauss(w, a, b)**2)
    print(f"({a}, {b}): {int_t} {int_w}")

print("\nДвустороннее затухание")
for a, b in test_params:
    int_t, int_w = equation(lambda t: f_t_exp(t, a, b)**2, lambda w: f_w_exp(w, a, b)**2)
    print(f"({a}, {b}): {int_t} {int_w}")