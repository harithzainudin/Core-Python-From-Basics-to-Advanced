# convert tuple to list and change some elements to the list then convert back to tuple.
# This is because, tuple are immutable
tuple_nums = (10, 20, 30)
print("Old tuple =", tuple_nums)
list_nums = list(tuple_nums)
list_nums[0] = 1000
tuple_number = tuple(list_nums)
print("New tuple =", tuple_number)

# print range of list
print("Range of list from 1 to 9 =", list(range(1, 10)))
print("Range of list from 2 to 10 but step 2 nums =", list(range(2, 10, 2)))

# print id
print("ID of list_nums =", id(list_nums))

# check the type
print("Check the type of list nums using type =", type(list_nums))
print("Check the type of list nums using isinstance =", isinstance(list_nums, list))