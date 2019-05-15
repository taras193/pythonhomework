# i = 5
# while i <15:
#     print (i)
#     i=i + 2

# for i in 'hello world':
#     print(i * 2, end='+')
    #end доукомплектовує в кінці кожної ітерації ті символи що в лапках

# spisok = [1-, 40, 20, 30]
# i=0
# while i < len(spisok):
#     spisok[i] = spisok[i] + 2
#     i=i + 1
#     print(spisok)

# for i in 'helllo world':
#     if i == 'o':
#         continue 



#Loop while#
# i = 0
# while i<101:
#     print (i, end=' ')
#     i=i + 2 

#Loop for#
# for i in range(1,100,2):
#     print(i, end=' ')

#brake#
# spisok = (2,4,5,6,7,8,9,10)
# for item in spisok:
#     if i % 2 ==1:
#     break
# print ("There is odd number in the list") if i % 2 ==1

# 1.  Роздрукувати всі парні числа менші 100 (написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for).
# 1.a
# nums = []
# for x in range (1,101):
#     if x%2 == 0:
#         nums.append(x)
# print(nums)

# 1.b
# nums = []
# i = 0
# while i <= 100:
#     i += 1
#     if i%2 == 0:
#         nums.append(i)
# print(nums)

# 2. Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).
# # 2.a
# odd = []
# for x in range (1,101):
#     if x%2 != 0:
#         odd.append(x)
#         continue
# print(odd)
# # 2.b
# odd2 = []
# i = 1
# while i > 0:
#     odd2.append(i)
#     i += 2
#     if i >= 100:
#         break
# print(odd2)

# # 3.Перевірити чи список містить непарні числа.
# # використати оператор break
# listnumm = (6, 4, 8, 6, 5, 4)
# for y in listnumm:
#     if y%2 != 0:
#         print("Has odd numbers")
#         break
# else: 
#     print("Has only even numbers")

# # 4. Створити список, який містить елементи цілочисельного типу, потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою. 
# # (Підказка: використати вбудовану функцію float ()).
# listfloat = []
# for integ in listnumm:
#     listfloat.append(float(integ))
# print(listfloat)

# 5. Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
#TO DO

# 6. Створити список, що складається з чотирьох елементів типу string. Потім, за допомогою циклу for, вивести елементи по черзі на екран.
# listforprint = ["element1","element2","element3","element4"]
# for x in listforprint:
#     print(x)

# 7. Змінити попередню програму так, щоб в кінці кожної букви елементів при виводі додавався певний символ, наприклад “#”.
# symb = "'"
# for x in listforprint:
#     for y in x:
#         print(y, end=symb)
#     print()