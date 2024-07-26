/*
Inspecting a relationship

You've just identified that the countries table has a many-to-many relationship with the languages table. That is, many languages can be spoken in a country, and a language can be spoken in many countries.

This exercise looks at each of these in turn. First, what is the best way to query all the different languages spoken in a country? And second, how is this different from the best way to query all the countries that speak each language?

Recall that when writing joins, many users prefer to write SQL code out of order by writing the join first (along with any table aliases), and writing the SELECT statement at the end.

Instructions
--1/3
    
    --Start with the join statement in line 6; perform an inner join with the countries table as c on the left with the languages table as l on the right.
    --Make use of the USING keyword to join on code in line 8.
    --Lastly, in line 2, select the country name, aliased as country, and the language name, aliased as language.

*/

-- Select country and language names, aliased
Select
    c.name as country,
    l.name as language
-- From countries (aliased)
FROM countries AS c
-- Join to languages (aliased)
INNER JOIN languages as l
-- Use code as the joining field with the USING keyword
USING(code);

/*
--2/3
    --Rearrange the SELECT statement so that the language column appears on the left and the country column on the right.
    --Sort the results by language.
*/
-- Rearrange SELECT statement, keeping aliases
SELECT  
    l.name AS language,
    c.name AS country
FROM countries AS c
INNER JOIN languages AS l
USING(code)
-- Order the results by language
order by language