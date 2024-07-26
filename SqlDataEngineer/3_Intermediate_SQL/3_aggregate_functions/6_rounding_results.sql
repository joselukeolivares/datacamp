/*
Rounding results

You found some valuable insights in the previous exercise, but many of the results were inconveniently long. We forgot to round! We won't make you redo them all; however, you'll update the worst offender in this exercise.

Instructions
-- Update the query by adding ROUND() around the calculation and round to two decimal places
*/

-- Round duration_hours to two decimal places
SELECT title, ROUND(duration / 60.0,2) AS duration_hours
FROM films;