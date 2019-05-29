##1.  Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне, чи введені дані коректні.
# class odd_even_error(Exception): 
#     def __init__(self, data): 
#         self.data = data
#     def __str__(self):
#         return repr(self.data)
# try:
#     usernum = int(input("Enter your num: "))
#     if usernum%2 == 0:
#         raise odd_even_error("Your number has to be odd")
#     else:
#         print("Your number is odd")
# except ValueError:
#     print("Please enter your number")
# except odd_even_error as e:
#     print ("We found that your number is incorrect:", e.data)

##2.Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення про те чи вік є парним чи непарним числом. 
##Необхідно передбачити можливість введення від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію. 
##Головний код має викликати функцію, яка обробляє введену інформацію.
# class odd_even_error(Exception): 
#     def __init__(self, data): 
#         self.data = data
#     def __str__(self):
#         return repr(self.data)
# class negative_number_error(Exception): 
#     def __init__(self, data): 
#         self.data = data
#     def __str__(self):
#         return repr(self.data)
#
# try:
#     usernum = int(input("Enter your age: "))
#     if usernum%2 == 0:
#         print("Your age is even")
#     else: print("Your age is odd")
#     if usernum<1:
#         raise negative_number_error("Your number has to be odd")
# except ValueError:
#     print("Error! You set an empty value! Please enter your number")
# except negative_number_error as n:
#     print("Error! Your age can not be less than 1 year. Please enter a value that is more than 1", n.data)

##3.Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, 
#передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій. 
#Використати блоки else та finaly.
# try:
#     usernum1, usernum2 = eval(input("Enter two values, divided by coma: "))
#     result = usernum1/usernum2
#     print("Your result of dividing is:", result)
# except ZeroDivisionError:
#     print("Black Hole was created. Please don't divide by zero in the future. You can not divide by zero")
# finally:
#     print("Thank you for using this simple program")

#4.Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, 
# який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) . 
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.
daysdict = {'Monday':1 , 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}
week_day = int(input("Enter week day: "))
try:
    if week_day = 1
        print()
except :
    print("")
finally:
    print("Thank you for using this simple program")


