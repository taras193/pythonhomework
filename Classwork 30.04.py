#1.Написати скрипт, який з двох введених чисел визначить, яке з них більше, а яке менше.
# a=float(input('Enter first value'))
# b=float(input('Enter second value'))
# if a>b:
#     print ('First value %s is bigger than second value %d' % (a, b))
# else:
#     print ('Second value %s is bigger than first value %d' % (b, a))

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
# a=float(input('Enter the value'))
# if a%2==0:
#     print('Value you have set "%d" is odd number' % (a))
# else:
#     print('Value you have set "%d" is even number' % (a))
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