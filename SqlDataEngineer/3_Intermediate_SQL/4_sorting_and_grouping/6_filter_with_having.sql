/*
Filter with HAVING

Your final keyword is HAVING. It works similarly to WHERE in that it is a filtering clause, with the difference that HAVING filters grouped data.

Filtering grouped data can be especially handy when working with a large dataset. When working with thousands or even millions of rows, HAVING will allow you to filter for just the group of data you want, such as films over two hours in length!

Practice using HAVING to find out which countries (or country) have the most varied film certifications.

Instructions:
    -Select country from the films table, and get the distinct count of certification aliased as certification_count.
    -Group the results by country.
    -Filter the unique count of certifications to only results greater than 10.

*/

-- Select the country and distinct count of certification as certification_count
SELECT 
    country,
    COUNT(DISTINCT(certification)) AS certification_count   
FROM films
-- Group by country
GROUP BY country
-- Filter results to countries with more than 10 different certifications
HAVING COUNT(DISTINCT(certification))>10
