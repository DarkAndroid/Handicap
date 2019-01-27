#coding=utf8

import os 
import random

#import xlwt

import numpy as np
import matplotlib.pyplot as plt

import re


files=os.listdir("REPORTS") 


for f in files:

    print (f)

    prepath = "REPORTS/"
    pgen = open(prepath+f,'r')
	
    prearr=[]
    #ppltn=np.empty((0,3), int)

		
    while True: 
        row = pgen.readline() 
        #print (row)
        if row.strip()=="":
            break
        arr = row.split(" ")
        #print (arr[1].strip())		
        prearr.append([int(arr[0]),int(arr[1].strip())])
					
    ppltn = np.array(prearr)				
	
    #print (ppltn)


    
    fig = plt.figure()
    '''
    plt.hist(ppltn)
    plt.title('Simple histogramm')
    plt.grid(True)
    '''
    x = ppltn[:,0]
    y = ppltn[:,1]
	
    plt.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')
    #plt.title('Scatter: $x$ versus $y$')
    plt.xlabel('$Population$ $(every$ $hundredth)$')
    plt.ylabel('$Average$ $number$ $of$ $mutations$')
	
    plt.savefig('%s.png' % f[:-4])
	
    pgen.close()
    plt.close()