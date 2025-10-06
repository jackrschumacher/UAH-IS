## IS 310 Project 5
## Author: Jack Schumacher
## Contact: js0342@uah.edu

# Install the following packages using pip (I did this in a virtual environment to avoid modifying the overall system state)
import pandas as pd
import numpy as np
import matplotlib, os


def read_Files():
    # Define file path  - read the raw string to avoid newline interpretation
    file1_location = r'C:\Users\jackr\Documents\UAH\UAH-IS\IS 310\Week 5\Data\Auto_1.csv'
    file2_location = r'C:\Users\jackr\Documents\UAH\UAH-IS\IS 310\Week 5\Data\Auto_2.csv'
    # Check if the file paths exist, then read to pandas and return. If not print error message
    if os.path.exists(file1_location) and os.path.exists(file2_location):
        file1_df = pd.read_csv(file1_location)
        file2_df = pd.read_csv(file2_location)

        return file1_df, file2_df
    else:
        print("The files inputted do not exist")

def main():
    file1_df, file2_df = read_Files()
    print(file1_df.head())
    print(file2_df.head())

# Validate main function exists
if __name__ == "__main__":
    main()