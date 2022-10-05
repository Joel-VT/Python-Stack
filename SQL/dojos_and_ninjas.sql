-- Query: Create 3 new dojos
INSERT INTO dojos (name)
VALUES ("Python"),
("Java"),
("C#");

-- Query: Delete the 3 dojos you just created
DELETE FROM dojos WHERE id = 3;
DELETE FROM dojos WHERE id = 2;
DELETE FROM dojos WHERE id = 1;

-- Query: Create 3 more dojos
INSERT INTO dojos (name)
VALUES ("Mern"),
("WebFundamentals"),
("JS");

-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Joel", "VT", 24, 4),
("Jordan", "Thomas", 26, 4),
("David", "Silva", 32, 4);

-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("George", "Varghese", 22, 5),
("Jacob", "Timothy", 30, 5),
("Dobrik", "David", 26, 5);

-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Spenser", "Rauch", 36, 6),
("Susie", "Mars", 34, 6),
("Steve", "Tobias", 32, 6);

-- Query: Retrieve all the ninjas from the first dojo
SELECT ninjas.*, dojos.name AS dojo_name 
FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id 
WHERE dojo_id = 4;

-- Query: Retrieve all the ninjas from the last dojo
SELECT ninjas.*, dojos.name AS dojo_name 
FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id 
WHERE dojo_id = 6;

-- Query: Retrieve the last ninja's dojo
SELECT dojos.* FROM ninjas
JOIN dojos ON ninjas.dojo_id = dojos.id
WHERE ninjas.id = 9;