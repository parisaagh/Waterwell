import math

def calculate_gallons(radius_in_inches, depth_in_feet):
     # Convert radius from inches to feet
     radius_in_feet = radius_in_inches / 12
     # Define constant pi   
     pi = 3.1415
     # Calculate the volume of the well casing in cubic feet
     volume_in_cubic_feet = float(pi) * (radius_in_feet ** 2) * depth_in_feet
     # Convert the volume to gallons (1 cubic foot = 7.48 gallons)
     volume_in_gallons = volume_in_cubic_feet * 7.48
     return volume_in_gallons

def main():
     print("This program calculates how much water will be available in a well.")
     radius = float(input("What is the radius of the casing in inches? "))
     depth = float(input("What is the depth of the well in feet? "))
     
     gallons = calculate_gallons(radius, depth)
     
     print(f"The well contains {gallons:.2f} gallons.")
     print("The Program successfully ended.")
     print("Please run the program again to do another calculation.")

if __name__ == "__main__":
     main()