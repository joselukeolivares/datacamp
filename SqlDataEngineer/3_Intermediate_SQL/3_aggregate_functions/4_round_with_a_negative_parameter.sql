/*
ROUND() with a negative parameter

A useful thing you can do with ROUND() is have a negative number as the decimal place parameter. This can come in handy if your manager only needs to know the average number of facebook_likes to the hundreds since granularity below one hundred likes won't impact decision making.

Social media plays a significant role in determining success. If a movie trailer is posted and barely gets any likes, the movie itself may not be successful. Remember how 2020's "Sonic the Hedgehog" movie got a revamp after the public saw the trailer?

Let's apply this to other parts of the dataset and see what the benchmark is for movie budgets so, in the future, it's clear whether the film is above or below budget.
*/

/*
Instructions
Calculate the average budget from the films table, aliased as avg_budget_thousands, and round to the nearest thousand.
*/

-- Calculate the average budget rounded to the thousands
SELECT
    ROUND(AVG(budget),-3) as avg_budget_thousands
FROM films
