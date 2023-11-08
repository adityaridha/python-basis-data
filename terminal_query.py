import psycopg2
from psycopg2.extras import DictCursor
from prettytable import PrettyTable

db_params = {
    "dbname": "polban2",
    "user": "postgres",
    "password": "Bandung#321",
    "host": "localhost",  
    "port": "5432",  
}

def print_data_as_table(data):
    table = PrettyTable()
    
    keys = list(dict(data[0]).keys())    
    table.field_names = keys
    
    for row in data:
        values = list(row.values())
        table.add_row(values)

    print(table)

def connect_and_read():
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor(cursor_factory=DictCursor)

        while True:
            user_query = input("Masukan nama mahasiswa (or 'exit' to quit): ")
            if user_query.lower() == 'exit':
                break
            
            query = "select * from mahasiswa where nama ilike '%{}%'".format(user_query)
            cursor.execute(query)
            data = cursor.fetchall()
            print_data_as_table(data)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    connect_and_read()
