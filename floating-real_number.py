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
    return [sign_bit,mantissa_int,mant,exponent_bias,exponent_unbias,real_no]

l = ['0011111111000000','0100001110000010','1111111010111010']
k = []
for i in l:
    k = convertToInt(i)
    print(k)
    
