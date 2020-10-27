import pymysql
import csv
# import cx_oracle  -----> Oracle
# import pymysql    -----> SQLserver
# import pymongo    -----> MongoDb


try:
    # connect to database
    db = pymysql.connect(host='localhost', port=3306, user='root', password='V@nilla7', database='information')
    if db:
        cursor = db.cursor()
        # insert all records from the file
        # open the file
        with open("realestate.csv", "r") as fobj:
            # cinvert file object to csv object
            reader = csv.reader(fobj)
            for record in reader:
                street = record[0]
                city = record[1]
                query = "insert into realestate values('{}', '{}')".format(street, city)
                cursor.execute(query)
        db.commit()
    db.close()

except Exception as err:
    print(err)