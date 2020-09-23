import hashlib
import csv
#from os import getcwd

def hash_password_hack(input_file_name, output_file_name):
    r = open (output_file_name,"w")
    with open (input_file_name) as f :
        inp = list(csv.reader(f))
        javab = dict()
        lbar = list()
        mains = dict()
        jkeys=list()
        
        for x in inp:
            mains [x[1]]= x[0]
            lbar.append (x[1])
            jkeys.append (x[0]) 
        for rain in range (0,9999):
            if lbar == []:
                break
            if rain<1000:
                if rain >99:
                    ra = '0' + str(rain)
                elif rain > 9 or rain == 99 :
                    ra = '00' + str(rain)
                elif rain < 10 :
                    ra = '000' + str(rain)
            else:
                ra = str(rain)
            ran = bytes(ra,'utf-8')
            xx = hashlib.sha256(ran).hexdigest()
            for y in lbar :
                if xx == y :
                    javab[mains[xx]] = ra
                    lbar.remove(xx)
    for ttt in jkeys:
        if ttt != jkeys[len(jkeys)-1]:
            r.write(str(ttt)+','+str(javab[ttt])+'''
''')
        else:
            r.write(str(ttt)+','+str(javab[ttt]))
    r.close


#hash_password_hack  (str(getcwd()+"\\"[0]+"1.csv"),str(getcwd()+"\\"[0]+"0.csv"))