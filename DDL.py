from mysql.connector import connection, Error


def user_exist(USERNAME):
    config={'user':'root','password':'belive_god1527','host':'localhost','database':'system_log'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("select * from user where USERNAME=%s",(USERNAME,))
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
    config={'user':'root','password':'belive_god1527','host':'localhost','database':'system_log'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("update user set password=%s where id=%s",(password,id))
    conn.commit()
    cur.close()
    conn.close()
    


def insert_user(USERNAME,password):
    config={'user':'root','password':'belive_god1527','host':'localhost','database':'system_log'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    SQL_QUERY="INSERT INTO user(USERNAME,PASSWORD) VALUES ( %s, %s)"
    cur.execute(SQL_QUERY,(USERNAME, password)) 
    conn.commit()
    cur.close()
    conn.close()




if __name__=='__main__':
    user_exist()
<<<<<<< HEAD
=======
    update_pass()
    insert_user()
>>>>>>> c4194e0d2840ce76d8b38a8ff5f8d1412ecd6a78
