CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id varchar(255) not null,
    latitude decimal(11,8) not null,
    longitude decimal(11,8) not null,
    label varchar(255) default null,
    current_status varchar(255),
    current_stop_sequence int,
    occupancy_status varchar(255),
    speed decimal,
    updated_at varchar(255),
    direction_id int
);

