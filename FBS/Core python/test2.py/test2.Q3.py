#A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
#for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
#length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
#cost of fencing the field.

import math

# Calculate the perimeter of the circular section (half circle)
radius = 20
circular_perimeter = math.pi * radius

# Calculate the perimeter of the rectangular section
length = 50
breadth = 40
rectangular_perimeter = 2 * (length + breadth)

# Total perimeter of the field
total_perimeter = circular_perimeter + rectangular_perimeter

# Total length of barbed wire needed (5 times)
total_wire_length = 5 * total_perimeter

# Cost of barbed wire per meter
cost_per_meter = 35

# Total cost of fencing
total_cost = total_wire_length * cost_per_meter

print("Total cost of fencing the field:", total_cost, "Rs")