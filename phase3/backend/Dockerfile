FROM python:3.8

WORKDIR /app

# ARG DB_HOST
# ENV DB_HOST 0.0.0.0

# ARG POSTGRES_USER
# ENV POSTGRES_USER postgres

# ARG ENV POSTGRES_DB
# ENV POSTGRES_DB flaskDB2

# ARG POSTGRES_PASSWORD
# ENV POSTGRES_PASSWORD alag3107

# ARG POSTGRES_PORT
# ENV POSTGRES_PORT 5432

# ARG PORT
# ENV PORT=${PORT:-5000}



# ARG DB_LISTEN_PORT
# ENV DB_LISTEN_PORT=${DB_LISTEN_PORT:-5432}

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE $LISTEN_PORT

# CMD ["python", "app.py"]
CMD python app.py

#---------------

# # Build stage
# FROM python:3.8.3-alpine as build

# WORKDIR /app

# # ARG DB_HOST
# # ENV DB_HOST 0.0.0.0

# # ARG POSTGRES_USER
# # ENV POSTGRES_USER postgres

# # ARG POSTGRES_DB
# # ENV POSTGRES_DB flaskDB2

# # ARG POSTGRES_PASSWORD
# # ENV POSTGRES_PASSWORD alag3107

# # ARG POSTGRES_PORT
# # ENV POSTGRES_PORT 5432

# # ARG PORT
# # ENV PORT=${PORT:-5000}

# # ARG DB_LISTEN_PORT
# # ENV DB_LISTEN_PORT=${DB_LISTEN_PORT:-5432}

# COPY . /app

# # Production stage
# FROM python:3.8.3-alpine

# WORKDIR /app

# COPY --from=build /app /app

# RUN pip install --no-cache-dir -r requirements.txt

# RUN apk add libpq gcc musl-dev postgresql-dev \
#     && pip install -r requirements.txt \
#     && pip install psycopg2

# ENV PATH="/app:${PATH}"

# EXPOSE $PORT

# CMD python app.py
