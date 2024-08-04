import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly
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

sp_search = fred.search('S&P', order_by='popularity', sort_order='desc')

# Test search results to ensure API is connected correctly
# print(sp_search.head())

# pull raw data and plot
sp500 = fred.get_series(series_id='SP500')
sp500.plot(title='S&P 500', figsize=(10, 5), lw=1.5)
plt.show()


# pull and join multiple data series

# Get state unemployment data
state_unemployment_df = fred.search('unemployment rate state', filter=('frequency', 'Monthly'))
# Filter the DataFrame
state_unemployment_df = state_unemployment_df.query('seasonal_adjustment == "Seasonally Adjusted" and units == "Percent"')
# For demonstration purposes, let's assume you want to plot the count of filtered results
state_unemployment_df = state_unemployment_df.loc[state_unemployment_df['title'].str.contains('Unemployment Rate')]

# Create an empty list to store the results
all_results = []

# Pull and join data for each state's unemployment rate series
for myid in state_unemployment_df.index:
    results = fred.get_series(myid)
    results = results.to_frame(name = myid)
    all_results.append(results)
# Join the dataframes
unemployment_results = pd.concat(all_results, axis=1)

# Drop the specified columns if they exist
columns_to_drop = ['M08310USM156SNBR', 'DSUR']
columns_in_df = [col for col in columns_to_drop if col in unemployment_results.columns]
unemployment_results = unemployment_results.drop(columns=columns_in_df)

unemployment_states = unemployment_results.drop('UNRATE', axis=1)

# Map state IDs to state names using the 'state_unemployment_df' DataFrame
state_id_to_name = state_unemployment_df['title'].str.replace('Unemployment Rate in ', '').to_dict()
unemployment_states.index = [state_id_to_name.get(i, i) for i in unemployment_states.index]

fig = px.line(unemployment_states, title='Unemployment Rate by State')

# Display the Plotly figure - It shows unemployment rates by state
plotly.io.show(fig)


# Pull April 2020 unemployment rate per state
if '2020-04-01' in unemployment_states.index:
    unemployment_april_2020 = unemployment_states.loc['2020-04-01'].T.sort_values()
    
    # Map state IDs to state names using the 'state_unemployment_df' DataFrame
    state_id_to_name = state_unemployment_df['title'].str.replace('Unemployment Rate in ', '').to_dict()
    unemployment_april_2020.index = [state_id_to_name.get(i, i) for i in unemployment_april_2020.index]
    
    unemployment_april_2020.plot(kind='bar', figsize=(10, 5))
    plt.title('Unemployment Rate by State in April 2020')
    plt.xlabel('State')
    plt.ylabel('Unemployment Rate')
    plt.show()
else:
    print("Date '2020-04-01' not found in the data.")