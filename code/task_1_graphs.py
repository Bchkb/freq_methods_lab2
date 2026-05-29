import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs('imgs', exist_ok=True)

FIG_SIZE = (7.09, 4.48)


data_points = [
    (1.0, 1.0, 'blue',   'a=1, b=1', 2.5, 0.6, 3, '--'), 
    (3.0, 1.0, 'orange', 'a=3, b=1', 2.0, 0.8, 1, '-'),
    (1.0, 3.0, 'red',    'a=1, b=3', 2.0, 0.6, 2, '-'), 
]

t = np.linspace(-10, 10, 2000)
w = np.linspace(-20, 20, 2000)

rect_orig = lambda t, a, b: np.where(np.abs(t) <= b, a, 0)
rect_four = lambda w, a, b: (1/np.sqrt(2*np.pi)) * np.where(w == 0, 2*a*b, 2*a*np.sin(w*b) / w)

tri_orig = lambda t, a, b: np.where(np.abs(t) <= b, a - np.abs(a*t/b), 0)
tri_four = lambda w, a, b: (1/np.sqrt(2*np.pi)) * np.where(w == 0, a*b, 4*a*np.sin(w*b/2)**2 / (b * w**2))

sinc_orig = lambda t, a, b: a * np.sinc(b * t / np.pi)
sinc_four = lambda w, a, b: np.where(np.abs(w) <= b, (a/b) * np.sqrt(np.pi/2), 0)

gauss_orig = lambda t, a, b: a * np.exp(-b * t**2)
gauss_four = lambda w, a, b: (a / np.sqrt(2*b)) * np.exp(-w**2 / (4*b))

exp_orig = lambda t, a, b: a * np.exp(-b * np.abs(t))
exp_four = lambda w, a, b: a * np.sqrt(2/np.pi) * (b / (b**2 + w**2))

def create_and_save_plot(filename, original_func, fourier_func):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=FIG_SIZE)
    
    # Построение оригинала
    for a, b, col, lbl, lw, alp, z, ls in data_points:
        ax1.plot(t, original_func(t, a, b), color=col, label=lbl, 
                 linewidth=lw, alpha=alp, zorder=z, linestyle=ls)
    
    ax1.set_xlabel('Время $t$', fontsize=12)
    ax1.set_ylabel('Амплитуда $f(t)$', fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.5)
    
    ylim_ax1 = ax1.get_ylim()
    ax1.set_ylim(ylim_ax1[0], ylim_ax1[1] * 1.25)
    ax1.legend(loc='upper right', fontsize=10)
    
    # Построение спектра
    for a, b, col, lbl, lw, alp, z, ls in data_points:
        ax2.plot(w, fourier_func(w, a, b), color=col, 
                 linewidth=lw, alpha=alp, zorder=z, linestyle=ls)
    
    ax2.set_xlabel('Частота $\\omega$', fontsize=12)
    ax2.set_ylabel('Амплитуда $\\hat{f}(\\omega)$', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.5)

    ylim_ax2 = ax2.get_ylim()
    ax2.set_ylim(ylim_ax2[0], ylim_ax2[1] * 1.15)

    plt.tight_layout()
    plt.savefig(f'imgs/{filename}.pdf', format='pdf', bbox_inches='tight')
    plt.close(fig) 


create_and_save_plot("1_rectangle", rect_orig, rect_four)
create_and_save_plot("2_triangle", tri_orig, tri_four)
create_and_save_plot("3_sinc", sinc_orig, sinc_four)
create_and_save_plot("4_gauss", gauss_orig, gauss_four)
create_and_save_plot("5_exp", exp_orig, exp_four)

print("Графики сохранены в папку imgs!")