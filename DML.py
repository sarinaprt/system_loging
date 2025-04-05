from mysql.connector import connection,Error

def drop_creat_database(system_log):
    config={'user':'root','password':'belive_god1527','host':'localhost','database':'system_log'}
    try:
        conn=connection.MySQLConnection(**config)
        cur=conn.cursor()
        cur.execute(f"DROP DATABASE IF EXISTS{system_log}")
        cur.execute(f"CREATE DATABASE {system_log}")
        conn.commit()
    except Error as e:
        print(f"error")
    finally:
        if cur:
            cur.close()
        if conn.is_connected():
            conn.close()

def user():
    config={'user':'root','password':'belive_god1527','host':'localhost','database':'system_log'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXIST USERS(
                id INT AUTO_INCREMENT PRIMERY KEY,
                USERNAME VARCHAR(50) UNIQUE NOT NULL,
                EMAIL VARCHAR(50) UNIQUE NOT NULL,
                CREATE_AT TIMSTAMP DEFULT CURRENT_TIMESTAMP

    )""")
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    database = 'system_log'  
    drop_creat_database(database)
    user()