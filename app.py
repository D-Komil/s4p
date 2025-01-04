import pandas as pd
import streamlit as st
import plotly.express as plt

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Handle missing values
df['model_year'] = df['model_year'].fillna(df['model_year'].median())
df['cylinders'] = df['cylinders'].fillna(df['cylinders'].median())
df['odometer'] = df['odometer'].fillna(df['odometer'].median())
df['paint_color'] = df['paint_color'].fillna('unknown')
df['is_4wd'] = df['is_4wd'].fillna(0).astype(bool)  # Convert to boolean

# Convert 'date_posted' to datetime
df['date_posted'] = pd.to_datetime(df['date_posted'])

# Remove outliers
price_outliers = df[(df['price'] < 500) | (df['price'] > 100000)].index
df.drop(price_outliers, inplace=True)

odometer_outliers = df[df['odometer'] > 500000].index
df.drop(odometer_outliers, inplace=True)

# Add "Manufacturer" column for further use
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# Convert all columns to string type
df = df.astype(str)

# Reset index after cleaning
df.reset_index(drop=True, inplace=True)

# create a text header above the dataframe
st.header('Data viewer') 

# display the dataframe with streamlit
st.dataframe(df)