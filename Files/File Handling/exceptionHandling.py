

try:
    filename = input("Enter filename: ")
    with open (filename, "r") as fobj:
        for line in fobj:
            line = line.strip()
            print(line)

except FileNotFoundError as err:
    print(err)
except TypeError as err:
    print(err)
except KeyError as err:
    print(err)
except (ValueError, FileExistsError, IndexError) as err:
    print(err)
except Exception as error:
    print("File does not exist")
    print("System error: ", error)