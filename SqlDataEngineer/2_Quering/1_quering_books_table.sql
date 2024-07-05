/*
Making queries DISTINCT

You've learned that the DISTINCT keyword can be used to return unique values in a field. In this exercise, you'll use this understanding to find out more about the books table!

There are 350 books in the books table, representing all of the books that our local library has available for checkout. But how many different authors are represented in these 350 books? The answer is surely less than 350. For example, J.K. Rowling wrote all seven Harry Potter books, so if our library has all Harry Potter books, seven books will be written by J.K Rowling. There are likely many more repeat authors!

Instructions 
    Write SQL code that returns a result set with just one column listing the unique authors in the books table.
    Update the code to return the unique author and genre combinations in the books table.

*/

-- Select unique authors from the books table
SELECT DISTINCT author from books;

-- Select unique authors and genre combinations from the books table
SELECT DISTINCT author,genre
FROM books;

/*
You've passed this exercise with DISTINCTion! Notice that you found 247 unique authors in the books table overall but 249 unique combinations of authors and genres. This means there are one or two authors who have written books in multiple genres!
*/

/*
Aliasing

While the default column names in a SQL result set come from the fields they are created from, you've learned that aliasing can be used to rename these result set columns. This can be helpful for clarifying the intent or contents of the column.

Your task in this exercise is to incorporate an alias into one of the SQL queries that you worked with in the previous exercise!

Instructions
    Add an alias to the SQL query to rename the author column to unique_author in the result set.

*/

-- Alias author so that it becomes unique_author
SELECT DISTINCT author as unique_author
FROM books;

/*
It's AS easy AS that! Great work. The alias you just implemented makes it clear that only unique authors are listed in the results and that there are no duplicates. This is clear even to someone who is reading only the result set and does not know the SQL code behind the results.
*/

/*
VIEWing your query

You've worked hard to create the below SQL query:

SELECT DISTINCT author AS unique_author
FROM books;

What if you'd like to be able to refer to it later, or allow others to access and use the results? The best way to do this is by creating a view. Recall that a view is a virtual table: it's very similar to a real table, but rather than the data itself being stored, the query code is stored for later use.

Instructions
    Check that the view was created by selecting all columns from library_authors.
    Check that the view was created by selecting all columns from library_authors

*/

-- Your code to create the view:
CREATE VIEW library_authors AS
SELECT DISTINCT author AS unique_author
FROM books;

-- Select all columns from library_authors
SELECT * FROM library_authors;

/*

Amazing! As your SQL queries become long and complex, you'll want to be able to save your queries for referencing later. Views can also be useful when the information contained in a database table isn't quite what you need. You can create your own custom view with exactly the information you are looking for, without needing to edit the database itself, which you may not have permission to do. Creating views is a valuable skill to have, and you've mastered it!

*/

