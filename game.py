# create a simple rock, papper, scissors game
# provide a welcome message
# get the user's name
# get the user's choice
# get the computer's choice
# determine the winner
# display the result
# ask the user if they want to play again
# say goodbye and end the game
import random
import time
import os
import sys
import platform
# clear the screen
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
# welcome message
def welcome():
    print("Welcome to Rock, Paper, Scissors!")
    print("Let's play a game!")
    time.sleep(1)
# get the user's name
def get_name():
    name = input("What is your name? ")
    print(f"Hello, {name}!")
    return name
# get the user's choice
def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_choice
# get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice
# determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"
    
# display the result
def display_result(user_choice, computer_choice, result):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)
# ask the user if they want to play again
def play_again():
    again = input("Do you want to play again? (yes/no): ").lower()
    while again not in ["yes", "no"]:
        print("Invalid choice. Please try again.")
        again = input("Do you want to play again? (yes/no): ").lower()
    return again == "yes"
# say goodbye and end the game
def goodbye():
    print("Thanks for playing!")
    print("Goodbye!")
    time.sleep(1)
# main function
def main():
    clear_screen()
    welcome()
    name = get_name()
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        if not play_again():
            break
    goodbye()
if __name__ == "__main__":
    main()
# This is a simple rock, paper, scissors game
