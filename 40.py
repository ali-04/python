
from re import findall 
w = input()



def list_get (lis,x,y):
    if len(lis) > x :
        return lis[x]
    else:
        return y




def in1 (x):
    return findall("^[\w\d]+@\w+\.[\w]+$",x)



if findall(".+@[^\d]+\.[^\d]+",list_get(in1(w),0,'')) == []:
    print ('WRONG')
else:
    if findall('[^\d]',list_get(findall ('^(.+)@',w),0,'')) != []:
        print('OK')
    else:
        print ('WRONG')