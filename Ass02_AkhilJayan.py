## Assignment 2
#Q1. Find the coulomb force between Q1 and Q2 which are "r" distance apart
q1 = float(input("Charge 1: "))
q2 = float(input("Charge 2: "))
r = float(input("Distance between them: "))
f = (9*(10**9)*q1*q2)/(r**2)
print("Force between the two charges is", f,"N")
