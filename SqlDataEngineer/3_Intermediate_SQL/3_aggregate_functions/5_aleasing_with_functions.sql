/*
Aliasing with functions

Aliasing can be a lifesaver, especially as we start to do more complex SQL queries with multiple criteria. Aliases help you keep your code clean and readable. For example, if you want to find the MAX() value of several fields without aliasing, you'll end up with the result with several columns called max and no idea which is which. You can fix this with aliasing.

Now, it's over to you to clean up the following queries.
*/

/*
Instructions
-- 1/3
-- Select the title and duration in hours for all films and alias as duration_hours; since the current durations are in minutes, you'll need to divide duration by 60.0
*/
-- Calculate the title and duration_hours from films
SELECT title, (duration/60.0) as duration_hours
FROM films;

/*
--2/3
--Calculate the percentage of people who are no longer alive and alias the result as percentage_dead
*/
-- Calculate the percentage of people who are no longer alive
SELECT COUNT(deathdate) * 100.0 / COUNT(*) AS percentage_dead
FROM people;