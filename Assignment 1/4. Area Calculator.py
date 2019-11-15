#############################
#--- 4. Area Calculator  ---#
#############################

print("-- Welcome Radius to Area converter -- \n")

pi = 3.14159265359
radius = float(input(' Please Enter the Radius of a Circle: '))
area = pi * radius * radius
circumference = 2 * pi * radius

print("\n")
print(" Area Of a Circle = %.2f" %area,)
print(" Circumference Of a Circle = %.2f" %circumference)