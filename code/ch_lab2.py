from scipy import integrate
import numpy as np

def equation(f_t, f_w):
    fun_t = integrate.quad(f_t, -np.inf, np.inf)
    fun_w = integrate.quad(f_w, -np.inf, np.inf)
    if abs(fun_t[0] - fun_w[0]) < 0.000001:
        check = 1
    else:
        check = 0
    return round(fun_t[0], 6), round(fun_w[0], 6), check

def f_t(t, a, b):
    # функция квадрата
    # if abs(t) <= b: 
    #     return a
    # else:
    #     return 0

    #Функция треугольника
    # if abs(t) <= b:
    #     return a - abs(a*t/b)
    # else:
    #     return 0

    #Кардинальный синус
    # return a * np.sin(b * t) / (b * t)

    #Функция Гаусс
    # return a * np.exp(-b*t**2) 

    #Двустороннее затухание
    return a * np.exp(-b* abs(t))


def f_w(w, a, b):
    # функция квадрата
    # return (1/np.sqrt(2 * np.pi)) * 2*a*np.sin(w * b)/w 

    #Функция треугольника
    # return (1/np.sqrt(2 * np.pi)) * ((4 * a * np.sin(w*b/2)**2)/(b*w**2))

    #Кардинальный синус
    # if abs(w) <= b:
    #     return (a / b) * np.sqrt(np.pi / 2)
    # else:
    #     return 0

    #Функция Гаусс
    # return a * np.sqrt(np.pi / b) * np.exp(-(w**2) / (4 * b)) 

    #Двустороннее затухание
    return a * np.sqrt(2/np.pi) * (b/(b**2 + w**2))

def result_func():
    ab = [[1, 1], [0.2, 5], [5, 0.2], [2, 10], [10, 2]]

    for sample in ab:
        a = sample[0]
        b = sample[1]
        print(equation(lambda t: f_t(t, a, b)**2, lambda w:f_w(w, a, b)**2))

