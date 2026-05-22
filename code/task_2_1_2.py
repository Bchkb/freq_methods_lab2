#улучшенная версия кода org_2.py
import numpy as np
import matplotlib.pyplot as plt

# Параметры (a, b) и цвета
params = [
    (1, 3, 'blue',   'c1 = -10'),
    (1, 3, 'orange', 'c2 = -0.3'),
    (1, 3, 'red',    'c3 = 20'),
    (1, 3, 'green',  'c4 = 5')
]

# Значения сдвигов c
shifts = [-10, -0.3, 20, 5]

# Ось времени
t = np.linspace(-30, 30, 2000)

def plot_shifted_exponential():
    # Создаем фигуру с одной осью (subplot 1x1)
    fig, ax = plt.subplots(figsize=(10, 5))

    for (a, b, col, lbl), c in zip(params, shifts):
        # Оригинал со сдвигом
        g_t = a * np.exp(-b * np.abs(t + c))
        
        # Отрисовка на одной оси
        ax.plot(t, g_t, color=col, lw=2, label=lbl)

    ax.set_title("Оригиналы g(t)")
    ax.set_xlabel("t")
    ax.set_ylabel("Амплитуда")
    ax.grid(True, linestyle='--', alpha=0.6)
    
    # Легенда вынесена за пределы осей, чтобы не перекрывать кривые
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()

    # Сохранение файла. bbox_inches='tight' гарантирует, что легенда не обрежется
    plt.savefig('C:\\Users\\fmusa\\ITMOStudies\\freg_methods\\freq_methods_lab2\\imgs\\originals_g.png', dpi=300, bbox_inches='tight')
    plt.close()

plot_shifted_exponential()