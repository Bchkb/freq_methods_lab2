import numpy as np
import matplotlib.pyplot as plt

# 1. Фиксированные параметры из условия
a_fixed = 5.0
b_fixed = 0.2
c_norm_const = np.sqrt(2.0 / np.pi)

# Параметры сдвига 'c' и соответствующие цвета из таблицы
shift_data = [
    {'c': -10.0, 'color': 'dodgerblue', 'name': 'c = -10 (Синий)'},
    {'c': -0.3,  'color': 'orange',     'name': 'c = -0.3 (Оранжевый)'},
    {'c': 20.0,  'color': 'crimson',    'name': 'c = 20 (Красный)'},
    {'c': 5.0,   'color': 'forestgreen', 'name': 'c = 5 (Зелёный)'}
]

# Вектор частот (чуть сузим диапазон, чтобы лучше видеть осцилляции для больших c)
w = np.linspace(-10, 10, 2000)

def setup_ax(ax, title):
    ax.set_title(title, fontsize=14, pad=15)
    ax.set_xlabel(r'Частота $\omega$', fontsize=12)
    ax.set_ylabel('Амплитуда', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.axhline(0, color='black', linewidth=1, alpha=0.5)
    ax.axvline(0, color='black', linewidth=1, alpha=0.5)

# --- ОКНО 1: Модуль (он будет один для всех, так как a и b фиксированы) ---
plt.figure("Модуль спектра (Фиксированный)", figsize=(9, 5))
envelope = (c_norm_const * a_fixed * b_fixed) / (b_fixed**2 + w**2)
plt.plot(w, envelope, color='black', lw=2, label=f'Огибающая (a=5, b=0.2)')
setup_ax(plt.gca(), r'Модуль спектра $|\hat{g}(\omega)|$ (одинаков для всех $c$)')
plt.legend()

# --- ОКНО 2: Re(ĝ(ω)) ---
plt.figure("Действительная часть", figsize=(9, 6))
for item in shift_data:
    c = item['c']
    re_part = envelope * np.cos(w * c)
    plt.plot(w, re_part, color=item['color'], label=item['name'], alpha=0.8)
setup_ax(plt.gca(), r'Действительная часть $Re(\hat{g}(\omega))$')
plt.legend(loc='upper right', fontsize=9)

# --- ОКНО 3: Мнимая часть Im(ĝ(ω)) ---
plt.figure("Мнимая часть", figsize=(9, 6))
for item in shift_data:
    c = item['c']
    im_part = envelope * np.sin(w * c)
    plt.plot(w, im_part, color=item['color'], label=item['name'], alpha=0.8)
setup_ax(plt.gca(), r'Мнимая часть $Im(\hat{g}(\omega))$')
plt.legend(loc='upper right', fontsize=9)

plt.show()