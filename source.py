from csv import reader
#from Collections import OrderedDict
from statistics import mean 
from os import getcwd
#print (getcwd()+"\\"[0]+"1.csv",getcwd()+"\\"[0]+"0.csv")

def calculate_averages (input_file_name, output_file_name):
    e = list()
    r = open (output_file_name,"w")
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
        r.write (sss+'''
''')
    r.close ()

    


def calculate_sorted_averages (input_file_name, output_file_name):
    r = open (output_file_name,"w")
    m = dict()
    cc = list()
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
        for ol in cc :
            sss = (str(ol)+","+str(m[ol]))
            r.write (sss+'''
''')
    r.close ()



            



    
    


#def calculate_three_best(input_file_name, output_file_name):
    


#def calculate_three_worst(input_file_name, output_file_name):
    


#def calculate_average_of_averages(input_file_name, output_file_name):
    
#calculate_sorted_averages  (str(getcwd()+"\\"[0]+"1.csv"),str(getcwd()+"\\"[0]+"0.csv"))









