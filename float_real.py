# Python program to convert
# IEEE 754 floating point representation
# into real value

# Function to convert Binary
# of Mantissa to float value.
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
    
    

	# variable to make a count
	# of negative power of 2.
	

	# variable to store
	# float value of mantissa.
	

	# Iterations through binary
	# Number. Standard form of
	# Mantissa is 1.M so we have
	# 0.M therefore we are taking
	# negative powers on 2 for
	# conversion.
	

		# Adding converted value of
		# Binary bits in every
		# iteration to float mantissa.
		

		# count will decrease by 1
		# as we move toward right.
		
		
	# returning mantissa in 1.M form.
    
	
    
    
    
    
    
    


if __name__ == "__main__":
	# Floating Point Representation
	# to be converted into real
	# value.
	ieee_32 = '1011100000000000'

	# First bit will be sign bit.
	

	# Next 8 bits will be
	# Exponent Bits in Biased
	# form.
	

	# In 32 Bit format bias
	# value is 127 so to have
	# unbiased exponent
	# subtract 127.
	

	# Next 23 Bits will be
	# Mantissa (1.M format)
	

	# Function call to convert
	# 23 binary bits into
	# 1.M real no. form
	value = convertToInt(ieee_32)

	# The final real no. obtained
	# by sign bit, mantissa and
	# Exponent.
	

	# Printing the obtained
	# Real value of floating
	# Point Representation.
	print("The float value of the given IEEE-754 representation is :",value)
