/*
Using WHERE with numbers

Filtering with WHERE allows you to analyze your data better. You may have a dataset that includes a range of different movies, and you need to do a case study on the most notable films with the biggest budgets. In this case, you'll want to filter your data to a specific budget range.

Now it's your turn to use the WHERE clause to filter numeric values!
*/

--Instructions

--1/3
--Select the film_id and imdb_score from the reviews table and filter on scores higher than 7.0.

-- Select film_ids and imdb_score with an imdb_score over 7.0
SELECT 
    film_id,
    imdb_score
FROM reviews
WHERE imdb_score>7.0;

--2/3
-- Select the film_id and facebook_likes of the first ten records with less than 1000 likes from the reviews table.

-- Select film_ids and facebook_likes for ten records with less than 1000 likes 
SELECT 
    film_id,
    facebook_likes
FROM reviews
WHERE facebook_likes < 1000
LIMIT 10;

--3/3
-- Count how many records have a num_votes of at least 100,000; use the alias films_over_100K_votes.

-- Count the records with at least 100,000 votes
SELECT
    count(*) as films_over_100K_votes
FROM reviews
WHERE num_votes >= 100000

/*
Using WHERE with text

WHERE can also filter string values.

Imagine you are part of an organization that gives 
cinematography awards, and you have several international 
categories. Before you confirm an award for every language 
listed in your dataset, it may be worth seeing if there are
 enough films of a specific language to make it a fair 
 competition. If there is only one movie or a significant
  skew, it may be worth considering a different way of giving
   international awards.

Let's try this out!
*/

/*
Instructions

    -Select and count the language field using the alias count_spanish.
    -Apply a filter to select only Spanish from the language field.
*/
-- Count the Spanish-language films
SELECT
    COUNT(language) AS count_spanish
FROM films
WHERE language='Spanish';