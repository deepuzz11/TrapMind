CREATE TABLE attack_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    attack_type VARCHAR(255),
    details TEXT
);

CREATE TABLE user_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    behavior_data TEXT,
    timestamp DATETIME
);
