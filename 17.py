asl = input ()
cad = asl.upper()
o = 0

for b in range (0,len (asl)):
    if asl[b] == cad[b]:
        o += 1
    else:
        o -= 1

if o <= 0:
    j = asl.lower()
else:
    j = asl.upper()         

print (j)

























