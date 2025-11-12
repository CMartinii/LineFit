def linear(m, x, b):
    return (m*x + b)

def slope_units(unit1, unit2):
    slp = unit1.rstrip("s") + "/" + unit2.rstrip("s")
    return slp

def print_equation(m, b, y_units, x_units):
    print("The equation of the line is: y =" , m , slope_units(y_units,x_units) , "x +" , b , y_units)
