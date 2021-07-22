"""
This is a program about to finding roots of a quadratic equation. A
quadratic equation like as 'ax^2 + bx + c =0' where 'a','b','c' are
some arbitary constant values. The roots could be real or complex value.
This program could calculate this roots"""


#Taking the values of a,b,c
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

#calculating discriminat
discriminat = (b**2) - (4*a*c)

#determiniing and calculating roots
if discriminat == 0:
    print("Roots are real and equal!")
    x = (-b)/(2*a)
    print("Root will be {}".format(x))
elif discriminat > 0:
    print("Roots are real and unequal!")
    x1 = (-b+(discriminat**0.5))/(2*a)
    x2 = (-b-(discriminat**0.5))/(2*a)
    print("First root will be {}".format(x1))
    print("second root will be {}".format(x2))
elif discriminat < 0:
    print("Roots are complex and conjugate!")
    x1 = (-b+(discriminat**0.5))/(2*a)
    x2 = (-b-(discriminat**0.5))/(2*a)
    print("First root will be {}".format(x1))
    print("second root will be {}".format(x2))
else:
    print("invaild input")