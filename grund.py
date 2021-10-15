import numpy as np
import matplotlib.pyplot as plt

# Dataimportering och benämning av konstanter
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
datalist =[data1,data2,data3,data4,data5,data6]
Umax = 7.6
Umin  =0.02
scaling = 1/100
patm = 101020
lamda = 0.000000633
d = 0.053

for i in range(6):
    filename = "data" + str(i+1) + ".txt"
    dataname = datalist[i]
    datafile = open(filename, 'r')
    for line in datafile:
        temp = int(line.strip())
        datalist[i].append(temp)
for j in range(6):
    for r in range(len(datalist[j])):
        datalist[j][r] = patm*(int(datalist[j][r])*scaling-Umin)/(Umax - Umin)
        
# Genomför de beräkningar som beskrivs i metod, linjär regression och medelvärdesbildning, samt 
# skapa grafik. Olika figurer har framtagits med varianter av nedanstående kod. 
t = 0
lutavg= 0
lutmax = 0
lutmin = 1
intercept_avg = 0
colorlist = ['r', 'g', 'b', 'y', 'k', 'm']
fig = plt.figure()
ax = fig.subplots()
for list in datalist:
    
    x = []
    for k in range(len(list)):
        x.append(list[k])

    y = range(len(list))    

    fit = np.polyfit(x,y,1)
    ang_coeff = fit[0]
    intercept = fit[1]
    ynew = []
    xcont = np.linspace(0,99500,99500)
    fit_eq = 0.00041658871664660866*xcont+intercept
    lapp = "data"+ str(t)
    ax.plot(x,y,'.', color = 'r', markersize = 5)
    if t ==5:
        ax.plot(xcont, fit_eq,color = 'k', label = lapp)
    
    #ax.plot(xcont, fit_eq,color = colorlist[t-1], alpha = 0.5, label = lapp)
    
    print(ang_coeff, "Lutning", t+1)
    print(intercept, "SKÄRNING ", t+1)
    t+=1
    lutmax = max(lutmax, ang_coeff)
    lutmin = min(lutmin, ang_coeff)
    lutavg += ang_coeff
    intercept_avg +=intercept 
#ax.plot(xcont, fit_eq,color = colorlist[t-1], alpha = 0.5, label = lapp)
ax.set_title('Linjära regressionens medelvärdeslinje, och samtliga datapunkter')
plt.xlabel('Tryck i vakuumkammaren [Pa]')
plt.ylabel('Interferensskiftningar')

#ax.legend()
plt.show()
lutavg = lutavg/6
print(intercept_avg/6, "Interceptavg")
print(lutavg, "lutavg")
print(lutmax, "lutmax")
print( lutmin, 'lutmin')
print(lutmax-lutmin, 'lutmax - lutmin')

k = lutavg *lamda/(2*d) 
print(k)
print('final result is n =', 1+k*patm)