/*
Sorting single fields
Now that you understand how ORDER BY works, you'll put it into practice. In this exercise, you'll work on sorting single fields only. This can be helpful to extract quick insights such as the top-grossing or top-scoring film.
The following exercises will help you gain further insights into the film database.
*/

/*
Instructions
--1/2
--Select the name of each person in the people table, sorted alphabetically.
*/
-- Select name from people and sort alphabetically
SELECT
    name
FROM people
ORDER BY name

/*
--2/2
--Select the title and duration for every film, from longest duration to shortest.
*/

-- Select the title and duration from longest to shortest film
SELECT
    title,
    duration
FROM films
ORDER BY duration DESC