/*
Formatting

Readable code is highly valued in the coding community and professional settings. Without proper formatting, code and results can be difficult to interpret. You'll often be working with other people that need to understand your code or be able to explain your results, so having a solid formatting habit is essential.

In this exercise, you'll correct poorly written code to better adhere to SQL style standards.
*/

--Instructions
--Adjust the sample code so that it is in line with standard practices.

-- Rewrite this query
select person_id, role from roles limit 10

--FIXED code 
SELECT 
    person_id,
    role
FROM roles 
LIMIT 10;