# write python program to capture any filename from the keyboard
# and display its filename and extensions separately

fileName = input("Enter any filename: ")

print("You entered: ", fileName)

output = fileName.split(".")

print("File name    : ", fileName)
print("Extension    : ", output[1])
