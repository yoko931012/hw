r = float(input("Please input a Richter scale value:"))
energy_joules = 10**(1.5*r+4.8)
tons_of_tnt = energy_joules/4.184*(10**9)
nutritious_lunches = energy_joules/2930200

print("Richter scale value:",r)
print("Equivalence in Joules:",energy_joules)
print("Equivalence in tons of TNT: ",tons_of_tnt)
print("Equivalence in the number of nutritious lunches:",nutritious_lunches)


