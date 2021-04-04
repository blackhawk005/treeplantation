import MySQLdb

def mysqldb():
    try:
        mydb = MySQLdb.connect(
            "us-cdbr-east-03.cleardb.com",
            "bf07c1db527b49",
            "3caf1e6d",
            "heroku_7c0e58c726f0b71"
        )
    except:
        print("Can't connect to database")
        return
    
    return mydb