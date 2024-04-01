-- After creating DATABASE in MYSQL
-- SQL script creates table for the Joy of Painting API.
-- Remember to start SQL server : service mysql start
-- execute code mysql -u root -p joy_of_painting < colors.sql
SET GLOBAL local_infile=true;
GRANT FILE ON *.* TO 'root'@'localhost';
CREATE DATABASE IF NOT EXISTS joy_of_painting;

USE joy_of_painting;
CREATE TABLE IF NOT EXISTS happy_bob(
    ID SERIAL PRIMARY KEY,
    Title VARCHAR(80), 
    Month VARCHAR(255),
    Date DATE,
    Episode VARCHAR(60),
    Subject VARCHAR(255),
    Painting_index INTEGER,
    Img_src VARCHAR(255),
    Season INTEGER NOT NULL,
    Episodes VARCHAR(20),
    Num_colors VARCHAR(255),
    Youtube_src VARCHAR(255),
    Colors VARCHAR(255),
    Color_hex VARCHAR(255)
);

LOAD DATA INFILE './data_source/beautiful_JOP.csv'
INTO TABLE happy_bob
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID, Title,  Month, @Date, Episode, Subject, Painting_index, Img_src, 
Season, Episodes, Num_colors, Youtube_src, Colors, Color_hex)
SET Date = STR_TO_DATE(@Date, '%m-%d-%Y');