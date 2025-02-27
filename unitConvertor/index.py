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

def main():
    print("Unit Converter")
    print("\nAvailable conversions:")
    print("1. Length (mm, cm, m, km, in, ft, yd, mi)")
    print("2. Weight (mg, g, kg, lb, oz)")
    print("3. Temperature (C, F, K)")
    
    choice = input("\nEnter conversion type (1/2/3): ")
    
    if choice == '1':
        value = float(input("Enter value: "))
        from_unit = input("Enter source unit: ").lower()
        to_unit = input("Enter target unit: ").lower()
        result = length_converter(value, from_unit, to_unit)
        print(f"\n{value} {from_unit} = {result:.4f} {to_unit}")
    
    elif choice == '2':
        value = float(input("Enter value: "))
        from_unit = input("Enter source unit: ").lower()
        to_unit = input("Enter target unit: ").lower()
        result = weight_converter(value, from_unit, to_unit)
        print(f"\n{value} {from_unit} = {result:.4f} {to_unit}")
    
    elif choice == '3':
        value = float(input("Enter value: "))
        from_unit = input("Enter source unit (C/F/K): ").upper()
        to_unit = input("Enter target unit (C/F/K): ").upper()
        result = temperature_converter(value, from_unit, to_unit)
        print(f"\n{value}°{from_unit} = {result:.2f}°{to_unit}")
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
