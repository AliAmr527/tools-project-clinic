import psycopg2
import os

# time.sleep(10)
#TODO:CHANGE THIS TO DB FOR THE CONTAINER TO WORK

DB_HOST = os.environ.get('DB_HOST')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_DB  = os.environ.get('POSTGRES_DB ')



initial_conn = psycopg2.connect(database = POSTGRES_DB, host=DB_HOST, user=POSTGRES_USER, password=POSTGRES_PASSWORD, port=POSTGRES_PORT)
initial_cur = initial_conn.cursor()

# Create the database if it doesn't exist
initial_cur.execute("CREATE DATABASE IF NOT EXISTS flaskDB2;")

initial_cur.close()
initial_conn.close()

conn = psycopg2.connect(database="flaskDB2",host="db",user="postgres",password="alag3107",port="5432")
cur = conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS Doctors 
#             (
#                 id serial PRIMARY KEY, 
#                 name varchar(100),
#                 appointments varchar(100)
#             );''')


cur.execute('''
            CREATE TABLE IF NOT EXISTS Users
            (
                id serial PRIMARY KEY NOT NULL,
                name varchar(100) NOT NULL,
                email varchar(100) UNIQUE NOT NULL,
                password varchar(50) NOT NULL,
                role varchar(100) NOT NULL
            );''')

#mock doctor data
#cur.execute(f'''INSERT INTO Doctors (name,password,profession) VALUES ('{doctorName}','123','brain surgeon')''')
#cur.execute(f'''DELETE FROM Doctors WHERE id=3''')

# cur.execute('''
#             CREATE TABLE IF NOT EXISTS Patients
#             (
#                 id serial PRIMARY KEY,
#                 name varchar(100),
#                 password varchar(50)
#             );''')

cur.execute('''
            CREATE TABLE IF NOT EXISTS Appointments
            (
                id serial PRIMARY KEY NOT NULL,
                date varchar(100) NOT NULL,
                hour varchar(100) NOT NULL,
                createdBy INT NOT NULL,
                occupiedBy INT,
                CONSTRAINT fk_doctor FOREIGN KEY(createdBy) REFERENCES Users(id),
                CONSTRAINT fk_patient FOREIGN KEY(occupiedBy) REFERENCES Users(id)
            );''')

#cur.execute(f'''INSERT INTO Appointments (slotName,createdBy) VALUES ('wed10',2)''')

#cur.execute(f'''INSERT INTO Patients (name,password) VALUES ('andrew','523')''')

#cur.execute(f'''UPDATE Appointments SET occupiedBy=1 WHERE id=6''')

#cur.execute('''INSERT INTO Doctors (name,appointments) VALUES ('ahmed','thu08'),('samy','wed10')''')

conn.commit()
cur.close()
conn.close()