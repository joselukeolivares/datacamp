/*
HAVING and sorting

Filtering and sorting go hand in hand and gives you greater interpretability by ordering our results.

Let's see this magic at work by writing a query showing what countries have the highest average film budgets.

Instructions:
    
    -Select the country and the average budget as average_budget, rounded to two decimal, from films.
    -Group the results by country.
    -Filter the results to countries with an average budget of more than one billion (1000000000).
    -Sort by descending order of the average_budget.

*/

-- Select the country and average_budget from films
SELECT
    country,
    AVG(budget) AS average_budget
FROM films
-- Group by country
GROUP BY country
-- Filter to countries with an average_budget of more than one billion
HAVING AVG(budget)>1000000000
-- Order by descending order of the aggregated budget
ORDER BY average_budget
