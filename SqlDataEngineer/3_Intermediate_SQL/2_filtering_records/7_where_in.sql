/*
WHERE IN

You now know you can query multiple conditions using the IN operator and a set of parentheses. It is a valuable piece of code that helps us keep our queries clean and concise.

Try using the IN operator yourself!
*/

--Instructions
--1/3
--Select the title and release_year of all films released in 1990 or 2000 that were longer than two hours.
SELECT 
    title,
    release_year
FROM films
WHERE 
release_year IN (1990,2000)
AND duration >120

--2/3
--Select the title and language of all films in English, Spanish, or French using IN
-- Find the title and language of all films in English, Spanish, and French
SELECT
    title,
    language
FROM films
WHERE language IN ('English','Spanish')

--3/3
--Select the title, certification and language of all films certified NC-17 or R that are in English, Italian, or Greek.
-- Find the title, certification, and language all films certified NC-17 or R that are in English, Italian, or Greek
SELECT 
    title,
    certification,
    language
FROM films
WHERE (certification='NC-17' or certification='R')
AND language IN ('English','Italian','Greek')
