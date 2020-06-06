"literal"
''
text = ""
foo = "bar"
ttt = 4.56
mlt = """
To be or not to be.
This is a multiline text.
Last line.
"""

print(mlt)

print(3 + 5)
print("3 + 5")
print("3" + "5") #concat
print(foo, text, ttt, mlt)
print("One", "Two", "Three", "Four")
print(5 - 3, 200- 356)
print(5 - 3, 200- 356, "Text")
print(5 - 3, 200- 356, "Text", sep = "<>")
print(5 - 3, 200- 356, "Text", sep = "", end="\n\n\n")
print(5 - 3, 200- 356, "Text", sep = "*-*-*-*", end="*-*-*-*\n")
print(end="%")

print("this" * 12)
print("this" + 12)
print(10 + 3.14)
print(3.14**2)
#PEMDAS
print(3 + 5 * 12)
print(5 / 2)
print(5 // 2) #floor division
print(-5 // 2)
print(14 % 3) #remainder, modulo
print(2 % 3)
print(2 % 2)
print(22 % 1)
print(22 // 7)

print(True)
print(False)
