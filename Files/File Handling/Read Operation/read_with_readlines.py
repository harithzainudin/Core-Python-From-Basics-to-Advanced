# 3) using readlines()
# not generally suggested as it displaying the complete file at a time
# output will be in the list format

# display all
with open("realestate.csv", "r") as fobj:
    print(fobj.readlines())

# display some particular lines
with open("realestate.csv", "r") as fobj:
    print(fobj.readlines()[20])