# Задача 4: Требуется определить, можно ли от шоколадки размером n × m 
# долек отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите размер первой стороны шоколадки: "))
m = int(input("Введите размер второй стороны шоколадки: "))
k = int(input("Введите размер кусочка: "))

if k < n * m and (k % n == 0 or k % m == 0):
    print('yes')
else:
    print('no')