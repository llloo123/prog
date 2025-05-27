import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,50)
y1 = x #линейная зависимость
y2 = [i**2 for i in x] #квадратичная зависимость

plt.figure(figsize=(9, 9)) #построение графика
plt.subplot(2, 1, 1)
plt.plot(x, y1) #построение графика            
plt.title('Зависимости: y1 = x, y2 = x^2') #заголовок
plt.ylabel('y1', fontsize=14) #ось ординат
plt.grid(True) #ось ординат    

plt.subplot(2, 1, 2)
plt.plot(x, y2) #gостроение графика         
plt.xlabel('x', fontsize=14) #ось абсцисс   
plt.ylabel('y2', fontsize=14) #ось ординат  
plt.grid(True) #включение отображение сетки   

plt.show()