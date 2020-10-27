
# 1) reading with file object
# fobj is file pointer or navigator for file references
with open("realestate.csv", "r") as fobj:
    for line in fobj:
        line = line.strip()
        output = line.split(",")
        print(output[0])
        print(output[1])
        print("-------------------")