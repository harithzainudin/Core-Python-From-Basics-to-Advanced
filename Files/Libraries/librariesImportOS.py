import os

print("Current directory =", os.getcwd())

print("Current username :", os.getlogin())

# list all the files
for file in os.listdir():
    print(file)

# files from D:
for file in os.listdir("D:\\"):
    print(file)

# delete file in the directory
# os.remove("put the file name")


# # delete extension files in current directory
# for file in os.listdir():
#     if file.endswith(".docx") and os.path.isfile(file)
#         os.remove(file)
#
# os.mkdir("testdir")
#
# # program to create 100 directories in the below format
# for val in range(1, 101):
#     os.mkdir("dir" + str(val))
#
# os.chdir(path)
#
# for val in range(1, 101)
#     os.rmdir("dir" + str(val))

# create empty file in python
# fobj = open("abcd.txt", "w"):
# fobj.close()

# display ONLY directories
for file in os.listdir():
    if os.path.isdir(file):
        print("This is a directory ", file)

# display ONLY file
for file in os.listdir():
    if os.path.isfile(file):
        print("This is a file ", file)