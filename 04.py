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


##iteration with conditional logic
values = [2, 6, 7, 8, 9, 12, 12, 15]
other_values = [4, 56, 78, 12, 5, 67]
def odds_sum(numbers):
  total = 0
  for number in numbers:
    if number % 2 == 1:
      total += number
  return(total)
  
  
print(odds_sum(values))
print(odds_sum(other_values))

##iterate over a list in reverse
bluey_family = ["mom", "dad", "bingo", "bluey"]
for character in bluey_family[::-1]:
  print(f"{character} has a total of {len(character)} characters.")

print(bluey_family)
print(bluey_family[::-1])
print(reversed(bluey_family))
print(type(reversed(bluey_family)))
# alternative way
for character in reversed(bluey_family):
  print(f"{character} has a total of {len(character)} characters.")


##
errands = ["gym", "lunch", "sleep", "jog"]
print(enumerate(errands))

for index, task in enumerate(errands):
  print(f"{task} is number {index + 1} on my list of things to do!")

## range function, returns a range object
range(5)

for number in range(11):
  print(number) #0-4
for number in range(-5, 11):
  print(number) #0-4
for number in range(-5, 100, 15):
  print(number) #0-4

#break keyword

print(3 in [0,1,2,3,4,5])

def contains(values, target):
  found = False
  for value in values:
    print(value)
    if value == target:
      found = True
      break
  return found

print(contains([0,1,2,3,4,5], 2))
print(contains(bluey_family, "dad"))

#continue keyword


      
