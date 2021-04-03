import MySQLdb

def mysqldb():
    try:
        mydb = MySQLdb.connect(
            "localhost",
            "root",
            "",
            "plantation"
        )
    except:
        print("Can't connect to database")
        return
    
    return mydb