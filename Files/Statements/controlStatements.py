# for loop with range
for val in range(1, 11):
    print("Range =", val)

# for loop with even numbers
for val in range(2, 10, 2):
    print("Even =", val)

# for loop with string
name = "Muhammad Harith"
for char in name:
    print("Characters =", char)

# for loop with list
list_nums = [10, 23, 432, 54]
for value in list_nums:
    print("List =", value)

# for loop with dictionary
dict_book = {"chap1": 10, "chap2": 30, "chap3": 20}
for key in dict_book.keys():
    print("Keys =", key)

# --------------------------------------------------------------------------------------------

# While loop
flag = 1

while flag <= 10:
    print("While =", flag)
    flag = flag + 1
