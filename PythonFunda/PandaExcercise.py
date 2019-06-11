import pandas as pd
df=pd.read_csv('pokemon_data.csv')
print(df)

print(df.head(3))
print(df.tail(3))


df=pd.read_excel('pokemon_data.xlsx')
print(df)


df=pd.read_csv('pokemon_data.txt', delimiter='\t')
print(df)

#Read Headers

print(df.columns)

print(df.columns[1])




print(df['Name'][0:5])

print(df.Name[0:5])

print(df[['Name','Type 1','HP']])

#Read Each Row
print(df.iloc[1])   

#Read Multiple Rows
print(df.iloc[1:4])

#Read a specific position
print(df.iloc[2,1]) #second row, first position

#Irerate through rows
for index,row in df.iterrows():
    print(index,row)
    

for index,row in df.iterrows():
    print(index,row['Name'])
    
df.loc[df['Type 1']=='Fire']

#To get mean/avg 
df.describe()

df.sort_values(['Name'], ascending=False)

df.sort_values(['Type 1','HP'], ascending=[1,0])

df['Total']=df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']

df.head(5)

#drop a column
df=df.drop(columns=['Total'])

#Adding Total in a different fashion
df['Total']=df.iloc[:,4:10].sum(axis=1)

#rearranging the columns
cols=list(df.columns)
df=df[cols[0:4]+[cols[-1]]+cols[4:12]]

df.to_csv('Modifiled_Pokemon.csv',index=False)


#Filtering columns
new_df = df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')]
new_df=new_df.reset_index(drop=True) #drops old indexes

#Finding a word
df.loc[df['Name'].str.contains('Mega')]

df.loc[~df['Name'].str.contains('Mega')]

 import re
#Using Regex
df.loc[df['Type 1'].str.contains('fire|grass',flags=re.I,regex=True)]

#Conditional Changes
df.loc[df['Type 1']=='Fire', 'Type 1']='Flamer'

print(df['Type 1'])

#reversing the changes
df.loc[df['Type 1']=='Flamer', 'Type 1']='Fire'

#modifying multiple values on conditional
df.loc[df['Total']>500,['Generation','Legendary']]=['Test 1','Test 2'] 

#Aggregate Statistics

df.groupby(['Type 1']).mean()
df.groupby(['Type 1']).sum()
df.groupby(['Type 1']).median()
df.groupby(['Type 1']).count()



#Working with large data

new_df=pd.DataFrame(columns=df.columns)

for df in pd.read_csv('Modifiled_Pokemon.csv',chunksize=5):
    results=df.groupby(['Type 1']).count()
    new_df=pd.concat([new_df,results])

print(new_df)
