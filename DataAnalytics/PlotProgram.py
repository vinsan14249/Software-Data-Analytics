#!/usr/bin/python

import matplotlib.pyplot as plt				# importing matlplotlib for plotting graph
import csv						# importing csv for reading csv file

filename = 'Data/test_dataset.csv';			# defining path for data_set file
category_id = ['FNB','TTD','SNS']			# hardcoding three categories

fields,rows,x1,y1,x2,y2,x3,y3 = [],[],[],[],[],[],[],[]
categoryArray = []
transactionArray = []
grossRevenueArray = []

with open(filename , 'r') as csvFile :			# reading file with csv reader 
	csvReader = csv.reader(csvFile)			# extracting field names from 1st row
	#csvReader = csv.DictReader(csvFile)			# data can be extracted using dictionary 
	fields = next(csvReader);

	for row in csvReader :				# getting csv columns into array
		categoryArray.append(row[2])
		transactionArray.append(row[3])
		grossRevenueArray.append(row[4])

lab1 = "Loaded from file "+filename+" "+category_id[0]
lab2 = "Loaded from file "+filename+" "+category_id[1]
lab3 = "Loaded from file "+filename+" "+category_id[2]

indices1 = [i for i ,x in enumerate(categoryArray) if x == category_id[0]]
indices2 = [i for i ,x in enumerate(categoryArray) if x == category_id[1]]
indices3 = [i for i ,x in enumerate(categoryArray) if x == category_id[2]]

for id in indices1:
	x1.append(transactionArray[id])
	y1.append(grossRevenueArray[id])

for id in indices2:
	x2.append(transactionArray[id])
	y2.append(grossRevenueArray[id])

for id in indices3:
	x3.append(transactionArray[id])
	y3.append(grossRevenueArray[id])

plt.plot(x1,y1,marker='o',color='c',label = lab1)
plt.plot(x2,y2,marker='o',color='g',label = lab2)
plt.plot(x3,y3,marker='o',color='r',label = lab3)
plt.grid(True)
plt.xlabel('TransactionValue')
plt.ylabel('Gross Revenue')
plt.title("Relation b/w number of transactions and Gross Revenue")
plt.show()

