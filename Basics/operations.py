a = 12
b = 5

print("Arithmetic Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

print("Comparison Operations:")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)

print("Logical Operations:")
print("Logical AND:", a > 10 and b < 10)
print("Logical OR:", a > 10 or b < 10)
print("Logical NOT:", not (a > 10))

print("Bitwise Operations:")
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

print("Assignment Operations:")
c = a
print("Initial value of c:", c)
c += b
print("After c += b:", c)
c -= b
print("After c -= b:", c)
c *= b
print("After c *= b:", c)
c /= b
print("After c /= b:", c)
c %= b
print("After c %= b:", c)
c **= b
print("After c **= b:", c)

print("Identity Operations:")
print("Is c the same object as a:", c is a)
print("Is c the same object as b:", c is b)
print("Is c not the same object as a:", c is not a)
print("Is c not the same object as b:", c is not b)

print("Membership Operations:")
list_example = [1, 2, 3, 4, 5]
print("Is 3 in list_example:", 3 in list_example)
print("Is 6 not in list_example:", 6 not in list_example)

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of list_example:", type(list_example))
