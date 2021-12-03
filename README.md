# WebAplicationClub

## Django Admin User

データベースに初期値を入れないと使いので注意してね (⋈◍＞◡＜◍)。✧♡

```bash
cd api && sh ./config/models/init_data.sh
```

```
email: TanakaTanao@club.hekuta.com
password: TESTAREA
```

## 環境構築方法

## Docker

最初は起動するのに時間かかります、、
待ってあげてください。。

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

```bash
pip install --upgrade pip
pip install pipenv
```

## pyflow

pyflowではmysqlの設定が必要になる。

mysqlをインストールして使ってください。

```bash
pyflow install
```

### Django起動
```bash
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
