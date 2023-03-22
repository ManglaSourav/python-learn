'''

Bit manipulation are the bit-wise operators 
& (and), 
| (or), 
~ (not),
^ (exclusive-or, xor), and 
shift operators a << b and a >> b.



Set union A | B
Set intersection A & B
Set subtraction A & ~B
Set negation ALL_BITS ^A or ~A
Set bit A |= 1 << bit
Clear bit A &= ~(1 << bit)
Test bit (A & 1 << bit) != 0
Extract last bit A&-A or A&~(A-1) or x^(x&(x-1))
Remove last bit A&(A-1)
Get all 1-bits ~0

'''
def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

def test_bit(value, bit):
    return (value & (1<<bit)) != 0

def extract_last_bit1(value):
    print_bin_dec(-value)
    return value & -value

def extract_last_bit2(value):
    return value & -(value-1)

def extract_last_bit3(value):
    return value^(value&(value-1))

def print_bin_dec(value, msg=""):
    print(msg, "Decimal = {} Binary = {}".format(value, bin(value)))

def remove_last_bit(value):
    return value & (value-1)


# val = 0b111
# print_bin_dec(set_bit(val, 2)) # set third bit to one from left side
# print(set_bit(val, 2))
# val = set_bit(val, 2)
# print(test_bit(val, 2)) # test third bit to one from left side
# print_bin_dec(val) # 0b1110 
# print_bin_dec(remove_last_bit(val)) # remove last bit
# print_bin_dec(extract_last_bit1(val),"extract_last_bit")
# print_bin_dec(extract_last_bit2(val),"extract_last_bit")
# print_bin_dec(extract_last_bit3(val),"extract_last_bit")


