#exercise4
file1 = open("week4.txt")
for line in file1 :
    x = line.split()
    print(x)
#Exercise 5
file2 = open("mbox-short.txt")
count = 0
for line in file2:
    if line.startswith('From'):
        count = count + 1
        m = line.split()
        print(m[1])
print(count)

