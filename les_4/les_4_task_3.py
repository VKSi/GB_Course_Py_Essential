# Vasilii Sitdikov
# GeekBrains Courses. Python Essential
# Lesson 4 task 3
# October 2019

# task: 3)	Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
#       Подсказка: использовать функцию range() и генератор.

# Solution:


def task_3():
    return [x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0]


print(task_3())
