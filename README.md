# 環境構築方法

### Pyflowをインストール
```bash
brew install pyflow
```

### ライブラリーをインストールする
```bash
pyflow package
```


### djangoサーバーを起動
```bash
pyflow manage.py migrate
pyflow manage.py runserver
```

### Pythonファイルをフォーマットする方法(Black)
```bash
pyflow black PythonファイルへのPath
```
