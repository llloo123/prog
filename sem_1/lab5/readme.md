# Лабораторная работа №5 
### (Вариант 1)
## Задание 
1) Создайте в каталоге для данной ЛР в своём репозитории виртуальное окружение и установите в него ```matplotlib``` и ```numpy```. Создайте файл ```requirements.txt```.
2) Откройте книгу [1] и выполните уроки 1-3. Первый урок можно начинать со стр. 8.
3) Выберите одну из неразрывных функции своего варианта из лабораторной работы №2, постройте график этой функции и касательную к ней. Добавьте на график заголовок, подписи осей, легенду, сетку, а также аннотацию к точке касания.
4) Добавьте в корень своего репозитория файл .gitignore отсюда, перед тем как делать очередной коммит.
5) Оформите отчёт в README.md. Отчёт должен содержать:
- графики, построенные во время выполнения уроков из книги
- объяснения процесса решения и график по заданию 4
6) Склонируйте этот репозиторий НЕ в ваш репозиторий, а рядом. Изучите использование этого инструмента и создайте pdf-версию своего отчёта из README.md. Добавьте её в репозиторий.

## Ход работы

1. `python3 -m venv env` 
2. `source env/bin/activate`
3. `pip install -U pip`
4. ` pip install 'пакеты'`
5. `pip freeze > requirements.txt`
6. `pip install -r requirements.txt`

## Выполнение уроков
### Урок 1.2
``` python
import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5],[1,2,3,4,5])
plt.show()
```
![1_2](lessons_1_3/images/1_2.png)
### Урок 1.3
``` python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = x

plt.title('Линейная зависимость y = x') 
plt.xlabel('x')
plt.ylabel('y') 
plt.grid()      

plt.plot(x, y) 
plt.show()
```
![1_3](lessons_1_3/images/1_3.png)
### Урок 1.4
``` python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,50)
y1 = x 
y2 = [i**2 for i in x] 

plt.title('Зависимость: y1 = x, y2 = x^2') 
plt.xlabel('x') 
plt.ylabel('y1, y2') 
plt.grid() 
plt.plot(x, y1, x, y2) 
plt.show()
```
![1_4](lessons_1_3/images/1_4.png)

### Урок 1.5
``` python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,50)
y1 = x 
y2 = [i**2 for i in x] 

plt.figure(figsize=(9, 9)) 
plt.subplot(2, 1, 1)
plt.plot(x, y1)      
plt.title('Зависимости: y1 = x, y2 = x^2') 
plt.ylabel('y1', fontsize=14) 
plt.grid(True) 

plt.subplot(2, 1, 2)
plt.plot(x, y2)   
plt.xlabel('x', fontsize=14) 
plt.ylabel('y2', fontsize=14) 
plt.grid(True)               

plt.show()
```
![1_5](lessons_1_3/images/1_5.png)

### Урок 1.6
``` python
import matplotlib.pyplot as plt

fruits = ['apple', 'peach', 'orange', 'bannana', 'melon'] 
counts = [34, 25, 43, 31, 17] 
plt.bar(fruits, counts) 
plt.title('Fruits!') 
plt.xlabel('Fruit') 
plt.ylabel('Count') 
plt.show()
```
![1_6](lessons_1_3/images/1_6.png)
### Урок 2.1 + 2.2
``` python
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]
plt.plot(x, y, label = 'steel price') 
plt.xlabel('Day', fontsize=15, color='blue')
plt.title('График', fontsize=17)
plt.ylabel('Price', fontsize=15, color='blue')
plt.legend()
plt.grid(True)
plt.text(15, 4, 'grow up!')
plt.show()
```
![2_1+2](lessons_1_3/images/2_1+2.png)
### Урок 2.3
``` python
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]
plt.plot(x, y, '--r')
plt.show()
```
![2_3](lessons_1_3/images/2_3.png)
### Урок 2.4
``` python
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]

plt.figure(figsize=(12, 7))
plt.subplot(2, 2, 1)
plt.plot(x, y1, '-')
plt.subplot(2, 2, 2)
plt.plot(x, y2, '--')
plt.subplot(2, 2, 3)
plt.plot(x, y3, '-.')
plt.subplot(2, 2, 4)
plt.plot(x, y4, ':')
plt.show()
```
![2_4](lessons_1_3/images/2_4.png)
### Урок 2.5
``` python
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]
plt.plot(x, y1, '-', x, y2, '--', x, y3, '-.', x, y4, ':')
plt.show()
```
![2_5](lessons_1_3/images/2_5.png)
### Урок 3.1
``` python
import matplotlib.pyplot as plt

locs = ['best', 'upper right', 'upper left', 'lower left',
'lower right', 'right', 'center left', 'center right',
'lower center', 'upper center', 'center']
x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]
plt.figure(figsize=(12, 12))
for i in range(3):
    for j in range(4):
        if i*4+j < 11:
           plt.subplot(3, 4, i*4+j+1)
           plt.title(locs[i*4+j])
           plt.plot(x, y1, 'o-r', label='line 1')
           plt.plot(x, y2, 'o-.g', label='line 2')
           plt.legend(loc=locs[i*4+j])
        else:
            break
plt.show()
```
![3_1](lessons_1_3/images/3_1.png)
