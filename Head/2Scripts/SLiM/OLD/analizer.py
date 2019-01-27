#coding=utf8

import os
import sys, string


# PARSE OUTPUT



path="report.txt"
report = open(path, "w")
        



#path3="alidirreps_test81_logs.txt"

#reps3 = open(path3, "w")

#fname = f[:-7].split("_")
#    lname= fname[1]
#    for fn in fname[2:]:
#        lname=lname+"_"+fn
#    print lname   
#    n=0
#    # Открытие файла с геномами
#    pgen = open(pgen_path,'r')
#    # Выбор нужного вида в файле геномов 
#xersh = genome.count("X") # Подсчет количества иксов    
	
	
files=os.listdir("sim0")	

if not os.path.exists("sim0reps"):
    os.makedirs("sim0reps")

reparr=[]

        
	
for f in files:	
	
    prepath = "sim0/"
    pgen = open(prepath+f,'r')
	
    path="sim0reps/report%s.txt" % f[:-4]
    reps = open(path, "w")
	
    gencount = 0
    globmutcount = 0
	
    while True: 
        row = pgen.readline() 
        #print (row)
        if row.strip()=="Genomes:":
            break
		
    while True: 
        row = pgen.readline() 
        #print (row)
        if row.strip()=="":
            break
        arr = row.split(" ")
	
        mutcount = len(arr[2:])
		
        reps.write("%s %s\n" % (arr[0],mutcount))
		
        gencount = gencount + 1
        globmutcount = globmutcount + mutcount

    pgen.close
	
	
    reparr.append([f[:-4],globmutcount/gencount])	


for rep in reparr:
    report.write("%s %s\n" % (rep[0],rep[1])) 	

   
           

  

