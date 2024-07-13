"""
Finding consistency

In this exercise and throughout this chapter, you'll be working with the airlines DataFrame which contains survey responses on the San Francisco Airport from airline customers.

The DataFrame contains flight metadata such as the airline, the destination, waiting times as well as answers to key questions regarding cleanliness, safety, and satisfaction. Another DataFrame named categories was created, containing all correct possible values for the survey columns.

In this exercise, you will use both of these DataFrames to find survey answers with inconsistent values, and drop them, effectively performing an outer and inner join on both these DataFrames as seen in the video exercise. The pandas package has been imported as pd, and the airlines and categories DataFrames are in your environment.


Instructions
1/4
    -Print the categories DataFrame and take a close look at all possible correct categories of the survey columns.
    -Print the unique values of the survey columns in airlines using the .unique() method.

"""

# Print categories DataFrame
print(categories)

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
print('Safety: ', airlines['safety'].unique(), "\n")
print('Satisfaction: ',airlines['satisfaction'].unique(), "\n")

"""
2/4
Question

-Take a look at the output. Out of the cleanliness, safety and satisfaction columns, which one has an inconsistent category and what is it?
Possible answers:
   *cleanliness because it has an Unacceptable category.
    cleanliness because it has a Terribly dirty category.
    satisfaction because it has a Very satisfied category.
    safety because it has a Neutral category.
"""

"""
3/4
    -Create a set out of the cleanliness column in airlines using set() and find the inconsistent category by finding the difference in the cleanliness column of categories.
    -Find rows of airlines with a cleanliness value not in categories and print the output.

"""

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

"""
4/4
    -Print the rows with the consistent categories of cleanliness only.

"""

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Print rows with consistent categories only
print(airlines[~cat_clean_rows])

"""
Exercise
1/3
Inconsistent categories

In this exercise, you'll be revisiting the airlines DataFrame from the previous lesson.

As a reminder, the DataFrame contains flight metadata such as the airline, the destination, waiting times as well as answers to key questions regarding cleanliness, safety, and satisfaction on the San Francisco Airport.

In this exercise, you will examine two categorical columns from this DataFrame, dest_region and dest_size respectively, assess how to address them and make sure that they are cleaned and ready for analysis. The pandas package has been imported as pd, and the airlines DataFrame is in your environment.

    Exercise
    -Print the unique values in dest_region and dest_size respectively.
"""

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

"""
2/3
Question

From looking at the output, what do you think is the problem with these columns?
Possible answers
     The dest_region column has only inconsistent values due to capitalization.
     The dest_region column has inconsistent values due to capitalization and has one value that needs to be remapped.
     The dest_size column has only inconsistent values due to leading and trailing spaces.
    *Both 2 and 3 are correct.

"""

"""
Inconsistent categories

In this exercise, you'll be revisiting the airlines DataFrame from the previous lesson.

As a reminder, the DataFrame contains flight metadata such as the airline, the destination, waiting times as well as answers to key questions regarding cleanliness, safety, and satisfaction on the San Francisco Airport.

In this exercise, you will examine two categorical columns from this DataFrame, dest_region and dest_size respectively, assess how to address them and make sure that they are cleaned and ready for analysis. The pandas package has been imported as pd, and the airlines DataFrame is in your environment.

3/4


    -Change the capitalization of all values of dest_region to lowercase.
    -Replace the 'eur' with 'europe' in dest_region using the .replace() method.

"""

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

"""
4/4

    -Strip white spaces from the dest_size column using the .strip() method.
    -Verify that the changes have been into effect by printing the unique values of the columns using .unique() .
"""

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower() 
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip()

# Verify changes have been effected
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())


