__author__ = 'Ji-seong Yang, jiyang@live.unc.edu, Onyen = jiyang'

# Import an appropriate module.
import random as rd


# A function to deal a card.
def deal_card():

    # Draw two random cards ranging from 1 to 13 and assign.
    card = rd.randint(1, 13)

    # Reassign the value with Jacks, Queens, and kings mapped to 10.
    if card == 11:
        card = 10
    elif card == 12:
        card = 10
    elif card == 13:
        card = 10

    # Return the value
    return card


# Define a function that handles the initial deal of two cards to the player and the "HIT or STAY" loop.
def get_player_score():

    # Draw two cards
    first_card = deal_card()
    second_card = deal_card()

    # Get the initial player score, which is the sum of the 1st and 2nd card scores.
    player_score = first_card + second_card

    # Print the initial player score and ask the user whether to HIT or STAY.
    print("Your hand of two cards has a total value of ", player_score, ".", sep='')
    hit_or_stay = input("Would you like to take another card? (y/n) ")

    # Draw a new card until the user chooses to STAY and update the player score.
    while hit_or_stay == 'y':
        new_card = deal_card()
        player_score += new_card

        # In the case the player is NOT busted.
        if player_score <= 21:

            # View the current player score and ask whether to HIT or STAY.
            print("Your hand now has a total value of ", player_score, ".", sep='')
            hit_or_stay = input("Would you like to take another card? (y/n) ")

        # In the case the player is busted.
        else:
            hit_or_stay = 'n'
            print("You BUSTED with a total value of ", player_score, "!", sep='')
            print()
            print("** You lose. **")
            print()

    # Return final player score
    return player_score


# Define a function that compares the scores of each party.
def compare_score():

    # Get the dealers's score and compare with the player
    player_score = get_player_score()

    # In the case the player is not busted and chose to STAY.
    if player_score <= 21:

        # View the latest player score after the player chose to STAY.
        print("You have stopped taking more cards with a hand value of ", player_score, ".", sep='')

        # Get the dealer score
        dealer_score = get_dealer_score()

        # In the case of the dealer is busted.
        if dealer_score > 21:
            print("The dealer BUSTED with a value of ", dealer_score, "!", sep='')
            print()
            print("** You win! **")
            print()

        # In the case of the dealer NOT busted.
        else:
            print("The dealer was dealt a hand with a value of ", dealer_score, ".", sep='')

            # Compare the dealer score with player score to determine who wins.
            if dealer_score >= player_score:
                print()
                print("** You lose! **")
                print()
            else:
                print()
                print("** You win! **")
                print()


# Define a function that generate the dealer's score
def get_dealer_score():

    # Draw two cards for the dealer.
    first_card = deal_card()
    second_card = deal_card()

    # Get the score of the dealer.
    dealer_score = first_card + second_card

    # Draw one more card for the dealer if whose score is below 16.
    if dealer_score < 16:
        dealer_score += deal_card()
    return dealer_score


# Define the main function that contains the the main loop.
def main():

    # Get the scores of the player and the dealer and compare them.
    compare_score()

    # Keep repeating the game as long as the player wants to play.
    play_again = input('Would you like to play again? (y/n) ')
    while play_again == 'y':
        compare_score()
        play_again = input('Would you like to play again? (y/n) ')


# Kick off the program!
main()