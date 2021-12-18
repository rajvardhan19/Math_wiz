# Question Builder

# List of Numeric Problems

# Importing function
import random
import math

# n stands for number of questions
n = int(input("Please enter the number of questions: "))

# Select the operation: Addition, substraction, ......

a = int(input("Please select the Question type: \n Press 1 for Addition  \n Press 2 for Multiplication  \n Enter your choice here:  " ))
digits = int(input("The operation should be performed on how many numbers: "))

x = 0
while (x < n):
   list = []
   i = 0
   x = x + 1
   while (i < digits):
      r = random.choice(range(11,20000))
      list.append(r)
      if len(list) == digits:
         if a == 1:
           print("Solve:")
           print(*list, sep = " + ")
           print("Answer = ", (sum(list)))
         elif a == 2:
            print("Solve:")
            print(*list, sep = " * ")
            print("Answer = ", math.prod(list)) 
         else:
            print("Operation Invalid!!!")
      i = i + 1
