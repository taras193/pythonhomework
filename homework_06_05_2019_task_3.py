#Поміняти між собою значення двох змінних, не використовуючи третьої змінної.

a = input("Enter first value 1:\")
b = input("Enter second value 2:\")

a, b = b, a

print(a)
print(b)