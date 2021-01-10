-- Script Update salary>=5000
UPDATE employees as emplo
INNER join countries as coun
ON emplo.country_id = coun.id
INNER join continents as cont
ON cont.id = coun.continent_id
SET emplo.salary = emplo.salary*(1+(cont.anual_adjustment/100))
WHERE emplo.salary >= 5000

