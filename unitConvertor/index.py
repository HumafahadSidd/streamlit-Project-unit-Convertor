import streamlit as st

def length_converter(value, from_unit, to_unit):
    # Dictionary of conversion factors to meters
    length_units = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }
    
    # Convert to meters first, then to desired unit
    meters = value * length_units[from_unit]
    result = meters / length_units[to_unit]
    return result

def weight_converter(value, from_unit, to_unit):
    # Dictionary of conversion factors to kilograms
    weight_units = {
        'mg': 0.000001,
        'g': 0.001,
        'kg': 1.0,
        'lb': 0.45359237,
        'oz': 0.028349523125
    }
    
    # Convert to kilograms first, then to desired unit
    kilograms = value * weight_units[from_unit]
    result = kilograms / weight_units[to_unit]
    return result

def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'C' and to_unit == 'F':
        return (value * 9/5) + 32
    elif from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5/9
    elif from_unit == 'C' and to_unit == 'K':
        return value + 273.15
    elif from_unit == 'K' and to_unit == 'C':
        return value - 273.15
    elif from_unit == 'F' and to_unit == 'K':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K' and to_unit == 'F':
        return (value - 273.15) * 9/5 + 32
    else:
        return value

# Streamlit UI
st.title("Unit Converter")

# Conversion type selection
conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Weight", "Temperature"]
)

# Input fields based on conversion type
if conversion_type == "Length":
    length_units = ['mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mi']
    col1, col2 = st.columns(2)
    
    with col1:
        value = st.number_input("Enter Value", value=0.0)
        from_unit = st.selectbox("From Unit", length_units)
    
    with col2:
        to_unit = st.selectbox("To Unit", length_units)
        result = length_converter(value, from_unit, to_unit)
        st.write(f"Result: {result:.4f} {to_unit}")

elif conversion_type == "Weight":
    weight_units = ['mg', 'g', 'kg', 'lb', 'oz']
    col1, col2 = st.columns(2)
    
    with col1:
        value = st.number_input("Enter Value", value=0.0)
        from_unit = st.selectbox("From Unit", weight_units)
    
    with col2:
        to_unit = st.selectbox("To Unit", weight_units)
        result = weight_converter(value, from_unit, to_unit)
        st.write(f"Result: {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    temp_units = ['C', 'F', 'K']
    col1, col2 = st.columns(2)
    
    with col1:
        value = st.number_input("Enter Value", value=0.0)
        from_unit = st.selectbox("From Unit", temp_units)
    
    with col2:
        to_unit = st.selectbox("To Unit", temp_units)
        result = temperature_converter(value, from_unit, to_unit)
        st.write(f"Result: {result:.2f}°{to_unit}")
