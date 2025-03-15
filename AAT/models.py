import sqlite3
def queryDb(database_path,table_name,sql):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(sql)
        res=cursor.fetchall()
        print("query result:")
        print(res)
        conn.close()
        return res

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

def getParameters(database_path, table_name,col_name)->list:
    """Counts the number of rows in a SQLite3 table."""
    res=queryDb(database_path,table_name,f"SELECT  {col_name}  FROM {table_name}")
    formatted_result = [parameter[0] for parameter in res]
    print("after formating")
    print(formatted_result)
    return formatted_result

def getFirstSARes(database_path,table_name):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        
        sql='SELECT intake_year,sa1 FROM Summative'
        res= cursor.execute(sql).fetchall()#a list of tuples,each tuple is a row

        res_by_yr={}
        for row in res:
            res_by_yr.setdefault(row[0],[]).append(row[1])
        
        for intake_yr in res_by_yr:
            res_by_yr[intake_yr].sort()
        
        conn.close()
        return res_by_yr

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    