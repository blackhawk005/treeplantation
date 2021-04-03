import MySQLdb

def mysqldb():
    try:
        mydb = MySQLdb.connect(
            "localhost",
            "coswebin_treeasurenss",
            "zthaL6#=HiTN",
            "coswebin_treeasurenss"
        )
    except:
        print("Can't connect to database")
        return
    
    return mydb