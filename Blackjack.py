import Art as Art
import random


print(Art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


your_deck = []
computer_deck = []
draw_card = True
computer_draw_card = True

counter = True
counter_2 = 0
game_on = True
game_just_end = False
if input("Do you want to play Blackjack? 'y' or 'n' ") == "n":
    counter = False

while counter:
    while game_on:
        if draw_card:
            random_value = random.choice(cards)
            if random_value == 11:
                if input("You got an ace. Do you want to use it as 1 or 11? ") == "1":
                    your_deck.append(1)
                else:
                    your_deck.append(random_value)
            else:
                print(f"You got a {random_value}.")
                your_deck.append(random_value)
            print(your_deck)

        if computer_draw_card:
            random_value = random.choice(cards)
            computer_deck.append(random_value)

        if counter_2 == 0:
            print(f"The computer got a {computer_deck}.")
            counter_2 += 1
        if draw_card:
            if input("Do you want to draw another card? 'y' or 'n' ") != "y":
                if not computer_draw_card:
                    game_just_end = True
                    game_on = False
                draw_card = False
        if not draw_card:
            if not computer_draw_card:
                game_just_end = True
                game_on = False

        if sum(computer_deck) > 16:
            computer_draw_card = False

    if sum(your_deck) > 21:
        print(f"Your total is {sum(your_deck)}.")
        print(f"The computer's total is {sum(computer_deck)}.")
        if sum(your_deck) > sum(computer_deck):
            print("You lose\n\n\n")
        elif sum(your_deck) < sum(computer_deck):
            print("You win\n\n\n")
        else:
            print("Draw")
    elif sum(your_deck) <= 21:
        print(f"Your total is {sum(your_deck)}.")
        print(f"The computer's total is {sum(computer_deck)}.")
        if sum(your_deck) < sum(computer_deck) < 21:
            print("You lose\n\n")
        elif sum(your_deck) < sum(computer_deck):
            print("You Win!\n\n")
        elif sum(your_deck) > sum(computer_deck):
            print("You Win!\n\n")
        else:
            print("Draw\n\n")
    if input("Do you want to play Blackjack? 'y' or 'n' ") == 'n':
        counter = False

    counter_2 = 0
    game_on = True
    game_just_end = False
    your_deck = []
    computer_deck = []
    computer_draw_card = True
    draw_card = True

print("Goodbye")
