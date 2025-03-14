CREATE DATABASE ids_db;
USE ids_db;
CREATE TABLE intrusions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip VARCHAR(255),
    port INT,
    payload TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
