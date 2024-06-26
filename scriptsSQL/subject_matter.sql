-- After creating DATABASE in MYSQL
-- SQL script that creates table subject_matter for the Joy of Painting API.
CREATE TABLE IF NOT EXISTS subject_matter (
    EPISODE VARCHAR(10),
    TITLE TEXT,
    APPLE_FRAME INT,
    AURORA_BOREALIS INT,
    BARN INT,
    BEACH INT,
    BOAT INT,
    BRIDGE INT,
    BUILDING INT,
    BUSHES INT,
    CABIN INT,
    CACTUS INT,
    CIRCLE_FRAME INT,
    CIRRUS INT,
    CLIFF INT,
    CLOUDS INT,
    CONIFER INT,
    CUMULUS INT,
    DECIDUOUS INT,
    DIANE_ANDRE INT,
    DOCK INT,
    DOUBLE_OVAL_FRAME INT,
    FARM INT,
    FENCE INT,
    FIRE INT,
    FLORIDA_FRAME INT,
    FLOWERS INT,
    FOG INT,
    FRAMED INT,
    GRASS INT,
    GUEST INT,
    HALF_CIRCLE_FRAME INT,
    HALF_OVAL_FRAME INT,
    HILLS INT,
    LAKE INT,
    LAKES INT,
    LIGHTHOUSE INT,
    MILL INT,
    MOON INT,
    MOUNTAIN INT,
    MOUNTAINS INT,
    NIGHT INT,
    OCEAN INT,
    OVAL_FRAME INT,
    PALM_TREES INT,
    PATH INT,
    PERSON INT,
    PORTRAIT INT,
    RECTANGLE_3D_FRAME INT,
    RECTANGULAR_FRAME INT,
    RIVER INT,
    ROCKS INT,
    SEASHELL_FRAME INT,
    SNOW INT,
    SNOWY_MOUNTAIN INT,
    SPLIT_FRAME INT,
    STEVE_ROSS INT,
    STRUCTURE INT,
    SUN INT,
    TOMB_FRAME INT,
    TREE INT,
    TREES INT,
    TRIPLE_FRAME INT,
    WATERFALL INT,
    WAVES INT,
    WINDMILL INT,
    WINDOW_FRAME INT,
    WINTER INT,
    WOOD_FRAMED INT
);

LOAD DATA INFILE './data_source/JOP_Subject_Matter'
INTO TABLE subject_matter
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
IGNORE 1 ROWS;