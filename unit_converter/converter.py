class temperature_c():
    def celsius(num):
        result = (num * 9/5) + 32
        return result

    def fahrenheit(num):
        result = (num - 32) * 5/9
        return result

class length_c():
    def cm_to_inch(num):
        result = num / 2.54
        return result

    def m_to_feet(num):
        result = num * 3.28
        return result

class weight_c():
    def kg_to_pound(num):
        result = num * 2.2046
        return result

    def pound_to_kg(num):  
        result = num / 2.2046
        return result


def show_menu():
    print("-" * 30)
    print("Temperature conversion => 1")
    print("Length conversion => 2")
    print("Weight conversion => 3")
    print("Exit => 4")

    try:
        num = int(input("Enter the change you want: "))
        if 1 <= num <= 4:
            return num
        else:
            print("Choose a number from 1 to 4")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None


def temperature_converter():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = input("Choose (1/2): ")
        value = float(input("Enter value: "))

        if choice == "1":
            result = temperature_c.celsius(value)
            print(f"{value}°C = {result:.2f}°F")
        elif choice == "2":
            result = temperature_c.fahrenheit(value)
            print(f"{value}°F = {result:.2f}°C")
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")


def length_converter():
    print("\nLength Conversion:")
    print("1. cm to inch")
    print("2. m to feet")

    try:
        choice = input("Choose (1/2): ")
        value = float(input("Enter value: "))

        if choice == "1":
            result = length_c.cm_to_inch(value)
            print(f"{value} cm = {result:.2f} inches")
        elif choice == "2":
            result = length_c.m_to_feet(value)
            print(f"{value} m = {result:.2f} feet")
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")


def weight_converter():
    print("\nWeight Conversion:")
    print("1. kg to pound")
    print("2. pound to kg")

    try:
        choice = input("Choose (1/2): ")
        value = float(input("Enter value: "))

        if choice == "1":
            result = weight_c.kg_to_pound(value)
            print(f"{value} kg = {result:.2f} pounds")
        elif choice == "2":
            result = weight_c.pound_to_kg(value)
            print(f"{value} pounds = {result:.2f} kg")
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")



print("Welcome to converter!")

while True:
    choice = show_menu()

    if choice == 1:
        temperature_converter()
    elif choice == 2:
        length_converter()
    elif choice == 3:
        weight_converter()
    elif choice == 4:
        print("Goodbye!")
        break
    elif choice is None:
        continue
