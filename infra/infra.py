import pandas as pd 
import sqlite3 
import os   

def databasePath():
    try:
        current_path = os.path.dirname(os.path.abspath(__file__))
        return f'{current_path}/../data/data.sqlite'
    except:
        raise
           
def queryDatabase(query):
    try: 
        connection = sqlite3.connect(databasePath())
        cur = connection.execute(query)
        names = list(map(lambda x: x[0], cur.description))
        data = cur.fetchall()
        connection.close()
        return [data, names]
    except:
        raise

def insertDatabase(query):
    try: 
        connection = sqlite3.connect(databasePath())
        connection.execute(query) 
        connection.commit()
        connection.close()
        return 'ok'
    except:
        raise 
    
def getDataFromMysql(query):
    try:
        cur, names = queryDatabase(query)
        data = pd.DataFrame(data=cur, columns=names) 
        return data 
    except:
        raise
 