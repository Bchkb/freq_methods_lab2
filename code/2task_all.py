import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs('imgs', exist_ok=True)

FIG_SIZE = (7.09, 4.48)

a = 1.0
b = 3.0

c_params = [
    (-3.0, 'blue',   'c = -3', '-'),
    (-0.5, 'orange', 'c = -0.5', '--'),
    (1.0,  'green',  'c = 1', '-.'),
    (2.0,  'red',    'c = 2', ':')
]

t = np.linspace(-10, 10, 2000)
w = np.linspace(-10, 10, 2000)

envelope = a * np.sqrt(2/np.pi) * (b / (b**2 + w**2))

# 1. Оригиналы
plt.figure(figsize=FIG_SIZE)
for c, col, lbl, ls in c_params:
    g_t = a * np.exp(-b * np.abs(t + c))
    plt.plot(t, g_t, color=col, label=lbl, linewidth=2, linestyle=ls)
plt.xlabel('Время $t$', fontsize=12)
plt.ylabel('Амплитуда $g(t)$', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right', fontsize=10)
plt.tight_layout()
plt.savefig('imgs/task2_originals.pdf', format='pdf', bbox_inches='tight')
plt.close()

# Функция для отрисовки спектров
def plot_spectrum(func_w, filename, ylabel):
    plt.figure(figsize=FIG_SIZE)
    
    plt.fill_between(w, envelope, -envelope, color='lightgray', alpha=0.3)
    plt.plot(w, envelope, color='gray', linestyle='--', linewidth=1, label='Огибающая $|\hat{g}(\omega)|$')
    plt.plot(w, -envelope, color='gray', linestyle='--', linewidth=1)
    
    for c, col, lbl, ls in c_params:
        plt.plot(w, func_w(w, c), color=col, label=lbl, linewidth=1.5, alpha=0.8, linestyle=ls)
        
    plt.xlabel('Частота $\\omega$', fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    
    ylim = plt.ylim()
    plt.ylim(ylim[0], ylim[1] * 1.3)
    plt.legend(loc='upper right', fontsize=9, ncol=2)
    
    plt.tight_layout()
    plt.savefig(f'imgs/{filename}.pdf', format='pdf', bbox_inches='tight')
    plt.close()

plot_spectrum(lambda w, c: envelope * np.cos(w * c), 
              'task2_re', 'Амплитуда $Re(\hat{g}(\omega))$')

plot_spectrum(lambda w, c: envelope * np.sin(w * c), 
              'task2_im', 'Амплитуда $Im(\hat{g}(\omega))$')

plt.figure(figsize=FIG_SIZE)
plt.plot(w, envelope, color='black', linewidth=2, label='Модуль спектра $|\hat{g}(\omega)|$')
plt.xlabel('Частота $\\omega$', fontsize=12)
plt.ylabel('Амплитуда $|\hat{g}(\omega)|$', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right', fontsize=10)
plt.tight_layout()
plt.savefig('imgs/task2_mod.pdf', format='pdf', bbox_inches='tight')
plt.close()

print("Графики сохранены в формате PDF в папку imgs!")