## IS 310 Project 5
## Author: Jack Schumacher
## Contact: js0342@uah.edu

# Install the following packages using pip (I did this in a virtual environment to avoid modifying the overall system state)
import pandas as pd
import numpy as np
import matplotlib
import os
from datetime import datetime

# Initialize the current date in order to use in functions
current_date = datetime.now()


def read_Files():
    # Define file path  - read the raw string to avoid newline interpretation. Using the relative file path here to avoid issues
    file1_location = r"Week 5/Data/Auto_1_with price.csv"
    file2_location = r"Week 5/Data/Auto_2_with price.csv"
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


def display_Merged_Df(merged_df):
    print("Merged Dataframe")
    print(merged_df.shape)
    print(merged_df.head(5))


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
    def standardize_Columns(file1_df, file2_df):
        file1_df.columns = file1_df.columns.str.lower()
        file2_df.columns = file2_df.columns.str.lower()

    # Call duplicate function and print number of duplicates found
    number_Duplicates_1, number_Duplicates_2 = remove_Duplicates(file1_df, file2_df)
    print(
        f" Duplicates in File 1:{number_Duplicates_1} \n Duplicates in File 2: {number_Duplicates_2}"
    )
    fix_Missing_Values(file1_df, file2_df)
    standardize_Columns(file1_df, file2_df)

    return file1_df, file2_df


def calculate_Statistics(file1_df, file2_df):
    def column_Row_Stats(file1_df, file2_df):
        # Pandas has a property that returns the index of the column labels, then measure the length of the index
        num_Columns1 = len(file1_df.columns)
        num_Columns2 = len(file2_df.columns)
        # Calculate length of rows using len() function
        num_Rows1 = len(file1_df)
        num_Rows2 = len(file2_df)
        # Print out the lengths of the number of columns and rows

        column_index1 = file1_df.columns
        column_index2 = file2_df.columns
        print(f"Number of Columns- File 1: {num_Columns1}")
        print(f"Number of Columns- File 2: {num_Columns2}")
        print(f"Number of Rows- File 1: {num_Rows1}")
        print(f"Number of Rows- File 2: {num_Rows2}")

        print("Column Statistics for File 1: \n")
        for column in column_index1:
            if pd.api.types.is_numeric_dtype(file1_df[column]):
                current_Column_Stats_Mean = file1_df[column].mean()
                current_Columns_Stats_Median = file1_df[column].mean()
                current_Column_Stats_Min = file1_df[column].mean()
                current_Column_Stats_Max = file1_df[column].mean()
                print(f"Column Statistics for:{column}")
                print(
                    f" Column Mean:{current_Column_Stats_Mean} \n Column Median: {current_Columns_Stats_Median} \n Column Minimum: {current_Column_Stats_Min} \n Column Maximum: {current_Column_Stats_Max} \n"
                )
        print("Column Statistics for File 2: \n")
        for column in column_index2:
            if pd.api.types.is_numeric_dtype(file2_df[column]):
                current_Column_Stats_Mean = file1_df[column].mean()
                current_Columns_Stats_Median = file1_df[column].mean()
                current_Column_Stats_Min = file1_df[column].mean()
                current_Column_Stats_Max = file1_df[column].mean()
                print(f"Column Statistics for:{column}")
                print(
                    f" Column Mean:{current_Column_Stats_Mean} \n Column Median: {current_Columns_Stats_Median} \n Column Minimum: {current_Column_Stats_Min} \n Column Maximum: {current_Column_Stats_Max} \n"
                )

    def identify_Columns(file1_df, file2_df):
        # Take the index of the column names in the dataframe and put it into a variable
        column_Names1 = file1_df.columns
        column_Names2 = file2_df.columns
        # Looks for columns that are shared between the two dataframes- Show this as a list in order to increase readability
        shared_columns = list(column_Names1.intersection(column_Names2))
        print(f"Shared Columns between dataframes: {shared_columns}")

    column_Row_Stats(file1_df, file2_df)
    identify_Columns(file1_df, file2_df)


