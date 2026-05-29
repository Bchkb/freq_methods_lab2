import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.integrate import trapezoid

FIG_SIZE = (10, 5)

path = 'music.mp3'
f_t, fs = librosa.load(path, sr=None, mono=True)
time_axis = np.linspace(0, len(f_t) / fs, len(f_t))

print(f"Файл загружен. Длительность: {len(f_t)/fs:.2f} сек. Отсчетов: {len(f_t)}")

plt.figure(figsize=FIG_SIZE)
plt.plot(time_axis, f_t, color='steelblue', lw=0.5) 
plt.xlabel('Время $t$, с', fontsize=14)
plt.ylabel('Амплитуда', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlim(0, len(f_t) / fs)
plt.tight_layout()
plt.savefig('imgs/mus_graph.pdf', format='pdf', bbox_inches='tight')
plt.close()

V_max = 1000  
dv = 5        
v_axis = np.arange(-V_max, V_max, dv)

print(f"Вычисляю интеграл для {len(v_axis)} частот...")
dt = 1 / fs

integrand = f_t * np.exp(-2j * np.pi * np.outer(v_axis, time_axis))
Y = trapezoid(integrand, dx=dt, axis=1)

amplitude_spectrum = np.abs(Y)
peaks, _ = find_peaks(amplitude_spectrum, 
                      height=np.max(amplitude_spectrum)*0.1, 
                      distance=len(v_axis)/20)

print("Расчет завершен успешно.")

plt.figure(figsize=FIG_SIZE)
plt.plot(v_axis, amplitude_spectrum, color='crimson', lw=1.5)
plt.xlabel('Частота $\\nu$, Гц', fontsize=14)
plt.ylabel('Амплитуда $|\hat{f}(\\nu)|$', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)

for peak in peaks:
    freq = v_axis[peak]
    amp = amplitude_spectrum[peak]

    plt.annotate(f'{freq:.0f} Гц', 
                 xy=(freq, amp), 
                 xytext=(0, 8), 
                 textcoords='offset points', 
                 fontsize=11, 
                 ha='center',
                 color='black',
                 fontweight='bold')

ylim = plt.ylim()
plt.ylim(ylim[0], ylim[1] * 1.15)

plt.tight_layout()
plt.savefig('imgs/furie_music.pdf', format='pdf', bbox_inches='tight')
plt.close()

print("Графики сохранены в формате PDF в папку imgs!")