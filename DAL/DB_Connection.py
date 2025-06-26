import pymysql

def _get_connection():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "eagleeyedb",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def execute(query, params=None, commit=True):
    conn = _get_connection()
    cursor = conn.cursor()

    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
            
        if commit:
            conn.commit()

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

        
