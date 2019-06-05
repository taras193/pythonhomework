

number_to = int(input("Enter amount of numbers"))

def adding(nn):
    return(nn[-2]+nn[-1])

fib2 = [0,1]

while fib2[-1] < number_to:
    fib2.append(adding(fib2))

for fbfb in fib2:
    if fbfb > number_to:
        fib2.remove(fbfb)

print(str(fib2))