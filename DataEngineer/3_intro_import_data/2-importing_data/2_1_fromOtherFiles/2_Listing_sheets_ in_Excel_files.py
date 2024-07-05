"""
Listing sheets in Excel files

Whether you like it or not, any working data scientist will need to deal with Excel spreadsheets at some point in time. You won't always want to do so in Excel, however!

Here, you'll learn how to use pandas to import Excel spreadsheets and how to list the names of the sheets in any loaded .xlsx file.

Recall from the video that, given an Excel file imported into a variable spreadsheet, you can retrieve a list of the sheet names using the attribute spreadsheet.sheet_names.

Specifically, you'll be loading and checking out the spreadsheet 'battledeath.xlsx', modified from the Peace Research Institute Oslo's (PRIO) dataset. This data contains age-adjusted mortality rates due to war in various countries over several years.

"""

"""
    Instructions
    Assign the spreadsheet filename (provided above) to the variable file.
    Pass the correct argument to pd.ExcelFile() to load the file using pandas, assigning the result to the variable xls.
    Print the sheetnames of the Excel spreadsheet by passing the necessary argument to the print() function.

"""

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)

"""

Importing sheets from Excel files

In the previous exercises, you saw that the Excel file contains two sheets, '2002' and '2004'. The next step is to import these.

In this exercise, you'll learn how to import any given sheet of your loaded .xlsx file as a DataFrame. You'll be able to do so by specifying either the sheet's name or its index.

The spreadsheet 'battledeath.xlsx' is already loaded as xls.

Instructions
100 XP

    Load the sheet '2004' into the DataFrame df1 using its name as a string.
    Print the head of df1 to the shell.
    Load the sheet 2002 into the DataFrame df2 using its index (0).
    Print the head of df2 to the shell

"""

# Load a sheet into a DataFrame by name: df1
df1 = xls.parse("2004")

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2=xls.parse(0)


# Print the head of the DataFrame df2
print(df2.head())


"""
Customizing your spreadsheet import

Here, you'll parse your spreadsheets and use additional arguments to skip rows, 
rename columns and select only particular columns.

The spreadsheet 'battledeath.xlsx' is already loaded as xls.

As before, you'll use the method parse(). This time, however, you'll add the 
additional arguments skiprows, names and usecols. These skip rows, name the 
columns and designate which columns to parse, respectively. All these arguments
can be assigned to lists containing the specific row numbers, strings and column numbers, as appropriate.

Instructions

    Parse the first sheet by index. In doing so, skip the first row of data and name the columns 'Country' and 'AAM due to War (2002)' using the argument names. The values passed to skiprows and names all need to be of type list.
    Parse the second sheet by index. In doing so, parse only the first column with the usecols parameter, skip the first row and rename the column 'Country'. The argument passed to usecols also needs to be of type list.

"""

# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())




