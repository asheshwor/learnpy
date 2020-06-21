#section 9

#list

empty = []
empty = list()

languages = ["Python", "R", "JavaScript", "LISP", "S", "C", "BASIC", "COBOL", "Scratch"]

print(len(languages))

print(languages[0:3])

meals = ["breakfast", "lunch", "dinner"]
print("lunch" in meals)
print("snack" not in meals)
print(meals[2])
# print(meals[4]) #this throws error
print(meals[0][-1]) #last character from first element in the list.
print(meals[-2])

print([1, 2] in [1, 2, 3])

## INDEXING INTO LIST

## SLICING MULTIPLE ELEMENTS FROM A LIST
print("reticulate"[2:5])
cities = ["London", "New York", "Sydney", "Tokyo", "Shanghai", "Bern", "Cape Town"]
print(cities[2:5])
print(cities[3:])
print(cities[:3])
print(cities[4:200])
print(cities[-4:-2])
print(cities[:-2]) #remove last two
print(cities[2:-2])
print(cities[::-2])
print(cities[::2])

#iteration

food = "glorius fries"

for character in food:
  print(character)

numbers = [2, 4,5,1,7]

for number in numbers:
  print(number ** 2)

print(number) #last value

total = 0
for number in numbers:
  total = total + number
  
print(total)

def sum_of_lengths(strings):
  total = 0
  
  for string in strings:
    total += len(string)
    
  return total


def product(numbers):
  total = 1
  
  for number in numbers:
    total *= number
    
  return total

product([1,2,4,5])
