# Economic Data Analysis Project

This project aims to analyze economic data using the Federal Reserve Economic Data (FRED) API. The analysis includes fetching various economic indicators, processing the data, and generating visualizations to understand economic trends.

## Table of Contents

- [Economic Data Analysis Project](#economic-data-analysis-project)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [API\_Key\_Setup](#api_key_setup)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ajwild320/Project_Economic_Data_Analysis
   ```
   ```bash
   cd economic-data-analysis
   ```

2. **Create and activate a virtual environment in Windows**:

    ```bash
    python -m venv .venv
    ```
    ```bash
    .venv\Scripts\activate
    ```
3. **Install Required Dependencies**:
   
   ```bash
   pip install -r requirements.txt
   ```

# Usage

1. **Set up your [FRED API key](#api_key_setup)**

2. **Run Analysis Script**
   
   ```bash
   python app.py
   ```

# Project Structure

economic-data-analysis/

│

├── .gitignore

├── README.md

├── requirements.txt

├── app.py

├── .env

├── data/

└── output/

**app.py**: Main script for data analysis.

**requirements.txt**: List of dependencies.

**.env**: Environment file containing the FRED API key.

**data/**: Directory to store raw data.

**output/**: Directory to save visualizations and results.


# Requirements

- pandas
- numpy
- matplotlib
- plotly
- python-dotenv
- os
- fredapi

# API_Key_Setup

To use the FRED API, you need to sign up for an API key [here](https://fredaccount.stlouisfed.org/apikeys)
. Once you have your API key:

1. Create a .env file in the project root directory.

2. Add your API key to the .env file:
   ```env
   FRED_API_KEY=your_api_key_here
   ```
