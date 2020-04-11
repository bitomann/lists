# Instructions

planet_list = ["Mercury", "Mars"]

# Use append() to add Jupiter and Saturn at the end of the list.
# vvv Append takes only one argument vvv
# planet_list.append("Jupiter")
# planet_list.append("Saturn")

# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
# vvv Extend takes a list (array in JS) vvv
planet_list.extend(["Jupiter", "Saturn"])


# Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")


# Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")
print(planet_list)


# Now that all the planets are in the list, slice the list in order 
# to get the rocky planets into a new list called rocky_planets.
rocky_planets = planet_list[0:4]
print(rocky_planets)


# Being good amateur astronomers, we know that Pluto is now a dwarf planet, 
# so use the del operation to remove it from the end of planet_list.
del planet_list[6]
print(planet_list)

# ***You can change (mutable) LISTS*** 
# ***You cannot change (immutable) TUPLES***
