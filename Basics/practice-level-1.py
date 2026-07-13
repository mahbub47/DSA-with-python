# # Task 01
# a = 10
# b = 3
# print("Before swapping: a =", a, ", b =", b)
# a = a ^ b # a = 10 ^ 3 = 9
# b = a ^ b # b = 9 ^ 3 = 10 = a
# a = a ^ b # a = 9 ^ 10 = 3 = b
# print("After swapping: a =", a, ", b =", b)


# # Task 02
# a = 12
# b = 5
# print("Before swapping: a =", a, ", b =", b)
# a, b = b, a
# print("After swapping: a =", a, ", b =", b)

# # task 03
# string = "Hello"
# print("Original string:", string)

# # way 01
# print("Reversed string using slicing:", string[::-1])

# #way 02
# print("Reversed string using reversed function:", "".join(reversed(string)))

# # way 03
# def reverse_string_loop(text):
#     result = ""
#     for char in text:
#         result = char + result
#     return result

# print("Reversed string using for loop:", reverse_string_loop(string))

# # way 04
# def reverse_string_pointers(text):
#     char_list = list(text)
#     left, right = 0, len(char_list) - 1
#     while left < right:
#         char_list[left], char_list[right] = char_list[right], char_list[left]
#         left += 1
#         right -= 1
#     return "".join(char_list)

# print("Reversed string using two pointers:", reverse_string_pointers(string))

# # way 05
# def reverse_string_recursion(text):
#     if len(text) <= 1:
#         return text
#     return reverse_string_recursion(text[1:]) + text[0]

# print("Reversed string using recursion:", reverse_string_recursion(string))

# # Task 04
# a = 5
# if a & 1:
#     print(a, "is odd")
# else:
#     print(a, "is even")

# # Task 05
# a = 5
# b = 3
# c = 6
# if a > b and a > c:
#     print(a, "is the largest number")
# elif b > a and b > c:
#     print(b, "is the largest number")
# else:
#     print(c, "is the largest number")

# highest = max(a, b, c)
# print("The largest number is:", highest)

# highest = a if (a > b and a > c) else (b if b > c else c)
# print("The largest number using ternary operator is:", highest)

# # Task 06
# a = 5
# b = 3
# c = 6
# if a < b and a < c:
#     print(a, "is the smallest number")
# elif b < a and b < c:
#     print(b, "is the smallest number")
# else:
#     print(c, "is the smallest number")

# smallest = min(a, b, c)
# print("The smallest number is:", smallest)

# smallest = a if (a < b and a < c) else (b if b < c else c)
# print("The smallest number using ternary operator is:", smallest)


# # Task 07
# a = 2000
# leap_year = a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)
# print(a, "is a leap year:", leap_year)

# # Task 08
# c = 12
# f = (c * 9/5) + 32
# print(c, "Celsius is equal to", f, "Fahrenheit")

# # Task 09
# f = 68
# c = (f - 32) * 5/9
# print(f, "Farenheit equals to", c, "Celcius")

# # Task 10
# r = 12
# area = 3.1416 * r**2
# print("area of circle with radius", r, "is:", area)

# # Task 11
# p = 1000
# r = 5
# t = 2
# simple_interest = (p * r * t) / 100
# print("Simple Interest for principal =", p, ", rate =", r, "%, time =", t, "years is:", simple_interest)

# # Task 12
# p = 1000
# r = 5
# t = 2
# n = 4
# compound_interest = p * (1 + r/(n*100))**(n*t)
# print("Compound Interest for principal =", p, ", rate =", r, "%, time =", t, "years, compounded", n, "times per year is:", compound_interest)

# # Task 13
# n = 4
# def factorial(num):
#   if num == 0 or num == 1:
#     return 1
  
#   result = 1
#   for i in range(2, num + 1):
#     result *= i
#   return result

# print("Factorial of", n, "is:", factorial(n))

# # Task 14
# n = 6
# for i in range(1, 11):
#   print(i, "x", n, "=", i * n)

# # Task 15
# n = 1234
# count = 0
# while n > 0:
#   n //= 10
#   count += 1
# print("Number of digits in", 1234, "is:", count)

# # Task 16
# n = 1234
# reversed_number = 0
# while n > 0:
#   digit = n % 10
#   reversed_number = reversed_number * 10 + digit
#   n //= 10
# print("Reversed number is:", reversed_number)

# # Task 17
# n = 1221

# def is_palindrome_math(num):
#   if num < 0:
#     return False
#   original_num = num
#   reversed_num = 0
#   while num > 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
#   return original_num == reversed_num

# def is_palindrome_string(num):
#   str_num = str(num)
#   return str_num == str_num[::-1]

# def is_palindrome_recursive(num):
#   str_num = str(num)
#   if len(str_num) <= 1:
#     return True
#   if str_num[0] != str_num[-1]:
#     return False
#   return is_palindrome_recursive(int(str_num[1:-1]))

