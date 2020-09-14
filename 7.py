import random

ma = 99
mi = 1

j = random.randint(mi,ma)

print (j)
g = input()

while g != "d" :
    if g == "k" :
        ma = j - 1
    elif g == "b" :
        mi = j + 1
    
    j = random.randint(mi,ma)

    print (j)
    g = input()


print ("ye chizi mishi!")        























