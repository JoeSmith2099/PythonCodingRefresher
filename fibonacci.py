#This program takes an integer up to 30 and prints out that amount of numbers in the fibonacci sequnce.
#I want to make it so it can print out any amount of numbers in the sequence, next.
n = int(input("How many numbers in the fibonacci sequence do you want? Don't exceed 30. "))

fibonacci_list=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,144,233,377,610,987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]

if n < 31:
  print("This program will print out the first " + str(n) + " numbers of the fibonacci sequence.")
  for i in range(0,n):
    print (fibonacci_list[i])
else:
  print("Don't exceed 30. ")