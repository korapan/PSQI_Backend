import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
from IPython.display import display, HTML # used to print out pretty pandas dataframes
import matplotlib.dates as dates
import matplotlib.lines as mlines

def connection():
    # specify user/password/where the database is
    sqluser = 'myuser'
    sqlpass = 'mypassword'
    dbname = 'postgres'
    schema_name = 'public'
    host = '127.0.0.1'

# connect to the database
    return  psycopg2.connect(dbname=dbname, user=sqluser, password=sqlpass, host=host)




def insert_data_psqi(ID, sex, ofAge, year, numoflearn, learnforweek):

    conn = connection()
#Creating a cursor object using the cursor() method
    cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
    sql = """INSERT INTO psqi (sex, age, Year, NumberOfLearn, LearnFor, id) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""

        # ข้อมูลที่ต้องการเพิ่ม
    record_to_insert = (sex, ofAge, year, numoflearn, learnforweek,ID)

        # Execute คำสั่ง SQL และใส่ข้อมูล
    cursor.execute(sql, record_to_insert)

    conn.commit()

    print("INSERT SUCCESS")
    conn.close

