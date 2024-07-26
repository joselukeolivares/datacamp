/*
Joining with aliased tables

Recall from the video that instead of writing full table names in queries, you can use table aliasing as a shortcut. The alias can be used in other parts of your query, such as the SELECT statement!

You also learned that when you SELECT fields, a field can be ambiguous. For example, imagine two tables, apples and oranges, both containing a column called color. You need to use the syntax apples.color or oranges.color in your SELECT statement to point SQL to the correct table. Without this, you would get the following error:

  column reference "color" is ambiguous

In this exercise, you'll practice joining with aliased tables. You'll use data from both the countries and economies tables to examine the inflation rate in 2010 and 2015.

When writing joins, many SQL users prefer to write the SELECT statement after writing the join code, in case the SELECT statement requires using table aliases.

--Instructions

    --Start with your inner join in line 5; join the tables countries AS c (left) with economies (right), aliasing economies AS e.
    --Next, use code as your joining field in line 7; do not use the USING command here.
    --Lastly, select the following columns in order in line 2: code from the countries table (aliased as country_code), name, year, and inflation_rate.

*/
-- Select fields with aliases
Select
    c.code as country_code,
    name,
    year,
    inflation_rate
FROM countries AS c
-- Join to economies (alias e)
inner join economies as e
-- Match on code field using table aliases
on c.code =e.code
