
# if any ocject is prefixed with *, it is called as tuple
def display(*info):
    for item in info:
        print(item)

display(1,2,3,4,5,6,78,34,23,23,46,736,254,213,1564)

# if any object is prefixed with **, it is store in dictionary
def displayData(**studinfo):
    for key, value in studinfo.items():
        print(key, value)

displayData(name='Rita', age=20, location='Kuala Lumpur')