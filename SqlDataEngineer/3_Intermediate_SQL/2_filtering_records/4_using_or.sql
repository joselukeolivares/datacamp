/*
Using OR

This time you'll write a query to get the title and release_year of films released in 1990 or 1999, which were in English or Spanish and took in more than $2,000,000 gross.

It looks like a lot, but you can build the query up one step at a time to get comfortable with the underlying concept in each step. Let's go!
*/


-- Instructions
-- 1/3
-- Find the title and year of films from the 1990 or 1999
SELECT
    title,
    release_year
FROM films
WHERE (release_year=1990 OR release_year=1999)

-- 2/3
-- Filter the records to only include English or Spanish-language films.
SELECT title, release_year
FROM films
WHERE (release_year = 1990 OR release_year = 1999)
-- Add a filter to see only English or Spanish-language films
AND (language='English' or language='Spanish');

--3/3
-- Finally, restrict the query to only return films worth more than $2,000,000 gross
SELECT title, release_year
FROM films
WHERE (release_year = 1990 OR release_year = 1999)
	AND (language = 'English' OR language = 'Spanish')
-- Filter films with more than $2,000,000 gross
AND gross>2000000;




