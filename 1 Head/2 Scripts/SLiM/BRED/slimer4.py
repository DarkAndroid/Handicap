#coding=utf8

import os
import sqlite3
import sys, string
import shutil

import numpy as np
import matplotlib.pyplot as plt

mrts = ["1e-09"]    #  ["1e-09","1e-08","1e-07"]            1e-7 или 0.0000001 => от 1/kkk (1e-06 peregruzka po pamyati)
eps = [0.00001]
gszs = [9999]
pszs = [10000]


n=0


for p in pszs:
    for g in gszs:
        for e in eps:
            for m in mrts:
                for j in range(1):


                    # GENERATE SIMULATIONS
            

            

                    print ("SIMULATION #%s :: %s : %s : %s \n" % (n,p,g,e*j))

                    if not os.path.exists("sims"):
                        os.makedirs("sims")
                    #if not os.path.exists("sim%sfix" % n):
                    #    os.makedirs("sim%sfix" % n)

                    path=("sim%s.slm" % n)
                    reps = open(path, "w")
                    #reps.write("%s %s %s %s\n" % (oi,words[oi],oj,words[oj]))



                    reps.write("initialize() {\n") 
                    reps.write("    defineConstant(\"C\", 10);      // number of loci\n")
                    reps.write("\n")
                    reps.write("    // Create our loci\n")
                    reps.write("    for (locus in 0:(C-1))\n") 
                    reps.write("    {\n")
                    reps.write("        // Effects for the nucleotides ATGC are drawn from a normal DFE\n")  
                    reps.write("        //effects = rnorm(4, mean=30, sd=0.05);\n") # effects = rnorm(4, mean=0, sd=0.05);\n")
                    reps.write("\n")
                    reps.write("        // Each locus is set up with its own mutType and geType\n")  
                    reps.write("        mtA = initializeMutationType(locus*4 + 0, 0.5, \"f\", 0.0001);\n")  # mtA = initializeMutationType(locus*4 + 0, 0.5, \"f\", effects[0]);\n") 
                    reps.write("        mtT = initializeMutationType(locus*4 + 1, 0.5, \"f\", 0.0001);\n")  # mtT = initializeMutationType(locus*4 + 1, 0.5, \"f\", effects[1]);\n")
                    reps.write("        mtG = initializeMutationType(locus*4 + 2, 0.5, \"f\", 0.0001);\n")  # mtG = initializeMutationType(locus*4 + 2, 0.5, \"f\", effects[2]);\n")
                    reps.write("        mtC = initializeMutationType(locus*4 + 3, 0.5, \"f\", 0.0001);\n")  # mtC = initializeMutationType(locus*4 + 3, 0.5, \"f\", effects[3]);\n")
                    reps.write("        mt = c(mtA, mtT, mtG, mtC);\n")  
                    reps.write("        geType = initializeGenomicElementType(locus, mt, c(1,1,1,1));\n")  
                    reps.write("        initializeGenomicElement(geType, locus, locus);\n")
                    reps.write("\n")
                    reps.write("        // We do not want mutations to stack or fix\n")  
                    reps.write("        mt.mutationStackPolicy = \"l\";\n")  
                    reps.write("        mt.mutationStackGroup = -1;\n")  
                    reps.write("        mt.convertToSubstitution = F;\n")
                    reps.write("\n")
                    reps.write("        // Each mutation type knows the nucleotide it represents\n")  
                    reps.write("        mtA.setValue(\"nucleotide\", \"A\");\n")  
                    reps.write("        mtT.setValue(\"nucleotide\", \"T\");\n")  
                    reps.write("        mtG.setValue(\"nucleotide\", \"G\");\n")  
                    reps.write("        mtC.setValue(\"nucleotide\", \"C\");\n") 
                    reps.write("    }\n") 
                    reps.write("\n")
                    reps.write("    initializeMutationRate(1e-7);   // 1e-6 includes 25% identity mutations\n")
                    reps.write("    initializeRecombinationRate(1e-8);\n")
                    reps.write("}\n") 
                    reps.write("\n")
                    reps.write("1 late() {\n")
                    reps.write("    sim.addSubpop(\"p1\", 100);\n")
                    
                    reps.write("\n")
                    reps.write("    // The initial population is fixed for a single wild-type\n")
                    reps.write("    // nucleotide fixed at each locus in the chromosome\n") 
                    reps.write("    geTypes = sim.chromosome.genomicElements.genomicElementType;\n") 
                    reps.write("    mutTypes = sapply(geTypes, \"sample(applyValue.mutationTypes, 1,  weights=applyValue.mutationFractions);\");\n")
                    reps.write("    p1.genomes.addNewDrawnMutation(mutTypes, 0:(C-1));\n") 
                    reps.write("\n")
                    reps.write("    cat(\"Initial nucleotide sequence:\");\n") 
                    reps.write("    cat(\" \" + paste(mutTypes.getValue(\"nucleotide\")) + \"\\n\\n\");\n")

                    reps.write("}\n")
                    reps.write("\n")
                    reps.write("2: late() {\n")
                    reps.write("    // optionally, we can unique new mutations onto existing mutations\n")
                    reps.write("    // this runs only in 2: - it is assumed the gen. 1 setup is uniqued\n") 
                    reps.write("    allMuts = sim.mutations;\n") 
                    reps.write("    newMuts = allMuts[allMuts.originGeneration == sim.generation];\n")
                    reps.write("\n")
                    reps.write("    if (size(newMuts))\n") 
                    reps.write("    {\n")  
                    reps.write("        genomes = sim.subpopulations.genomes;\n")  
                    reps.write("        oldMuts = allMuts[allMuts.originGeneration != sim.generation];\n")  
                    reps.write("        oldMutsPositions = oldMuts.position;\n")  
                    reps.write("        newMutsPositions = newMuts.position;\n")  
                    reps.write("        uniquePositions = unique(newMutsPositions, preserveOrder=F);\n")  
                    reps.write("        overlappingMuts = (size(newMutsPositions) != size(uniquePositions));\n")
                    reps.write("\n")
                    reps.write("        for (newMut in newMuts)\n")  
                    reps.write("        {\n")   
                    reps.write("            newMutLocus = newMut.position;\n")   
                    reps.write("            newMutType = newMut.mutationType;\n")   
                    reps.write("            oldLocus = oldMuts[oldMutsPositions == newMutLocus];\n")   
                    reps.write("            oldMatched = oldLocus[oldLocus.mutationType == newMutType];\n")
                    reps.write("\n")
                    reps.write("            if (size(oldMatched) == 1)\n")   
                    reps.write("            {\n")
                    reps.write("                // We found a match; this nucleotide already exists, substitute\n")    
                    reps.write("                containing = genomes[genomes.containsMutations(newMut)];\n")    
                    reps.write("                containing.removeMutations(newMut);\n")    
                    reps.write("                containing.addMutations(oldMatched);\n")   
                    reps.write("            }\n")
                    reps.write("            else if (overlappingMuts)\n")   
                    reps.write("            {\n")
                    reps.write("                // First instance; it is now the standard reference mutation\n")    
                    reps.write("                oldMuts = c(oldMuts, newMut);\n")    
                    reps.write("                oldMutsPositions = c(oldMutsPositions, newMutLocus);\n")   
                    reps.write("            }\n")  
                    reps.write("        }\n") 
                    reps.write("    }\n")
                    reps.write("}\n")
                    reps.write("\n")


                    #reps.write("100 late() {\n")
                    #reps.write("    sim.outputFull("sims.out");\n")
                    #reps.write("}\n")

                    for i in range(1,1000):

                        #reps.write("%s late() { sim.outputFull(\"sim%s/sim%s_%s.out\"); }\n" % (i*100,n,n,i*100))
                        #reps.write("%s late() { sim.outputFixedMutations(\"sim%sfix/sim%s_%s.out\"); }\n" % (i*100,n,n,i*100))

                        reps.write("%s late() {\n" % (i*100))

                        reps.write("subpop = sim.subpopulations[sim.subpopulations.id == 1];\n")
                        reps.write("s = subpop.individualCount;\n")
                        reps.write("inds = subpop.individuals;\n")
                        reps.write("c1 = sum(inds.countOfMutationsOfType(m1)) %s s;\n" % ("%"))
                        reps.write("writeFile(\"sims/sim%s.out\", \"%s \" + c1, append=T);\n" % (n,i*100))
                        #reps.write("catn(\"%s \" + c1);\n" % (i*100))

                        reps.write("}\n")



                    reps.write("\n")
                    reps.write("100001 late() {\n") 
                    reps.write("    muts = p1.genomes.mutations;   // all mutations, no uniquing\n")
                    reps.write("\n")
                    reps.write("    for (locus in 0:(C-1))\n") 
                    reps.write("    {\n")  
                    reps.write("        locusMuts = muts[muts.position == locus];\n")  
                    reps.write("        totalMuts = size(locusMuts);\n")  
                    reps.write("        uniqueMuts = unique(locusMuts);\n")  
                    reps.write("\n")
                    reps.write("        catn(\"Base position \" + locus + \":\");\n")
                    reps.write("\n")
                    reps.write("        for (mut in uniqueMuts)\n") 
                    reps.write("        {\n")
                    reps.write("            // figure out which nucleotide mut represents\n")   
                    reps.write("            mutType = mut.mutationType;\n")   
                    reps.write("            nucleotide = mutType.getValue(\"nucleotide\");\n")   
                    reps.write("            cat(\"   \" + nucleotide + \": \");\n")   
                    reps.write("\n")
                    reps.write("            nucCount = sum(locusMuts == mut);\n")   
                    reps.write("            nucPercent = format(\"%s0.1f%s%s\", (nucCount / totalMuts) * 100);\n" % ("%","%","%"))   
                    reps.write("\n")
                    reps.write("            cat(nucCount + \" / \" + totalMuts + \" (\" + nucPercent + \")\");\n")   
                    reps.write("            cat(\", s == \" + mut.selectionCoeff + \"\\n\");\n")  
                    reps.write("        }\n") 
                    reps.write("    }\n")
                    reps.write("}\n") 



                    reps.close()






                    # EXECUTE SIMULATION

                    # ./slim death.slm

                    # LINUX CODE
                    #os.system('./slim sim%s.slm' % n)
                    os.system('/home/jester/VIC/build/./slim sim%s.slm' % n)








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

                    n = n + 1


