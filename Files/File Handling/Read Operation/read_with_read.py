# 2) using fobj.read
# not generally suggested as it displaying the complete file at a time
# it is the best way to read small config files


with open("realestate.csv", "r") as fobj:
    print(fobj.read())