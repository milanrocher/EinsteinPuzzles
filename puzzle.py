from z3 import *

"""
First Puzzle: Houses
"""

print("------------"
      "First Puzzle"
      "------------")

# Variables for house colours
Yellow, Blue, Red, Ivory, Green = Ints('Yellow Blue Red Ivory Green')
# Variables for nationalities
Norwegian, Ukrainian, Englishman, Spaniard, Japanese = Ints('Norwegian Ukrainian Englishman Spaniard Japanese')
# Variables for drinks
Water, Tea, Milk, OrangeJuice, Coffee = Ints('Water Tea Milk OrangeJuice Coffee')
# Variables for sweets
BarOnes, KitKats, KrispyKremes, ThinMints, MMs = Ints('BarOnes KitsKats KrispyKremes ThinMints MMs')
# Variables for pets
Fox, Horse, Snails, Dog, Crocodile = Ints('Fox Horse Snails Dog Crocodile')

# Create the Z3 solver
s = Solver()

# House colours are distinct
s.add(Distinct([Yellow, Blue, Red, Ivory, Green]))
# Nationalities are distinct
s.add(Distinct([Norwegian, Ukrainian, Englishman, Spaniard, Japanese]))
# Drinks are distinct
s.add(Distinct([Water, Tea, Milk, OrangeJuice, Coffee]))
# Sweets are distinct
s.add(Distinct([BarOnes, KitKats, KrispyKremes, ThinMints, MMs]))
# Pets are distinct
s.add(Distinct([Fox, Horse, Snails, Dog, Crocodile]))

# Constrain all variables to be between 0 and 4, both inclusive
for colour in [Yellow, Blue, Red, Ivory, Green]:
    s.add(0 <= colour, colour <= 4)
for nationality in [Norwegian, Ukrainian, Englishman, Spaniard, Japanese]:
    s.add(0 <= nationality, nationality <= 4)
for drink in [Water, Tea, Milk, OrangeJuice, Coffee]:
    s.add(0 <= drink, drink <= 4)
for sweet in [BarOnes, KitKats, KrispyKremes, ThinMints, MMs]:
    s.add(0 <= sweet, sweet <= 4)
for pet in [Fox, Horse, Snails, Dog, Crocodile]:
    s.add(0 <= pet, pet <= 4)

# The Englishman lives in the red house.
s.add(Englishman == Red)
# The Spaniard owns the dog.
s.add(Spaniard == Dog)
# Coffee is drunk in the green house.
s.add(Coffee == Green)
# The Ukrainian drinks tea.
s.add(Ukrainian == Tea)
# The green house is immediately to the right of the ivory house.
s.add(Green == Ivory + 1)
# The KrispyKremes eater owns snails.
s.add(KrispyKremes == Snails)
# BarOnes are eaten in the yellow house.
s.add(BarOnes == Yellow)
# Milk is drunk in the middle house.
s.add(Milk == 2)
# The Norwegian lives in the first house.
s.add(Norwegian == 0)
# The man who eats KitKats lives in the house next to the man with the fox.
s.add(Or(KitKats == Fox + 1, KitKats == Fox - 1))
# BarOnes are eaten in the house next to the house where the horse is kept.
s.add(Or(BarOnes == Horse + 1, BarOnes == Horse - 1))
# The ThinMints eater drinks orange juice.
s.add(ThinMints == OrangeJuice)
# The Japanese man eats MMs.
s.add(Japanese == MMs)
# The Norwegian lives next to the blue house.
s.add(Or(Norwegian == Blue + 1, Norwegian == Blue - 1))

# Solve the problem
r = s.check()
if r == unsat:
    exit(0)
else:
    # Print the solution
    colours = {}
    nationalities = {}
    drinks = {}
    sweets = {}
    pets = {}

    m = s.model()
    for d in m.decls():
        idx = m[d].as_long()
        if d.name() in ["Yellow", "Blue", "Red", "Ivory", "Green"]:
            colours[idx] = d.name()
        elif d.name() in ["Norwegian", "Ukrainian", "Englishman", "Spaniard", "Japanese"]:
            nationalities[idx] = d.name()
        elif d.name() in ["Water", "Tea", "Milk", "OrangeJuice", "Coffee"]:
            drinks[idx] = d.name()
        elif d.name() in ["BarOnes", "KitsKats", "KrispyKremes", "ThinMints", "MMs"]:
            sweets[idx] = d.name()
        elif d.name() in ["Fox", "Horse", "Snails", "Dog", "Crocodile"]:
            pets[idx] = d.name()
    for i in range(5):
        print(f"The {nationalities[i]} lives in the {colours[i]} house, eats "
              f"{sweets[i]}, drinks {drinks[i]}, and owns a {pets[i]}.")

