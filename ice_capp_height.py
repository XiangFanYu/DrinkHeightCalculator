
import math

print("Iced Capp Weight Calculator")

#ask the user if they prefer metric or imperial

#for imperial, calculate pounds and ounces
if(input("Press [m] for metric and [i] for imperial: ") == "i"):
    weight = int(input("How much do you weight in pounds (lbs)? "))

    ozWeight = weight*16

    cups = ozWeight/22

    numCups = str(math.ceil(cups))

    print("You need to weigh the equivalent of " + numCups + " large Iced Capps.")

#for metric, calculate kg and mL
else:
    weight = int(input("How much do you weight in kilograms (kg)? "))

    mlWeight = weight*1000

    cups = mlWeight/648

    numCups = str(math.ceil(cups))

    print("You need to weigh the equivalent of " + numCups + " large Iced Capps.")
