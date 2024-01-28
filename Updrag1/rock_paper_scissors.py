#Import ramdom
import random

while True:
    
    #Array of possible choices
    possible_choice = ["Rock", "Paper", "Scissors"]

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    #user choice
    usr_choice = int(input("Enter your choice :"))

    while usr_choice > 3 or usr_choice <1:
      usr_choice = int(input('Please Enter Valid Choice :'))

    usr_choice -= 1     
    usr_choice_name = possible_choice[usr_choice]
    # Computer choice
    comp_choice = random.randint(0,2)

    comp_choice_name = possible_choice[comp_choice]

    print(f"\nYou chose {usr_choice_name}, computer chose {comp_choice_name}.\n")
    
    # decision regarding result of the game.
    if usr_choice == comp_choice:
        print(f"\nIt's a tie!")
    elif usr_choice == 0:
        if comp_choice == 2:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif usr_choice == 1:
        if comp_choice == 0:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif usr_choice == 2:
        if comp_choice == 1:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    
    # Ask user if user wants to continue playing game 
    play_again = input("\nDo You Want To Play again? (y/n): ").lower()
    if play_again != "y":
        break