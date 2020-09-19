from csv import reader
#from Collections import OrderedDict
from statistics import mean 
from os import getcwd
#calculate_averages
def W (input_file_name, output_file_name):
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

    


def calculate_sorted_averages(input_file_name, output_file_name):
    
    


#def calculate_three_best(input_file_name, output_file_name):
    


#def calculate_three_worst(input_file_name, output_file_name):
    


#def calculate_average_of_averages(input_file_name, output_file_name):
    
#W  (getcwd()+"\\"[0]+"1.csv",getcwd()+"\\"[0]+"0.csv")










