from mysql.connector import connection, Error


def user_exist(USERNAME):
    config={'user':'root','password':'','host':'localhost','database':'system_log'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("select * from USERS where USERNAME=%s",(USERNAME,))
    user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if user:
        user_id=user[0]
        password_sql=user[2]
        return user_id,password_sql
    else:
        return None

def update_pass(password,id):
    config={'user':'root','password':'','host':'localhost','database':'system_log'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("update USERS set password=%s where id=%s",(password,id))
    conn.commit()
    cur.close()
    conn.close()
    


def insert_user(USERNAME,password):
    config={'user':'root','password':'','host':'localhost','database':'system_log'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    SQL_QUERY="INSERT INTO USERS(USERNAME,PASSWORD) VALUES ( %s, %s)"
    cur.execute(SQL_QUERY,(USERNAME, password)) 
    conn.commit()
    cur.close()
    conn.close()


def get_calendar_note(id,DATE_TIME):
    config={'user':'root','password':'','host':'localhost','database':'system_log'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("SELECT NOTE FROM CALENDER WHERE id=%s and DATE_TIME=%s ",(id,DATE_TIME))
    detail=cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if detail:
        return detail[0][0]
    else:
        return None
def update_or_insert_calendar(user_id,date,NOTE):
    config={'user':'root','password':'','host':'localhost','database':'system_log'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("SELECT NOTE FROM CALENDER WHERE id=%s and DATE_TIME=%s ",(user_id,date))
    detail=cur.fetchall()

    if detail:
        cur.execute("UPDATE CALENDER SET NOTE=%s WHERE ID=%s and DATE_TIME=%s",(NOTE,user_id,date))
    else:
        cur.execute("INSERT INTO CALENDER (id,DATE_TIME,NOTE) VALUES (%s,%s,%s)",(user_id,date,NOTE))
    conn.commit()
    cur.close()
    conn.close()
        

if __name__=='__main__':
    user_exist()
    update_pass()
    insert_user()
    get_calendar_note()
    update_or_insert_calendar()
