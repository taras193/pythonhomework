#1.Написати скрипт, який з двох введених чисел визначить, яке з них більше, а яке менше.
# a=int(input("Please set first value"))
# b=int(input("Please set second value"))
# if a > b:
#     print (a)
# else:
#      print (b)
# #TEACHER
# a=int(input("Input the number a="))
# b=int(input("Input the number b="))
# if a <= b:
#     min_value, max_value = a,b
# else:
#     min_value, max_value = b,a
# st="The number a={0} is minimal number, the number b={1} is maximum number" .format(min_value, max_value)
# print (st)
#2.Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне повідомлення.
# c=int(input("Please set any value"))
# mod=c % 2
# if mod>0:
#     print("This is an odd number")
# else:
#     print("This is an even number")
#Teacher V
# num = int(input("enter a number"))
# if (num % 2) == 0:
#     print("The number {0} is even" .format(num))
# else:
#     print("The number {0} is odd" .format(num))
#3.Написати скрипт, який обчислить факторіал введеного числа.
# Recursive
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))

#4.Написати скрипт, який знайде найбільший спільний дільник НСД та найменше спільне кратне НСК двох чисел.
# a=int(input("Please set first value"))
# b=int(input("Please set second value"))
# d = 2
# a_checked= a % d
# b_checked= b % d
# print(a_checked)
# print(b_checked)
# if a_checked is 0 and b_checked is 0:
#     print (d)
# else: d+1