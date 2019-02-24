#coding=utf8

import os
import sqlite3
import sys, string
import shutil

#import numpy as np
#import matplotlib.pyplot as plt

mrts = [5] # NOTHING MEANS
eps = [0.00001] # NOTHING MEANS
gszs = [9999] # NOTHING MEANS
pszs = [10000] # NOTHING MEANS


n=0


for p in pszs: # NOTHING MEANS
    for g in gszs: # NOTHING MEANS
        for e in eps: # NOTHING MEANS
            for m in mrts: # NOTHING MEANS
                for j in range(1): # NOTHING MEANS


                    # GENERATE SIMULATIONS
            

            

                    print ("SIMULATION #%s :: %s\n" % (n,m))

                    #if not os.path.exists("sims"):
                    #    os.makedirs("sims")
                    #if not os.path.exists("sim%sfix" % n):
                    #    os.makedirs("sim%sfix" % n)

                    #path=("sim%s.slm" % n)
                    #reps = open(path, "w")
                    #reps.write("%s %s %s %s\n" % (oi,words[oi],oj,words[oj]))





                    # GENERATE FILE avida.cfg

                    fsrc = "default/avida.cfg"
                    fdst = "avida.cfg"
                    shutil.copyfile(fsrc, fdst)

                    with open ('avida.cfg', 'r') as f:
                        old_data = f.read()

                    new_data = old_data.replace('WORLD_X 60', 'WORLD_X %s' % m)
                    new_data = new_data.replace('WORLD_Y 60', 'WORLD_Y %s' % m)

                    with open ('avida.cfg', 'w') as f:
                        f.write(new_data)


                    # GENERATE FILE default-heads.org
					
                    fsrc = "default/default-heads.org"
                    fdst = "default-heads.org"
                    shutil.copyfile(fsrc, fdst)				
					
					
                    # GENERATE FILE events.cfg
					
                    fsrc = "default/events.cfg"
                    fdst = "events.cfg"
                    shutil.copyfile(fsrc, fdst)					
					
					
                    # GENERATE FILE environment.cfg

                    fsrc = "default/environment.cfg"
                    fdst = "environment.cfg"
                    shutil.copyfile(fsrc, fdst)




                    # EXECUTE SIMULATION

                    # WINDOWS CODE
                    #os.system(r'c:/"Program Files"/"Mozilla Firefox"/firefox.exe')
                    os.system('avida.exe')

                    os.remove("avida.cfg")
                    os.remove("default-heads.org")
                    os.remove("events.cfg")
                    os.remove("environment.cfg")


                    #shutil.copytree("data", "data1")
                    os.rename("data", "data%s" % n)


                    """


                    # ANALIZE AND WRITE IN RESULTS
                    path="sims/sim%s.out" % n
                    pgen = open(path, "r")

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
    

                    

                    # DotPlot
                    plt.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')
                    plt.title('Sim%s: $pop:%s$ $gnm:%s$ $sel:%s$ $mtrt:%s$' % (n,p,g+1,e*j,m))
                    plt.xlabel('$Population$ $(every$ $hundredth)$')
                    plt.ylabel('$Average$ $number$ $of$ $mutations$')
                    plt.savefig('sim%sdot.png' % n, dpi = 300)
                    plt.close()



                    # LinePlot
                    plt.plot(x, y, lw = 1, color = '#539caf', alpha = 1)
                    plt.title('Sim%s: $pop:%s$ $gnm:%s$ $sel:%s$ $mtrt:%s$' % (n,p,g+1,e*j,m))
                    plt.xlabel('$Population$ $(every$ $hundredth)$')
                    plt.ylabel('$Average$ $number$ $of$ $mutations$')
                    plt.savefig('sim%sline.png' % n, dpi = 300)
                    plt.close()  



                    pgen.close()
 
                    """
					
                    n = n + 1