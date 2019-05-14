#1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.
# values=[]
# a=(input('Enter values'))
# values.extend(a)
# print (max(values))
# print (min(values))

# amount_of_values=input(int('Please input amount of values to compare')
# for a in range(amount_of_values)

# 2.  В інтервалі від 1 до 10 визначити числа 
# -парні, які діляться на 2,
# -непарні, які діляться на 3, 
# -числа, які не діляться на 2 та 3.



# div2=[x for x in range(1,11) if x%2==0]
# print (div2)
# div3=[x for x in range(1,11) if x%3==0]
# print(div3)
# divelse=[x for x in range(1,11)if x%2!=0 if x%3!=0]
# print(divelse)

# for x in range(1, 11):
#     if x % 2 == 0:
#         print(x, 'is even multiple of 2')
#     elif x % 3 == 0:
#         print(x, 'is an odd multiple of 3')
#     else:
#         print(x, 'not divisible by 2 and 3')

#4 Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while) 
# login=input('Enter a login here') 
# logval='first'
# while login!=logval:
#     print('Login is invalid, please try one more time')
#     login=input('Enter a login here') 
# else: print('Congratulations, your login is approved')

# 5.  Перший випадок. 
# Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число. При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).
num=input(int('Enter a value'))
while num>0:
    print('Enter one more value')
    num=input(int('Enter a value'))
else: print('There was negative number meet')