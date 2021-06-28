# Empty line
print()
# Double quotations
print("Hello, World ! ")
# Single quotations
print(':D')
# Use "" for '
print("Don't")
# Variables
w = "worry"
a = 'about'
ap = "apostrophes"
print(w)
print(a)
print(ap)
# Multi-Line Strings can be """x""" or '''x''' -- indents count
lorem = """Lorem ipsum dolor sit amet,
	consectetur adipiscing elit,
		sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(lorem)
print()

# Variables
four = 4
five = 5

six = '6'	# Not an int, is str
seven = "7"	# Not an int, is str

oneJ, twoJ = 1j, 2j

byteHi = b"Hi"
byteA4 = bytearray(4)
mvb2 = memoryview(bytes(2))

print(five)
print(six)
print(seven)

print(four * 2)
print(five + four)
print(five - four)
print(five / four)

print(oneJ)
print(twoJ)

print(byteHi)
print(byteA4)
print(mvb2)

t = True
f = False
if five > four:
	print(t)
print()

# Multiple Variables
cats, dogs, rabbits = "Cats", "dogs", "rabbits"
print(cats + ", " + dogs + ", and " + rabbits + " are cute")

_six, _seven = 6, 7
print(_six + _seven)

paper = pa = papers = "Paper"
print(paper + " " + pa + " " + papers)

# Defining Functions
def cute():
	are = " are "
	global bun
	bun = "bunnies"
	print("The cutest animals" + are + bun)
cute()
print(bun)

earth = "Earth"
print(earth)
def world():
	global earth
	earth = "Earth is awesome"
	print(earth)
world()			# Declaring the function -- not declaring = no global earth change
print(earth)	# is now "Earth is awesome" b/c of the global change
print()

# List
animals = ["Hamsters", "Snakes", "Elephants", "Hedgehogs"]
ham, sna, ele, hed = animals
print(ham + " " + sna + " " + hed + " " + ele)
print(animals)
# Tuple
fruits = ("Watermelon", "Apple", "Cherry")
print(fruits)
# Set
veggies = {"Carrots", "Lettuce", "Broccoli"}
print(veggies)
# Frozen Set
colours = frozenset({"Black", "White", "Pink"})
print(colours)
# Dict
details = {"name" : "Dracula", "age" : 100, "life state": "vampire"}
print(details)
# Arrays
arr = "Today is the 28th of June."
print(arr[1])	# o of Today
print(arr[13])	# 2 of 28
print(arr[22])	# u of June
print(len(arr))	# length
print(arr[9:17])	# Prints the characters from 9 to 17 ( not included )
print(arr[:5])		# From Start to 5 ( not included )
print(arr[21:])		# From 21 to end ( not included )
print(arr[-5:-1])	# Start slice from the end of the string
print(arr.upper())	# Uppercase
print(arr.lower())	# lowercase
print(arr.strip())	# Removes whitespace from start or end
print(arr.replace("2", "1"))	# Replaces characters
print(arr.split(" "))	# Splits if there are " " ( spaces )
print("July" in arr)	# Checks if July is in arr
print("May" not in arr)	# Checks if May is NOT in arr
if "June" in arr:		# Checks if June is in arr
	print("June is in the array")
if "April" not in arr:		# Checks if April is NOT in arr
	print("April is not in the array")
# For loop
for b in "banana":
	print(b)
print()

# Casting
wool	= str("Wool")
one		= int(1)
nOne	= int(-1)
twoPT5	= float(2.5)
n2e10	= float(-2.0e10)
r36		= range(3, 6)
threeJ	= complex(3j)
threeP5J= complex(3+5j)
nthreeJ = complex(-3j)
hero	= dict(name = "Batman", city = "Gotham")
veg		= set(("Potato", "Beans", "Corn"))
colour	= frozenset({"Red", "Green", "Blue"})
bool5	= bool(5 < 2)
byte2	= bytes(2)
byteA3	= bytearray(3)
mvb1	= memoryview(bytes(1))

print(wool)
print(one)
print(nOne)
print(twoPT5)
print(n2e10)
print(one + twoPT5)
print(r36)
print(threeJ)
print(threeP5J)
print(nthreeJ)
print(hero)
print(veg)
print(colour)
print(bool5)
print(byte2)
print(byteA3)
print(mvb1)
print()

# Conversions
t2 = 32		# int
e34 = 83.4	# float
fivej = 5j	# complex
flconv = float(t2)		# int to float
inconv = int(e34)		# float to int
coconv = complex(t2)	# int to complex
print(flconv)
print(inconv)
print(coconv)
print(type(flconv))
print(type(inconv))
print(type(coconv))
print()

# type() function for Data Types
print(type(one))		# int(+-#)
print(type(twoPT5))		# float(+-#.#)
print(type(six))		# 'str'
print(type(seven))		# "str"
print(type(w))			# "str"
print(type(a))			# 'str'
print(type(oneJ + twoJ))	# complex numbers
print(type(animals))	# list -- []
print(type(fruits))		# tuple -- ()
print(type(r36))		# range -- (#, #)
print(type(details))	# dict -- {"paired" : "info"}
print(type(veggies))	# set -- {}
print(type(colours))		# frozenset -- ({}) -- unordered
print(type(t))			# bool -- True / False
print(type(byteHi))		# bytes
print(type(byteA4))		# byte array
print(type(mvb2))		# memoryview(bytes(#))
print()
