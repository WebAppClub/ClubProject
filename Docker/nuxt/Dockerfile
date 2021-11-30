FROM node:lts
ENV LANG=C.UTF-8 TZ=Asia/Tokyo
WORKDIR /app
RUN apt-get update && \
    apt-get upgrade -y
RUN yarn install
COPY ./web .
ENV HOST 0.0.0.0
