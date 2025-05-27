import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x + x**3)
    
x = np.linspace(0, 2, 500)  
y = f(x)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = cos(x + x³)', color='blue', linewidth=2)
plt.title('График функции f(x) = cos(x + x³)', fontsize=16)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Линия x=0
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Линия y=0
plt.axhline(y=1, color='red', linestyle='--', linewidth=2, label='касательная')
plt.text(1.6,1, 'Точка касания')
plt.grid(alpha=0.6)  # Включение сетки
plt.legend(fontsize=12)  # Легенда
plt.show()
