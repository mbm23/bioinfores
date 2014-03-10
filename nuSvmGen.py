import random
import unicodedata
import sys 


def simulate_sequence(length):
     dna = ['a','g','c','t']
     sequence = ''
     for i in range (length) :
          sequence += random.choice (dna)
     return sequence

def defineVars(f,numChar,lenDna):
     f.write("MODULE main\n")
     f.write("VAR\n")
     for i in range(0,numChar):
           f.write('a' + str(i) + ": {a, c, t, g};\n")
     
     f.write("VAR pos: 0.." + str(lenDna) + ";\n")
      
def writeProg(numChar, seq,f):
     f.write("INIT (\n")
     i =0 
     for i in range(0,len(seq)-numChar - 1):
           f.write("(")
           for j in range(0,numChar):
                 f.write("a" + str(j) + "=" + seq[i+j] + " & ")
           f.write("pos=" + str(i) +")|\n")
     f.write("(")
     for j in range(0,numChar):
           f.write("a" + str(j) + "=" + seq[i+j] + " & ")
     f.write("pos=" + str(i + 1) +") \n )")                
        
        
        
c =10
l =7010
seq = simulate_sequence(l)
fhand = open('C:\\Users\\mcallimb\\Documents\\GitHub\\bioinfores\svnsample7000.smv','w')

defineVars(fhand,c,l)
writeProg(c, seq,fhand)
fhand.close()