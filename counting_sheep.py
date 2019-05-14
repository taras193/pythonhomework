#Consider an array of sheep where some sheep may be missing from their place. 
#We need a function that counts the number of sheep present in the array (true means present).
def count_sheeps(arrayOfSheeps):
    a=int(0)
    for x in (arrayOfSheeps):
        if x==1: 
            a+=1
    return a