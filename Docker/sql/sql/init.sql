CREATE USER 'user' @'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
CREATE USER 'user' @'%' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT ALL PRIVILEGES ON < 指 定 す る DB >.* TO 'user' @'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON < 指 定 す る DB >.* TO 'user' @'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;