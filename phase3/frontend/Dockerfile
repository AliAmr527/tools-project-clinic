FROM node:20.9.0 as build

WORKDIR /app

COPY package.json /app/
RUN npm install

COPY . /app/
RUN npm run build 


FROM nginxinc/nginx-unprivileged:alpine3.18-perl

USER root

RUN touch /tmp/nginx.pid

RUN chmod 777 /tmp/nginx.pid


USER nginx

COPY --from=build  /app/dist/first_project/ /usr/share/nginx/html

