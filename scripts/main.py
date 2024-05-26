"""
main.py

This module serves as the entry point for the Excel Visualization App.
It initializes the main Tkinter window and runs the application.
"""

import tkinter as tk
from app import ExcelVisualizationApp

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelVisualizationApp(root)
    root.mainloop()