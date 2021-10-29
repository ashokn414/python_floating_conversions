import csv
norm = 50
filename = "values.csv"
fields = []
rows = []
with open(filename,'r') as csvfile:
    reader = csv.reader(csvfile)
    fields = next(reader)

    for row in reader:
        rows.append(row)

for row in rows:
    a = float(row[0])/norm
    b = float(row[1])/norm
    row[0] = a
    row[1] = b
    #print("the "+str(rows.index(row))+" co-ordinate is "+"("+str(a)+","+str(b)+")")

fields = ["normalized x coordinate","normalized y cordinate"]
filename = "normalised_values.csv"

with open(filename,'w') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(fields)
    writer.writerows(rows)