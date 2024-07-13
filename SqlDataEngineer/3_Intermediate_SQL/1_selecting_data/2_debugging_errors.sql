/*
Debugging errors

Debugging is an essential skill for all coders, and it comes from making many mistakes and learning from them.

In this exercise, you'll be given some buggy code that you'll need to fix.
*/
--Instructions
-- 1/3
-- Debug and fix the SQL query provided.
-- Debug this code
SELECT certfication
FROM films
LIMIT 5;

-- Fixed code
SELECT certification
FROM films
LIMIT 5;

-- 2/3
-- Find the two errors in this code; the same error has been repeated twice
-- Debug this code
SELECT film_id imdb_score num_votes
FROM reviews;

-- Fixed code
SELECT film_id, imdb_score, num_votes
FROM reviews;

-- 3/3
-- Find the two bugs in this final query.
-- Debug this code
SELECT COUNNT(birthdate) AS count_birthdays
FROM peeple;

--fixed code
SELECT COUNT(birthdate) AS count_birthdays
FROM people;

