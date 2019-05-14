# for x in range(0, 100, 2):
#     print (x)
#     if x == 26:
#         break

################  MOON  CALCULATIONS ##############################
# 2019 13.860000000000001
# 2020 14.025
# 2021 14.190000000000001
# my_kg=float(84)
# moon_k=float(0.165)
# for year in range(2019, 2025):
#     my_moon_kg=my_kg*moon_k
#     if my_moon_kg >= 14.5:
#         break
#     print(year, my_moon_kg)
#     my_kg+=1

# counter=int(1)
# ingredients = ['bread', 'butter', 'salami', 'ketchup', 'tomato']
# for x in ingredients:
#     print (counter, x)
#     counter+=1

#def moon_weight(my_kg, k_year_increase )
my_kg=float(84)
moon_k=float(0.165)
kg_year_increase=1
year_start=2019
year_end=2050
for year in range(year_start, year_end):
    my_moon_kg=my_kg*moon_k
    # if my_moon_kg >= 14.5:
    #     break
    print(year, my_moon_kg)
    my_kg+=kg_year_increase