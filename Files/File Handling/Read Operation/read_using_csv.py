# 4) read using csv library
# Advantage : each line will be converted to list automatically

import csv

# fobj is file object used for reading any kind of file
with open("realestate.csv", "r") as fobj:
    # converting file object to csv object
    reader = csv.reader(fobj)
    for line in reader:
        print(line)
