-- Create Database
CREATE DATABASE IF NOT EXISTS notes_db;

USE notes_db;

-- Create Table
CREATE TABLE IF NOT EXISTS notes (
    note_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    content TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create View (Hide content)
CREATE OR REPLACE VIEW notes_view AS
SELECT note_id, title, created_at FROM notes;