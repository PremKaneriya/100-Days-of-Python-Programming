# Tuple operations

# Manipulationg
name = ("piyush", "sanjay", "bhalobashi")
org = list(name)
org.append("mushamushi")
org.pop(2)
org[0] = "hola"
name = tuple(org)
print(name)

vegFood = ("Panner", "rajma", "roti")
nonVegFood = ("chicken", "fish")
both = vegFood + nonVegFood
print(both)

# Tuple Methods
tipks = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tipks.count(3)
print('Count of 3 in Tuple1 is:', res)

tips = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tips.index(3)
print('First occurrence of 3 is', res)