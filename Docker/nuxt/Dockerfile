FROM node:lts
ENV LANG=C.UTF-8 TZ=Asia/Tokyo
WORKDIR /app
RUN apt-get update && \
    apt-get upgrade -y
COPY ./package*.json ./
RUN yarn install
COPY ./ .
ENV HOST 0.0.0.0