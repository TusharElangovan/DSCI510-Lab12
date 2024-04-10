import streamlit as st
import pandas as pd

# Reading the CSV Datafile 
df = pd.read_csv("car_data.csv")

#  Default Values Declaration
car_name_filter = ""
transmission_filter = ["Manual", "Automatic"]  # Default: both selected
price_min, price_max = 0, 20
year_min, year_max = 2000,2024

# Create the sidebar with filter options
st.sidebar.header("Car Filters")
car_name_filter = st.sidebar.text_input("Car Name (Optional)")
transmission_filter = st.sidebar.multiselect("Transmission", ["Manual", "Automatic"], default=["Manual", "Automatic"])
price_min, price_max = st.sidebar.slider("Selling Price Range", min_value=0.0, max_value=df["Selling_Price"].max(), value=(0.0, 20.0))
year_min, year_max = st.sidebar.slider("Year Range", min_value=df["Year"].min(), max_value=df["Year"].max(), value=(2000, 2024))
st.sidebar.button("Apply Filters")

# Apply filters based on user selections
filtered_df = df.copy()
if car_name_filter:
    filtered_df = filtered_df[filtered_df["Car_Name"].str.contains(car_name_filter, case=False)]
if transmission_filter != ["Manual", "Automatic"]:
    filtered_df = filtered_df[filtered_df["Transmission"].isin(transmission_filter)]
filtered_df = filtered_df[(filtered_df["Selling_Price"] >= price_min) & (filtered_df["Selling_Price"] <= price_max)]
filtered_df = filtered_df[(filtered_df["Year"] >= year_min) & (filtered_df["Year"] <= year_max)]

# Display the filtered data on the main screen
st.header("Filtered Car Data")
if filtered_df.empty:
    st.write("No cars match the current filters.")
else:
    st.table(filtered_df)