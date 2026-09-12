#Write a program to calculate the total cost of painting. The interior of building with four
#equal sized walls.

total_height = float(input("Enter the height of the walls (in meters): "))
total_width = float(input("Enter the width of the walls (in meters): "))
paint_cost_per_square_meter = float(input("Enter the cost of paint per square meter: "))

# Calculate the total area of the walls
total_area = 4 * total_height * total_width

# Calculate the total cost of painting
total_cost = total_area * paint_cost_per_square_meter

print(f"The total cost of painting is: ${total_cost:.2f}")