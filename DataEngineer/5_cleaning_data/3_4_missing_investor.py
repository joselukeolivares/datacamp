"""
Missing investors

Dealing with missing data is one of the most common tasks in data science. There are a variety of types of missingness, as well as a variety of types of solutions to missing data.

You just received a new version of the banking DataFrame containing data on the amount held and invested for new and existing customers. However, there are rows with missing inv_amount values.

You know for a fact that most customers below 25 do not have investment accounts yet, and suspect it could be driving the missingness. The pandas, missingno and matplotlib.pyplot packages have been imported as pd, msno and plt respectively. The banking DataFrame is in your environment.

Instructions
1/4

    -Print the number of missing values by column in the banking DataFrame.
    -Plot and show the missingness matrix of banking with the msno.matrix() function.


"""

# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

"""
2/4
    -Isolate the values of banking missing values of inv_amount into missing_investors and with non-missing inv_amount values into investors.

"""

# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

"""
2/3
    Question:
    Now that you've isolated banking into investors and missing_investors, use the .describe() method on both of these DataFrames in the IPython shell to understand whether there are structural differences between them. What do you think is going on?
         Possible answers
         The data is missing completely at random and there are no drivers behind the missingness.
        *The inv_amount is missing only for young customers, since the average age in missing_investors is 22 and the maximum age is 25.
         The inv_amount is missing only for old customers, since the average age in missing_investors is 42 and the maximum age is 59.

print(investors.describe())
          age  acct_amount  inv_amount
count  84.000       84.000      84.000
mean   43.560    75095.273   44717.885
std    10.411    32414.506   26031.246
min    26.000    12209.840    3216.720
25%    34.000    57373.062   22736.037
50%    45.000    83061.845   44498.460
75%    53.000    94165.965   66176.803
max    59.000   250046.760   93552.690

print(missing_investors.describe())  
          age  acct_amount  inv_amount        
count  13.000       13.000         0.0
mean   21.846    73231.238         NaN
std     1.519    25553.327         NaN
min    20.000    21942.370         NaN
25%    21.000    66947.300         NaN
50%    21.000    86028.480         NaN
75%    23.000    89855.980         NaN
max    25.000    99998.350         NaN
"""

#4/4
# Sort the banking DataFrame by the age column and plot the missingness matrix of banking_sorted.

# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

# Sort banking by age and visualize
banking_sorted = banking.sort_values(by='age')
msno.matrix(banking_sorted)
plt.show()
