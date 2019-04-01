#coding=utf8

import os
import sqlite3
import sys, string
import shutil

import numpy as np
import matplotlib.pyplot as plt

mrts = ["1e-05","1e-06"]    #  ["1e-09","1e-08","1e-07"]            1e-7 или 0.0000001 => от 1/kkk (1e-06 peregruzka po pamyati)
eps = ["1e-01","1e-02","1e-03"]
gszs = [99999]
pszs = [10000]# [100000]
gnrtn = 1000


n=0


for p in pszs:
    for g in gszs:
        for e in eps:
            for m in mrts:
                for j in range(1):


                    # GENERATE SIMULATIONS
            

            

                    print ("SIMULATION #%s :: %s : %s : %s \n" % (n,p,g,e))

                    if not os.path.exists("sims"):
                        os.makedirs("sims")
                    #########################################################################################################
                    # if not os.path.exists("sim%sfix" % n):
                    #     os.makedirs("sim%sfix" % n)

                    path=("sim%s.slm" % n)
                    reps = open(path, "w")
                    #reps.write("%s %s %s %s\n" % (oi,words[oi],oj,words[oj]))


                    #// set up a simple neutral simulation
                    reps.write("initialize() {\n")
                    reps.write("	initializeMutationRate(%s);\n" % m)
	
                    #// m1 mutation type: neutral
                    reps.write("	initializeMutationType(\"m1\", 0.5, \"f\", -%s);\n" % e) # normal ?  itializeMutationType("m2", 0.5, "n", 0.0, 1.0);   // QTL
				
				    #// Off fixation of mutations
                    reps.write("	m1.convertToSubstitution = F;\n")

                    #// g1 genomic element type: uses m1 for all mutations
                    reps.write("	initializeGenomicElementType(\"g1\", m1, 1.0);\n")
	
                    #// uniform chromosome of length 100 kb with uniform recombination
                    reps.write("	initializeGenomicElement(g1, 0, %s);\n" % g)
                    reps.write("	initializeRecombinationRate(1e-8);\n")
                    reps.write("}")

                    #// create a population of 500 individuals
                    reps.write("1 {")
                    reps.write("	sim.addSubpop(\"p1\", %s);\n" % p)
                    reps.write("}")

                    #// output samples of 10 genomes periodically, all fixed mutations at end
                    #reps.write("1000 late() { p1.outputSample(10); }\n")
                    #reps.write("2000 late() { p1.outputSample(10); }\n")
                    #reps.write("1000 late() { sim.outputFixedMutations(); }\n")
                    #reps.write("1000 late() { sim.outputFull(); }\n")
                    #reps.write("1000 late() { sim.outputFull(\"/tmp/slim_\" + simID + \".txt\"); }\n")
                    #reps.write("1000 late() { sim.outputFull(\"sim%s.out\"); }\n" % n)

                    for i in range(1,gnrtn+1):

                        #reps.write("%s late() { sim.outputFull(\"sim%s/sim%s_%s.out\"); }\n" % (i*100,n,n,i*100))
                        #reps.write("%s late() { sim.outputFixedMutations(\"sim%sfix/sim%s_%s.out\"); }\n" % (i*100,n,n,i*100))

                        reps.write("%s late() {\n" % (i))

                        reps.write("subpop = sim.subpopulations[sim.subpopulations.id == 1];\n")
                        #reps.write("s = subpop.individualCount;\n")
                        reps.write("inds = subpop.individuals;\n")
                        reps.write("c1 = sum(inds.countOfMutationsOfType(m1));\n")
                        reps.write("writeFile(\"sims/sim%s.out\", \"%s \" + c1, append=T);\n" % (n,i))
                        #reps.write("catn(\"%s \" + c1);\n" % (i*100))
                        #########################################################################################################
                        # reps.write("p1.outputSample(100);\n")
                        # reps.write("sim.outputFixedMutations();\n")
                        #reps.write("sim.outputFull(\"sim%sfix/sim%s_%s.out\");\n" % (n,n,i))
                        reps.write("}\n")


                    reps.close()






                    # EXECUTE SIMULATION

                    # ./slim death.slm

                    # LINUX CODE
                    #os.system('./slim sim%s.slm' % n)
                    os.system('/home/jester/VIC/build/./slim sim%s.slm' % n)








                    # ANALIZE AND WRITE IN RESULTS
                    print ("\nANALIZING OF RESULTS\n")
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
                        prearr.append([int(arr[0]),float(float(arr[1].strip())/float(p))])
                            
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
                    # plt.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')
                    # plt.title('Sim%s: $pop:%s$ $gnm:%s$ $sel:%s$ $mtrt:%s$' % (n,p,g+1,e*j,m))
                    # plt.xlabel('$Population$ $(every$ $hundredth)$')
                    # plt.ylabel('$Average$ $number$ $of$ $mutations$')
                    # plt.savefig('sim%sdot.png' % n, dpi = 300)
                    # plt.close()



                    # LinePlot
                    plt.plot(x, y, lw = 1, color = '#539caf', alpha = 1)
                    plt.title('Sim%s: $pop:%s$ $gnm:%s$ $sel:%s$ $mtrt:%s$' % (n,p,g+1,e,m))
                    plt.xlabel('$Generation$')
                    plt.ylabel('$Average$ $number$ $of$ $mutations$')
                    plt.savefig('sim%s_pop%s_gnm%s_sel%s_mtrt%s.png' % (n,p,g+1,e,m), dpi = 300)
                    plt.close()  

                    




                    pgen.close()

                    n = n + 1

##################################################
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sims')
shutil.rmtree(path)