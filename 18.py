asl = input ().lower()
p = ""

for k in range (0,len (asl)):
    # print ((len (asl)-1) - k)
    p += asl  [(len (asl)-1) - k]

#print (p)

if asl == p:
    print ("palindrome")
else:
    print ("not palindrome")
























