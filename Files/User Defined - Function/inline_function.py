# lambda function
# function = lambda variables: expression
#lambda is the replacement of single line function ONLY
# execution is faster using lambda
increment = lambda x : x + 5

total = increment(10)
print(total)

# -------------------------------------------------------

add = lambda x,y : x +y
total = add(10, 20)

# -------------------------------------------------------

checkValue = lambda x: True if x == 100 else False
print(checkValue(100))