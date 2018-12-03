import pandas
df = pandas.read_csv('linkedin-export/Publications.csv')
#print(df)

for i in df.columns:
    print(i)
