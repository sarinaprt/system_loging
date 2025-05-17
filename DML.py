from mysql.connector import connection,Error

def drop_creat_database(system_log):
    config={'user':'root','password':'','host':'localhost'}
    try:
        conn=connection.MySQLConnection(**config)
        cur=conn.cursor()
        cur.execute(f"DROP DATABASE IF EXISTS {system_log}")
        cur.execute(f"CREATE DATABASE {system_log}")
        conn.commit()
        cur.close()
        conn.close()
    except Error as e:
        print(f"error")
    


def user():
    config={'user':'root','password':'','host':'localhost','database':'system_log'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS USERS(
                id INT AUTO_INCREMENT PRIMARY  KEY,
                USERNAME VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL,
                CREATE_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )""")
    conn.commit()
    cur.close()
    conn.close()

def calender():
    config={'user':'root','password':'','host':'localhost','database':'system_log'}
    conn=connection.MySQLConnection(**config)
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS CALENDER(
                id INT AUTO_INCREMENT,
                DATE_TIME DATE,
                NOTE TEXT,
                PRIMARY KEY(id , DATE_TIME),
                FOREIGN KEY (id) REFERENCES USERS(id)
    )""")
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    database = 'system_log'  
    drop_creat_database(database)
    user()
    calender()