#!/usr/bin/env python
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import csv

GeFile = 'FDG03-CAL_xls.csv'
SiFile = 'FSD100-CAL_xls.csv'
InGaAsFile = 'FGA21-CAL_xls.csv' 




reader = csv.reader(open(GeFile,'rU'),dialect='excel')
GeRawData = [row for row in reader]
GeData = np.array([[float(row[0]),float(row[1])] for row in GeRawData[2:]])
ax = plt.plot(GeData.T[0],GeData.T[1],label='Ge')
plt.xlabel(GeRawData[1][0])
plt.ylabel(GeRawData[1][1])
#plt.legend(ax,'Ge')

reader = csv.reader(open(SiFile,'rU'),dialect='excel')
SiRawData = [row for row in reader]
SiData = []
for row in SiRawData[2:]:
	if row[0] == '':
		continue
	SiData.append([float(row[0]),float(row[1])])
SiData = np.array(SiData)

#SiData = np.array([[float(row[0]),float(row[1])] for row in SiRawData[2:]])
plt.plot(SiData.T[0],SiData.T[1],label='Si')
plt.xlabel(SiRawData[1][0])
plt.ylabel(SiRawData[1][1])

reader = csv.reader(open(InGaAsFile,'rU'),dialect='excel')
InGaAsRawData = [row for row in reader]
InGaAsData = np.array([[float(row[0]),float(row[1])] for row in InGaAsRawData[2:]])
plt.plot(InGaAsData.T[0],InGaAsData.T[1],label='InGaAs')
plt.xlabel(InGaAsRawData[1][0])
plt.ylabel(InGaAsRawData[1][1])

fig = plt.gcf() #get current figure
fig.set_figwidth(3.6)
fig.set_figheight(2.7)
#plt.subplots_adjust(bottom=0.15)
plt.legend(loc='upper left')
plt.savefig('detectorResponsivity.pdf',bbox='tight')
#plt.show()
