from csv import reader
#from Collections import OrderedDict
from statistics import mean 
from os import getcwd
#print (getcwd()+"\\"[0]+"1.csv",getcwd()+"\\"[0]+"0.csv")

def calculate_averages (input_file_name, output_file_name):
    e = list()
    r = open (output_file_name,"w")
    sss = str()
    with open (input_file_name) as f :
        d = reader(f)
        #print (list(d))
        for aa in list(d):
            #print (aa)
            for ds in range (1,len(aa)) :
                aa [ds] = int(aa [ds])
            pr = ([aa[0],mean(aa[1:])])
            e.append (pr)
    #print (r)
    for l in e: 
        #print (l)
        sss = (str(l[0])+","+str(l[1]))
        if l != (e [len(e)-1]):
            r.write (sss+'''
''')
        else:
            r.write (sss)
    r.close ()

    


def calculate_sorted_averages (input_file_name, output_file_name):
    r = open (output_file_name,"w")
    m = dict()
    cc = list()
    sss = str()
    with open (input_file_name) as f :
        d = reader(f)
        po = list(d)
        oio = int(len(po))
        for aa in po:
            for ds in range (1,len(list(aa))) :
                aa [ds] = int(aa [ds])
            m [aa[0]]=mean(aa[1:])
            cc.append (aa[0])
        for lk in range (0,oio):
            for lm in range (0,oio):
                if m[cc[lm]] < m[cc[lk]] :
                    nnnn = cc[lm]
                    cc[lm] = cc[lk]
                    cc[lk] = nnnn
                elif cc[lm] < cc[lk] and m[cc[lm]] == m[cc[lk]]:
                    nnnn = cc[lm]
                    cc[lm] = cc[lk]
                    cc[lk] = nnnn
        for ol in cc :
            sss = (str(ol)+","+str(m[ol]))
            if ol != cc [len(cc)-1]:
                r.write (sss+'''
''')
            else:
                r.write (sss)

    r.close ()



            



    

def calculate_three_best (input_file_name, output_file_name):
    r = open (output_file_name,"w")
    m = dict()
    cc = list()
    sss = list()
    with open (input_file_name) as f :
        d = reader(f)
        po = list(d)
        oio = int(len(po))
        for aa in po:
            for ds in range (1,len(list(aa))) :
                aa [ds] = int(aa [ds])
            m [aa[0]]=mean(aa[1:])
            cc.append (aa[0])
        for lk in range (0,oio):
            for lm in range (0,oio):
                if m[cc[lm]] > m[cc[lk]] :
                    nnnn = cc[lm]
                    cc[lm] = cc[lk]
                    cc[lk] = nnnn
                elif cc[lm] > cc[lk] and m[cc[lm]] == m[cc[lk]]:
                    nnnn = cc[lm]
                    cc[lm] = cc[lk]
                    cc[lk] = nnnn
        for oz in range (len(cc)-3,len(cc)) :
            ol = cc[oz]
            sss.append  (str(ol)+","+str(m[ol]))
        for cma in range (0,3):
            cmb = 2 - cma
            if cma != 2:
                r.write (sss[cmb]+'''
''')
            else:
                r.write (sss[cmb])
    r.close ()

    


def calculate_three_worst (input_file_name, output_file_name):
    r = open (output_file_name,"w")
    m = dict()
    cc = list()
    sss = str()
    with open (input_file_name) as f :
        d = reader(f)
        po = list(d)
        oio = int(len(po))
        for aa in po:
            for ds in range (1,len(list(aa))) :
                aa [ds] = int(aa [ds])
            m [aa[0]]=mean(aa[1:])
            cc.append (aa[0])
        for lk in range (0,oio):
            for lm in range (0,oio):
                if m[cc[lm]] > m[cc[lk]] :
                    nnnn = cc[lm]
                    cc[lm] = cc[lk]
                    cc[lk] = nnnn
                elif cc[lm] > cc[lk] and m[cc[lm]] == m[cc[lk]]:
                    nnnn = cc[lm]
                    cc[lm] = cc[lk]
                    cc[lk] = nnnn
        for obe in range (0,3) :
            ol = cc [obe]
            sss = (str(m[ol]))
            if obe != 2 :

                r.write (sss+'''
''')
            else :
                r.write (sss)
    r.close ()
    


def calculate_average_of_averages(input_file_name, output_file_name):
    e = list()
    r = open (output_file_name,"w")
    sss = str()
    ddd = list ()
    with open (input_file_name) as f :
        d = reader(f)
        #print (list(d))
        for aa in list(d):
            #print (aa)
            for ds in range (1,len(aa)) :
                aa [ds] = int(aa [ds])
            pr = ([aa[0],mean(aa[1:])])
            e.append (pr)
    #print (r)
    for l in e: 
        ddd.append(l[1])
        #print (l)
    sss = (str(mean(ddd)))
    r.write (sss)
    r.close ()




calculate_average_of_averages  (str(getcwd()+"\\"[0]+"3.csv"),str(getcwd()+"\\"[0]+"0.csv"))










