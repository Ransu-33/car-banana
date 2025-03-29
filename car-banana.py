import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt


data = pd.read_csv(r'C:\Users\Lance\Desktop\python_projects\car-banana\vehicles_us.csv')

#
data['date_posted'] = pd.to_datetime(data['date_posted'])
data['date_posted'] = pd.DatetimeIndex(data['date_posted']).year
data.rename(columns={'date_posted': 'listing_year'}, inplace=True)

data['manufacturer'] = data['model'].apply(lambda x: x.split()[0])

# Get the top 5 manufacturers
top_manufacturers = data['manufacturer'].value_counts().head(5).index.tolist()

# Filter for only top 5 manufacturers
filtered_data = data[data['manufacturer'].isin(top_manufacturers)]

# Get the average price by condition and manufacturer
five_avg_price = filtered_data.groupby(['condition', 'manufacturer'])['price'].mean().reset_index()

# Creates bar chart
fig = px.bar(five_avg_price,
             x='condition',
             y='price',
             color='manufacturer',
             barmode='group',
             title='Average Price of Top 5 Manufacturers by Condition',
             category_orders={"condition": ["new", "like new", "excellent", "good", "fair", "salvage"]},
             labels={
                 'condition': 'Condition',
                 'price': 'Price (USD)',
                 'manufacturer': 'Manufacturer'})

st.plotly_chart(fig)