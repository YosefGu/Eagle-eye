import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passord = "",
        database = "engleeyedb"
    )
    return conn

def execute(query):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query)

        query_type = query.strip().split()[0].lower()

        if query_type == 'select':
            return cursor.fetchall()
        if query_type == 'insert':
            return cursor.lastrowid
        if query_type in ('update', 'delete'):
            return cursor.rowcount
        else:
            return None
    except Exception as e:
        print("Error running query: ", e)
    
    finally:
        cursor.close()
        conn.close()
        
        
