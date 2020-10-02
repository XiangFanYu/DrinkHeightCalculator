#makes me thirsty, but I ain't a firsty
import math

print("Boba Tower Time")

#height and whatever math
print("How tall are you in feet and inches?")

feet = int(input("Feet?"))
inches = int(input("Inches?"))

totalHeight = (feet * 12) + inches

cups = totalHeight/7.6

numCups = math.ceil(cups)

oz = numCups * 17

numCups = str(numCups)
ounces = str(oz)
print("You need to drink " + numCups + " cups of boba to reach your height")
print("That is about " + ounces + " ounces of boba")
