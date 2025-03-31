import pandas as pd
import streamlit as st
import plotly.express as px


data = pd.read_csv('vehicles_us.csv',
                   dtype={'price': 'float64'},
                   engine='python',
                   na_values=['N/A', 'Nhttps://car-banana.onrender.com/A', '']
                   )

# Add manufacturer column
data['manufacturer'] = data['model'].apply(lambda x: x.split()[0])

# Get the top 5 manufacturers
top_manufacturers = data['manufacturer'].value_counts().head(5).index.tolist()

# Filter for only top 5 manufacturers
filtered_data = data[data['manufacturer'].isin(top_manufacturers)]

# Get the average price by condition and manufacturer
five_avg_price = filtered_data.groupby(['condition', 'manufacturer'])['price'].mean().reset_index()

# Header and display for the dataframe
st.header('Data of Car Sales')

# Create checkbox to remove manufacturers with less than 500 cars
remove_less_than_500 = st.checkbox('Remove Manufacturers with Less than 500 Cars')
if remove_less_than_500:
    # Get count of each manufacturer and filter with > 500 entries
    count_manufacturers = data['manufacturer'].value_counts()
    keep_500 = count_manufacturers[count_manufacturers > 500].index

    # Filter initial dataframe
    count_data = data[data['manufacturer'].isin(keep_500)]
else:
    count_data = data

st.dataframe(count_data)

st.header('Average Price of Top 5 Manufacturers by Condition')
# Creates bar chart
fig = px.bar(five_avg_price,
             x='condition',
             y='price',
             color='manufacturer',
             barmode='group',
             category_orders={"condition": ["new", "like new", "excellent", "good", "fair", "salvage"]},
             labels={
                 'condition': 'Condition',
                 'price': 'Price (USD)',
                 'manufacturer': 'Manufacturer'})
st.plotly_chart(fig)


# Creates scatter plot showing relationship between vehicle price and days listed
st.header('Price of Vehicles by Days on the Market for each manufacturer')
# get list of manufacturers
manufacturer_list = sorted(data['manufacturer'].unique())
# get user inputs from dropdowns
select_manufacturer = st.selectbox(label='Manufacturer 1',  # title of dropdown
                              options=manufacturer_list,  # lists manufacturers in dropdown
                              index=manufacturer_list.index('toyota')  # default selection
                              )
# filter dataframe for selected manufacturers
compare_price = data[(data['manufacturer'] == select_manufacturer) & (data['price'] > 500)]
# Creates the plotly scatter plot
scatter_price = px.scatter(compare_price,
                 x='days_listed',
                 y='price',
                 )
st.write(scatter_price)

model_filter = data[data['model_year'] >= 1980]
# Creates histogram of model years
st.header('Model Year Distribution')
model_hist = px.histogram(model_filter,
                          x='model_year',
                          nbins=40,
                          labels={'model_year': 'Model Year'}
                              ).update_layout(yaxis_title='Frequency')
st.write(model_hist)
