import pandas
df = pandas.read_csv('linkedin_export/Publications.csv')
#print(df)

for i in df.columns:
    print(i)
