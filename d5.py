# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

ax = int(input('Введите ax: '))
ay = int(input('Введите ay: '))
bx = int(input('Введите bx: '))
by = int(input('Введите by: '))
print(f'A:({ax}, {ay}), B:({bx}, {by})')
distance = ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5
print(round(distance, 2))
