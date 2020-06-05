print(12 + 78)
print(12 // 5)
## Boolean operators
## difference from R
## in R, TRUE and FALSE
print(True)
print(False)

#more operators

print(5 == 23)
print(12 == (3 * 4))

print(12 == "12")
print("Heaps good" == "Heaps good")
print("" == "")
print(6 == 6.0) #
print(None)
print( 6 == None)
print(True == False)
print(True == True)
print(True != False)
print(12 != "12")

print(2 << 1) #follow up later
print( 4 < 8 < 12 < 120)

#type operator

print(type(12.09))
print(type(12))
print(type(True))
print(type("foo"))
print(type([1,2,3]))
print(type([]))
#complex number

complex(1, 2)

#int float and str

print(int(3.14))
print(round(3.14))
print(int("34"))
print(int("34.66")) #ERROR
print(float("34.66")) #works
print(str(3.14))

#variable assignment
a, b = 3, 4
print(b, a)

#augumented assignment operator
mynum = 5
mynum += 5
print(mynum)
mynum = 25
mynum /= 5
print(mynum)

#input
first_name = input("Enter your name: ")
print(first_name)

#exceptions
print("4" + 6)
print(6 + "4")
int("text")

float(print)
int("3 pidgeons")
print(adf)

def output_text():
  print("this is some text.")
  print(3.1415926536)
  
output_text()

def convert_to_currency(x = 0):
    return("$" + str(int(x)))
    
convert_to_currency(12)
convert_to_currency("12")
convert_to_currency()

type(None) #NoneType

def word_multiplier(word: str, times: int) -> str: 
  return(word * times)
  
print(word_multiplier("three", 4))
print(word_multiplier(12, 4))
print(word_multiplier("12", 4))

print(len("2" * 8))
print("length"[1])
print("length"[-1])
print("This is some long text."[13:22])
print("This is some long text."[13:-1])
print("This is some long text."[13:])
print("This is some long text."[8:])
print("This is some long text."[:7])
print("This is some long text."[:])
print("motorcycle"[2:6])
print("retrograde"[8:])
print("santacon"[5:15])
print("hippocampus"[5:])
# print("\n")
print("sanitarium"[-8:-5])
print("genius"[:4])

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(len(alphabet))
print(alphabet[0:10:2])
print(alphabet[0:26:2])
print(alphabet[:26:3])
print(alphabet[::3])
print(alphabet[::-1])
file_name = r"x:\news\travel"
print(file_name)
print(alphabet,
  alphabet[::-1])

print("nop" in alphabet)
print("nop" not in alphabet)

#methods
print(alphabet.find("n"))
print(alphabet.find("n", 20))
print(alphabet.capitalize())

print(alphabet.index("c"))
print(alphabet.index("DD"))
print(alphabet.casefold())


quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')
print("Substring 'let it':", result)

result = quote.rfind('small')
print("Substring 'small ':", result)

result = quote.rfind('be,')
if  (result != -1):
  print("Highest index where 'be,' occurs:", result)
else:
  print("Doesn't contain substring")
  
my_text = "Wikipedia is a free online encyclopedia, \
created and edited by volunteers around the world and \
hosted by the Wikimedia Foundation."
print(my_text)
print(my_text.rfind("and"))
print(my_text.find("and"))
print(my_text.rfind("W"))
print(my_text.rfind("a"))

print(my_text.startswith("Wikipedia"))
print(my_text.endswith("."))

print(my_text.count("the"))

print(my_text.title())
print(my_text.upper())
print(my_text.lower())
print(my_text.swapcase())
print("MOUNT EVEREST".title().swapcase())

print(my_text.islower())
print("MOUNT EVEREST 8484".isupper())
print("MOUNT EVEREST 8484".istitle())
print("MOUNT EVEREST 8484".isalpha())
print("MOUNT EVEREST 8484".isnumeric())
print("8484m".isalnum())
print(" ".isspace())
print("8484".isnumeric())

text_with_space = " adsfasd     fadsfads "
print(len(text_with_space)) 
print(text_with_space.rstrip()) #remove from one side only
print(len(text_with_space.rstrip()))
print(len(text_with_space.lstrip()))
print(len(text_with_space.strip())) #both side

phone_number = "+977 190 9767 987"
print(phone_number.replace(" ", "--"))
#name adj noun
mad_libs = "{} laughted at the {} {}."
print(mad_libs)
print(mad_libs.format("Alex", "silly", "motorcycle"))
print(mad_libs.format("Monica", "tall", "noodle"))
mad_libs = "{1} laughted at the {2} {2}."
print(mad_libs)
print(mad_libs.format("Alex", "silly", "motorcycle"))
print(mad_libs.format("Monica", "tall", "noodle"))
mad_libs = "{name} laughted at the {adjective} {noun}."
print(mad_libs.format(name = "Alex",
  adjective = "silly",
  noun = "motorcycle"))

