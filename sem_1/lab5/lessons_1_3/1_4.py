import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,50)
y1 = x #линейная зависимость
y2 = [i**2 for i in x] #квадратичная зависимость

plt.title('Зависимость: y1 = x, y2 = x^2') #заголовок
plt.xlabel('x') # ось абсцисс
plt.ylabel('y1, y2') # ось ординат   
plt.grid() # включение отображение сетки
plt.plot(x, y1, x, y2) # построение графика
plt.show()