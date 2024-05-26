"""
data_processing.py

This module provides functions for generating datasets for different types
of visualizations and validating input data. It includes utility functions
for handling numeric and categorical data.
"""

def generate_scatter_plot_data_set(column_one_name, column_two_name, numeric_list_one, numeric_list_two):
    """Generates scatter plot data set using two numeric lists."""
    verify_data_length(numeric_list_one, numeric_list_two)
    assert is_numeric_list(numeric_list_one), "**ALL INPUTS MUST BE NUMERICAL!**"
    assert is_numeric_list(numeric_list_two), "**ALL INPUTS MUST BE NUMERICAL!**"

    data_set = {
        column_one_name: numeric_list_one,
        column_two_name: numeric_list_two
    }
    return data_set

def generate_pie_chart_data_set(column_one_name, column_two_name, categorical_list, numeric_list):
    """Generates pie chart data set using a categorical list and numeric list."""
    verify_data_length(categorical_list, numeric_list)
    assert is_string_list(categorical_list), "**ALL INPUTS MUST BE CATEGORICAL!**"
    assert is_numeric_list(numeric_list), "**ALL INPUTS MUST BE NUMERICAL!**"

    data_set = {
        column_one_name: categorical_list,
        column_two_name: numeric_list
    }
    return data_set

def generate_bar_graph_data_set(column_one_name, column_two_name, categorical_list, numeric_list):
    """Generates bar graph data set using a categorical list and numeric list."""
    verify_data_length(categorical_list, numeric_list)
    assert is_string_list(categorical_list), "**ALL INPUTS MUST BE CATEGORICAL!**"
    assert is_numeric_list(numeric_list), "**ALL INPUTS MUST BE NUMERICAL!**"

    data_set = {
        column_one_name: categorical_list,
        column_two_name: numeric_list
    }
    return data_set

def generate_histogram_data_set(column_one_name, column_two_name, categorical_list, numeric_list):
    """Generates histogram data set using a categorical list and numeric list."""
    verify_data_length(categorical_list, numeric_list)
    assert is_string_list(categorical_list), "**ALL INPUTS MUST BE CATEGORICAL!**"
    assert is_numeric_list(numeric_list), "**ALL INPUTS MUST BE NUMERICAL!**"

    data_set = {
        column_one_name: categorical_list,
        column_two_name: numeric_list
    }
    return data_set

def verify_data_length(list_one, list_two):
    """Verifies our data inputs are the same length for creating proper data sets."""
    if len(list_one) != len(list_two):
        raise ValueError("Both lists must be of the same length.")
    return True

def is_number(num):
    """Checks if the input is a numeric value."""
    try:
        float(num)
        return True
    except ValueError:
        return False

def is_numeric_list(list):
    """Checks if all inputs in the list are numeric values."""
    return all(is_number(num) for num in list)

def is_string_list(list):
    """Checks if all inputs in the list are string values."""
    return all(isinstance(s, str) for s in list)
