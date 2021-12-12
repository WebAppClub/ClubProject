# アカウントに関するモデルについて

ユーザー情報や権限に関するモデル

## Userモデル

|  Column  |  Type  | null | blank | Key | 備考 |
|   ----   |  ----  | ---- |  ---  | --- | ---- |
| id | PrimaryKey | - | - | PK | - |
| email | EmailField | - | - | - | 無し |
| password | 標準 | - | - | - | - |
| username | TextField | False | False | - | 32文字まで |
| last_login | DateTimeField | True | True | - | ログイン最終日 |
| data_joined | DateTimeField | False | False | - | - |
| is_admin | BooleanField | True | True | - | 開発環境にのみ適用 |
| is_staff | BooleanField | True | True | - | 開発環境にのみ適用 |
| account_permission | PK | - | - | AccountTypeモデル | [詳しくはAccountTypeモデルの説明を参照](##AccountTypeモデル)|
| is_deleted | BooleanField | True | True | - | アカウント削除されているかどうか |
| is_verified | False | True | - | メール認証されているか |ny
| created_at | - | - | - | - | 作成日時 |
| updated_at | - | - | - | - | 更新日時 |

## User_infoモデル

|  Column  |  Type  | null | blank | Key | 備考 |
|   ----   |  ----  | ---- |  ---  | --- | ---- |
| id | PrimaryKey | - | - | PK | - |
| user_id | ForeignKey | - | - | FK | = |
| first_name | CharField | False | False | - | 苗字 |
| middle_name | CharField | False | False | - | ミドルネーム |
| last_name | CharField | False | False | - | 名前 |
| first_name_reading | CharField | False | False | - | 苗字(カタカナ) |
| middle_name_reading | CharField | False | False | - | ミドルネーム(カタカナ) |
| last_name_reading | CharField | False | False | - | 名前(カタカナ) |
| accept_newsletter | BooleanField | True | True | - | お得情報送信許可 |
| money | PositiveIntegerField | True | True | - | default = 0 |
| all_paid | PositiveIntegerField | True | True | - | default = 0 |
| tel | CharField | True | True | - | 必須ではない |
| birthday | DateTimeField | True | True | - | - |
| address_level_1 | CharField | False | False | - | 都道府県 |
| address_level_2 | CharField | False | False | - | 市区町村 |
| address_line_1 | CharField | False | False | - | 番地・マンション名(1行目) |
| address_line_2 | CharField | False | False | - | 番地・マンション名(2行目) |
| created_at | - | - | - | - | 作成日時 |
| updated_at | - | - | - | - | 更新日時 |

--------

### get_full_name関数

**User**のフルネームを返してくれる関数

ミドルネームあるかないか関係なく取得することが可能

<p style="font-size: 18px;">
    帰り値 : <span style="color: orange; font-weight: bolder;">str</span>
</p>

<p style="font-size: 18px;">
    引数 : self, reading = <span style="color: orange; font-weight: bolder;">False</span>
</p>


**コード**
```py
def get_full_name(self, reading=False) -> str:
    if reading:
        if self.middle_name_reading is None:
            return " ".join([self.first_name_reading, self.last_name_reading])
        else:
            return " ".join(
                [
                    self.first_name_reading,
                    self.middle_name_reading,
                    self.last_name_reading,
                ]
            )
    else:
        if self.middle_name is None:
            return " ".join([self.first_name, self.last_name])
        else:
            return " ".join([self.first_name, self.middle_name, self.last_name])
```

### get_user_address関数

Userの住所を返してくれる関数

<p style="font-size: 18px;">
    帰り値 : <span style="color: orange; font-weight: bolder;">str</span> , <span style="color: orange; font-weight: bolder;">list</span>
</p>

<p style="font-size: 18px;">
    引数 : self, in_list = <span style="color: orange; font-weight: bolder;">False</span>
</p>

**コード**
```py
def get_user_address(self, in_list=False) -> str or list:
    address_list = [
        self.address_level_1,
        self.address_level_2,
        self.address_line_1,
        self.address_line_2,
    ]

    address_list = [address for address in address_list if not address is None]

    if in_list:
        return address_list
    else:
        return " ".join(address_list)
```


## AccountPermissionモデル

このモデルは変更される可能性が大きいです。

それぞれはアカウントの種類に分けて、権限分けができる感じです。

|  Column  |  Type  | null | blank | Key | 備考 |
|   ----   |  ----  | ---- |  ---  | --- | ---- |
| id | PrimaryKey | - | - | PK | - |
| name | TextField | False | False | - | 24文字まで |
| description | TextField | False | False | - | 720文字まで |
| is_can_buy | BooleanField | False | False | - | - |
| is_can_sell | BooleanField | False | False | - | - |
| is_can_open_admin | BooleanField | False | False | - | - |
| is_can_delete_account_permission | BooleanField | False | False | - | - |
| is_can_create_account_permission | BooleanField | False | False | - | - |
| is_can_delete_account | BooleanField | False | False | - | - |