#1.  Спробуйте переписати наступний код через map. Він приймає список реальних імен і замінює їх прізвищами, використовуючи  більш надійний метод.
# names = ['Sam', 'Don', 'Daniel'] 
# hasnames = map(hash, names)
# print (list(hasnames))

#2.Вивести список кольору “red”, який найчастіше зустрічається в даному списку  
#[“red”, “green”, “black”, “red”, “brown”, “red”, “blue”, “red”, “red”, “yellow” ]
#використовуючи функцію filter.
# color_names=['red', 'green', 'black', 'red', 'brown', 'red', 'blue', 'red', 'red', 'yellow']
# result = list(filter(lambda x: x =='red' , color_names))
# print(result)

#

# names1 = ['Amir', 'Barry','Chales', 'Dao']
# names2 = names1
# names3 = names1[:]

# names2[0]= 'Alice'
# names3[1]= 'Bob'

# sum = 0
# for ls in (names1, names2, names3):
#     if ls[0] == 'Alice':
#         sum += 1
#     if ls[1] == 'Bob':
#         sum += 10

# print(sum)

# print (0XA + 0xa)

# def dostuff(param1, *param2):
#     print(type(param2))

# dostuff('apples', 'bananas', 'cherry', 'dates')

# class parent:
#     def __init__(self, param):
#         self.v1 = param
# class child(parent):
#     def __init__(self,param):
#         self.v2 = param
# obj=child(11)
# print(obj.v1 + " " + obj.v2)

# class Person:
#     def __init__(self,id):
#         self.id = id
# obama = Person(100)

# obama.__dict__['age']=49
# print(obama.age +len(obama.__dict__))

# kvps = {'1': 1, '2': 2}
# theCopy = kvps.copy()

# kvps['1']=5
# sum =kvps['1'] +theCopy['1']
# print(sum)

