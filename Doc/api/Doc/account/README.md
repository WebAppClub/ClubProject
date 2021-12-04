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
| account_type | PK | - | - | AccountTypeモデル | [詳しくはAccountTypeモデルの説明を参照](##AccountTypeモデル)|
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
| tel | TextField | True | True | - | 必須ではない |
| birthday | DateTimeField | True | True | - | - |
| address_level_1 | TextField | False | False | - | 都道府県 |
| address_level_2 | TextField | False | False | - | 市区町村 |
| address_line_1 | TextField | False | False | - | 番地・マンション名(1行目) |
| address_line_2 | TextField | False | False | - | 番地・マンション名(2行目) |
| created_at | - | - | - | - | 作成日時 |
| updated_at | - | - | - | - | 更新日時 |

## AccountTypeモデル

|  Column  |  Type  | null | blank | Key | 備考 |
|   ----   |  ----  | ---- |  ---  | --- | ---- |
| id | PrimaryKey | - | - | PK | - |
| name | TextField | False | False | - | 24文字まで |
| description | TextField | False | False | - | 720文字まで |

## AccountPermission

このモデルは変更される可能性が大きいです。

それぞれはアカウントの種類に分けて、権限分けができる感じです。

|  Column  |  Type  | null | blank | Key | 備考 |
|   ----   |  ----  | ---- |  ---  | --- | ---- |
| id | PrimaryKey | - | - | PK | - |
| is_can_buy | BooleanField | False | False | - | - |
| is_can_sell | BooleanField | False | False | - | - |
| is_can_open_admin | BooleanField | False | False | - | - |
| is_can_create_account_type | BooleanField | False | False | - | - |
| is_can_delete_account_type | BooleanField | False | False | - | - |
| is_can_delete_account_permission | BooleanField | False | False | - | - |
| is_can_create_account_permission | BooleanField | False | False | - | - |
| is_can_delete_account | BooleanField | False | False | - | - |