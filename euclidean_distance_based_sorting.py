import math 
import csv
############################################################
def edbs(x,y):
    cx=0
    cy=0
    e = []
    for i in range(0,len(x)):
        cx+=x[i]
        cy+=y[i]
    
    cx = cx/len(x)
    cy = cy/len(y)

    for i in range(0,len(x)):
        e.append(math.sqrt(math.pow((x[i]-cx),2)+math.pow((y[i]-cy),2)))
  

    for i in range(0,len(e)):
        for j in range(i+1,len(e)):
            if(e[i]>e[j]):
                temp = e[i]
                e[i] = e[j]
                e[j] = temp
    return e
#################################################################
filename = "normalised_values.csv"
fields = []
rows = []
a = []
b = []
with open(filename,'r') as csvfile:
    reader = csv.reader(csvfile)
    fields = next(reader)

    for row in reader:
        if(row!=[]):
            rows.append(row)
for row in rows:
    a.append(float(row[0]))
    b.append(float(row[1]))

l = edbs(a,b)
fields = ["euclidean distances"]
filename = "distances.dat"

with open(filename,'w') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(fields)
    writer.writerows(map(lambda x: [x], l))

print(l)
            
            
            
    
    
    
    