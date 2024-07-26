/*
Answering business questions

In the real world, every SQL query starts with a business question. Then it is up to you to decide how to write the query that answers the question. Let's try this out.

Which release_year had the most language diversity?

Take your time to translate this question into code. We'll get you started then it's up to you to test your queries in the console.

"Most language diversity" can be interpreted as COUNT(DISTINCT ___). Now over to you.

Possible answers:
    -2005
    -1916
   *-2006
    -1990
*/
SELECT release_year,
        COUNT(DISTINCT language) as lenguajes
FROM films
GROUP BY release_year
ORDER BY lenguajes DESC
