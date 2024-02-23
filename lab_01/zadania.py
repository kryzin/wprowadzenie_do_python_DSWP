# 1 --------------------------------------------------
# dwa obiekty int i float, różne wartości konstruktora
import datetime

int_a = int("783", 16)
int_b = int(19)

float_a = float(3.14)
float_b = float("3.5555")

print("ints: ", int_a, " ", int_b)
print("floats: ", float_a, " ", float_b)

# 2 --------------------------------------------------
# wykorzystaj metody

float_c = 50
# if float_c.is_integer():
#     print(float_c, " is also integer")
if float_a.as_integer_ratio()[1] == 1:
    print(float_a, " is also an integer")

if float_c.as_integer_ratio()[1] == 1:
    print(float_c, " is also an integer")

print(bin(int_a))
print(int_a.bit_count())

# 3 ---------------------------------------------------
# bin/int
int_b = bin(int_b)
print("bin: ", int_b)
int_b = int(int_b, 2)
print("int: ", int_b)

# 4 ---------------------------------------------------
# 4 przykłady operatorów binarnych
import datetime

switch = False
# przełącz switch
switch = not switch
print("Switch: ", switch)

def xor(a, b):
    return (a & ~b) | (~a & b)

a = True
b = False
print("XOR: ", xor(a, b))

def binary_to_gray(n):
    """Convert Binary to Gray"""
    n = int(n, 2)
    n ^= (n >> 1)
    return bin(n)[2:]

n = bin(14)
print(binary_to_gray(n))

# 5 ---------------------------------------
float_a = float.hex(float_a)
print("Hex: ", float_a)
float_a = float.fromhex(float_a)
print(float_a)