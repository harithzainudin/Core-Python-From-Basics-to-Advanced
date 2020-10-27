# 5. Dictionary - hash or map
# contains elements in key value pairs, defined in {}
# object = {key:value, key:value, key:value]
# key is used to identify the value, keys can be number OR string
# values can be number OR string OR list OR tuple OR dictionary
# example books contents - keys(chapter), values(page number)

dict_book = {"chap1": 10, "chap2": 30, "chap3": 20}
print(dict_book)

# if new chap1, then the values will be overwrite
dict_book = {"chap1": 10, "chap2": 30, "chap3": 20, "chap1": 999}
print(dict_book)
print("This is chapter 1 values =", dict_book["chap1"])
print("This is chapter 2 values =", dict_book["chap2"])
print("This is chapter 3 values =", dict_book["chap3"])

# the values is a list
dict_book_detail = {"chap1": ["Ali", "Johor", 10], "chap2": ["Ahmad", "Selangor", 30],
                    "chap3": ["Sunita", "Kelantan", 342]}
print(dict_book_detail)
print("This is chapter 1 values =", dict_book_detail["chap1"])

# adding new key:value
dict_book_detail["chap4"] = 234

# --------------------------------------------------------------------------------------------------------

# Nested Data in Dictionaries

nested_data = {
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}

# only want to access "Standard Generalized Markup Language"
print(nested_data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm'])

nested_data_with_list = {"menu": {
    "id": "file",
    "value": "File",
    "popup": {
        "menuitem": [
            {"value": "New", "onclick": "CreateNewDoc()"},
            {"value": "Open", "onclick": "OpenDoc()"},
            {"value": "Close", "onclick": "CloseDoc()"}
        ]
    }
}}

# accessing value in a list in dictionaries
print(nested_data_with_list['menu']['popup']['menuitem'][0]['value'])
print(nested_data_with_list['menu']['popup']['menuitem'][1]['value'])
print(nested_data_with_list['menu']['popup']['menuitem'][2]['value'])

