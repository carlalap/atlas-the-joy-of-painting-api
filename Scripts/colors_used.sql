-- After creating DATABASE in MYSQL
-- SQL script that creates table color_used for the Joy of Painting API.
CREATE TABLE color_used (
    id SERIAL PRIMARY KEY,
    painting_index INT,
    img_src VARCHAR(255),
    painting_title TEXT,
    season INT,
    episode INT,
    num_colors INT,
    youtube_src VARCHAR(255),
    colors TEXT,
    color_hex TEXT,
    Black_Gesso INT,
    Bright_Red INT,
    Burnt_Umber INT,
    Cadmium_Yellow INT,
    Dark_Sienna INT,
    Indian_Red INT,
    Indian_Yellow INT,
    Liquid_Black INT,
    Liquid_Clear INT,
    Midnight_Black INT,
    Phthalo_Blue INT,
    Phthalo_Green INT,
    Prussian_Blue INT,
    Sap_Green INT,
    Titanium_White INT,
    Van_Dyke_Brown INT,
    Yellow_Ochre INT,
    Alizarin_Crimson INT
);

LOAD DATA INFILE './data_source/JOP_Colors_Used'
INTO TABLE color_used
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
