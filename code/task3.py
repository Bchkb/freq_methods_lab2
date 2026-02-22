import librosa
import numpy as np
import matplotlib.pyplot as plt

# 1. Загрузка всего файла
# sr=None — сохраняем оригинальную частоту дискретизации
# mono=True — librosa сама смешает каналы в один (удобно для анализа)
path = 'music.mp3'
f_t, fs = librosa.load(path, sr=None, mono=True)

def music_data():
    return f_t

print(f"Файл загружен полностью.")
print(f"Частота дискретизации: {fs} Гц")
print(f"Общее количество отсчетов: {len(f_t)}")
print(f"Длительность: {len(f_t)/fs:.2f} секунд")

# 2. Построение графика для всей длины массива
plt.figure(figsize=(15, 5))

# Создаем временную ось для всего файла
time_axis = np.linspace(0, len(f_t) / fs, len(f_t))

# Строим весь сигнал
plt.plot(time_axis, f_t, color='steelblue', lw=0.5) 

plt.title('Аккорд 28')
plt.xlabel('Время (секунды)')
plt.ylabel('Амплитуда')
plt.grid(True, alpha=0.3)

# Чтобы график не «задыхался», можно ограничить пределы по осям
plt.xlim(0, len(f_t) / fs)
plt.tight_layout()
plt.show()