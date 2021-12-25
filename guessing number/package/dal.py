import sqlite3




def create_table():
    try:
        connection = sqlite3.Connection("file/app.db")
        cursor = connection.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS user (
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
        """
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except sqlite3.Error as err:
        return ("ERROR",err)
    else:
        return ("SUCCESS",None)
    finally:
        if connection:
            connection.close()
    
                
def insert(username,password):
    try:
        connection = sqlite3.Connection("file/app.db")
        cursor = connection.cursor()

        query = """        
            INSERT INTO user(username,password)
            VALUES (?,?);
        """      
        val = (username,password)

        cursor.execute(query,val)
        connection.commit()

        cursor.close()
        
    except sqlite3.Error as err:
        return ("ERROR",err)
    else:
        return ("SUCCESS",None)
    finally:
        if connection:
            connection.close()
        
     
def select(username=None,password=None):
    try:
        connection = sqlite3.Connection("file/app.db")
        cursor = connection.cursor()

        query = """        
            SELECT * FROM user
        """  
        
        if username!="" and password!="":
              query += f"Where username='{username}' and password='{password}'"  

        cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        
    except sqlite3.Error as err:
        return ("ERROR",err)
    else:
        return ("SUCCESS",res)
    finally:
        if connection:
            connection.close()



