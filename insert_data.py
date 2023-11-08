import psycopg2
from psycopg2.extras import DictCursor

db_params = {
    "dbname": "polban2",
    "user": "postgres",
    "password": "Bandung#321",
    "host": "localhost",  
    "port": "5432",  
}

try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor(cursor_factory=DictCursor)
    
    insert_sql = """
    INSERT INTO mahasiswa (nim, nama, nomor_hp)
    VALUES (%s, %s, %s)
    """
    
    cursor.execute(insert_sql, ('1013310223', 'Muhammad Aditya R', '085959619159'))
    connection.commit()

    cursor.execute("SELECT nim, nama FROM mahasiswa")
    data = cursor.fetchall()

    for row in data:
        print(dict(row))

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
