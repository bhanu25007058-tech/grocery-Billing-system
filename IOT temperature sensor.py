import random
import time

min_temp = float(input("Enter minimum temperature limit: "))
max_temp = float(input("Enter maximum temperature limit: "))

reading = 1
while reading <= 5:
    temp = random.randint(0, 100)
    print("Current temperature:", temp)

    if temp > max_temp:
        print("Alert: Temperature is too high")
    elif temp < min_temp:
        print("Alert: Temperature is too low")
    else:
        print("Temperature is within acceptable limit")

    print()
    time.sleep(2)
    reading = reading + 1
