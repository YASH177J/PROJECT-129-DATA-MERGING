import csv
import pandas as pd

file1="bright_stars.csv"
file2="dwarf_stars.csv"

d1=[]
d2=[]

with open(file1,"r",encoding="utf8") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        d1.append(i)

with open(file2,"r",encoding="utf8") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        d2.append(i)

header1=d1[0]
header2=d2[0]

planetData1=d1[1:]
planetData2=d2[1:]

headers=header1+header2

planetData=[]

for i in planetData1:
    planetData.append(i)

for j in planetData2:
    planetData.append(j)

with open("total_stars.csv","w",encoding="utf8") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetData)

df=pd.read_csv('total_stars.csv')
df.tail(8)