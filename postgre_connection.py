import psycopg2
from psycopg2.extras import DictCursor


try:
    connection = psycopg2.connect(
        host='localhost', 
        user='postgres', 
        password='Bandung#321', 
        dbname='polban2'
        )

cursor = connection.cursor(cursor_factory=DictCursor)


cursor.execute("SELECT nim, nama FROM mahasiswa")
data = cursor.fetchall()

for row in data:
    print(dict(row)['nama'])
    
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")