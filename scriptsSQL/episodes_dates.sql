-- After creating DATABASE in MYSQL
-- SQL script that creates table episodes_dates for the Joy of Painting API.
CREATE TABLE IF NOT EXISTS episodes_dates (
    id SERIAL PRIMARY KEY,
    title TEXT,
	episode_date DATE
);

LOAD DATA INFILE './data_source/JOP_Episode_Dates'
INTO TABLE episodes_dates
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(title, @var1, @var2)
SET episode_date = STR_TO_DATE(CONCAT(@var2, ' ', @var1), '%Y %M %d');
