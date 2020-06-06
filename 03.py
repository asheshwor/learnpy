#section 8
#control flow

if 5 > 3:
  print("greater than")
  print("one more line")
  
if -1 > 3:
  print("greater than")
  print("one more line")
  
if -1:
  print("some text")
if None:
  print("some text")
  
print(bool(-3))
print(bool(0))
print(bool(""))
print(bool(None))


if (23 > 29):
  print("some text")
else:
  print("other text")

def positive_or_negative(number):
  if number > 0:
    return "positive"
  elif number < 0:
    return "negative"
  else:
    return "zero"
    
positive_or_negative(12)
positive_or_negative(0)
positive_or_negative(-3.2)

zip_code = "96848"
#check
if (len(zip_code) == 5):
  check = "valid"
else:
    check = "invalid"
print(check)
check2 = "valid" if len(zip_code) == 5 else "invalid"
print(check2)

if len(zip_code) == 5 and bool(2):
  check = "valid"
else:
  check = "invalid"
print(check)

value = 95
if value > 90 and value < 100:
  print("yes")
else:
  print("no")
if 90 < value < 100:
  print("yes")
else:
  print("no")

#and or not
print(not True)

count = 0

while count <= 5:
 print(count)
 count += 1

invalid_number = True

while invalid_number:
  user_value = int(input("please enter a number greater than 100: "))
  if user_value > 100:
    print(f"That works! {user_value} is greater than 100.")
    invalid_number = False
  else:
    print("That doesn't work!")
    
def count_down_from(number):
  start = int(number)
  while start > 0:
    print(start)
    start -= 1
    
count_down_from(10.2)
#recursion
def count_down_from(number):
  if number <= 0:
    return
  print(int(number))
  count_down_from(number - 1)
