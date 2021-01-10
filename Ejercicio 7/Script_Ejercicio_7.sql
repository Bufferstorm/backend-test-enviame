-- Crear tabla countries
CREATE TABLE countries ( id int(10) unsigned NOT NULL AUTO_INCREMENT, continent_id int(11) NOT NULL, name varchar(25) NOT NULL, PRIMARY KEY (id) );

-- Crear tabla continents
CREATE TABLE continents ( id int(10) unsigned NOT NULL AUTO_INCREMENT, name varchar(25) NOT NULL, anual_adjustment int(11) NOT NULL, PRIMARY KEY (id) );

-- Crear tabla employees
CREATE TABLE employees ( id int(10) unsigned NOT NULL AUTO_INCREMENT, country_id int(11) NOT NULL, first_name varchar(25) NOT NULL, last_name varchar(25) NOT NULL, salary int(11) NOT NULL, PRIMARY KEY (id) );

-- Agregar datos a continents
insert into continents values (null, 'Am�rica', 4); insert into continents values (null, 'Europa', 5); insert into continents values (null, 'Asia', 6); insert into continents values (null, 'Ocean�a', 6); insert into continents values (null, 'Africa', 5);

-- Agregar datos a countries
insert into countries values (null, 1, 'Chile'); insert into countries values (null, 1, 'Argentina'); insert into countries values (null, 1, 'Canad�'); insert into countries values (null, 1, 'Colombia'); insert into countries values (null, 2, 'Alemania'); insert into countries values (null, 2, 'Francia'); insert into countries values (null, 2, 'Espa�a'); insert into countries values (null, 2, 'Grecia'); insert into countries values (null, 3, 'India'); insert into countries values (null, 3, 'Jap�n'); insert into countries values (null, 3, 'Corea del Sur'); insert into countries values (null, 4, 'Australia');

-- Agregar datos a employees
insert into employees values (null, 1, 'Pedro', 'Rojas', 2000); insert into employees values (null, 2, 'Luciano', 'Alessandri', 2100); insert into employees values (null, 3, 'John', 'Carter', 3050); insert into employees values (null, 4, 'Alejandra', 'Benavides', 2150); insert into employees values (null, 5, 'Moritz', 'Baring', 6000); insert into employees values (null, 6, 'Thierry', 'Henry', 5900); insert into employees values (null, 7, 'Sergio', 'Ramos', 6200); insert into employees values (null, 8, 'Nikoleta', 'Kyriakopulu', 7000); insert into employees values (null, 9, 'Aamir', 'Khan', 2000); insert into employees values (null, 10, 'Takumi', 'Fujiwara', 5000); insert into employees values (null, 11, 'Heung-min', 'Son', 5100); insert into employees values (null, 12, 'Peter', 'Johnson', 6100);

-- Query Select with join
select * from employees as emplo
inner join countries as coun
on emplo.country_id = coun.id
inner join continents as cont
on cont.id = coun.continent_id

-- Script Update salary>=5000
UPDATE employees as emplo
INNER join countries as coun
ON emplo.country_id = coun.id
INNER join continents as cont
ON cont.id = coun.continent_id
SET emplo.salary = emplo.salary*(1+(cont.anual_adjustment/100))
WHERE emplo.salary >= 5000

