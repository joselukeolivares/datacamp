/*
Combining aggregate functions with WHERE

When combining aggregate functions with WHERE, you get a powerful tool that allows you to get more granular with your insights, for example, to get the total budget of movies made from the year 2010 onwards.

This combination is useful when you only want to summarize a subset of your data. In your film-industry role, as an example, you may like to summarize each certification category to compare how they each perform or if one certification has a higher average budget than another.

Let's see what insights you can gain about the financials in the dataset.
*/

/*
--Instructions
--1/4
-- Use SUM() to calculate the total gross for all films made in the year 2000 or later, and use the alias total_gross.
*/
-- Calculate the sum of gross from the year 2000 or later
SELECT
    SUM(gross) AS total_gross
FROM films
WHERE release_year >=2000

/*
2/4
---- Calculate the average gross of films that start with A
*/
-- Calculate the average gross of films that start with A

SELECT
    AVG(gross) AS avg_gross_A
FROM films
WHERE title LIKE 'A%'

/*
3/4
-- Calculate the lowest gross film in 1994 and use the alias lowest_gross
*/
-- Calculate the lowest gross film in 1994
SELECT
    MIN(gross) as lowest_gross
FROM films
WHERE release_year=1994

/*
4/4
*/
-- Calculate the highest gross film released between 2000-2012
SELECT 
    MAX(gross) AS highest_gross
FROM films
WHERE release_year BETWEEN 2000 AND 2010;