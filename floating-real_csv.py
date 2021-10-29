import csv
#########################################
def convertToInt(a):
    mant = 0
    power_count = -1
    mantissa_int = 0
    expo = a[1:6]
    s = a[0]
    mant_str = a[6:]
    for i in mant_str:
        mantissa_int += (int(i) * pow(2, power_count))
        power_count -= 1
    mant = mantissa_int + 1
    sign_bit = int(s)
    exponent_bias = int(expo, 2)
    exponent_unbias = exponent_bias - 15
    real_no = pow(-1, sign_bit) * mant * pow(2, exponent_unbias)
    return real_no
###################################################
filename = "floating_values.csv"
fields = []
rows = []
with open(filename,'r') as csvfile:
    reader = csv.reader(csvfile)
    fields = next(reader)

    for row in reader:
        if(row!=[]):
            rows.append(row)
        

for row in rows:
    a = convertToInt(row[0])
    b = convertToInt(row[1])
    row[0] = a
    row[1] = b
    #print("the "+str(rows.index(row))+" co-ordinate is "+"("+str(a)+","+str(b)+")")

fields = ["normalized x coordinate","normalized y cordinate"]
filename = "float_to_normalized_values.csv"

with open(filename,'w') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(fields)
    writer.writerows(rows)