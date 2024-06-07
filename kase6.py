# Звездный прямоугольник

# def draw_box():
#     print("*"*10)
#     for  _ in range(12):
#         print("*", ' ' * 6, "*")
#     print("*" * 10)
# draw_box()

# Звездный треугольник 1

# def draw_triangle():
#     for i in range(10):
#         print("*"*i)
# draw_triangle()

# Звездный треугольник

# Определение функции draw_triangle()

# def draw_triangle(base,fill):
    # for i in range(base // 2):
    #     print(fill * (i + 1))
    # for i in range(base // 2, -1, -1):
    #     print(fill * (i + 1))
# draw_triangle(5,'*')

# ФИО

# def print_fio(name,surname,patronymic):
#     print(name[0],surname[0],patronymic[0])
# print_fio('Пушкин','Александр','Сергеевич')

# Сумма цифр

# def print_digit_sum():
#     num  = int(input())
#     n =0
#     while num > 0:
#         n += num % 10
#         num //= 10
#     print(n)
# print_digit_sum()

# Конвертер километров

# def convert_to_miles(km):
#     miles = km  *  0.6214
#     print(miles)
# convert_to_miles(1)

# Количество дней

# def get_days(month):
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         days = 31
#     elif month in [4, 6, 9, 11]:
#         days = 30
#     else:
#         days = 28
#     print(days)
# get_days(1)

# Делители 1

# Делители 2