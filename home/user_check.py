from home.mysql import mysqldb

def user_check():
    mydb = mysqldb()
    mycursor = mydb.cursor()
    query = "select user from home_users"
    mycursor.execute(query)
    result = mycursor.fetchall()
    old_user_list = []
    for i in result:
        old_user_list.append(i[0])
    print(old_user_list)

    query2 = "select username from auth_user"
    mycursor.execute(query2)
    new_result = mycursor.fetchall()
    new_user_list = []
    for j in new_result:
        new_user_list.append(j[0])
    print(new_user_list)

    for i in old_user_list:
        if i not in new_user_list:
            query3 = "delete from maps_blog where user='" + i + "'"
            mycursor.execute(query3)
            query3 = "delete from schedule_tt where host='" + i + "'"
            mycursor.execute(query3)
            query4 = "delete from home_users where user='" + i + "'"
            mycursor.execute(query4)
            mydb.commit()
