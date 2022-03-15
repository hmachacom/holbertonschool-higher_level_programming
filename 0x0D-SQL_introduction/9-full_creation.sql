-- create full table
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO second_table(id, name, SCORE) VALUE(1, "John", 10);
INSERT INTO second_table(id, name, SCORE) VALUE(2, "Alex", 3);
INSERT INTO second_table(id, name, SCORE) VALUE(3, "Bob", 14);
INSERT INTO second_table(id, name, SCORE) VALUE(4, "George", 8);