# def is_palindrome_two_pointers(num):
#   str_num = str(num)
#   left, right = 0, len(str_num) - 1
#   while left < right:
#     if str_num[left] != str_num[right]:
#       return False
#     left += 1
#     right -= 1
#   return True

# def is_palindrome_stack(num):
#   str_num = str(num)
#   stack = []
#   for char in str_num:
#     stack.append(char)
#   for char in str_num:
#     if char != stack.pop():
#       return False
#   return True

# def is_palindrome_deque(num):
#   from collections import deque
#   str_num = str(num)
#   dq = deque(str_num)
#   while len(dq) > 1:
#     if dq.popleft() != dq.pop():
#       return False
#   return True

# def is_palindrome_list(num):
#   str_num = str(num)
#   char_list = list(str_num)
#   return char_list == char_list[::-1]

# def is_palindrome_set(num):
#   str_num = str(num)
#   return set(str_num) == set(str_num[::-1])

# def is_palindrome_dict(num):
#   str_num = str(num)
#   char_dict = {}
#   for char in str_num:
#     char_dict[char] = char_dict.get(char, 0) + 1
#   for char in str_num:
#     if char_dict[char] != char_dict.get(char, 0):
#       return False
#   return True

# print("Is", n, "a palindrome (string method)?", is_palindrome_string(n))

# # Task 18
# string = "racecar"
# def is_palindrome_string_method(s):
#     return s == s[::-1]

# print("Is", string, "a palindrome (string method)?", is_palindrome_string_method(string))

# # Task 19
# number = 12345
# def sum_of_digits(num):
#     total = 0
#     while num > 0:
#         total += num % 10
#         num //= 10
#     return total

# print("Sum of digits in", number, "is:", sum_of_digits(number))

# # Task 20
# number = 153
# def is_armstrong(num):
#   num_str = str(num)
#   num_digits = len(num_str)
#   sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
#   return sum_of_powers == num

# print("Is", number, "an Armstrong number?", is_armstrong(number))

# # Task 21
# a = 48
# b = 18
# def find_gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x

# print("GCD of", a, "and", b, "is:", find_gcd(a, b))

# # Task 22
# a = 48
# b = 18
# def find_lcm(x, y):
#     def gcd(x, y):
#         while y:
#             x, y = y, x % y
#         return x

#     return abs(x * y) // gcd(x, y)

# print("LCM of", a, "and", b, "is:", find_lcm(a, b))

# # Task 23
# n = 7
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# print("Is", n, "a prime number?", is_prime(n))

# # Task 24
# number1, number2 = int(input("Enter first number: ")), int(input("Enter second number: "))
# for i in range(number1, number2 + 1):
#   if i > 1:
#     for j in range(2, int(i**0.5) + 1):
#       if i % j == 0:
#         break
#     else:
#       print(i, end = " ")

# print()

# # Task 25
# number = int(input("Enter a number: "))
# def fibonacci(n):
#   if n<= 0:
#     return []
#   elif n == 1:
#     return [0]
#   elif n == 2:
#     return [0, 1]
#   fib_sequence = [0,1]
#   for i in range(2, n):
#     next_number = fib_sequence[-1] + fib_sequence[-2]
#     fib_sequence.append(next_number)
#   return fib_sequence

# print("Fibonacci sequence up to", number, "terms is:", fibonacci(number))

# # Task 26
# number = int(input("Enter a number: "))
# def find_fibonacci(n):
#   if n <= 0:
#     return -1
#   elif n == 1:
#     return 0
#   elif n == 2:
#     return 1
  
#   return find_fibonacci(n-1) + find_fibonacci(n-2)

# print(number, " Fibonacci is ", find_fibonacci(number))

# # Task 27
# string = input("Enter any text: ")
# charArray = list(string)
# vowel = 0
# consonants = 0
# for char in charArray:
#   if char == "A" or char == "a" or char == "E" or char == "e" or char == "I" or char == "i" or char == "O" or char == "o" or char == "U" or char == "u":
#     vowel += 1
#   else:
#     consonants += 1

# print(string, f" has {vowel} vowels and {consonants} consonants")

# Task 28
# string = input("Enter a text: ")
# char_array = list(string)
# upper = 0
# lower = 0
# others = 0
# for char in char_array:
#   ascii = ord(char)
#   if ascii >= 65 and ascii <= 90:
#     upper += 1
#   elif ascii >= 97 and ascii <= 122:
#     lower += 1
#   else:
#     others += 1

# print(string, f" text contains {upper} Uppercase, {lower} Lowercases, and {others} Others")

# # Task 29
# char = input("Enter a character: ")
# ascii = ord(char)
# print(f"The ASCII value of {char} is ", ascii)

# # Task 30
# string = input("Enter a text: ")
# set = set()
# new_string = ""
# for char in list(string):
#   if set.__contains__(char):
#     continue
#   set.add(char)
#   new_string += char

# print("New string is ", new_string)