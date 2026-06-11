CREATE DATABASE prices;

USE prices;

CREATE TABLE market (
  id int NOT NULL AUTO_INCREMENT,
  market_date date DEFAULT NULL,
  price decimal(10,0) NOT NULL,
  PRIMARY KEY (id)
);
