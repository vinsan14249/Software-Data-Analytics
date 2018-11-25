import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename='Data/test_dataset.csv'
df = pd.read_csv(filename,encoding='utf-8')

#1. Dataframe for customer_id, Transactions
print (df[['customer_id','Transactions']])

print ("-------------------------------------------------")
print (df.columns)
print ("-------------------------------------------------")

#2.  customer_id renamed to user_id
df = df.rename(columns={'customer_id':'user_id'})

print("\n2. Column names after renaming are as follows :  ",df.columns)

# 3. the mean of GR for category FNB
df1 = df.loc[df['category_id'] == 'FNB']
#print (df1)
mean_GR_FNB = df1['GR'].mean()

print("\n3. Mean of GR for category FNB : "+str(mean_GR_FNB))

# 4. the customer_id/user_id where category = GTW & TransactionValue >0 
df2 = df.loc[df['category_id'] == 'GTW' ]
df3 = df2.loc[df['TransactionValue'] > 1]
df4 = list(df3['user_id'])
print ("\n4. The customer_id/user_id where category = GTW & TransactionValue > 0 is: ",df4)

# 5. The category has max no of purchases
dg = df.groupby('category_id')
category = []
transactionSum = []
for name,group in dg:
	category.append(group['category_id'].unique())
	transactionSum.append(group['Transactions'].sum())
max_no_purchase = max(transactionSum)
index = transactionSum.index(max_no_purchase)

print ("\n5. Category that has maximum number of purchases :",category[index])

# 6. Plot GR for SNS month on month
df5 = df.loc[df['category_id'] == 'SNS']
print(df5)




ax = df5[['GR','date']].plot(kind='bar', title ="V comp", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("GR for SNS", fontsize=12)
plt.show()
