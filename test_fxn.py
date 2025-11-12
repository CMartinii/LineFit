from fitting_functions import *

x = linear(2, 3, 4)
print(x)

units = slope_units("kg", "meters")
print(units)

unit2 = slope_units("meters", "sec")
print(unit2)

print_equation(4, 1, "kg", "meters")
