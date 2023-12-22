import psycopg2
from psycopg2 import OperationalError
import time
import sys

def wait_for_db(host, port, user, password, dbname, retries=30, delay=2):
    for _ in range(retries):
        try:
            conn = psycopg2.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                dbname=dbname
            )
            conn.close()
            print("Database is ready.")
            return
        except OperationalError as e:
            print(f"Database is not ready yet. Retrying in {delay} seconds...")
            time.sleep(delay)
    print("Unable to connect to the database. Exiting.")
    sys.exit(1)

if __name__ == "__main__":
    wait_for_db(
        host="db",
        port="5432",
        user="postgres",
        password="alag3107",
        dbname="flaskDB2"
    )
