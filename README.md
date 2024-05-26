# Excel Visualization 

Excel Visualization is a graphical user interface (GUI) application that allows users to input data, generate various types of visualizations (scatter plots, bar graphs, histograms, and pie charts), and save or load the data to and from Excel files. This project was developed to enhance my skills in data visualization and Python programming, utilizing a variety of modern libraries and frameworks.

## Table of Contents

- [Motivation](#motivation)
- [Features](#features)
- [Libraries Used](#libraries-used)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [License](#license)

## Motivation

As a computer science student, I aim to improve my Python programming skills and gain experience with data visualization libraries. The idea behind Excel Visualization was to create a practical tool that allows users to visualize their data easily while providing me with hands-on experience in using Pandas, Seaborn, and Matplotlib for data manipulation and visualization. This project also helped me become proficient in handling Excel files with Python.

## Features

- **Input Data**: Users can input data for different types of graphs directly through the GUI.
- **Generate Visualizations**: Create scatter plots, bar graphs, histograms, and pie charts based on the input data.
- **Save and Load Data**: Save the current dataset to an Excel file or load data from an existing Excel file.
- **Reset Inputs**: Clear all inputs to start fresh.
- **Error Handling**: Handles exceptions for file operations to ensure a smooth user experience.

## Libraries Used

- **Tkinter**: For building the GUI of the application.
- **Pandas**: For data manipulation and handling Excel files.
- **Seaborn**: For creating attractive and informative statistical graphics.
- **Matplotlib**: For plotting graphs and visualizations.
- **Openpyxl**: For reading and writing Excel files.

## Screenshots

![Scatter Plot](screenshots/scatter_plot.png)
![Bar Graph](screenshots/bar_graph.png)
![Histogram](screenshots/histogram.png)
![Pie Chart](screenshots/pie_chart.png)

## Project Structure

- `main.py`: Entry point for the application. Initializes and runs the Tkinter main window.
- `app.py`: Contains the `ExcelVisualizationApp` class that defines the GUI and its functionalities.
- `excel_operations.py`: Provides functions for reading from and writing to Excel files.
- `data_processing.py`: Contains functions to generate datasets for different types of graphs.
- `data_visualization.py`: Contains functions to generate and display different types of graphs using Seaborn and Matplotlib.
