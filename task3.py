# Задание 3.

# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
# Пример:
# Введите число n: 3
# n + nn + nnn = 369

# a = int(input("Введите целое положительное число: "))
# b = int (a * 2)
# c = int (a * 3)
# print("n + nn + nnn = {}{}{}".format(a,b,c)))

a = int(input("Введите целое положительное число: "))
b = a * 10 + a
c = a * 100 + b
print(f"Сумма чисел n + nn + nnn = {a + b + c}")