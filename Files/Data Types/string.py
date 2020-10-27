# 2. STRING - can be defined in single Quotes OR double quotes OR triple quotes

# single quotes
str_single = 'Hello World!'
str_double = "Hello World!"
str_triple = """Hello World!"""

# Triple quotes - used for multiline printing
str_variable1 = '''My name is Muhammad Harith. I am currently studying in Universiti Putra Malaysia
I am expected to graduate in 2021. I love to learn new things.
'''
print(str_variable1)

# string[start:stop:step]
# Index in String
print("This is index 0 =", str_double[0])
print("This is index 1 =", str_double[1])
print("This is index 2 =", str_double[2])
print("This is index 3 =", str_double[3])
print("This is index 4 =", str_double[4])

print("Range from 0 to 5 =", str_double[0:5])  # Range of index, from 0 to 5 but excluding index 5
print(str_double[2:])  # start from 2 until end
print("Range of everything =", str_double[:])  # Range of everything
print("Range of everything v2 =", str_double[::])  # Range of everything
print("Print in range 2 =", str_double[0:12:2])  # Start from index 0 to 12, in range 2
print("Print from the back =", str_double[-2])  # start from the back and print that index
print("Inverse =", str_double[::-1])  # inverse

# Concatenation
str_concatenation = str_double + str_single
print("This is concatenation =", str_concatenation)
print(str_single + str_double)
print(str_single + " " + str_double)