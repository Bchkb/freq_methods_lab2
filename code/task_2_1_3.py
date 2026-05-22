import numpy as np
import matplotlib.pyplot as plt
import os

a_fixed = 1
b_fixed = 3
c_norm_const = np.sqrt(2.0 / np.pi)

# Контрастные цвета и разные типы линий для чёткого разделения
shift_data = [
    {'c': -10.0, 'color': 'blue',   'linestyle': '-',  'name': 'c = -10 (Синий)'},
    {'c': -0.3,  'color': 'orange', 'linestyle': '--', 'name': 'c = -0.3 (Оранжевый)'},
    {'c': 20.0,  'color': 'green',  'linestyle': ':',  'name': 'c = 20 (Зелёный)'},
    {'c': 5.0,   'color': 'crimson','linestyle': '-.', 'name': 'c = 5 (Красный)'}
]

w = np.linspace(-10, 10, 2000)
envelope = (c_norm_const * a_fixed * b_fixed) / (b_fixed**2 + w**2)

save_dir = r'C:\Users\fmusa\ITMOStudies\freg_methods\freq_methods_lab2\imgs'
os.makedirs(save_dir, exist_ok=True)

def setup_ax(ax, title):
    ax.set_title(title, fontsize=14, pad=15)
    ax.set_xlabel(r'Частота $\omega$', fontsize=12)
    ax.set_ylabel('Амплитуда', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.axhline(0, color='black', linewidth=1, alpha=0.5)
    ax.axvline(0, color='black', linewidth=1, alpha=0.5)

# Модуль
plt.figure("Модуль спектра", figsize=(9, 5))
plt.plot(w, envelope, color='black', lw=2.5, label='Огибающая')
setup_ax(plt.gca(), r'Модуль спектра $|\hat{g}(\omega)|$')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'g_fix.png'), dpi=300, bbox_inches='tight')
plt.close()

# Действительная часть
plt.figure("Действительная часть", figsize=(9, 6))
plt.fill_between(w, -envelope, envelope, color='gray', alpha=0.15, label='Границы огибающей')
for item in shift_data:
    c = item['c']
    re_part = envelope * np.cos(w * c)
    plt.plot(w, re_part, color=item['color'], linestyle=item['linestyle'], lw=2, label=item['name'], alpha=0.85)
setup_ax(plt.gca(), r'Действительная часть $Re(\hat{g}(\omega))$')
plt.legend(loc='upper right', fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 're_fix.png'), dpi=300, bbox_inches='tight')
plt.close()

# Мнимая часть
plt.figure("Мнимая часть", figsize=(9, 6))
plt.fill_between(w, -envelope, envelope, color='gray', alpha=0.15, label='Границы огибающей')
for item in shift_data:
    c = item['c']
    im_part = envelope * np.sin(w * c)
    plt.plot(w, im_part, color=item['color'], linestyle=item['linestyle'], lw=2, label=item['name'], alpha=0.85)
setup_ax(plt.gca(), r'Мнимая часть $Im(\hat{g}(\omega))$')
plt.legend(loc='upper right', fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(save_dir, 'im_fix.png'), dpi=300, bbox_inches='tight')
plt.close()

plt.show()