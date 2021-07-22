side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

half_perimeter = (side1+side2+side3)/2

area = (half_perimeter*(half_perimeter-side1)*(half_perimeter-side2)*(half_perimeter-side3)) ** 0.5
print("Area of the circle: {}".format(area))