def merge_dataframes(file1_df, file2_df):
    # Create a key column in both files to allow for easier merge
    file1_df = file1_df.reset_index().rename(columns={"index": "Key"})
    file2_df = file2_df.reset_index().rename(columns={"index": "Key"})

    # Merge on the key column
    merged_df = pd.merge(
        file1_df, file2_df, on="Key", how="outer", suffixes=("_df1", "_df2")
    )
    # Drop the key column upon merge
    merged_df = merged_df.drop(columns="Key")

    """
    Column Names:
    * There will be _x and _y suffixes after these
    * miles_per_gallon
    * engine
    * volume
    * hp
    * pounds
    * torque
    * source
    * year
    * make
    * price

    
    """

    # Need to strip out the _x and _y suffix- Data was merged on year, so will not try to get rid of that
    def remove_Merge_Duplicates(merged_df):
        # Setup the default column names
        default_Col_Names = [
            "miles_per_gallon",
            "engine",
            "volume",
            "hp",
            "pounds",
            "torque",
            "source",
            "make",
            "price",
            "year",
        ]
        # Iterate through the column names and add the _df1 and _df2 suffixes
        for column in default_Col_Names:
            col1_Merged_Name = f"{column}_df1"
            col2_Merged_Name = f"{column}_df2"
            if (
                col1_Merged_Name in merged_df.columns
                and col2_Merged_Name in merged_df.columns
            ):
                merged_df[column] = merged_df[col1_Merged_Name].combine_first(
                    merged_df[col2_Merged_Name]
                )
                merged_df = merged_df.drop(
                    columns=[col1_Merged_Name, col2_Merged_Name], errors="ignore"
                )

        merged_df.drop_duplicates(inplace=True)
        display_Merged_Df(merged_df)
        return merged_df

    merged_df = remove_Merge_Duplicates(merged_df)
    return merged_df


# Create the price to weight column by
def create_Columns(merged_df):
    # Create a new column with the price of the vehicle/weight of the vehicle
    merged_df["price_to_weight_ratio"] = merged_df["price"] / merged_df["pounds"]
    display_Merged_Df(merged_df)

    # Create horsepower bins- automatically cut based off of input data. Need to convert hp from string to numeric
    merged_df["hp"] = pd.to_numeric(merged_df["hp"], errors="coerce")
    mean_hp = merged_df["hp"].mean()
    # Fill empty spots with mean

    merged_df["hp"] = merged_df["hp"].fillna(mean_hp)
    merged_df["horsepower_category"] = pd.cut(merged_df["hp"], 3)
    print(f"Horsepower categories: \n{merged_df['horsepower_category'].value_counts()}")

    # Get the current year and then subtract the year that the car was built in
    current_year = current_date.year
    merged_df["car_age"] = current_year - merged_df["year"]
    merged_df["car_age"] = pd.to_numeric(merged_df["year"], errors="coerce").astype(int)

    return merged_df


def group_Cols_Calc_Stats(merged_df):
    # Group by engine type and calculate the mean horsepower
    avg_hp = merged_df.groupby("engine")["hp"].mean()
    print(f"\n Average price engine type vs hp: \n {avg_hp}")
    # Calculate the total hp in each of the groups
    total_hp = merged_df.groupby("engine")["hp"].sum()
    print(f"\n Total horsepower per engine type: \n {total_hp}")
    # Calculate the number of items in each of the hp groups
    counts_Per_Group = merged_df.groupby("engine").size()
    print(f"\n Items per engine type: {counts_Per_Group}")
    # Use the avg_hp series to sort the data in descending order. Then use head(5) to display the top 5 values
    sorted_By_Hp = avg_hp.sort_values(ascending = False)
    print(f"\n Data sorted by horsepower and engine type (top 5): \n {sorted_By_Hp.head(5)}")
    return merged_df


def main():
    file1_df, file2_df = read_Files()

    display_df(file1_df, file2_df)
    file1_df, file2_df = clean_Data(file1_df, file2_df)
    # display_df(file1_df, file2_df)  # TODO: Remove later after validation
    calculate_Statistics(file1_df, file2_df)
    merged_df = merge_dataframes(file1_df, file2_df)

    merged_df = create_Columns(merged_df)
    merged_df = group_Cols_Calc_Stats(merged_df)


# Validate main function     exists
if __name__ == "__main__":
    main()
