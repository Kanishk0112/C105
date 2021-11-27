import csv
import math
with open ("C:/Users/Hp/Desktop/White HAt Junior/PYTHON/C105/data.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
data=filedata[0]
#finding mean
def Mean(data):
    n=len(data)
    total=0
    for x in data:
        total=total+int(x)
    Mean=total/n
    return Mean
#finding square and getting values
Squarelist=[]
for n in data:
    a=int(n)-Mean(data)
    a=a**2
    Squarelist.append(a)
#getting Sum
Sum=0
for i in Squarelist:
    Sum=Sum+1
#dividing the sum by total values
result=Sum/(len(data)-1)
StandardDeviation=math.sqrt(result)
print(StandardDeviation)                    
