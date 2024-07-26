/*
Combining filtering and selecting

Time for a little challenge. So far, your SQL vocabulary from this course includes COUNT(), DISTINCT, LIMIT, WHERE, OR, AND, BETWEEN, LIKE, NOT LIKE, and IN. In this exercise, you will try to use some of these together. Writing more complex queries will be standard for you as you become a qualified SQL programmer.

As this query will be a little more complicated than what you've seen so far, we've included a bit of code to get you started. You will be using DISTINCT here too because, surprise, there are two movies named 'Hamlet' in this dataset!

Follow the instructions to find out what 90's films we have in our dataset that would be suitable for English-speaking teens.
*/

/*
Instructions

    -Count the unique titles from the films database and use the alias provided.
    -Filter to include only movies with a release_year from 1990 to 1999, inclusive.
    -Add another filter narrowing your query down to English-language films.
    -Add a final filter to select only films with 'G', 'PG', 'PG-13' certifications.
*/
-- Count the unique titles
SELECT COUNT(DISTINCT(title)) AS nineties_english_films_for_teens
FROM films
-- Filter to release_years to between 1990 and 1999
WHERE (release_year BETWEEN 1990 AND 1999)
-- Filter to English-language films
AND language='English'
-- Narrow it down to G, PG, and PG-13 certifications
AND certification in ('G','PG','PG-13');
