import random

def deal_Cards():
    """This method is returns a card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def compare(users_score, computer_score):
    if users_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, computer has blackjack"
    elif users_score == 0:
        return "You win! you have blackjack"
    elif users_score > 21:
        return "You went over!"
    elif computer_score > 21:
        return "The computer went over!"
    elif users_score > computer_score:
        return "You win!"
    else:
        return "You lose"

def Calculate_Cards(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

user_cards = []
computer_cards = []
is_game_over = False
for _ in range(2):
    user_cards.append(deal_Cards())
    computer_cards.append(deal_Cards())

while not is_game_over:


    user_Score = Calculate_Cards(user_cards)
    computer_score = Calculate_Cards(computer_cards)

    print(f" Your cards: {user_cards} Your score: {user_Score}")
    print(f" computer first card: {computer_cards[0]}")



    if user_Score == 0 or computer_score == 0 or user_Score > 21:
        is_game_over = True
    else:
        should_deal = input("Type 'Y' to get another card and type 'N' to pass").lower()
        if should_deal == "y":
            user_cards.append(deal_Cards())
        else:
            is_game_over = True


while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_Cards())
    computer_score = Calculate_Cards(computer_cards)

print(f"your final hand: {user_cards}, your final score: {user_Score}")
print(f"Computer final hand: {computer_cards}, computer final score: {computer_score}")

print(compare(user_Score, computer_score))