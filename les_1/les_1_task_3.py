# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 1 task 3
# October 2019

# task:	Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#       Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
# assumption: Из примера не понятно, требуется работа с цифрами или с любыми числами. Реализована работа с числами.

# Solution:
n = input("Введите любое целое число 'n': ")  # Тип string оставлен намеренно, он нам пока нужен
print(f"{n} + {2 * n} + {3 * n} = {int(n) + int(2 * n) + int(3 * n)}")
