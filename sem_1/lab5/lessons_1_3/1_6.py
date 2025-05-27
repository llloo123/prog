import matplotlib.pyplot as plt
fruits = ['apple', 'peach', 'orange', 'bannana', 'melon'] #название фруктов
counts = [34, 25, 43, 31, 17] #количество фруктов
plt.bar(fruits, counts) #построение вертикальной столбчатой диаграммы
plt.title('Fruits!') #заголовок
plt.xlabel('Fruit') #ось абцисс
plt.ylabel('Count') #ось ординат
plt.show()