# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function to handle user interaction
def main():
    try:
        # Prompt the user to enter the temperature
        temp_input = input("Enter the temperature to convert: ").strip()

        # Validate if the input is numeric
        if temp_input.replace('.', '', 1).isdigit() or (temp_input.startswith('-') and temp_input[1:].replace('.', '', 1).isdigit()):
            temp = float(temp_input)
        else:
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        # Prompt the user to specify if the temperature is in Celsius or Fahrenheit
        temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform the conversion based on the unit
        if temp_unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")
        elif temp_unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
