import psycopg2
from my_flight_package.decorators import db_error_handler

@db_error_handler
def init_db():
    conn = psycopg2.connect(dbname="flights", user="postgres", password="18181818", host="localhost", port="5432")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS flights (
                        id SERIAL PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        destination TEXT,
                        price REAL,
                        flight_date DATE,
                        class TEXT)''')

    conn.commit()
    conn.close()
