##Load CSV files
df1 = pd.read_csv('world_population.csv')
new_labels = ['year','population']
df2 = pd.read_csv('world_population.csv', header=0, names=new_labels)
df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')
df2.to_csv(file_clean, index=False)


## Rename columns
list_labels = ['year','artist','song','chart weeks']
df.columns = list_labels
