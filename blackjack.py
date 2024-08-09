import random

PlayAgain = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while PlayAgain:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == 'y':
        player = random.choices(cards, k=2)
        computer = random.choices(cards, k=2)
        
        playerTotalScore = sum(player)
        computerTotalScore = sum(computer)

        print(f"Your cards: {player}, current score: {playerTotalScore}")
        print(f"Computer's first card: {computer[0]}")

        # Player's turn
        while playerTotalScore < 21:
            choice = input("Type 'h' to hit or 's' to stand: ")
            if choice == 'h':
                player.append(random.choice(cards))
                playerTotalScore = sum(player)
                print(f"Your cards: {player}, current score: {playerTotalScore}")
            else:
                break
        
        # Check for player's bust
        if playerTotalScore > 21:
            print("You went over 21! You lose.")
            continue
        
        # Computer's turn
        while computerTotalScore < 17:
            computer.append(random.choice(cards))
            computerTotalScore = sum(computer)
        
        print(f"Computer's final hand: {computer}, final score: {computerTotalScore}")
        
        # Determine the winner
        if computerTotalScore > 21:
            print("Computer went over 21! You win!")
        elif computerTotalScore > playerTotalScore:
            print("Computer wins!")
        elif computerTotalScore < playerTotalScore:
            print("You win!")
        else:
            print("It's a draw!")
    
    else:
        PlayAgain = False


    
