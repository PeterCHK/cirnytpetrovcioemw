create user crypto identified by 'good-firm';

create database crypto;

use crypto

create table ip (`from` VARCHAR(12) NOT NULL, `to` VARCHAR(12) NOT NULL, `short` VARCHAR(2) NOT NULL, `country` VARCHAR(32) NOT NULL);

LOAD DATA LOCAL INFILE '/home/pc/projects/interview/crypto.com/q1/IP2LOCATION-LITE-DB1.CSV'
INTO TABLE ip
FIELDS TERMINATED BY ',' ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;
