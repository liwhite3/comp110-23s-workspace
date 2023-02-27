"""If its raining, tell me to pack an unbrella"""

weather: str = input("What is the weather like? ")

if (weather == "rainy"):
    print("Pack an umbrella!")
    print("But splash in the puddles!")
else:
    if (weather == "snowy"):
        print("Pack a jacket")
    print("You don't need an umbrella!")