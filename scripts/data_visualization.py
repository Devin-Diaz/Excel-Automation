"""
visualization.py

This module provides functions for generating various data visualizations
using pandas, seaborn, and matplotlib. The visualizations include scatter
plots, pie charts, bar graphs, and histograms.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_scatter_plot(data_set):
    """
    Generates and displays a scatter plot using the provided dataset.

    Parameters:
    data_set (dict): The dataset containing the data to plot. The dictionary should have two keys representing the
                     columns for the x and y axes.
    """
    df = pd.DataFrame(data_set)
    x_column, y_column = df.columns
    sns.scatterplot(data=df, x=x_column, y=y_column)
    plt.title('Scatter Plot')
    plt.show()

def generate_pie_chart(data_set):
    """
    Generates and displays a pie chart using the provided dataset.

    Parameters:
    data_set (dict): The dataset containing the data to plot. The dictionary should have two keys representing the
                     category and numeric values for the pie chart.
    """
    df = pd.DataFrame(data_set)
    category_column, numeric_column = df.columns
    plt.pie(df[numeric_column], labels=df[category_column], autopct='%1.1f%%')
    plt.title('Pie Chart')
    plt.show()

def generate_bar_graph(data_set):
    """
    Generates and displays a bar graph using the provided dataset.

    Parameters:
    data_set (dict): The dataset containing the data to plot. The dictionary should have two keys representing the
                     categories and numeric values for the bar graph.
    """
    df = pd.DataFrame(data_set)
    category_column, numeric_column = df.columns
    
    # Convert numeric column to numeric type
    df[numeric_column] = pd.to_numeric(df[numeric_column])
    
    # Create the bar plot
    sns.barplot(data=df, x=category_column, y=numeric_column)
    
    # Set the y-axis limits to start at 0
    plt.ylim(0, df[numeric_column].max() * 1.1)
    
    plt.title('Bar Graph')
    plt.xlabel(category_column)
    plt.ylabel(numeric_column)
    plt.show()

def generate_histogram(data_set):
    """
    Generates and displays a histogram using the provided dataset.

    Parameters:
    data_set (dict): The dataset containing the data to plot. The dictionary should have two keys representing the
                     category and numeric values for the histogram. Only the numeric values will be used for binning.
    """
    df = pd.DataFrame(data_set)
    value_column = df.columns[1]  # Get the second column name for values
    sns.histplot(data=df, x=value_column)
    plt.title('Histogram')
    plt.show()
