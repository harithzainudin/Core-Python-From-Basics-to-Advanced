# write a program to write all the number 1 to 100 to the file line by line

fobj = open("fileNumbers.txt", "w")

for val in range(1, 101):
    fobj.write(str(val) + "\n")

fobj.close()