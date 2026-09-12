##Write a program to accept distance in km and convert it into meters and
##centimeters both.
input_distance_km = float(input("Enter distance in kilometers: "))
input_distance_m = input_distance_km * 1000
input_distance_cm = input_distance_km * 100000
print("Distance in meters:", input_distance_m)
print("Distance in centimeters:", input_distance_cm)
