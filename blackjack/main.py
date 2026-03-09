import random
import os

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Takes a list of cards and returns the score.
    Returns 0 if there is a blackjack (ace + 10).
    Replaces ace (11) with 1 if the total score exceeds 21.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 represents a blackjack

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    """Compares scores and returns the result as a string."""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😁"
    else:
        return "You lose 😤"

def play_game():
    os.system("cls" if os.name == "nt" else "clear")
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                  
      `------'                           |__/            
    """)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal 2 cards to each
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_deal = input("Type 'y' to get another card, 'n' to pass: ").strip().lower()
            if should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer draws until score is at least 17
    while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    final_user_score = calculate_score(user_cards)
    final_computer_score = calculate_score(computer_cards)

    print(f"\n   Your final hand: {user_cards}, final score: {final_user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {final_computer_score}")
    print(compare(final_user_score, final_computer_score))


while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower() == 'y':
    play_game()
