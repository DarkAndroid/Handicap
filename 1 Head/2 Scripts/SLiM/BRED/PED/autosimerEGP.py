#coding=utf8

import os
import sqlite3
import sys, string
import shutil



eps = [0.00001,0.00001,0.0001,0.001,0.01,0.1,1.0]
gszs = [999,9999,99999,999999]
pszs = [1000,10000,100000,1000000]


n=0


for p in pszs:
    for g in gszs:
        for e in eps:


            # GENERATE SIMULATIONS
            

            

            print ("SIMULATION #%s :: %s : %s : %s \n" % (n,p,g,e))

            if not os.path.exists("sim%s" % n):
                os.makedirs("sim%s" % n)

            path=("sim%s.slm" % n)
            reps = open(path, "w")
            #reps.write("%s %s %s %s\n" % (oi,words[oi],oj,words[oj]))


            #// set up a simple neutral simulation
            reps.write("initialize() {\n")
            reps.write("	initializeMutationRate(1e-07);\n")
	
            #// m1 mutation type: neutral
            reps.write("	initializeMutationType(\"m1\", 0.5, \"f\", -%f);\n" % e)

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

            for i in range(1,101):

                reps.write("%s late() { sim.outputFull(\"sim%s/sim%s_%s.out\");\n" % (i*100,n,n,i*100))
                reps.write("subpop = sim.subpopulations[sim.subpopulations.id == 1];\n")
                reps.write("s = subpop.individualCount;\n")
                reps.write("inds = subpop.individuals;\n")
              
                reps.write("for (i in inds){\n")
                reps.write("    writeFile(\"sim%s.out\", \"%s \" + i.pedigreeID +\"   \" + i.pedigreeParentIDs, append=T);\n" % (n,i*100))
                reps.write("    writeFile(\"simGP%s.out\", \" \" +i.pedigreeGrandparentIDs, append=T);\n")
                reps.write("}\n")
                reps.write("}\n")

            reps.close()






            # EXECUTE SIMULATION

            # ./slim death.slm

            # LINUX CODE
            os.system('/home/jester/VIC/build/./slim sim%s.slm' % n)






            # PARSE OUTPUT
            path="report%s.txt" % n
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
	
	
            files=os.listdir("sim%s" % n)	

            if not os.path.exists("sim%sreps" % n):
                os.makedirs("sim%sreps" % n)

            reparr=[]

        
	
            for f in files:	
	
                prepath = "sim%s/" % n
                pgen = open(prepath+f,'r')
	
                path="sim%sreps/report%s.txt" % (n,f[:-4])
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
	
	
                reparr.append([int(f[:-4].split("_")[1]),globmutcount/gencount])	

            reparr.sort()

            for rep in reparr:
                report.write("%s %s\n" % (rep[0],rep[1])) 	

            report.close()

            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sim%s' % n)
            shutil.rmtree(path)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sim%sreps' % n)
            shutil.rmtree(path)



            # ANALIZE AND WRITE IN RESULTS





            n = n + 1


