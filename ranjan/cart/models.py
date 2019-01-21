from django.db import models

# Create your models here.

'''create table customer(
    email varchar(50),
    firstname varchar(30),
    lastname varchar(30),
    password varchar(30),
    phone varchar(15),
    address varchar(100),
    city varchar(30),
    pin varchar(10)
    primary key (email);'''


'''create table products(
    pid varchar(30),
    name varchar(50),
    description varchar(150), 
    imgurl varchar(200), 
    price int,
    primary key (pid))'''

'''insert into products(pid,name,description, imgurl,price) values
 ('111' , 'chair', 'its a red very big chair', 'image ka url', 800);'''


''' Create table cartdata(
    email varchar(50),
    pid varchar(30),
    fromdate date,
    todate date,
    count int,
    FOREIGN KEY (email) REFERENCES customer(email),
    FOREIGN KEY (pid) REFERENCES products(pid),
    primary key(email,pid,fromdate,todate));
'''

''' 
create table address(
    addid int not null auto_increment,
    email varchar(50),
    locality varchar(100),
    city varchar(30),
    pin varchar(10),
    primary key (addid),
    FOREIGN KEY (email) REFERENCES customer(email));
'''

''' Create table delivery(
    delid int not null auto_increment,
    email varchar(50),
    pid varchar(30),
    fromdate date,
    todate date,
    count int,
    addid int,
    FOREIGN KEY (addid) REFERENCES address(addid),
    FOREIGN KEY (email) REFERENCES customer(email),
    FOREIGN KEY (pid) REFERENCES products(pid),
    primary key(delid));
'''

