import pandas as pd
import numpy as np


# File path for the Excel file where the data will be saved
FILE_PATH = 'Tester-Sheets\\tester-excel-sheet.xlsx'
parsed_file_path = FILE_PATH.split('\\')
FILE_NAME = parsed_file_path[-1]  # Extracts the file name from the file path


# Generates a data set for histograms or count plots
def histogramOrCountPlotDataSet():
    """
    Generates a sample data set for creating histogram or count plots.

    Returns:
        dict: A dictionary containing sample numerical and categorical data.
    """

    # Create a dictionary with sample data
    data_set = {
        # Array of 100 random numbers with a mean of 50 and standard deviation of 15
        'NumericalColumn1': np.random.normal(50, 15, 100),

        # Array of 100 random numbers from an exponential distribution with a scale (std) of 5
        'NumericalColumn2': np.random.exponential(5, 100),

        # Array of 100 random categorical values chosen from the given list
        'CategoricalColumn1': np.random.choice(['A', 'B', 'C', 'D'], 100),

        # Array of 100 random categorical values chosen from the given list
        'CategoricalColumn2': np.random.choice(['X', 'Y', 'Z'], 100)
    }

    return data_set


# Generates a data set for scatter plots or pair plots
def scatterOrPairPlotDataSet():
    """
    Generates a sample data set for creating scatter plots or pair plots.

    Returns:
        dict: A dictionary containing sample numerical data.
    """

    # Create a dictionary with sample data
    data_set = {
        # Array of 100 random numbers with a mean of 50 and standard deviation of 15
        'NumericalColumn1': np.random.normal(50, 15, 100),

        # Array of 100 random numbers with a mean of 70 and standard deviation of 20
        'NumericalColumn2': np.random.normal(70, 20, 100),

        # Array of 100 random numbers with a mean of 80 and standard deviation of 35
        'NumericalColumn3': np.random.normal(80, 35, 100)
    }

    return data_set


# Writes multiple data sets to different sheets in an Excel file
def writeToExcelSheet(file_path, data_sets):
    """
    Writes multiple data sets to different sheets in an Excel file.

    Args:
        file_path (str): The file path where the Excel file will be saved.
        data_sets (list): A list of dictionaries containing the data sets to be written.
    """

    # Convert each dictionary in the list to a DataFrame and add to the data_frame_list
    data_frame_list = [pd.DataFrame(data_set) for data_set in data_sets]

    # Write each DataFrame to a separate sheet in the Excel file
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        for i, df in enumerate(data_frame_list):
            sheet_name = f'Sheet{i+1}'  # Create a sheet name like 'Sheet1', 'Sheet2', etc.
            df.to_excel(writer, sheet_name=sheet_name, index=False)  # Write DataFrame to the sheet

    # Print a success message
    print(f'Data successfully written to {FILE_NAME}!')


# List of data sets to be written to the Excel file
inputs = [scatterOrPairPlotDataSet(), histogramOrCountPlotDataSet(), histogramOrCountPlotDataSet()]

# Call the function to write data to the Excel file
writeToExcelSheet(FILE_PATH, inputs)
