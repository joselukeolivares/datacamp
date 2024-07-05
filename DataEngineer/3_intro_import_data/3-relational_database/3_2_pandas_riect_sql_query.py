"""
Pandas and The Hello World of SQL Queries!

Here, you'll take advantage of the power of pandas to write the results of your SQL query to a DataFrame in one swift line of Python code!

You'll first import pandas and create the SQLite 'Chinook.sqlite' engine. Then you'll query the database to select all records from the Album table.

Recall that to select all records from the Orders table in the Northwind database, Hugo executed the following command:

df = pd.read_sql_query("SELECT * FROM Orders", engine)

Instructions
100 XP

    Import the pandas package using the alias pd.
    Using the function create_engine(), create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.
    Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from the following query: select all records from the table Album.
    The remainder of the code is included to confirm that the DataFrame created by this method is equal to that created by the previous method that you learned.

"""

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine=create_engine("sqlite:///Chinook.sqlite")

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Album", engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))

"""
Pandas for more complex querying

Here, you'll become more familiar with the pandas function read_sql_query() by using it to execute a more complex query: a SELECT statement followed by both a WHERE clause AND an ORDER BY clause.

You'll build a DataFrame that contains the rows of the Employee table for which the EmployeeId is greater than or equal to 6 and you'll order these entries by BirthDate.
Instructions
100 XP

    Using the function create_engine(), create an engine for the SQLite database Chinook.sqlite and assign it to the variable engine.
    Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from the following query: select all records from the Employee table where the EmployeeId is greater than or equal to 6 and ordered by BirthDate (make sure to use WHERE and ORDER BY in this precise order).
"""

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df=pd.read_sql_query("select * from Employee where EmployeeId>=6 order by (BirthDate)",engine)


# Print head of DataFrame
print(df.head())

"""
Exercise
The power of SQL lies in relationships between tables: INNER JOIN

Here, you'll perform your first INNER JOIN! You'll be working with your favourite SQLite database, Chinook.sqlite. For each record in the Album table, you'll extract the Title along with the Name of the Artist. The latter will come from the Artist table and so you will need to INNER JOIN these two tables on the ArtistID column of both.

Recall that to INNER JOIN the Orders and Customers tables from the Northwind database, Hugo executed the following SQL query:

"SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID"

The following code has already been executed to import the necessary packages and to create the engine:

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')

Instructions
100 XP

    Assign to rs the results from the following query: select all the records, extracting the Title of the record and Name of the artist of each record from the Album table and the Artist table, respectively. To do so, INNER JOIN these two tables on the ArtistID column of both.
    In a call to pd.DataFrame(), apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
    Set the DataFrame's column names to the corresponding names of the table columns.

"""

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs=con.execute("select al.Title,a.Name  from Album al inner join Artist a a.ArtistID=al.ArtistID")
    df=pd.DataFrame(rs.fetchall())
    df.columns=rs.keys()

# Print head of DataFrame df
print(df.head())


"""
Filtering your INNER JOIN

Congrats on performing your first INNER JOIN! You're now going to finish this chapter with one final exercise in which you perform an INNER JOIN and filter the result using a WHERE clause.

Recall that to INNER JOIN the Orders and Customers tables from the Northwind database, Hugo executed the following SQL query:

"SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID"

The following code has already been executed to import the necessary packages and to create the engine:

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')

Instructions
100 XP

    Use the pandas function read_sql_query() to assign to the variable df the DataFrame of results from the following query: select all records from PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId that satisfy the condition Milliseconds < 250000.

"""

# Execute query and store records in DataFrame: df
df=pd.read_sql_query("select * from  PlaylistTrack inner join Track on PlaylistTrack.TrackId=Track.TrackId where Milliseconds<250000",engine)

# Print head of DataFrame
print(df.head())