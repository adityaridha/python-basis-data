import psycopg2

connection = psycopg2.connect(host='localhost', user='postgres', password='Bandung#321', dbname='polban2')
cursor = connection.cursor()

cursor.execute("SELECT nim, nama FROM mahasiswa")
data = cursor.fetchall()

for row in data:
    print(row)
    
cursor.close()
connection.close()