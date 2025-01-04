import pandas as pd
import streamlit as st
import plotly.express as plt

# Load the dataset
data = pd.read_csv('vehicles_us.csv')

# Handle missing values
data['model_year'] = data['model_year'].fillna(data['model_year'].median())
data['cylinders'] = data['cylinders'].fillna(data['cylinders'].median())
data['odometer'] = data['odometer'].fillna(data['odometer'].median())
data['paint_color'] = data['paint_color'].fillna('unknown')
data['is_4wd'] = data['is_4wd'].fillna(0).astype(bool)  # Convert to boolean

# Convert 'date_posted' to datetime
data['date_posted'] = pd.to_datetime(data['date_posted'])

# Remove outliers
price_outliers = data[(data['price'] < 500) | (data['price'] > 100000)].index
data.drop(price_outliers, inplace=True)

odometer_outliers = data[data['odometer'] > 500000].index
data.drop(odometer_outliers, inplace=True)

# Reset index after cleaning
data.reset_index(drop=True, inplace=True)
