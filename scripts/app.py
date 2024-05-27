"""
app.py

This module provides a graphical user interface (GUI) for visualizing data using various types of graphs. 
The interface allows users to input data, generate scatter plots, bar graphs, histograms, and pie charts, 
and save or load the data to and from Excel files. The application is built using Tkinter for the GUI, 
Pandas for data manipulation, Seaborn for data visualization, and Matplotlib for plotting. 
The interface includes options to reset inputs and handle exceptions for file operations.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from excel_operations import search_for_file
from data_processing import generate_scatter_plot_data_set, generate_bar_graph_data_set, generate_histogram_data_set, generate_pie_chart_data_set
from data_visualization import generate_scatter_plot, generate_bar_graph, generate_histogram, generate_pie_chart

class ExcelVisualizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Visualization")
        
        # Define primary and secondary colors
        self.primary_color = "#87CEEB"  # Light blue
        self.secondary_color = "#F5F5F5"  # Very light gray
        self.save_button_color = "#4CAF50"  # Green
        self.load_button_color = "#FFD700"  # Yellow

        # Configure root window
        self.root.configure(bg=self.secondary_color)
        self.root.geometry("600x400")  # Set the window size

        # Initialize current_data_set
        self.current_data_set = None

        # Set the style
        self.style = ttk.Style()
        self.style.configure('TLabel', background=self.secondary_color, foreground='black', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12), padding=10)
        self.style.configure('TFrame', background=self.secondary_color)
        self.style.map('Save.TButton', background=[('active', self.save_button_color), ('!active', self.save_button_color)], foreground=[('active', 'black'), ('!active', 'black')])
        self.style.map('Load.TButton', background=[('active', self.load_button_color), ('!active', self.load_button_color)], foreground=[('active', 'black'), ('!active', 'black')])

        self.graph_type = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        header_frame = ttk.Frame(self.root, style='TFrame')
        header_frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        ttk.Label(header_frame, text="Excel Visualization", style='TLabel', font=('Arial', 16, 'bold')).pack()

        main_frame = ttk.Frame(self.root, style='TFrame')
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(main_frame, text="Select Graph Type:", style='TLabel').grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        graph_options = ["Scatter Plot", "Bar Graph", "Histogram", "Pie Chart"]
        self.graph_type_combo = ttk.Combobox(main_frame, values=graph_options, textvariable=self.graph_type, font=('Arial', 12), width=20)
        self.graph_type_combo.grid(row=0, column=1, padx=10, pady=10)
        self.graph_type_combo.bind("<<ComboboxSelected>>", self.update_input_fields)

        self.input_frame = ttk.Frame(main_frame, style='TFrame')
        self.input_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.submit_button = ttk.Button(main_frame, text="Submit", command=self.collect_and_visualize_data, style='TButton', width=20)
        self.submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.reset_button = ttk.Button(main_frame, text="Reset", command=self.reset_inputs, style='TButton', width=20)
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.save_button = ttk.Button(main_frame, text="Save Data", command=self.save_data, style='Save.TButton', width=20)
        self.save_button.grid(row=4, column=0, padx=10, pady=10)

        self.load_button = ttk.Button(main_frame, text="Load Data", command=self.load_data, style='Load.TButton', width=20)
        self.load_button.grid(row=4, column=1, padx=10, pady=10)

    def update_input_fields(self, event):
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        graph_type = self.graph_type.get()
        if graph_type == "Scatter Plot":
            self.create_input_fields("X values (comma separated)", "Y values (comma separated)")
        elif graph_type == "Bar Graph":
            self.create_input_fields("Categories (comma separated)", "Values (comma separated)")
        elif graph_type == "Histogram":
            self.create_input_field("Values (comma separated)")
        elif graph_type == "Pie Chart":
            self.create_input_fields("Categories (comma separated)", "Values (comma separated)")

    def create_input_fields(self, label_text1, label_text2):
        ttk.Label(self.input_frame, text=label_text1, style='TLabel').pack(padx=10, pady=5)
        self.entry1 = ttk.Entry(self.input_frame, font=('Arial', 12), width=30)
        self.entry1.pack(padx=10, pady=5)
        
        ttk.Label(self.input_frame, text=label_text2, style='TLabel').pack(padx=10, pady=5)
        self.entry2 = ttk.Entry(self.input_frame, font=('Arial', 12), width=30)
        self.entry2.pack(padx=10, pady=5)

    def create_input_field(self, label_text):
        ttk.Label(self.input_frame, text=label_text, style='TLabel').pack(padx=10, pady=5)
        self.entry1 = ttk.Entry(self.input_frame, font=('Arial', 12), width=30)
        self.entry1.pack(padx=10, pady=5)

    def collect_and_visualize_data(self):
        """
        Collects the data from input fields and visualizes it using the selected graph type.
        """
        graph_type = self.graph_type.get()
        data_set = {}

        if graph_type == "Scatter Plot":
            x_values = self.entry1.get().split(',')
            y_values = self.entry2.get().split(',')
            data_set = generate_scatter_plot_data_set('x', 'y', x_values, y_values)
            generate_scatter_plot(data_set)
        elif graph_type == "Bar Graph":
            categories = self.entry1.get().split(',')
            values = self.entry2.get().split(',')
            data_set = generate_bar_graph_data_set('category', 'value', categories, values)
            generate_bar_graph(data_set)
        elif graph_type == "Histogram":
            values = self.entry1.get().split(',')
            data_set = generate_histogram_data_set('category', 'value', ['category'] * len(values), values)
            generate_histogram(data_set)
        elif graph_type == "Pie Chart":
            categories = self.entry1.get().split(',')
            values = self.entry2.get().split(',')
            data_set = generate_pie_chart_data_set('category', 'value', categories, values)
            generate_pie_chart(data_set)
        
        self.current_data_set = data_set  # Save the current dataset for saving
        print(f"Current data set: {self.current_data_set}")

    def reset_inputs(self):
        """
        Resets the input fields and selected graph type.
        """
        self.graph_type.set('')
        for widget in self.input_frame.winfo_children():
            widget.destroy()

    def save_data(self):
        """
        Saves the current dataset to an Excel file.
        """
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_path and self.current_data_set:
            print(f"Saving data set to {file_path}")
            search_for_file(file_path, 'write', self.current_data_set)
        else:
            messagebox.showerror("Error", "No data to save.")

    def load_data(self):
        """
        Loads a dataset from an Excel file.
        """
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            data_frames = search_for_file(file_path, 'read')
            if data_frames:
                df = list(data_frames.values())[0]  # Assuming the first sheet is the relevant one
                data_set = df.to_dict(orient='list')
                self.current_data_set = data_set
                print(f"Loaded data set: {self.current_data_set}")
                # Automatically update the input fields and plot the data
                self.auto_fill_inputs_and_plot(data_set)

    def auto_fill_inputs_and_plot(self, data_set):
        """
        Automatically fills the input fields and visualizes the data based on the selected graph type.
        """
        graph_type = self.graph_type.get()
        if graph_type == "Scatter Plot":
            generate_scatter_plot(data_set)
        elif graph_type == "Bar Graph":
            generate_bar_graph(data_set)
        elif graph_type == "Histogram":
            generate_histogram(data_set)
        elif graph_type == "Pie Chart":
            generate_pie_chart(data_set)


