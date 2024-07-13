"""
Uniform currencies

In this exercise and throughout this chapter, you will be working with a retail banking dataset stored in the banking DataFrame. The dataset contains data on the amount of money stored in accounts (acct_amount), their currency (acct_cur), amount invested (inv_amount), account opening date (account_opened), and last transaction date (last_transaction) that were consolidated from American and European branches.

You are tasked with understanding the average account size and how investments vary by the size of account, however in order to produce this analysis accurately, you first need to unify the currency amount into dollars. The pandas package has been imported as pd, and the banking DataFrame is in your environment.

Instructions:
    -Find the rows of acct_cur in banking that are equal to 'euro' and store them in the variable acct_eu.
    -Find all the rows of acct_amount in banking that fit the acct_eu condition, and convert them to USD by multiplying them with 1.1.
    -Find all the rows of acct_cur in banking that fit the acct_eu condition, set them to 'dollar'.

"""


#3/4
# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'
#print(banking.loc[3])

# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1

# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'
#print(banking.loc[3])

# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar'

#4/4
"""
    -Extract the year from the amended account_opened column and assign it to the acct_year column.
    -Print the newly created acct_year column.
"""

# Print the header of account_opend
print(banking['account_opened'].head())

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format = True,
                                           # Return missing value for error
                                           errors = 'coerce') 

# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')

# Print acct_year
print(banking['acct_year'])

"""
The .sum() function in pandas has several parameters that you can use to customize its behavior. Here are the key parameters:

    axis:
        0 or 'index': Sum along the index (rows).
        1 or 'columns': Sum along the columns.

    skipna:
        True (default): Exclude NA/null values when computing the sum.
        False: Include NA/null values, which will result in NA/null in the output if any NA/null values are present.

    level:
        If the axis is a MultiIndex (hierarchical), sum along a particular level, collapsing into a DataFrame.

    numeric_only:
        None (default): Include all columns.
        True: Include only float, int, boolean columns. If None, will attempt to use everything, then use only numeric data.

    min_count:
        Minimum number of valid values to perform the operation. If fewer than min_count non-NA values are present, the result will be NA.

"""
