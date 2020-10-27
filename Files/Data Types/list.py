# 3. List - contain set of elements, defined in [], can be set of nums, strings or combination

list_numbers = [12, 34, 23, 56, 45645, 234, 7862]
list_language = ["English", "Malay", "Mandarin", "Tamil"]
list_numbs_language = [34, 76, 54, "Python", "Java", "C++"]

# Concatenation
output = list_numbers + list_language
print("Concatenation of 2 list =", output)

# Index
print("Index 0 =", list_numbers[0])  # Only list in index 0
print("Index 0 to 4 =", list_numbers[0:5])  # print from index 0 to 5 excluding index 5
print("Everything with step of 2 =", list_language[::2])  # every 2
print("Reversing list =", list_language[::-1]) # reverse the list

# Change index 0 with other numbers
list_numbers[0] = 1000
print("Updated list =", list_numbers)
