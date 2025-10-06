#### **Data Analytics Using Python Libraries**

For this challenge, you will use three Python libraries - _pandas__**,**_ _numpy__**,**_ and _matplotlib_ _**\-**_ to perform advanced data analysis and visualization. Please review the references under the Week 6 module to learn more about these libraries. Using these libraries, develop a Python program that performs the following steps:

#### **Instructions**

1.  **Load and Inspect the Data**
    
    *   Read the two data files below as two separate dataframes:
        
        *   [Auto\_1.csv](https://uah.instructure.com/courses/84115/files/10269269?wrap=1)[Download Auto\_1.csv](https://uah.instructure.com/courses/84115/files/10269269/download?download_frd=1)
            
        *   [Auto\_2.csv](https://uah.instructure.com/courses/84115/files/10269271?wrap=1)[Download Auto\_2.csv](https://uah.instructure.com/courses/84115/files/10269271/download?download_frd=1)
            
            *   **OR** (_based on your choice for operations 5 and 6_)
                
        *   [Auto\_1\_with price.csv](https://uah.instructure.com/courses/84115/files/10269272?wrap=1)[Download Auto\_1\_with price.csv](https://uah.instructure.com/courses/84115/files/10269272/download?download_frd=1)
            
        *   [Auto\_2\_with price.csv](https://uah.instructure.com/courses/84115/files/10269277?wrap=1)[Download Auto\_2\_with price.csv](https://uah.instructure.com/courses/84115/files/10269277/download?download_frd=1)
            
    *   Display the first 5 rows of each dataframe to understand their structure.
        
    *   Print a summary of each dataframe using .info() and .describe() to analyze column types, missing values, and basic statistics.
        
2.  **Data Cleaning**
    
    *   Check for missing data in both dataframes:
        
        *   For numerical columns with missing values, replace them with the column mean.
            
        *   For categorical columns with missing values, replace them with the most frequent value (mode).
            
    *   Check for duplicate rows in both dataframes and remove them if they exist. Print how many duplicates were removed.
        
    *   Standardize column names (e.g., convert all column names to lowercase) to ensure consistency across both dataframes.
        
3.  **Data Exploration**
    
    *   Print the total number of observations (_rows_) and features (_columns_) in each dataframe.
        
    *   Identify columns shared between both datasets and columns unique to each dataset.
        
    *   Calculate summary statistics (mean, median, min, max) for at least three numerical columns in each dataframe.
        
4.  **Merge Dataframes**
    
    *   Combine the two dataframes into a single dataframe using an appropriate join method (e.g., _inner join_ or _outer join_). Use a common key column for merging if available; otherwise, create one if necessary.
        
    *   After merging, ensure there are no duplicate rows in the combined dataframe.
        
    *   Print the shape of the merged dataframe and display its first 5 rows.
        
5.  **Feature Transformation**
    
    *   Create a new column called _price\_to\_weight\_ratio_ by dividing the price of each car by its weight. Use numpy functions to handle any potential division by zero errors.
        
        *   _For the price, if you are using the_ _**Auto\_1.csv**_ _and_ _**Auto\_2.csv**_ _datasets, you can generate a new column with the random prices using df\['price'\] = \[1100, 1400, 2500, ....\]_
            
            *   _OR_
                
        *   _You can use the_ _**Auto\_1 with price.csv**_ _and_ _**Auto\_2 with price.csv**_ _datasets which already has the price column in the dataset._
            
    *   Extract a new column called _car\_age_ by subtracting the car's manufacturing year from the current year (use Python's datetime module if needed).
        
    *   Categorize cars into bins based on their horsepower (e.g., low, medium, high) using pandas' cut() function. Add this as a new column called _horsepower\_category_.
        
6.  **Aggregation and Grouping**
    
    *   Group the data by a relevant categorical column (e.g., _car\_make_ or _fuel\_type_) and calculate aggregated statistics such as:
        
        *   Average price
            
        *   Total weight
            
        *   Count of cars in each group
            
    *   Sort the grouped data by one of these statistics (e.g., _average price_) in descending order and display the top 5 groups.
        
7.  **Advanced Visualizations**
    
    *   Create at least three visualizations using matplotlib:
        
        *   A bar chart showing aggregated statistics (e.g., _average price by car\_make_ or _total weight by fuel\_type_).
            
        *   A scatter plot comparing two numerical columns (e.g., _miles\_per\_gallon_ vs. _horsepower_) with appropriate labels, title, and color coding based on a categorical variable.
            
        *   A line chart showing trends over time if a time-based column exists (e.g., _average price_ or _weight_ by _manufacturing year_).
            
8.  **Correlation Analysis**
    
    *   Identify relationships between numerical variables by calculating pairwise correlations using pandas' .corr() method.
        
    *   Visualize these correlations using a heatmap from matplotlib or seaborn to identify strong positive or negative relationships.
        
9.  **Export Results**
    
    *   Save the cleaned and transformed dataframe into a new CSV file called cleaned\_automobiles.csv.
        
    *   Save one of your visualizations as an image file (e.g., PNG or JPG).
        

Submit your python file as _lastName\_firstName\_PC\_5.py_

**Grading Rubric:**

*   deduct 5 points if program fails to execute the operations specified above
    
*   deduct 5 points if program fails to export the saved files
    
*   deduct 5 points if program fails to run and has errors
    
*   deduct 5 point for code without appropriate comments and pseudocode.
    
*   0 if someone else's work or something from the internet or a book is submitted.