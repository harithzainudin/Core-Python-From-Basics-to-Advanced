import pymysql
# import cx_oracle  -----> Oracle
# import pymysql    -----> SQLserver
# import pymongo    -----> MongoDb


try:
    # connect to database
    db = pymysql.connect(host='localhost', port=3306, user='root', password='V@nilla7', database='information')
    if db:
        cursor = db.cursor()
        query = "select * from realestate"
        cursor.execute(query)
        for record in cursor.fetchall():
            print(record)

    db.close()

except Exception as err:
    print(err)