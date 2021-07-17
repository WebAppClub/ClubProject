# 環境構築方法

### Pyflowをインストール
```bash
brew install pyflow
```

### ライブラリーをインストールする
```bash
pyflow package
```
その後に1を選ぶ


### djangoサーバーを起動
```bash
pyflow manage.py migrate
pyflow manage.py runserver
```

### Pythonファイルをフォーマットする方法(Black)
```bash
pyflow black PythonファイルへのPath
```

### Python or Djangoのコマンドを使う時
```bash
pyflow そのコマンド
```

## Build Setup

```bash
# 依存関係をインストールする
$ yarn install

# 0.0.0.0:3333でホットリロードを提供
$ yarn dev

# 本番用にビルドしてサーバーを立ち上げる
$ yarn build
$ yarn start

# 静的プロジェクトの生成
$ yarn generate
```
