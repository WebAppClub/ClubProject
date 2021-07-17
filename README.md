#基本的な開発ルール

### Pythonファイルは必ずBlackを通す
### Pythonファイル内で新しく関数を作った場合必ずその帰り値の値を書く

```python
def double_number(double_num) -> int:
  return double_num * 2
```

### Pythonファイル内で新しく関数を作った場合必ずその関数の説明文を書く

```python
def test():
  """
  testと表示させる関数
  """
  print("test")
```

# Django環境構築方法

### Pyflowをインストール
```bash
$ brew install pyflow
```

### ライブラリーをインストールする
```bash
$ pyflow package
```
その後に1を選ぶ


### djangoサーバーを起動
```bash
$ pyflow manage.py migrate
$ pyflow manage.py runserver
```

### Pythonファイルをフォーマットする方法(Black)
```bash
$ pyflow black PythonファイルへのPath
```

### Python or Djangoのコマンドを使う時
```bash
$ pyflow そのコマンド
```

# Nuxt.jsとVuetify.jsインストール
## 環境構築方法

### 開発を始める方法
Node.jsをインストールしといてください。
やり方は下を参照しください
わからなかったらサークル責任者まで
https://github.com/hokaccha/nodebrew

### yarnをインストール
```bash
$ npm install --global yarn
```

### 依存関係をインストールする
```bash
$ yarn install
```

### 0.0.0.0:3333でホットリロードを提供
```bash
$ yarn dev
```

### 本番用にビルドしてサーバーを立ち上げる
```bash
$ yarn build
$ yarn start
```

### 静的プロジェクトの生成
```bash
$ yarn generate
```
