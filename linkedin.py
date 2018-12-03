import pandas
df = pandas.read_csv('linkedin-export/Certifications.csv')
#print(df)

for i in df.columns:
    print(i)
