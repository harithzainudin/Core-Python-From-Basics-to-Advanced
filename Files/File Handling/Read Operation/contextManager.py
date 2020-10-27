
# if any line is starting with keyword "with", it is known as context manager
# Advantage: file will be closed automatically when it comes out of indentation

with open("contextManager.txt", "w") as fobj:
    for val in range(1, 101):
        fobj.write(str(val) + "\n")
