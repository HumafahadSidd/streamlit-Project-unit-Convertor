import streamlit as st

st.title("Unit Converter🕹")
st.write("Convert between different units of measurement.")
st.write("Select a conversion type and enter the value to convert.")

# Dropdown to select conversion type
conversion_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter value to convert", min_value=0.0, step=0.2)

# Length conversions
if conversion_type == "Length":
    length_type = st.selectbox("Select length conversion type", 
                               ["Meters to Feet", "Feet to Meters", "Kilometers to Miles", 
                                "Miles to Kilometers", "Meters to Kilometers", "Kilometers to Meters"])
    if length_type == "Meters to Feet":
        converted_value = value * 3.28084
        st.write(f"{value} meters is equal to {converted_value:.2f} feet.")
    elif length_type == "Feet to Meters":
        converted_value = value / 3.28084
        st.write(f"{value} feet is equal to {converted_value:.2f} meters.")
    elif length_type == "Kilometers to Miles":
        converted_value = value * 0.621371
        st.write(f"{value} kilometers is equal to {converted_value:.2f} miles.")
    elif length_type == "Miles to Kilometers":
        converted_value = value / 0.621371
        st.write(f"{value} miles is equal to {converted_value:.2f} kilometers.")
    elif length_type == "Meters to Kilometers":
        converted_value = value / 1000
        st.write(f"{value} meters is equal to {converted_value:.2f} kilometers.")
    elif length_type == "Kilometers to Meters":
        converted_value = value * 1000
        st.write(f"{value} kilometers is equal to {converted_value:.2f} meters.")

# Weight conversions
elif conversion_type == "Weight":
    weight_type = st.selectbox("Select weight conversion type", ["Kilograms to Pounds", "Pounds to Kilograms"])
    if weight_type == "Kilograms to Pounds":
        converted_value = value * 2.20462
        st.write(f"{value} kilograms is equal to {converted_value:.2f} pounds.")
    elif weight_type == "Pounds to Kilograms":
        converted_value = value / 2.20462
        st.write(f"{value} pounds is equal to {converted_value:.2f} kilograms.")

# Temperature conversions
elif conversion_type == "Temperature":
    temp_type = st.selectbox("Select temperature conversion type", 
                              ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"])
    if temp_type == "Celsius to Kelvin":
        converted_value = value + 273.15
        st.write(f"{value} degrees Celsius is equal to {converted_value:.2f} Kelvin.")
    elif temp_type == "Kelvin to Celsius":
        converted_value = value - 273.15
        st.write(f"{value} Kelvin is equal to {converted_value:.2f} degrees Celsius.")
    elif temp_type == "Celsius to Fahrenheit":
        converted_value = (value * 9/5) + 32
        st.write(f"{value} degrees Celsius is equal to {converted_value:.2f} degrees Fahrenheit.")
    elif temp_type == "Fahrenheit to Celsius":
        converted_value = (value - 32) * 5/9
        st.write(f"{value} degrees Fahrenheit is equal to {converted_value:.2f} degrees Celsius.")

# Default fallback if no valid option is selected
else:
    st.write("Please select a valid conversion type.")