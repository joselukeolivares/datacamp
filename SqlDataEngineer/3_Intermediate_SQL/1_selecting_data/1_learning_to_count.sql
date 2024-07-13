/*
Learning to COUNT()

You saw how to use COUNT() in the video. Do you remember what it returns?

Here is a query counting film_id. Select the answer below that correctly describes what the query will return.

SELECT COUNT(film_id) AS count_film_id
FROM reviews;

Run the query in the console to test your theory!

Possible answers:
    The number of unique films in the reviews table.
   *The number of records containing a film_id.
    The total number of records in the reviews table.
    The sum of the film_id field.

*/


/*
Practice with COUNT()

As you've seen, COUNT(*) tells you how many records are in a table. However, if you want to count the number of non-missing values in a particular field, you can call COUNT() on just that field.

Let's get some practice with COUNT()! You can look at the data in the tables throughout these exercises by clicking on the table name in the console.

Instructions 
1/3
    -Count the total number of records in the people table, aliasing the result as count_records.
*/

-- Count the number of records in the people table
SELECT count(*) as count_records FROM people;

-- 2/3 
-- Count the number of birthdates in the people table
SELECT COUNT(birthdate) as count_birthdate from people;

--3/3 
-- Count the records for languages and countries represented in the films table
SELECT COUNT(language ) as count_languages,COUNT(country) as count_countries  FROM films;

/*
SELECT DISTINCT

Often query results will include many duplicate values. You can use the DISTINCT keyword to select the unique values from a field.

This might be useful if, for example, you're interested in knowing which languages are represented in the films table. See if you can find out what countries are represented in this table with the following exercises.
*/

--Instructions
--1/2
-- Return the unique countries from the films table
SELECT DISTINCT(country) from films;

-- 2/2
-- Return the number of unique countries represented in the films table, aliased as count_distinct_countries.
-- Count the distinct countries from the films table
SELECT COUNT(DISTINCT country) as count_distinct_countries from films;