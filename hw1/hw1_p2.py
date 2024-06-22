# input force, m1, distance
f = int(input("Input the force: "))
m1 = int(input("Input the mass of m1: "))
dis = int(input("Input the distance: "))

#setting the gravity value
g = 6.67 * (10 ** -11)

#calculate m2 and print it out
# m2 = F * r^2 / G / m1
m2 = (f * (dis ** 2)) / (g * m1)
print("The mass of m2 = ", m2)

#setting speed of light
c = 299792458

#calculate Energy of m2 and print it out
e = m2 * (c ** 2)
print("The energy of m2 = ", e)