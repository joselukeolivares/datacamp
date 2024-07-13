/*
LIKE and NOT LIKE

The LIKE and NOT LIKE operators can be used to find records that either match or do not match a specified pattern, respectively. They can be coupled with the wildcards % and _. The % will match zero or many characters, and _ will match a single character.

This is useful when you want to filter text, but not to an exact word.

Do the following exercises to gain some practice with these keywords.
*/

/*
Instructions
*/

--1/3
--Select the names of all people whose names begin with 'B'.
-- Select the names that start with B
Select 
    name
From people
WHERE name LIKE 'B%'
;

--2/3
-- Select the names of people whose names have 'r' as the second letter.
SELECT name
FROM people
-- Select the names that have r as the second letter
WHERE name LIKE '_r%'

--3/3
--Select the names of people whose names don't start with 'A'.
SELECT name
FROM people
-- Select names that don't start with A
WHERE name NOT LIKE 'A%'