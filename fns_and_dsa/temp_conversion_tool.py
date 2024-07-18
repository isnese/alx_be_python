# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion Functions
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# User Interaction
def main():
    try:
        # Prompt user for input
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Validate user input
        if unit not in ['C', 'F']:
            raise ValueError("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
        # Perform conversion based on user input
        if unit == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted_temperature:.1f}°C")
        elif unit == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted_temperature:.1f}°F")
    
    except ValueError as e:
        print(f"Error: {e}. Please enter a numeric value for temperature.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the main function
if __name__ == "__main__":
    main()
