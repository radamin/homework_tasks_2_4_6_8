# Задание 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# Решение

# 1.Найдём остаток от деления "abc" на 10, записать его в переменную "с". Это будет третья цифра числа.
# 2.Избавимся от третьей цифры в числе "abc", разделив его нацело на 10.
# 3.Найдём остаток от деления "ab" на 10, записав его в переменную "в". Это будет вторая цифра числа.
# 4.Избавимся от цифры "b" в числе "ab", разделив его нацело на 10.
# 5.Число "a" однозначное. Это первая цифра исходного числа.
# 6.Складываем оставшееся число "a" со значениями переменных "b" и "c".

# n = input("Enter a three-digit number: ")
# abc = int(n)

# c = abc % 10
# ab = abc // 10
# b = ab % 10
# a = ab // 10

# print(f"The sum of the digits of a number: {abc} ->", a + b + c, (f"({a} + {b} + {c})"))