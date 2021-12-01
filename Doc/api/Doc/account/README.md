# アカウントに関するモデルについて

ユーザー情報や権限に関するモデル

## Userモデル

|  Column  |  Type  | null | blank | Key | 備考 |
|   ----   |  ----  | ---- |  ---  | --- | ---- |
| id | PrimaryKey | - | - | PK | - |
| email | EmailField | - | - | - | 無し|
| password | 標準 | - | - | - | - |
| nickname | TextField | False | False | - | 32文字まで |
| last_login | DateTimeField | True | True | - | - |
| data_joined | DateTimeField | False | False | - | - |
| is_admin | BooleanField | False | False | - | 開発環境にのみ適用 |
| is_staff | BooleanField | False | False | - | 開発環境にのみ適用 |
| account_type | PK | - | - | AccountTypeモデル | [詳しくはAccountTypeモデルの説明を参照](##AccountTypeモデル)

## User_infoモデル

## AccountTypeモデル

## AccountPermission