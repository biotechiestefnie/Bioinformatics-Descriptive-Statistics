Descriptive Statistics and Lists in Bioinformatics

Descriptive Statistics and Lists is a project consisting of a collection of 3 data files and a python program that when run from the terminal, will calculate a series of descriptive statistics from a specified column within any one of the data files.

## Description

This project is designed to be run from the terminal. The module **stats_in_python.py** calculates a series of descriptive statistics for numeric data found in the specified column of any specified one of the tab-delimited input files, labeled **'data_file.txt'**, **'data_file2.txt'**, and **'data_file3.txt'**, which are included in the project directory. The module reads the data from the indicated column, processes it, and calculates the following statistical metrics while ignoring non-numeric values and not-a-number ('NaN') values: **total number of values in column, quantity of valid numbers in column, and average, maximum, minimum, variance, standard deviation, and median** of all valid numbers in the column. Once calculated, these statistics are printed to the screen for the user to view. The program takes **command-line arguments** for the **input file** and the **column number** to be analyzed. 

## Program Overview

The stats_in_python.py script performs the following tasks:  
1. **Reads the specified column** from the tab-delimited input file.
2. **Filters out non-numeric and NaN** values and creates a list of valid data
3. **Calculates descriptive statistics:** count, valid number count, average, maximum, variance, standard deviation, and median.
4. **Handles special cases:** appropriate messages are displayed if the column contains only non-numeric values, all values are NaN, or the column index is out of bounds.
5. **Displays results** to the screen so user can view the statistical calculations for the valid data from the column.

### Example Command

python3 stats_in_python.py data_file3.txt 3

### Example Output

    Column: 3

        Count     =   125.000 
        ValidNum  =   125.000
        Average   =    57.440 
        Maximum   =    97.000
        Minimum   =    16.000
        Variance  =   308.490
        Std Dev   =    17.564
        Median    =    58.000

## Getting Started

### Dependencies

* Python 3.11  


* Operating System: macOS  


* Python Modules:  

  * sys  
  
  * math  
  

* Data files:  

  * data_file.txt  
  
  * data_file2.txt  

  * data_file3.txt  


* The program must be run from the OS terminal.

### Installing

1. **Download the project files**


2. **Extract the zip file:**
   * On Windows: Right-click the zip file and select "Extract All..."
   * On macOS: Double-click the zip file to extract it.
   * On Linux: Use the command 'unzip assignment2.zip' in the terminal.


3. **Ensure that the data files** (data_file.txt, data_file2.txt, data_file3.txt) are present in the extracted project directory.


### Executing program

To run the program, follow these steps:

1. Open the OS terminal window.
2. Navigate to project directory
3. Run the following command:
```
python3 stats_in_python.py <input_file> <column_number>
```

For example:
```
python3 stats_in_python.py data_file3.txt 3
```


## Help

If you encounter any issues, please check to make sure that:

  * The input file is correctly specified.
  * The column number is within valid range (-100000 to 100000).
  * The data file contains numeric values in specified column.

To get a helper message:
```
python3 stats_in_python.py --help
```

## Authors

Stefanie Moreno
[moreno.st@northeastern.edu]
[https://github.com/biotechiestefnie]

## Version History

* 0.1
    * Initial Release
  

* Committed to the following repository under private status on GitHub: https://github.com/biotechiestefnie/Bioinformatics_6200_Assignment_1

## License

Access to this project is only available upon request from Stefanie Moreno and Northeastern University due to Northeastern University's copyright laws pertaining to works created for an assignment in one of the university's courses. For more information or for access, please contact Stefanie Moreno at moreno.st@northeastern.edu

## Acknowledgments

The program **stats_in_python.py** and the associated **README.md** was designed to fulfill the requirements of Assignment 2 in Bioinf6200 at Northeastern University for Spring 2025, as assigned by Dr. Chelsey Leslin. All data files were provided by Dr. Leslin.
