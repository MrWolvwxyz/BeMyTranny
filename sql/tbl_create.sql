drop table user;
drop table post;

CREATE TABLE user(
userid int auto_increment PRIMARY KEY,
username VARCHAR(20),
password VARCHAR(20),
email VARCHAR(40)
);

create table post(
postid int auto_increment,
title varchar(50),
description varchar(256),
origin varchar(20),
target varchar(20),
pathtophoto varchar(128),
userid int,
primary key (postid)
);


insert into post (title, description, origin, target, pathtophoto, userid)
values 
('post1', 'bunny is cute', 'English', 'Chinese', 'where.jpg', 1);
