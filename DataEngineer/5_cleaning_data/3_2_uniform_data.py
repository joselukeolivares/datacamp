"""
Uniform dates

After having unified the currencies of your different account amounts, you want to add a temporal dimension to your analysis and see how customers have been investing their money given the size of their account over each year. The account_opened column represents when customers opened their accounts and is a good proxy for segmenting customer activity and investment over time.

However, since this data was consolidated from multiple sources, you need to make sure that all dates are of the same format. You will do so by converting this column into a datetime object, while making sure that the format is inferred and potentially incorrect formats are set to missing. The banking DataFrame is in your environment and pandas was imported as pd.
"""

#Instructions
#1/4
#Print the header of account_opened from the banking DataFrame and take a look at the different results.
# Print the header of account_opened
print(
    banking['account_opened'].head()
)

"""
0          2018-03-05
1            21-01-18
2    January 26, 2018
3            21-14-17
4            05-06-17
Name: account_opened, dtype: object
"""

"""
2/4
Question
Take a look at the output. You tried converting the values to datetime using the default to_datetime() function without changing any argument, however received the following error:

    -The to_datetime() function needs to be explicitly told which date format each row is in.
    -The to_datetime() function can only be applied on YY-mm-dd date formats.
   *-The 21-14-17 entry is erroneous and leads to an error
"""

#3/4
#Convert the account_opened column to datetime, while making sure the date format is inferred and that erroneous formats that raise error return a missing value.

# Print the header of account_opened

print(banking['account_opened'].head())

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format = True,
                                           # Return missing value for error
                                           errors = 'coerce') 



