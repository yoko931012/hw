#input height of ball 1
h_b1 = int(input("Input the height of the 1st ball: "))

#input mass of ball 1
m_b1 = int(input("Input the mass of the 1st ball: "))

#input mass of ball 2
m_b2 = int(input("Input the mass of the 2nd ball: "))

#potential Energy(U) of ball 1
u = m_b1 * 9.8 * h_b1

#calculate velocity of ball1 after slide
v1_square = u * 2 / m_b1
v1 = v1_square ** (1/2)
print("The velocity of the 1st ball after slide: ", v1, " m/s")

#calculate velocity of ball 2 after collide
v2_square = u * 2 / m_b2
v2 = v2_square ** (1/2)
print("The velocity of the 2nd ball after collision: ", v2, " m/s")