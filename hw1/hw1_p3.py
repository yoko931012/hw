#input the velocity
v = int(input("Input velocity: "))

#calcuate the percent of light speed
c = 299792458
per_of_l = v / c
print("Percentage of light speed = ", per_of_l)

#calculate gumma
tmp = 1 - (per_of_l ** 2)
gumma = 1 / (tmp ** (1/2))

#light year to each planet
al_ce = 4.3     #Alpha Centauri
ba_st = 6.0     #Barnard’s Star
bete = 309      #Betelgeuse
an_ga = 2000000 #Andromeda Galaxy

#travel time to each planet
tt_al_ce = al_ce / gumma
tt_ba_st = ba_st / gumma
tt_bete = bete / gumma
tt_an_ga = an_ga / gumma

#print
print("Travel time to Alpha Centauri = {:.6f}".format(tt_al_ce))
print("Travel time to Barnard's Star = {:.6f}".format(tt_ba_st))
print("Travel time to Betelgeuse (in the Milky Way) = {:.6f}".format(tt_bete))
print("Travel time to Andromeda Galaxy (closest galaxy) = {:.6f}".format(tt_an_ga))

