#This program takes an integer and prints out that amount of numbers in the fibonacci sequnce.
#THe first two numbers in the sequnce are hardcoded and I can't figure out what's going on wrong.
n = int(input("How many numbers in the fibonacci sequence do you want?  "))

last_num =0
current_num=1

print(last_num)
print(current_num)
for i in range (0,n):
  sum = last_num + current_num
  last_num = current_num
  current_num = sum
  print(sum)



print("This program will print out the first " + str(n) + " numbers of the fibonacci sequence.")
