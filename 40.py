from re import findall 
w = input()
def in1 (x):
    return findall("^[\w\d]+@\w+\.[\w]+$",x)

if findall(".+@[^\d]+\.[^\d]+",in1(w)[0]) == []:
    print ('WRONG')
else:
    if findall('[^\d]',findall ('^(.+)@',w)[0]) != []:
        print('OK')
    else:
        print ('WRONG')