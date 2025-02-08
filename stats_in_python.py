"""
stats_in_python.py
Author: Stefanie Moreno
Project: Descriptive Statistics and Lists
Date: 2025-02-09
Description: This script calculates descriptive statistics for a specified column in a tab-delimited input file.
"""

# Import the essential modules
import sys # for command line arguments
import math # for mathematical functions and constants

# Function to calculate statistics
def calculate_statistics(numbers):
    """
    Computes count, valid count, average, max, min, variance, std dev, and median of a list, excluding 'Nan' values.
    """
    # Count total entries in list and assign to variable
    count = len(numbers)
    # Filter out 'NaN' values and keep only valid numbers assigned to variable
    valid_numbers = [num for num in numbers if not math.isnan(num)]
    # Count number of valid entries and assign to variable
    valid_count = len(valid_numbers)

    # Create error message for if there are no valid numbers
    if valid_count == 0:
        return "Error: There were no valid numbers in column in file"

    # For valid numbers and assign to variable:
    # Calculate average
    average = sum(valid_numbers) / valid_count
    # Find maximum
    maximum = max(valid_numbers)
    # Find minimum
    minimum = min(valid_numbers)
    # Calculate variance
    variance = sum((x - average) ** 2 for x in valid_numbers) / valid_count
    # Calculate standard deviation
    std_dev = math.sqrt(variance)
    # Sort then calculate median
    sorted_numbers = sorted(valid_numbers)
    median = (sorted_numbers[valid_count // 2] if valid_count % 2 == 1 else
              (sorted_numbers[valid_count // 2 - 1 ] + sorted_numbers[valid_count // 2]))

    # Return all calculated statistics as tuple
    return count, valid_count, average, maximum, minimum, variance, std_dev, median


def read_numbers_from_file(file_name, column_to_parse):
    """
    Reads numbers from specified column in file, ignoring 'NaNs'. Returns list of valid numbers.
    """
    # Initialize empty list to store numbers
    numbers = []
    # Open and process the file, specify encoding
    with open(file_name, 'r', encoding='utf-8') as infile:
        for line in infile:
            try:
                # Split each line by tab character and extract value from specified column
                value = line.split('\t')[column_to_parse]
                # Convert extracted value to float
                num = float(value)
                # Append number to list if not 'Nan'
                if not math.isnan(num):
                    numbers.append(num)
            except ValueError:
                # Skip line if value cannot be converted to float and print notification to screen
                print(f"Skipping line: could not convert {value} to float")
            except IndexError:
                # Exit if there is no valid 'list index' in specified column and print notification to screen
                print(f"Exiting: There is no valid 'list index' in column {column_to_parse} in line {line}")
                sys.exit(1)
    return numbers


# Function to print statistics
def print_statistics(column_to_parse, stats):
    """
    Prints calculated statistics for specified column. Delivers error messages if stats is a string.
    """
    # Print the results
    if isinstance(stats, str):
        print(stats)
    else:
        # Unpack returned statistics tuple
        count, valid_count, average, maximum, minimum, variance, std_dev, median = stats
        # Print column number
        print(f"    Column: {column_to_parse}\n\n")
        # Print count of total entries
        print(f"        Count     =   {count:8.3f}")
        # For valid entries, print to screen
        # The count
        print(f"        ValidNum  =   {valid_count:8.3f}")
        # The average
        print(f"        Average   =   {average:8.3f}")
        # The maximum
        print(f"        Maximum   =   {maximum:8.3f}")
        # The minimum
        print(f"        Minimum   =   {minimum:8.3f}")
        # The variance
        print(f"        Variance  =   {variance:8.3f}")
        # The standard deviation
        print(f"        Std Dev   =   {std_dev:8.3f}")
        # And finally, the median
        print(f"        Median    =   {median:8.3f}")


# Main function to encapsulate main script logic
def main():
    """
    Processes input file and column, calculates statistics, prints results. Usage: python3 script.py <file> <column>.
    """
    # Check for the correct number of command line arguments
    if len(sys.argv) < 3:
        # Print usage message and exit if arguments are missing
        print("Usage: python3 stats_in_python.py <input_file> <column_number>")
        sys.exit(1)

    # Get the file name and column to parse from command line arguments
    file_name = sys.argv[1]
    column_to_parse = int(sys.argv[2])

    # Read numbers from specified file and column
    numbers = read_numbers_from_file(file_name, column_to_parse)
    # Calculate statistics for numbers
    stats = calculate_statistics(numbers)
    # Print calculated statistics
    print_statistics(column_to_parse, stats)

# Execution point for script
if __name__ == "__main__":
    main()
