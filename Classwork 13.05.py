# import pyowm
# city=input("What city you are interested:\n")
# owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')    

# observation = owm.weather_at_place(city)
# w = observation.get_weather()
# temperature=w.get_temperature('celsius')['temp']

# print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")
# print("In this city "+ w.get_detailed_status()+", wind speed is "+str(w.get_wind()["speed"])+"m/s, humidity is "+str(w.get_humidity())+"%.")

# 1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 
# і пропонує користувачу вгадати це число. Програма зчитує числа, які вводить користувач і 
# видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем. 
# Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання. 
# (для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())

# from random import randint
# secretnum = randint(1,100)
# print (secretnum)
# usernum=int(input('Set a number in range 1-100:'))
# while usernum == secretnum:
#     print('You guessed the number!')
    
# else: 
#     print("Try again!")
#     usernum=int(input('Set a number in range 1-100:'))

# 2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
#(для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).
TO DO 