## Assignment 1
#Q1. Find area and perimeter of right angled triangle.(Given: Base and Height taken from the user)
base = float(input("Base: "))
height = float(input("Height: "))
area = 0.5*base*height
hypo = ((base**2)+(height**2))**0.5
peri = base + height + hypo
print("Perimeter is", peri,"cm")
print("Area is", area,"sqcm")


