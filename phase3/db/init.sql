DROP DATABASE IF EXISTS flaskDB2;
CREATE DATABASE flaskDB2;

CREATE TABLE IF NOT EXISTS Users
            (
                id serial PRIMARY KEY NOT NULL,
                name varchar(100) NOT NULL,
                email varchar(100) UNIQUE NOT NULL,
                password varchar(50) NOT NULL,
                role varchar(100) NOT NULL
            );

CREATE TABLE IF NOT EXISTS Appointments
            (
                id serial PRIMARY KEY NOT NULL,
                date varchar(100) NOT NULL,
                hour varchar(100) NOT NULL,
                createdBy INT NOT NULL,
                occupiedBy INT,
                CONSTRAINT fk_doctor FOREIGN KEY(createdBy) REFERENCES Users(id),
                CONSTRAINT fk_patient FOREIGN KEY(occupiedBy) REFERENCES Users(id)
            );