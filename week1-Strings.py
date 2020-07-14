# Exercise 6.5 String manipulation
#print("hello")
#greet = 'Hello Bob'
#vamos = type(greet[0:4])
#print(vamos)
str = 'X-DSPAM-Confidence:0.8475'
print(type(str))
loc = str.find(':')
locend = len(str)
l = type(str[loc+1:locend])
# you can also use str[loc+1:]
v = str[loc+1:locend]
type(v)
m = float(v)
print(type(m))
print(m)
# fl = print(str[loc+1:locend])
# print(type(fl))
# output type is NoneType


 