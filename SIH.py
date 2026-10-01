#import random

#number = random.randint(1, 100)

#print(" Number Guessing Game")
#print("I have selected a number between 1 and 100.")

#while True:
 #   guess = int(input("Enter your guess: "))

    #if guess < number:
       # print("Too low! Try again.")
    #elif guess > number:
        #print("Too high! Try again.")
    #else:
      #  print(" Congratulations! You guessed the correct number.")
       # break
       
       # Simple Calculator

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")