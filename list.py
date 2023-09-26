list =[]
total =0

elements = int(input("How many elements do you want in this list? "))

for i in range (0,elements):
  index = int(input("Give me a number. ")) 
  list.append(index)
  
print(list)

for i in list:
  total+=i

print("The sum of all the numbers in the list is " + str(total))

average = (int(total) / len(list))

print("The average of the numbers in the list is " + str(average))
print("The largest number in the list is " + str(max(list)))
print("The smallest number in the list is " + str(min(list)))

