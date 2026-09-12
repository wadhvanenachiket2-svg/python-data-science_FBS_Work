##Convert distant given in feet and inches into meter and centimeter.
feet=int(input("Enter distance in feet:"))
inches=int(input("Enter distance in inches:"))

total_inches=feet*12+inches
total_centimeters=total_inches*2.54
total_meters=total_centimeters/100

print("Distance in meters:",total_meters)
print("Distance in centimeteres:",total_centimeters)
