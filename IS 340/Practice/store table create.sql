CREATE TABLE store
(storeid VARCHAR(3) NOT NULL,
storezip CHAR(5) NOT NULL,
regionid CHAR(1) NOT NULL,
PRIMARY KEY(storeid),
FOREIGN KEY (regionid) REFERENCES region(regionid));