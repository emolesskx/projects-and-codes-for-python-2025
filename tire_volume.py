import datetime

# Function to calculate the tire volume
def calculate_tire_volume(width, aspect_ratio, diameter):
    # Formula for tire volume (approximated)
    volume = ((width / 1000) ** 2) * aspect_ratio * (diameter + (width / 1000)) * 3.1416
    return volume

# Function to calculate tire weight based on volume and a material density (assumed value)
def calculate_tire_weight(volume):
    # Assume the density of the tire material is approximately 1.1 grams per cubic cm
    density = 1.1  # in g/cm^3
    volume_in_cm3 = volume * 1000  # Converting volume from liters to cubic centimeters
    weight = density * volume_in_cm3  # Weight in grams
    return weight

# Function to validate user input (ensure it's a positive number)
def get_positive_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("The value must be positive.")
            return value
        except ValueError as e:
            print(e)
            continue

# Main program
if __name__ == "__main__":
    # Get input from the user with input validation
    width = get_positive_input("Enter the tire width in millimeters: ")
    aspect_ratio = get_positive_input("Enter the aspect ratio of the tire: ")
    diameter = get_positive_input("Enter the diameter of the wheel in inches: ")
    
    # Calculate the volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)
    
    # Calculate the weight of the tire (optional creative feature)
    weight = calculate_tire_weight(volume)
    
    # Get the current date
    current_date = datetime.datetime.now().date()

    # Open the file for appending and write the data
    try:
        with open("volumes.txt", "a+") as file:  # Open volumes.txt in append mode
            # Check if the file is empty and add a header if necessary
            file.seek(0)
            if file.read(1) == '':
                file.write("Date, Width (mm), Aspect Ratio, Diameter (inches), Volume (L), Weight (grams)\n")

            # Write the tire data to the file
            file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {round(volume, 2)}, {round(weight, 2)}\n")
        
        print("The following data has been appended to volumes.txt:")
        print(f"Date: {current_date}")
        print(f"Width: {width} mm")
        print(f"Aspect Ratio: {aspect_ratio}")
        print(f"Diameter: {diameter} inches")
        print(f"Volume: {round(volume, 2)} L")
        print(f"Weight: {round(weight, 2)} grams")
    except Exception as e:
        print(f"An error occurred: {e}")
