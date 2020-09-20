create schema contactos;
use contactos;
create table mycontactos(
id int primary key auto_increment not null,
nombre char(60),
numero char(16),
email varchar(200)
);
create table block(
id int primary key auto_increment,
titulo char(200),
nota varchar(300));