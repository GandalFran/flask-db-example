
/*create db*/
CREATE DATABASE SENSOR_EXAMPLE;
USE SENSOR_EXAMPLE;

/*create table for sensor data*/
CREATE TABLE SENSOR_DATA (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    DATA TEXT,
    DATA_TYPE VARCHAR(100) NOT NULL,
    ORIGIN VARCHAR(100) NOT NULL
);

/*create user and grant privileges*/
CREATE USER 'sensor_ingest'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON SENSOR_EXAMPLE.* to sensor_ingest@'localhost' IDENTIFIED BY '1234';