"""
Second Puzzle: Ships
"""

print("\n-------------"
      "Second Puzzle"
      "-------------")

# Variables for nationalities
French, Greek, Brazilian, English, Spanish = Ints('French Greek Brazilian English Spanish')
# Variables for departure times
Five, Six, Seven, Eight, Nine = Ints('Five Six Seven Eight Nine')
# Variables for exterior colours
Blue, Black, Red, Green, White = Ints('Blue Black Red Green White')
# Variables for cargo
Tea, Coffee, Cocoa, Rice, Corn = Ints('Tea Coffee Cocoa Rice Corn')
# Variables for destinations
PortSaid, Marseille, Manila, Genoa, Hamburg = Ints('PortSaid Marseille Manila Genoa Hamburg')

# Create the Z3 solver
s = Solver()

# Nationalities are distinct
s.add(Distinct([French, Greek, Brazilian, English, Spanish]))
# Departure time are distinct
s.add(Distinct([Five, Six, Seven, Eight, Nine]))
# Exterior colours are distinct
s.add(Distinct([Blue, Black, Red, Green, White]))
# Cargoes are distinct
s.add(Distinct([Tea, Coffee, Cocoa, Rice, Corn]))
# Destinations are distinct
s.add(Distinct([PortSaid, Marseille, Manila, Genoa, Hamburg]))

# Constrain all variables to be between 0 and 4, both inclusive
for nationality in [French, Greek, Brazilian, English, Spanish]:
    s.add(0 <= nationality, nationality <= 4)
for time in [Five, Six, Seven, Eight, Nine]:
    s.add(0 <= time, time <= 4)
for colour in [Blue, Black, Red, Green, White]:
    s.add(0 <= colour, colour <= 4)
for cargo in [Tea, Coffee, Cocoa, Rice, Corn]:
    s.add(0 <= cargo, cargo <= 4)
for destination in [PortSaid, Marseille, Manila, Genoa, Hamburg]:
    s.add(0 <= destination, destination <= 4)

# The Greek ship leaves at six and carries coffee.
s.add(Greek == Six)
s.add(Greek == Coffee)
# The Ship in the middle has a black exterior.
s.add(Black == 2)
# The English ship leaves at nine.
s.add(English == Nine)
# The French ship with blue exterior is to the left of a ship that carries
# coffee.
s.add(French < Coffee)
s.add(French == Blue)
# To the right of the ship carrying cocoa is a ship going to Marseille.
s.add(Cocoa < Marseille)
# The Brazilian ship is heading for Manila.
s.add(Brazilian == Manila)
# Next to the ship carrying rice is a ship with a green exterior.
s.add(Or(Rice == Green + 1, Rice == Green - 1))
# A ship going to Genoa leaves at five.
s.add(Genoa == Five)
# The Spanish ship leaves at seven and is to the right of the ship going to
# Marseille.
s.add(Spanish == Seven)
s.add(Spanish > Marseille)
# The ship with a red exterior goes to Hamburg.
s.add(Red == Hamburg)
# Next to the ship leaving at seven is a ship with a white exterior.
s.add(Or(White == Seven + 1, White == Seven - 1))
# The ship on the border carries corn.
s.add(Corn == 0 or Corn == 4)
# The ship with a black exterior leaves at eight.
s.add(Black == Eight)
# The ship carrying corn is anchored next to the ship carrying rice.
s.add(Or(Corn == Rice + 1, Corn == Rice - 1))
# The ship to Hamburg leaves at six.
s.add(Hamburg == Six)

# Solve the puzzle
r = s.check()
if r == unsat:
    exit(0)
else:
    # Print the solution
    nationalities = {}
    depart_times = {}
    colours = {}
    cargoes = {}
    destinations = {}

    m = s.model()
    for d in m.decls():
        idx = m[d].as_long()
        if d.name() in ["French", "Greek", "Brazilian", "English", "Spanish"]:
            nationalities[idx] = d.name()
        elif d.name() in ["Five", "Six", "Seven", "Eight", "Nine"]:
            depart_times[idx] = d.name()
        elif d.name() in ["Blue", "Black", "Red", "Green", "White"]:
            colours[idx] = d.name()
        elif d.name() in ["Tea", "Coffee", "Cocoa", "Rice", "Corn"]:
            cargoes[idx] = d.name()
        elif d.name() in ["PortSaid", "Marseille", "Manila", "Genoa", "Hamburg"]:
            destinations[idx] = d.name()
    for i in range(5):
        print(f"The {colours[i]} {nationalities[i]} ship leaves at "
              f"{depart_times[i]}, carrying {cargoes[i]} to {destinations[i]}.")
