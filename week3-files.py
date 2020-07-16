#Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:
#python shout.py
#Enter a file name: mbox-short.txt
#FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
#RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
#RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#     SAT, 05 JAN 2008 09:14:16 -0500
filename = input("filename : ")
df = open(filename,'r')
count = 0 
z = 0.0
for line in df :
    l = line.rstrip()
   # print(l.upper())
    
    if line.startswith('X-DSPAM-Confidence:'):
        y = float(line[19:])
        print(y)
        z = y + z
        print(z)
        count = count + 1
print(count)
print(z)
avg = z / count
print(avg)

        #float(y)
        #print(y.rstrip()) 
        #count = count + 1 

# Exercise 3 
file1 = input("enter file name :")
try :
    df = open(file1)
    count = 0 
    for line in df :
        count = count+1
except:
    if (file1 == 'lalala'):
        print (file1, "you have been punk'd")
    else :
        print("file cannot be opened")



    

    

  





