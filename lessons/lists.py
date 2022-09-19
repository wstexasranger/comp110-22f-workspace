"""Examples of using lists."""


from random import  randint

words: list[str] = list("")
rolls: list[int] = list()
rolls.append(1)
rolls.append(3)


# access an individual item
print(rolls[0])

# length of a list
print(len(rolls))
# last item of the list will be len(rolls)-1
while len(rolls) == 0 or rolls[len(rolls)-1] != 1:
    rolls.append(randint(1, 6))
print(rolls)

#remove an item from the list by it's index "pop"
rolls.pop(len(rolls)-1)
print(rolls)
#sum the values of the list
i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1
print(f"Total score: {sum}")