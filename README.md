import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random


. Software Requirements
Operating System: The application is a desktop GUI program and requires a graphical operating system. It has been tested and is compatible with:
Windows 10 / 11
macOS 10.15 (Catalina) or newer
Modern Linux distributions with a desktop environment (e.g., Ubuntu 20.04+, Fedora 36+, Mint 21+)
Python: You must have Python installed on your system.
Required Version: Python 3.8 or newer.
Git (Optional): Required only for cloning the repository from GitHub. It is not needed to simply run the application.

2. Hardware Requirements
The application is lightweight and should run smoothly on most modern computers.
RAM: Minimum of 2 GB RAM.
Disk Space: At least 50 MB of free disk space for the application and its dependencies.
Internet Connection: An active internet connection is required for two features:
To download the Python libraries during the initial setup.
For the application to fetch real-time data from the open weather-API.

3. Python Library Dependencies
The project relies on several external Python libraries. These can be easily installed using pip, Python's package installer.
requests: For making HTTP requests to the external currency API.

 For efficient data manipulation and aggregation, especially for creating the spending analysis weather graphs.
matplotlib: For generating the data visualizations .

Installation
You can install all required libraries at once by navigating to the project folder in your terminal and running the following command:
pip install -r requirements.txt


Alternatively, you can install them manually:
pip install requests ...............


4. API Key Requirement
The application's multi-currency features (the financial summary and the currency converter) depend on an external API.
Service: open weather-API
Requirement: You must obtain a free API key from their website.
The first time you run the application, it will prompt
