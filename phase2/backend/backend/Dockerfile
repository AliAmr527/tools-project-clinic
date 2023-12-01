FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV LISTEN_PORT=5000
EXPOSE 5000

# ENV FLASK_APP app.py

CMD ["python", "app.py"]

############

# FROM node:lts-bullseye-slim

# WORKDIR /angularApp

# COPY ./angular /angularApp

# ENV LISTEN_PORT_ANGULAR=4200
# EXPOSE 4200

# CMD ["ng serve"]