"""Demonstration of dictionaries."""


# Declare the type of a dictionarys
schools: dict[str, int]

# initialize to an empty dictionary
schools = dict()

# Set a key value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_000

# Print a dictionary literal representation
print(schools)

# Access a value by its key (aka Look up)
print(f"UNC has {schools['UNC']} students") 
#Note the use of single quotes to enable the fstring to 
# run properly, no nesting of quotes allowed

# How to remove a key value pair from a dictionary by its key
schools.pop("Duke")
print(schools)

# Test for the existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools.")
else:
    print("No instances of 'Duke' in schools")

# Update/reassign  a key value pair
schools["UNC"] = 20_000
schools["NCSU"] += 900

# Demonstration of dictionary literals
schools = {} # same as dict()

# Alternatively, initialize key value pairs
schools = {"UNC": 19999, "Duke": 16777, "NCSU": 29000}
print(schools)

# What happens when a key does not exist?
#print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")