FROM postgres:latest

# ARG DB_HOST
# ENV DB_HOST localhost

# ARG POSTGRES_USER
# ENV POSTGRES_USER postgres

# ARG ENV POSTGRES_DB 
# ENV POSTGRES_DB flaskDB2

# ARG POSTGRES_PASSWORD
# ENV POSTGRES_PASSWORD alag3107

# ARG POSTGRES_PORT
# ENV POSTGRES_PORT 5432

# ARG PGDATA
# ENV PGDATA /var/lib/postgresql/data/pgdata

COPY init.sql /docker-entrypoint-initdb.d/

WORKDIR /app

COPY . /app


USER root


USER postgres

EXPOSE 5432
