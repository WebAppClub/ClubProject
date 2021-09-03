# Django環境構築方法

## Pipenvの環境構築

#### pipを最新バージョンにする

```bash
$ pip install --upgrade pip
```

#### Pipenvをインストールする

```bash
$ pip install pipenv
```

`pipenv`とターミナルもしくはコマンドプロンプトで打って何か出れば成功です

#### ライブラリーをインストール

```bash
$ pipenv install
```

#### Djangoサーバーを起動

```bash
# cd backend
$ pipenv run python manage.py migrate
$ pipenv run python manage.py runserver
```

#### Pythonファイルをフォーマットする方法(Black)
```bash
$ pipenv run python black
$ pipenv run python manage.py runserver
```