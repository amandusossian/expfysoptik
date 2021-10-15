import numpy as np
import matplotlib.pyplot as plt

#funktion som genomför iterationer för prediktkioner
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

# Dataimportering och benämning av konstanter
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

 #ordnar värmeförloppen till att ändra riktning och sätter starttemperaturer       
datalist[0].reverse()
datalist[4].reverse()
ktot = [0 for i in range(49)]
starttemperaturer = [24,8,8,6,24]

# Medelvärdesbildar steglängder 
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

#skalar om steglängden i enighet med teoretiska ekvationerna i rapporten. 
for i in range(len(ktot)):
    ktot[i] = ktot[i]*633*10**(-9)/(2*0.056)



print(ktot[20])
print(len(ktot))


# Allt under här genererar grafiska representationerna, beroende på vad som är utkommenterat visas olika figurer

# Skapar n-T figuren
a = []
b = range(6,49)
for t in range(6,49):
    pred = prediction(t,ktot)
    print(pred)
    a.append(pred)

degree_sign = u'\N{DEGREE SIGN}'

#fig = plt.figure()
#plt.plot(b,a)
#plt.xlabel("Temperatur [" + degree_sign +"C]" )
#plt.ylabel("Brytningsindex")
#fig.suptitle('Brytningsindex för vatten vid olika temperaturer')

# Nedan här skapas Avvikelse-figuren, genom att skapa listor innehållandes varje grads average, max, och min antal interferensskiftningar
# , för att sedan skapa de vertikala linjerna

maxi = [0 for i in range(len(datalist[0]))]
mini = [50 for i in range(len(datalist[0]))]
for j in range(len(datalist)):
    for i in range(len(datalist[0])):
        maxi[i] = max(datalist[j][i], maxi[i])
        if datalist[j][i] !=0:
            mini[i] = min(datalist[j][i], mini[i])
        
for i in range(5):
    mini[i] = 0


diff = [0 for i in range(len(datalist[0]))]
for i in range(len(maxi)):
    diff[i] = maxi[i]-mini[i]

avg = [0 for i in range(len(datalist[0]))]
for i in range(len(datalist[0])):
    temp = 0
    nonzeros = 0
    for j in range(len(datalist)):
        temp += datalist[j][i]
        if datalist[j][i] !=0:
            nonzeros+=1
    if temp != 0:
        avg[i] = temp/nonzeros

print(avg)
errorx = range(len(datalist[0]))
errory = [[]for i in range(len(datalist[0]))]
for i in range(len(datalist[0])):
    errory[i] = [mini[i], maxi[i]]
fig = plt.figure()
plt.plot(errorx, avg,'.', color = 'r', label = 'Interferensskiftningar')
for i in range(len(datalist[0])):
    plt.vlines(x = errorx[i], ymin = errory[i][0], ymax = errory[i][1],color = 'k')
    plt.hlines(xmin = errorx[i]-0.3, xmax = errorx[i]+0.3, y = errory[i][0], color = 'k')
    plt.hlines(xmin = errorx[i]-0.3, xmax = errorx[i]+0.3, y = errory[i][1], color = 'k')
plt.vlines(x = errorx[0], ymin = errory[0][0], ymax = errory[0][1],color = 'k', label = 'Avvikelser')
plt.xlabel("Temperatur [" + degree_sign +"C]" )
plt.ylabel('Interferensskiftningar')
plt.suptitle('Interferensskiftningar vid olika temperatur, samt avvikelser')
plt.legend()
plt.show()

