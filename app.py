import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

from dotenv import load_dotenv
import os

from fredapi import Fred

load_dotenv()
api_key = os.getenv('FRED_API_KEY')

plt.style.use('fivethirtyeight')
pd.set_option('display.max_columns', 500)
color_pal = plt.rcParams['axes.prop_cycle'].by_key()['color']

# Create an instance of the fred api
fred = Fred(api_key=api_key)

