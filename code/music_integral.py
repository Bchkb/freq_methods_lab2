import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# --- 1. ЗАГРУЗКА ПОЛНОГО MP3 ФАЙЛА ---
path = 'music.mp3'
# mono=True смешивает каналы, sr=None оставляет родную частоту
f_t, fs = librosa.load(path, sr=None, mono=True)

# Создаем массив времени для всего файла
time_axis = np.linspace(0, len(f_t) / fs, len(f_t))

print(f"Файл загружен. Длительность: {len(f_t)/fs:.2f} сек. Отсчетов: {len(f_t)}")

# --- 2. НАСТРОЙКА ЧАСТОТНОЙ СЕТКИ ---
# ВНИМАНИЕ: Для огромных файлов не делайте dv слишком маленьким, 
# иначе не хватит оперативной памяти!
V_max = 1000  # До какой частоты смотрим спектр
dv = 5        # Шаг частоты (Гц)
v_axis = np.arange(-V_max, V_max, dv)

# --- 3. ЧИСЛЕННОЕ ИНТЕГРИРОВАНИЕ (БЕЗ ОБРЕЗКИ) ---
print(f"Вычисляю численный интеграл для {len(v_axis)} частот...")

# Чтобы не вешать компьютер циклом, используем матричное умножение.
# Это эквивалентно сумме f(t) * exp(...) * dt для каждой частоты.
dt = 1 / fs
# Создаем комплексную экспоненту сразу для всех пар (частота, время)
# Используем порции (batches), если файл экстремально большой
exponent = np.exp(-2j * np.pi * np.outer(v_axis, time_axis))
Y = np.dot(exponent, f_t) * dt

print("Расчет завершен успешно.")
amplitude_spectrum = np.abs(Y)
peaks, properties = find_peaks(amplitude_spectrum, 
                               height=np.max(amplitude_spectrum)*0.1, 
                               distance=len(v_axis)/20)
# --- 4. ВИЗУАЛИЗАЦИЯ ---
plt.figure(figsize=(12, 8))

# # Весь сигнал во времени
# plt.subplot(2, 1, 1)
# plt.plot(time_axis, f_t, color='steelblue', lw=0.1) # lw=0.1 чтобы линия была тонкой
# plt.title('Полный сигнал f(t)')
# plt.xlabel('Время (с)')
# plt.ylabel('Амплитуда')
# plt.grid(True, alpha=0.3)

# Спектр (модуль Фурье-образа)
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