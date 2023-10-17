from z3 import *

"""
First Puzzle: Houses
"""

print("------------"
      "First Puzzle"
      "------------")

# Variables for house colours
Yellow, Blue, Red, Ivory, Green = Ints(
    'Yellow Blue Red Ivory Green'
)
# Variables for nationalities
Norwegian, Ukrainian, Englishman, Spaniard, Japanese = Ints(
    'Norwegian Ukrainian Englishman Spaniard Japanese'
)
# Variables for drinks
Water, Tea, Milk, OrangeJuice, Coffee = Ints(
    'Water Tea Milk OrangeJuice Coffee'
)
# Variables for sweets
BarOnes, KitKats, KrispyKremes, ThinMints, MMs = Ints(
    'BarOnes KitsKats KrispyKremes ThinMints MMs'
)
# Variables for pets
Fox, Horse, Snails, Dog, Crocodile = Ints(
    'Fox Horse Snails Dog Crocodile'
)

# Create the Z3 solver
s = Solver()

# House colours are distinct
s.add(Distinct(Yellow, Blue, Red, Ivory, Green))
# Nationalities are distinct
s.add(Distinct(Norwegian, Ukrainian, Englishman, Spaniard, Japanese))
# Drinks are distinct
s.add(Distinct(Water, Tea, Milk, OrangeJuice, Coffee))
# Sweets are distinct
s.add(Distinct(BarOnes, KitKats, KrispyKremes, ThinMints, MMs))
# Pets are distinct
s.add(Distinct(Fox, Horse, Snails, Dog, Crocodile))

# Constrain all variables to be between 0 and 4, both inclusive
variables = [Yellow, Blue, Red, Ivory, Green,
             Norwegian, Ukrainian, Englishman, Spaniard, Japanese,
             Water, Tea, Milk, OrangeJuice, Coffee,
             BarOnes, KitKats, KrispyKremes, ThinMints, MMs,
             Fox, Horse, Snails, Dog, Crocodile]
for var in variables:
    s.add(0 <= var, var <= 4)

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
print(r)
if r == unsat:
    exit(0)
m = s.model()

# Print the solution
print(m)

"""
Second Puzzle: Ships
"""

print("-------------"
      "Second Puzzle"
      "-------------")

# Variables for nationalities
French, Greek, Brazilian, English, Spanish = Ints(
    'French Greek Brazilian English Spanish'
)
# Variables for departure times
Five, Six, Seven, Eight, Nine = Ints(
    'Five Six Seven Eight Nine'
)
# Variables for exterior colours
Blue, Black, Red, Green, White = Ints(
    'Blue Black Red Green White'
)
# Variables for cargo
Tea, Coffee, Cocoa, Rice, Corn = Ints(
    'Tea Coffee Cocoa Rice Corn'
)
# Variables for destinations
PortSaid, Marseille, Manila, Genoa, Hamburg = Ints(
    'PortSaid Marseille Manila Genoa Hamburg'
)

# Create the Z3 solver
s = Solver()

# Nationalities are distinct
s.add(Distinct(French, Greek, Brazilian, English, Spanish))
# Departure time are distinct
s.add(Distinct(Five, Six, Seven, Eight, Nine))
# Exterior colours are distinct
s.add(Distinct(Blue, Black, Red, Green, White))
# Cargoes are distinct
s.add(Distinct(Tea, Coffee, Cocoa, Rice, Corn))
# Destinations are distinct
s.add(Distinct(PortSaid, Marseille, Manila, Genoa, Hamburg))

# Constrain all variables to be between 0 and 4, both inclusive
variables = [French, Greek, Brazilian, English, Spanish,
             Five, Six, Seven, Eight, Nine,
             Blue, Black, Red, Green, White,
             Tea, Coffee, Cocoa, Rice, Corn,
             PortSaid, Marseille, Manila, Genoa, Hamburg]
for var in variables:
    s.add(0 <= var, var <= 4)

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
print(r)
if r == unsat:
    exit(0)
m = s.model()

# Print the solution
print(m)
