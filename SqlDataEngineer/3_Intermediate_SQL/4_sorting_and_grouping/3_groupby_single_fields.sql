/*
GROUP BY single fields

GROUP BY is a SQL keyword that allows you to group and summarize results with the additional use of aggregate functions. For example, films can be grouped by the certification and language before counting the film titles in each group. This allows you to see how many films had a particular certification and language grouping.

In the following steps, you'll summarize other groups of films to learn more about the films in your database.

Instructions
--1/2
---- Find the release_year and film_count of each year
*/
-- Find the release_year and film_count of each year
SELECT
    release_year,
    COUNT(*) as film_count
FROM films
GROUP BY release_year

/*
--2/2
-- Select the release_year and average duration aliased as avg_duration of all films, grouped by release_year.
*/
-- Find the release_year and average duration of films for each year
SELECT
    release_year,
    AVG(duration) as avg_duration
FROM films
GROUP BY (release_year)
