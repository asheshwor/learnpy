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

