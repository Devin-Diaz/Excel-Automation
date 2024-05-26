"""
excel_operations.py

This module provides functions for writing data to an Excel sheet and reading data from an Excel file.
These functions are useful for saving and loading datasets for data visualizations. Additionally, 
exceptions are handled for read and write operations if the file is not found.
"""

import pandas as pd

def write_to_excel_file(file_path, data_set):
    """
    Writes the provided dataset to an Excel file at the specified path.

    Parameters:
    file_path (str): The path to the Excel file where the data should be written.
    data_set (dict): The dataset to write, where keys are column names and values are lists of data.
    """
    # Convert numeric lists to numeric types
    for key, value in data_set.items():
        if all(isinstance(i, str) and i.isdigit() for i in value):
            data_set[key] = [int(i) for i in value]
        elif all(isinstance(i, str) and is_float(i) for i in value):
            data_set[key] = [float(i) for i in value]

    df = pd.DataFrame(data_set)
    df.to_excel(file_path, index=False)

def read_excel_file(file_path):
    """
    Reads data from an Excel file and returns a dictionary of DataFrames, with sheet names as keys.

    Parameters:
    file_path (str): The path to the Excel file to read.

    Returns:
    dict: A dictionary where the keys are sheet names and the values are DataFrames containing the data.
    """
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names
    df = {sheet: pd.read_excel(file_path, sheet_name=sheet) for sheet in sheet_names}
    return df

def search_for_file(file_path, operation, data_set=None):
    """
    Tries to read from or write to the specified Excel file, handling any exceptions that may occur.

    Parameters:
    file_path (str): The path to the Excel file.
    operation (str): The operation to perform, either 'read' or 'write'.
    data_set (dict, optional): The dataset to write if the operation is 'write'.

    Returns:
    dict: If the operation is 'read', returns a dictionary of DataFrames containing the data.
    None: If the operation is 'write' or an exception occurs.
    """
    try:
        if operation == 'read':
            print(f"Attempting to read from file: {file_path}")
            return read_excel_file(file_path)
        elif operation == 'write':
            if data_set is not None:
                print(f"Attempting to write to file: {file_path} with data: {data_set}")
                write_to_excel_file(file_path, data_set)
                print("Write operation successful.")
            else:
                raise ValueError("No dataset provided for write operation.")
        else:
            raise ValueError("Invalid operation specified. Use 'read' or 'write'.")
    except Exception as e:
        print(f"An error occurred while trying to {operation} the file: {e}")
        return None
    
def is_float(value):
    """
    Checks if a string value can be converted to a float.

    Parameters:
    value (str): The string to check.

    Returns:
    bool: True if the string can be converted to a float, False otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False