import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# ЗАГРУЗКА ПОЛНОГО MP3 ФАЙЛА 
path = 'music.mp3'
f_t, fs = librosa.load(path, sr=None, mono=True)

# Создаем массив времени для всего файла
time_axis = np.linspace(0, len(f_t) / fs, len(f_t))

print(f"Файл загружен. Длительность: {len(f_t)/fs:.2f} сек. Отсчетов: {len(f_t)}")

# НАСТРОЙКА ЧАСТОТНОЙ СЕТКИ 
V_max = 1000  
dv = 5        
v_axis = np.arange(-V_max, V_max, dv)

# ЧИСЛЕННОЕ ИНТЕГРИРОВАНИЕ
print(f"Вычисляю численный интеграл для {len(v_axis)} частот...")

dt = 1 / fs

exponent = np.exp(-2j * np.pi * np.outer(v_axis, time_axis))
Y = np.dot(exponent, f_t) * dt

print("Расчет завершен успешно.")
amplitude_spectrum = np.abs(Y)
peaks, properties = find_peaks(amplitude_spectrum, 
                               height=np.max(amplitude_spectrum)*0.1, 
                               distance=len(v_axis)/20)
# ВИЗУАЛИЗАЦИЯ 
plt.figure(figsize=(12, 8))
plt.plot(v_axis, np.abs(Y), color='crimson')
plt.title('Модуль Фурье-образа')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.grid(True)

plt.tight_layout()
for peak in peaks:
    freq = v_axis[peak]
    amp = amplitude_spectrum[peak]
    plt.annotate(f'{freq:.0f} Hz', 
                 xy=(freq, amp), 
                 xytext=(10, 5), 
                 textcoords='offset points', 
                 fontsize=9, 
                 color='darkred',
                 fontweight='bold')
plt.show()