##Calculate the cost of painting the following building’s walls (both interior and
##exterior). You need to accept area (one wall) and cost of both interior and
##exterior wall.
area = int(input("Enter the area of one wall: "))
interior_cost = float(input("Enter the cost of interior wall painting per unit area: "))
exterior_cost = float(input("Enter the cost of exterior wall painting per unit area: "))
print("Total cost of painting the interior wall:", area * interior_cost)
print("Total cost of painting the exterior wall:", area * exterior_cost)





#Below diagram is of two joint rooms.
#It is upper view of building.
interior_area = int(input("Enter the area of interior walls: "))
exterior_area = int(input("Enter the area of exterior walls: "))
print("Total cost of painting the interior walls:", interior_area * interior_cost)
print("Total cost of painting the exterior walls:", exterior_area * exterior_cost)