hand = []

while True:
    card = eval(input("Please enter a card value: "))

    hand.append(card)

    if sum(hand) >= 21 or len(hand) == 3:
        break

print("Your final hand is:", hand, "\nIts value is: ", sum(hand))

if sum(hand) > 21:
    print("Too high!")
elif sum(hand) == 21:
    print("Good!")
else:
    print("Not bad!")
