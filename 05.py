import sys

print(sys.argv)
print(type(sys.argv))

##Debuigng code


#replacing values in list

movies = ["Happy Feet", "Up", "Assignment", "Jaws", "Mary and Max", "Wake in Fright"]
print(movies)
movies[3:5] = ["Gravity", "Red"] #3 & 4 replaced
print(movies)
movies[3:5] = ["300"]
print(movies)
movies[2:4] = ["Shooting star", "The Artist", "Simpsons the Movie", "Endearment"]
print(movies)
movies[2:4] = ["Shooting star", "The Artist", "Simpsons the Movie", "Endearment"]
print(movies)
movies[-3:-1] = ["The Prince", "The Fountainhead"]
print(movies)
movies[2] = "School of Rock"
print(movies)
movies[1:5] = ["Red", "War", "Everest"] #5 is exclusive
print(movies)


#append method
countries = ["Canada", "Australia", "Japan", "Thailand"]
print(countries)
print(len(countries))
countries.append("Vietnam")
print(countries)
print(len(countries))
countries.append("Norway")
print(len(countries))

#building a list from another list
powerball_numbers = [4,8,15,16,23,42]
def squares(numbers):
  squares = [] #blank list to start off with
  for number in numbers:
    squares.append(number ** 2)
  return(squares)
print(squares(powerball_numbers))

def convert_to_floats(numbers):
  floats = []
  for number in numbers:
    floats.append(float(number))
  return(floats)
print(convert_to_floats(powerball_numbers))
print(convert_to_floats([12, 25, 252]))

#even or odd
def even_or_odd(numbers):
  results = []
  for value in numbers:
    if value % 2 == 0:
      results.append(True)
    else:
      results.append(False)
  return(results)
  
print(even_or_odd(powerball_numbers))

# **note** this is not the best way to this in Python

def only_evens(numbers):
  evens = []
  
  for number in numbers:
    if number % 2 == 0:
      evens.append(number)
  return evens
  
print(only_evens([12,45,56,78,77]))

def long_strings(strings):
  results = []
  
  for string in strings:
    if len(string) >= 5:
      results.append(string)
  return results
  
print(long_strings(["apple", "lime","watermelon", "dragon fruit", "kiwi", "pea"]))

#append a list using extend method
mountains = ["Sagarmatha", "K2", "Macchhepucchere", "Dhaulagari", "Kanchenjunga", "Lhotse", "Makalu"]
print(mountains)   
extra_mountains = ["Dhaulagari", "Cho Oyu"]
mountains.extend(extra_mountains)
print(mountains)
mountains.extend([])
print(mountains)
mountains = ["Sagarmatha", "K2", "Macchhepucchere", "Dhaulagari", "Kanchenjunga", "Lhotse", "Makalu"]
extra_mountains = ["Dhaulagari", "Cho Oyu"]
new_mountains =  mountains + extra_mountains
print(new_mountains)
 
plays = ["Hamlet", "Macbeth", "King Lear"]
print(plays)
#insert, NOT override
plays.insert(1, "Julius Ceasar")
print(plays)
plays.insert(0, "Romeo & Juliet")
print(plays)


