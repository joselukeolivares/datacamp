"""
Exercise
Using File to import HDF5 files

The h5py package has been imported in the environment and the file LIGO_data.hdf5 is loaded in the object h5py_file.

What is the correct way of using the h5py function, File(), to import the file in h5py_file into an object, h5py_data, for reading only?
Instructions

Possible answers
    h5py_data = File(h5py_file, 'r')
  * h5py_data = h5py.File(h5py_file, 'r')
    h5py_data = h5py.File(h5py_file, read)
    h5py_data = h5py.File(h5py_file, 'read')

"""

"""
Exercise
Using h5py to import HDF5 files

The file 'LIGO_data.hdf5' is already in your working directory. In this exercise, you'll import it using the h5py library. You'll also print out its datatype to confirm you have imported it correctly. You'll then study the structure of the file in order to see precisely what HDF groups it contains.

You can find the LIGO data plus loads of documentation and tutorials here. There is also a great tutorial on Signal Processing with the data here.
Instructions


    Import the package h5py.
    Assign the name of the file to the variable file.
    Load the file as read only into the variable data.
    Print the datatype of data.
    Print the names of the groups in the HDF5 file 'LIGO_data.hdf5'.

"""

# Import packages
import numpy as np
import h5py

# Assign filename: file
file='LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)


"""
Extracting data from your HDF5 file

In this exercise, you'll extract some of the LIGO experiment's actual data from the HDF5 file and you'll visualize it.

To do so, you'll need to first explore the HDF5 group 'strain'.
Instructions


    Assign the HDF5 group data['strain'] to group.
    In the for loop, print out the keys of the HDF5 group in group.
    Assign the time series data data['strain']['Strain'] to a NumPy array called strain.
    Set num_samples equal to 10000, the number of time points we wish to sample.
    Execute the rest of the code to produce a plot of the time series data in LIGO_data.hdf5.

"""    

# Get the HDF5 group: group
group=data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain=np.array(data['strain']['Strain'])

# Set number of time points to sample: num_samples
num_samples=10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
