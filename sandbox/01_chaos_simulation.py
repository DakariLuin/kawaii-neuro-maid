import numpy as np
import matplotlib.pyplot as plt

# 1. Симулируем стабильную рутину (Синусоида)
time_steps = np.arange(0, 100)
routine_signal = np.sin(time_steps * 0.2) + 1.0  # Плавная, предсказуемая волна

# 2. Симулируем динамический хаос
# Классическая формула хаоса: X_next = r * X * (1 - X)
# При r = 3.9 система становится абсолютно непредсказуемой и хаотичной
chaos_signal = []
x = 0.5  # Стартовая точка активности
r = 3.9  # Коэффициент хаоса
for _ in range(100):
    x = r * x * (1.0 - x)
    chaos_signal.append(x)
chaos_signal = np.array(chaos_signal)

# 3. Рисуем графики и сохраняем картинку
plt.figure(figsize=(12, 5))

# Левый график: Стабильное поведение
plt.subplot(1, 2, 1)
plt.plot(routine_signal, color='green', marker='o', linestyle='-', alpha=0.7)
plt.title("Stable Routine (Low Chaos)")
plt.xlabel("Time Steps")
plt.ylabel("Activity Level")
plt.grid(True)

# Правый график: Хаос
plt.subplot(1, 2, 2)
plt.plot(chaos_signal, color='red', marker='x', linestyle='-', alpha=0.7)
plt.title("Chaotic State (High Chaos / Unpredictable)")
plt.xlabel("Time Steps")
plt.ylabel("Activity Level")
plt.grid(True)

# Сохраняем результат в файл
plt.tight_layout()
plt.savefig("sandbox/chaos_comparison.png")
print("График сохранен в папку 'sandbox/chaos_comparison.png'")