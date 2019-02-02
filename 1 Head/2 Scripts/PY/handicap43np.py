#coding=utf8

# Подключение библиотек
import os 
import random

import xlwt

import numpy as np
import matplotlib.pyplot as plt

import re


# Указание файла с геномами
#pgen_path = 'genomes.fa'
# Ввод путей к базам данных и геному
'''
if __name__ == "__main__":
    if len (sys.argv) > 1:
        files = os.listdir(sys.argv[1])
        prepath=("%s\\" % (sys.argv[1]))
    elif len (sys.argv) > 2:
        files = os.listdir(sys.argv[1])
        prepath=("%s\\" % (sys.argv[1]))
        pgen_path = sys.argv[2]
pgen = open(pgen_path,'r')
nucAlphabet = {'a', 't', 'g', 'c', 'x'}
xersh=0
'''



def raritet (stand):
    #print ("raritet")
    
    #a=random.randrange(0, 2, 1)

    #print (a)
    
    #b=random.randrange(0, 2, 1)
    #c=random.randrange(0, 2, 1)

    
    #if a==1 and b==1 and c==1:

    #if a==1 and b==1:
    #if a==1:
        
        #print ("HANDICAP")
        #input()

    r=random.randrange(1, 1001, 1)


    if r==1000:
        return [stand+100,1]
    else:
        return [stand,0]



def childs ():
    #print ("raritet")
    
    a=random.randrange(0, 2, 1)
    b=random.randrange(0, 2, 1)
    c=random.randrange(0, 2, 1)

        
    return a+b+c
    


def regen (arr):
    newarr=np.array([])
    #for a in range(0,len(arr),2):
    
    #print (arr[0])
    chi=random.randrange(1, 2, 1)
    for ch in range(chi):
        newborn=raritet((arr[0][0]+arr[len(arr)-1][0])/2+random.randrange(0, 5, 1))
        if newborn[0]<1200:
            newarr=np.array([newborn])
    for a in range(1,len(arr)):
        chi=random.randrange(1, 2, 1)
        for ch in range(chi):
            newborn=raritet((arr[a][0]+arr[a-1][0])/2+random.randrange(0, 5, 1))
            if newborn[0]<1200:
                if len(newarr)==0:
                    newarr=np.array([newborn])
                else:
                    newarr=np.vstack((newarr,newborn))
                #del arr[a]
                #del arr[a-1]
    return newarr
        








def output(filename, sheet, list1):
    book = xlwt.Workbook()
    sh = book.add_sheet(sheet, cell_overwrite_ok=True)


    col1_name = 'mut'
    col2_name = 'han'

    rowc=0

    sh.write(rowc, 0, col1_name)
    sh.write(rowc, 1, col2_name)
    
    rowc=1

    for m in list1:
        #print (m)
        #print (e1)
        #print (rowc)
        #print (rowc)
        #print (m)
        sh.write(rowc, 0, int(m[0]))
        rowc+=1

    rowc=1

    for m in list1:
        #print (rowc)
        
        sh.write(rowc, 1, int(m[1]))
        rowc+=1

    book.save(filename)






dpoi=np.random.poisson(1000, 10000)






#ppltn=np.random.poisson(1000, (1, 10000,2))

print ("Init")
'''
for n in range(0,10):
    ran=random.randrange(900, 1100, 1)
    ppltn.append([ran,0])
'''
ppltn=np.array([[dpoi[0],0]])
for n in range(1,len(dpoi)):
    #ran=random.randrange(900, 1100, 1)
    #print (np.array([dpoi[n],0]))
    ppltn=np.vstack((ppltn,[dpoi[n],0]))

#print (ppltn)
    

'''
path="start.csv"
reps = open(path, "w")
for ind in ppltn:
    reps.write("%s;%s\n" % (ind[0],ind[1]))
'''    
output("simulation_start.xls", "start", ppltn)


print ("Simulation")

for n in range(100):
    print ("Generation %s" % n)
    ppltn=regen(ppltn)
    # hist()
    fig = plt.figure()
    plt.hist(ppltn[:,0],100)
    plt.title('Simple histogramm')
    plt.grid(True)
    plt.savefig('filename%s.png' % n, dpi = 300)



'''
path2="finish.csv"
reps2 = open(path2, "w")
for ind in ppltn:
    reps2.write("%s;%s\n" % (ind[0],ind[1]))
'''

output("simulation_finish.xls", "finish", ppltn)