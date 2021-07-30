import MySQLdb
# from django.core.checks.messages import DEBUG
from NSS.settings import DEBUG

def mysqldb():
    try:
        print(DEBUG)
        if DEBUG==True:
            mydb = MySQLdb.connect(
                "us-cdbr-east-03.cleardb.com",
                "bf07c1db527b49",
                "3caf1e6d",
                "heroku_7c0e58c726f0b71"
            )
        # elif DEBUG==True:
        #     mydb = MySQLdb.connect(
        #         "localhost",
        #         "root",
        #         "",
        #         "plantation"
        #     )
    except:
        print("Can't connect to database")
        return
    
    return mydb