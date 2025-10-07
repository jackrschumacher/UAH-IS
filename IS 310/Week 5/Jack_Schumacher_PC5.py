## IS 310 Project 5
## Author: Jack Schumacher
## Contact: js0342@uah.edu

# Install the following packages using pip (I did this in a virtual environment to avoid modifying the overall system state)
import pandas as pd
import numpy as np
import matplotlib, os


def read_Files():
    # Define file path  - read the raw string to avoid newline interpretation
    file1_location = (
        r"C:\Users\jackr\Documents\UAH\UAH-IS\IS 310\Week 5\Data\Auto_1.csv"
    )
    file2_location = (
        r"C:\Users\jackr\Documents\UAH\UAH-IS\IS 310\Week 5\Data\Auto_2.csv"
    )
    # Check if the file paths exist, then read to pandas and return. If not print error message
    if os.path.exists(file1_location) and os.path.exists(file2_location):
        file1_df = pd.read_csv(file1_location)
        file2_df = pd.read_csv(file2_location)

        return file1_df, file2_df
    else:
        print("The files inputted do not exist")


#
def display_df(file1_df, file2_df):
    print("Data Summary:")
    print("File 1:")
    print(file1_df.head(5))
    print(file1_df.info())
    print(file1_df.describe())
    print("File 2:")
    print(file2_df.head(5))
    print(file2_df.info())
    print(file2_df.describe())


def clean_Data(file1_df, file2_df):
    # Count the number of duplicates in each file, drop duplicates
    def remove_Duplicates(file1_df, file2_df):
        number_Duplicates_1 = file1_df.duplicated().sum()
        number_Duplicates_2 = file2_df.duplicated().sum()
        file1_df.drop_duplicates(inplace=True)
        file2_df.drop_duplicates(inplace=True)

        return number_Duplicates_1, number_Duplicates_2

    def fix_Missing_Values(file1_df, file2_df):
        # Create dataframes for numerical columns in order to calculate average
        file1_numerical = file1_df.select_dtypes(include=["number"])
        file2_numerical = file2_df.select_dtypes(include=["number"])

        # Need to store this as a list because unlike for numerical values pandas handling of categories is not efficient, so it is easier to use a list 
        file1_category = file1_df.select_dtypes(include=["category"]).columns.tolist()
        file2_category = file2_df.select_dtypes(include=["category"]).columns.tolist()

        # Calculate current column mean- fill empty data with the mean of the current column-then iterate onto the next one Store back into original dataframe
        for column in file1_numerical:
            current_Col_Mean = file1_numerical[column].mean()
            file1_numerical[column] = file1_numerical[column].fillna(current_Col_Mean)
            file1_df[column] = file1_numerical[column]

        for column in file2_numerical:
            current_Col_Mean = file2_numerical[column].mean()
            file2_numerical[column] = file2_numerical[column].fillna(current_Col_Mean)
            file2_df[column] = file2_numerical[column]
        # Calculate current column mode- fill empty data with the mean of the current column-then iterate onto the next one. Store back into original dataframe
        for column in file1_category:
            current_Col_Mode = file1_category[column].mode()
            file1_category[column] = file1_category[column].fillna(current_Col_Mode)
            file1_df[column] = file1_category[column]
        for column in file2_category:
            current_Col_Mode = file2_category[column].mode()
            file2_category[column] = file2_category[column].fillna(current_Col_Mode)
            file1_df[column] = file2_category[column]

    # Set all the columns in the dataframe to lowercase
    def standardize_Columns(file1_df,file2_df):
        file1_df.columns = file1_df.columns.str.lower()
        file2_df.columns = file2_df.columns.str.lower()
    # Call duplicate function and print number of duplicates found
    number_Duplicates_1, number_Duplicates_2 = remove_Duplicates(file1_df, file2_df)
    print(
        f" Duplicates in File 1:{number_Duplicates_1} \n Duplicates in File 2: {number_Duplicates_2}"
    )
    fix_Missing_Values(file1_df, file2_df)
    standardize_Columns(file1_df,file2_df)

    return file1_df, file2_df

def main():
    file1_df, file2_df = read_Files()

    display_df(file1_df, file2_df)
    file1_df,file2_df = clean_Data(file1_df, file2_df)
    display_df(file1_df, file2_df) # TODO: Remove later after validation

# Validate main function exists
if __name__ == "__main__":
    main()
