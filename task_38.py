# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , 
# разность d и количество элементов n будет задано автоматически. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

a1 = 2
d = 3
n = 4

for i in range(n):
    k = a1 + (i+1-1)*d
    print(k)