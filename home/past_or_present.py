from datetime import date, datetime
from home.mysql import mysqldb
import MySQLdb

def past_or_present():
    today = date.today()
    now = datetime.now()
    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%y-%m-%d %H:%M:%S")
    print(dt_string)
    # mydb = MySQLdb.connect(
    #     "localhost",
    #     "root",
    #     "",
    #     "plantation"
    # )
    mydb = mysqldb()
    mycursor = mydb.cursor()
    # query ='INSERT INTO schedule_pastevents SELECT * FROM schedule_tt WHERE unique_id="4284d9f6-5b44-4105-b863-4731de9251b6"'
    query = 'SELECT date, time, unique_id from schedule_tt'
    mycursor.execute(query)
    result = mycursor.fetchall()
    event_date = ''
    for i in result:
        event_date_time = '' + i[0] + ' ' + i[1]
        date_time_obj = datetime.strptime(event_date_time, '%Y-%m-%d %H:%M:%S')
        if now > date_time_obj:
            print('Event is done')
            print(i[2])
            query_2 = 'INSERT INTO schedule_pastevents SELECT * FROM schedule_tt WHERE unique_id="' + i[2] + '"'
            mycursor.execute(query_2)
            mydb.commit()
            
            query_3 = "DELETE FROM schedule_tt WHERE unique_id='" + i[2] + "'"
            mycursor.execute(query_3)
            mydb.commit()
        elif now < date_time_obj:
            print('Event will come')

