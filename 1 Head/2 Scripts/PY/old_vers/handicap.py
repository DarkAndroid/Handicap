#coding=utf8

# Подключение библиотек
import os 
import random

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

def extractWordsTen(s, alphabet):
    arr = []
    n=10
    for i in range(len(s)-n+1):
        arr.append(''.join(s[i:i+n]))
    return arr

# Получение последовательности комплиментарной относительно данной
def compmaster (seq1):    
    arr1=[]
    s2=""
    for char in seq1:
        if char=='A':
            arr1.append('T')
        elif char=='T':
            arr1.append('A')
        elif char=='G':
            arr1.append('C')
        elif char=='C':
            arr1.append('G')
        else:
            arr1.append('N')
    s2=(''.join(arr1))
    return s2

# Получение последовательности зеркальной относительно данной
def polimaster (seq1):
    arr2=[]
    s3=""
    for char in seq1:
        arr2.append(char)
    s3=(''.join(reversed(arr2)))  
    return s3

# Получение последовательности инвертированной относительно данной
def invertmaster (seq1):   
    arr1=[]
    s2=""
    for char in seq1:   
        if char=='A':
            arr1.append('T')
        elif char=='T':
            arr1.append('A')
        elif char=='G':
            arr1.append('C')
        elif char=='C':
            arr1.append('G')
        else:
            arr1.append('N')
    arr3=reversed(arr1)
    s4=""  
    s4=(''.join(arr3))  
    return s4

# Вычисление расстояния Левенштеина между двумя последовательностями
def lev(s, t):
    if s == t: return 0
    elif len(s) == 0: return len(t)
    elif len(t) == 0: return len(s)
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]
    return v1[len(t)]



def raritet (stand):
    #print ("raritet")
    
    a=random.randrange(0, 2, 1)

    #print (a)
    
    b=random.randrange(0, 2, 1)
    c=random.randrange(0, 2, 1)

    
    if a==1 and b==1 and c==1:
    #if a==1 and b==1:
    #if a==1:
        
        #print ("HANDICAP")
        #input()
        return [stand+100,1]
    else:
        return [stand,0]
    


def regen (arr):
    newarr=[]
    #for a in range(0,len(arr),2):
    newborn=raritet((arr[0][0]+arr[len(arr)-1][0])/2+random.randrange(0, 5, 1))
    if newborn[0]<1200:
        newarr.append(newborn)
    for a in range(1,len(arr)):
        newborn=raritet((arr[a][0]+arr[a-1][0])/2+random.randrange(0, 5, 1))
        if newborn[0]<1200:
            newarr.append(newborn)
        #del arr[a]
        #del arr[a-1]
    return newarr
        




ppltn=[]
print ("Init")
for n in range(0,10000):
    ran=random.randrange(900, 1100, 1)
    ppltn.append([ran,0])
    


path="start.csv"
reps = open(path, "w")
for ind in ppltn:
    reps.write("%s;%s\n" % (ind[0],ind[1]))
    



for n in range(10):
    print ("Generation %s" % n)
    ppltn=regen(ppltn)




path2="finish.csv"
reps2 = open(path2, "w")
for ind in ppltn:
    reps2.write("%s;%s\n" % (ind[0],ind[1]))
