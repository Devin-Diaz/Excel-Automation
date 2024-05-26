import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from excel_operations import search_for_file
from data_processing import generate_scatter_plot_data, generate_bar_graph_data, generate_histogram_data, generate_pie_chart_data
from data_visualization import generate_scatter_plot, generate_bar_graph, generate_histogram, generate_pie_chart

class ExcelVisualzationApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Excel Visualization App')

        self.graph_type = tk.StringVar()
        self.create_widgets()
    
    