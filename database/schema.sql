CREATE TABLE attacks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    attack_type VARCHAR(255),
    description TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
