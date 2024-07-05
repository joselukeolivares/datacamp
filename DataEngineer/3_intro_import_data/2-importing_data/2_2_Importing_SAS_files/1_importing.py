"""
Importing SAS files

In this exercise, you'll figure out how to import a SAS file as a DataFrame using SAS7BDAT and pandas. The file 'sales.sas7bdat' is already in your working directory and both pandas and matplotlib.pyplot have already been imported as follows:

import pandas as pd
import matplotlib.pyplot as plt

The data are adapted from the website of the undergraduate text book Principles of Econometrics by Hill, Griffiths and Lim.
Instructions

    Import the module SAS7BDAT from the library sas7bdat.
    In the context of the file 'sales.sas7bdat', load its contents to a DataFrame df_sas, using the method to_data_frame() on the object file.
    Print the head of the DataFrame df_sas.
    Execute your entire script to produce a histogram plot!

"""

# Import sas7bdat package
# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas=file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())


# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

"""
Using read_stata to import Stata files

The pandas package has been imported in the environment as pd and the file disarea.dta is in your working directory. The data consist of disease extents for several diseases in various countries (more information can be found here).

What is the correct way of using the read_stata() function to import disarea.dta into the object df?
Instructions
50 XP
Possible answers

df = 'disarea.dta'
df = read_stata.pd('disarea.dta')
df = pd.read_stata('disarea.dta')
df = pd.read_stata(disarea.dta)

"""
df=pd.read_stata("disarea.dta")

print(df.head())