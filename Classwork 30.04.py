#################First Task#################
# a=int(input("Please set first value"))
# b=int(input("Please set second value"))
# if a > b:
#     print (a)
# else:
#      print (b)
# #TEACHER V
# a=int(input("Input the number a="))
# b=int(input("Input the number b="))
# if a <= b:
#     min_value, max_value = a,b
# else:
#     min_value, max_value = b,a
# st="The number a={0} is minimal number, the number b={1} is maximum number" .format(min_value, max_value)
# print (st)
#################Second Task#################
#My V
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
#################Third Task FACTORIAL#################
# f=int(input("Please set any value you want to count"))
# n=int (1)
# if f == 0:
#     print (1)
# elif n < f:
#     f = f * (f-1)
#     n+1
# else:
#     print (f)
#################Third Task FACTORIAL_2_StackOverflow#################
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))

################# Fourth Task ################
a=int(input("Please set first value"))
b=int(input("Please set second value"))
d = 2
a_checked= a % d
b_checked= b % d
print(a_checked)
print(b_checked)
if a_checked is 0 and b_checked is 0:
    print (d)
else: d+1