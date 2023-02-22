#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

while True:
    n =int(input("Введите число N > 1 "))
    if n >1:
        break
b =[1]
step=1
while step*2 < n:
    step = step*2
    b.append(step)
print(b)
