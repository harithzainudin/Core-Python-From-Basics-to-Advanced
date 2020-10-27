# method in Python
# to get help/description of some method, go to console and type help(str.capitalize)
# change 'capitalize' keywords with anything that you want to know

# STRING METHOD
str_language = "PYTHON programming"

print("Capitalize the string =", str_language.capitalize())  # capitalize the first character

print("Lowering the character of the string =", str_language.lower())  # converting all the characters to lower case

print("Is the string contain all uppercase? =", str_language.isupper())  # checking if the string have all uppercase

print("Changing the string to title =", str_language.title())  # words start with uppercased characters

print("Centering the string with 40 spaces =", str_language.center(40))  # center the string with 40 spaces

print("Centering the string with 40 spaces and filled with * =",
      str_language.center(40, "*"))  # center the string with 40 spaces and fill it with *

print("Replace the word Python with ruby =",
      str_language.replace("PYTHON", "ruby"))  # changed certain words to another words

print("Checking the string is starting with z? =",
      str_language.endswith("z"))  # checking if the string ending with certain character

print("Checking is the string starting with s? =",
      str_language.startswith("s"))  # checking if the string starting with certain character

print("The length of the string  =", len((str_language)))  # finding the length of the string, will include spaces
str_language = str_language.strip()  # get rid of whitespaces at both ends
print("Length of the string after strip =", len(str_language))

# using method in if else
print("Is the string starting with p?")
if str_language.startswith("p"):
    print("Yes, the string is starting with p")
else:
    print("No, the string is not starting with p")

# splitting the string and convert it into list
str_language = "python:ruby:java:c++"
print(str_language.split(":"))

# -----------------------------------------------------------------------------------------------------

# LIST METHOD

# convert list to string
list_language = ["python", "ruby", "c++", "java"]
print("Converting list into string =", ",".join(list_language))

# append new element to list_languages
list_language.append("swift")
print("After APPENDING new element =", list_language)

# extending with many elements
list_language.extend(["go", "php", "r"])
print("After EXTENDING new elements =", list_language)

# get count of certain values in the list
getCount = list_language.count("python")
print("Number of word 'python' in the list =", getCount)

# inserting new element into the list
# insert(where to insert, what to insert)
# insert(index no, element)
list_language.insert(0, "javascript")
print("After inserting new element in index 0 =", list_language)

# pop element from the list, if no index no is given, will pop everything
list_language.pop(3)
print("After pop element at index 2 =", list_language)

# remove element from the list directly, no index no is needed
list_language.remove("r")
print("After remove r =", list_language)

# reverse the list
list_language.reverse()
print("After reversing the list =", list_language)

# sort the list in ascending order either number( 0, 1, 2...) or character (a, b, c...)
list_language.sort()
print("After sorting the list =", list_language)

# sort the list descending order
list_language.sort(reverse=True)
print("After sorting the list in descending =", list_language)

# -----------------------------------------------------------------------------------------------------

# TUPLE METHOD
# have only 2 methods, count and index. this is because tuple is immutable

tuple_number = (12, 13, 14, 15)
print(tuple_number.count(12))
print(tuple_number.index(12))

# -----------------------------------------------------------------------------------------------------

# DICTIONARY METHOD

dict_book = {"chap1": 10, "chap2": 30, "chap3": 20}
dict_book1 = {"chap10": 90, "chap11": 70, "chap12": 50}

# add new key-value pair
dict_book["chap4"] = 40
print("New dictionary after add new key-value pair =", dict_book)

# display only keys
print("ONLY keys =", dict_book.keys())

# display only values
print("ONLY values =", dict_book.values())

# using items to display
print("Using item =", dict_book.items())

# get the values of certain keys, if no values will return none
print("What inside chap100 =", dict_book.get("chap100"))

# pop out key-value from dictionary
dict_book.pop("chap1")
print("After pop key-value =", dict_book)

# remove random key-value pairs
dict_book.popitem()
print("After randomly pop value =", dict_book)

# adding 2 dictionaries
final_dict = {**dict_book, **dict_book1}
print("Adding 2 dictionaries =", final_dict)

# adding 2 dictionaries v2
dict_book.update(dict_book1)
print("Adding with update method =", dict_book)

# -----------------------------------------------------------------------------------------------------

# SET METHOD
setA = {1, 3, 4, 5, 7,45}
setB = {45, 23, 76}

# add new values into set
setA.add(100)
print(setA)

print("Contain all set =", setA.union(setB))
print("Intersect =", setA.intersection(setB))