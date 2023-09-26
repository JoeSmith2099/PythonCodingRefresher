#This program takes a string and reverses it to check if it is a palindrome,
#meaning it is the same word spelled forwards and backwards.

string = str(input("Give me a word. "))

print("Let's see if " + string + " is a palnindrome.")

reverseString = ""

for i in string:
  reverseString = i + reverseString

if reverseString == string:
  print("Since " + string + " backwards is " + reverseString +
        ", we know that " + string + " is a palindrome.")
else:
  print("Since " + string + " backwards is " + reverseString + ", " + string + " isn't a palindrome and I don't like it.")
