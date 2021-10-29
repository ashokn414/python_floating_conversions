# for normalization we need to have the maxima of x and y values with the help of which 
# we can normalise the given values
import csv
filename = "values.csv"
fields = []
rows = []
with open(filename,'r') as csvfile:
    reader = csv.reader(csvfile)
    fields = next(reader)

    for row in reader:
        rows.append(row)

for row in rows:
    for col in row:
        a = col[0]
norm=50

#a = float(input("enter the x cordinate:"))
#b = float(input("enter the y cordinate:"))
if (a>norm or b>norm or a<-(norm) or b<-(norm)):
    print("the value given is invalid/out of bound")
else:
    a = a/norm
    b = b/norm
    print("the normalized values are "+str(a)+","+str(b))