# WebAplicationClub

## 環境構築方法

## Docker

```bash
docker-compose build
docker-compose up -d
```


# Django

## pipenv

pipenvではmysqlの設定が必要になる。
mysqlをインストールして使ってください。

```bash
pipenv install
```

### Django起動

```
cd api/
pipenv run python manage.py runserver
```

### pipenvのインストール

```
pip install --upgrade pip
pip install pipenv
```

## pyflow

pyflowではmysqlの設定が必要になる。
mysqlをインストールして使ってください。

```
pyflow install
```

### Django起動
```
cd api/
pyflow manage.py runserver
```

### pyflowのインストール

```bash
brew install pyflow
```


# Nuxt.js

node.jsとyarnをインストールしといてください。
その後に

```bash
yarn install
```

起動するには

```bash
yarn dev
```
