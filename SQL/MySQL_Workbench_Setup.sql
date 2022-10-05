-- Write the query to select all the names in the database. The columns should appear, even if there are no records in the database yet
SELECT * FROM names;

-- Insert your own name into the database!
INSERT INTO names (name) VALUES ("Joel");

-- Insert another name or, NINJA BONUS: insert more than one name in a single statement.
INSERT INTO names (name) 
VALUES ("Jordan"), 
("Micheal");

-- Optional: Try creating, updating and deleting records using the statements you've learn about.
UPDATE names SET name = "Ninja" WHERE id = 2;

DELETE FROM names WHERE id = 2;