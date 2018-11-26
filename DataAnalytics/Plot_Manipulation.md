# Requirement
[PLOTTING LIBRARY]
Show the nature of relationship between two variables (Number of Transactions &  GR) for each category in R/Python(use any library for plotting).

[DATA MANUPLATION]
Perform operations over data :
1.Return the field customer_id, Transactions
2.Rename the columns customer_id to user_id
3.What is the mean of GR for category FNB
4.Return the customer_id/user_id where category = GTW & TransactionValue >0 
5.Which category has maximum number of purchases(HINT: Transactions)
6.Plot the GR for SNS month on month  

Things you should know about the data set: 
Field Name: GR: Gross Revenue | category_id: business category 

Category ID	Name
GTW	Travel
HNL	Hobbies & Learning
SNM	Spa & Massages
LOS	Home & Auto Services
MVE	Movies & Events
ACT	Activities
BNS	Beauty & Salon
HEA	Health
FIT	Fitness
FNB	Food & Beverages
LOR	In-store Retail
SNS	Spa & Salon
HNF	Health & Fitness
TTD	Things To Do

##Solution & Design

[PLOTTING LIBRARY]	PlotProgram.py

- Open and Read CSV file(csvReader)
using csvReader descriptor add colums(category_id,Transactions,GR) into array.
- create index over category array and and find indices for the points to be plotted as per the category hardcoded in category_id array .
- using indices create array's that can be plotted using matplotlib.

1. open file
2. read columns to array
3. find indices from array to plot 
4. create array with items on indices
5. create label
6. plot using plt.plot(x1,y1,marker='o',color='c',label = lab1)
7. plot.show() to show plotted graph


[DATA MANUPLATION] ManipulationProgram.py

Read csv using pandas import (pd) and iterate over df descriptor.
'''
df = pd.read_csv(filename,encoding='utf-8')
'''
1. df[['<column_1>','<column_2>']] 
- return's the number of column required from the whole column.

2. df = df.rename(columns={'<OLD_column_name>':'<NEW_column_name>'})
- return the renamed column's names

3. df.loc[df['<column_name>'] == '<conditional_param>']
- df.loc iterates the dataframe as per column specified and returns output as per the condition.

4. df1['<column_name>'].mean()
- finds mean for all of the column's values by iterating.

5. df.groupby('<column_name>')
- iterate and groups the dataframe's rows based on the column_name specified.

6. df5[['<column_1>','<column_2>']].plot(kind='bar', title ="Plot GR for SNS", figsize=(15, 10), legend=True, fontsize=12)
- plot's data based on the colum's specified and other parameters for aligning the format of the plotted graph.



