from mysql.connector import connection, Error

def insert_user(USERNAME,password):
    config={'user':'root','password':'password','host':'localhost','database':'system_log'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    SQL_QUERY="INSERT INTO USERS(USERNAME,PASSWORD) VALUES ( %s, %s)"

    cur.execute(SQL_QUERY,(USERNAME, password, CREATE_AT)) 
    conn.commit()
    cur.close()
    conn.close()




if __name__=='__main__':
    insert_user()
