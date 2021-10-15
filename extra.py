import numpy as np
import matplotlib.pyplot as plt

def prediction(temp, kvals):
    retur = 1.3333333
    if temp>20:
        k = kvals[19:temp+1]
        for value in k:
            retur-=  value
        return retur
    if temp<20:
        k = kvals[temp:20]
        for value in k:
            retur+= value
        return retur
    return retur


data21 = []
data22 = []
data23 = []
data24 = []
data25 = []
data26 = []
datalist =[data21,data22,data23,data24, data25]
Umax = 7.6
Umin  =0.02
scaling = 1/100
patm = 101020

for i in range(len(datalist)):
    filename = "data2" + str(i+1) + ".txt"
    dataname = datalist[i]
    datafile = open(filename, 'r')
    for line in datafile:
        temp = int(line.strip())
        datalist[i].append(temp)
        
datalist[0].reverse()
datalist[4].reverse()
ktot = [0 for i in range(49)]
starttemperaturer = [24,8,8,6,24]

for list in datalist:
    for i in range(49):
        if list[i]==0:
            pass
        else: 
            ktot[i]+= list[i]
        
for i in range(49): 
    k = 0
    for list in datalist:
        if list[i]!=0:
            k = k+1
    if k>1:
        ktot[i]= ktot[i]/k

for i in range(len(ktot)):
    ktot[i] = ktot[i]*633*10**(-9)/(2*0.056)



print(ktot[20])
print(len(ktot))



a = []
b = range(6,49)
for t in range(6,49):
    pred = prediction(t,ktot)
    print(pred)
    a.append(pred)

degree_sign = u'\N{DEGREE SIGN}'

fig = plt.figure()
plt.plot(b,a)
plt.xlabel("Temperatur [" + degree_sign +"C]" )
plt.ylabel("Brytningsindex")
fig.suptitle('Brytningsindex för vatten vid olika temperaturer')
plt.show()

