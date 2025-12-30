from utils.input_utils import *

def main():
    print("Welcome to Hogwarts Adventure!")
    from menu import launch_menu_choice

    while True:
        launch_menu_choice()
        play_again = ask_choice("\nWould you like to play again? (yes/no): ",["yes","no"])
        if play_again != 'yes':
            print("\nThank you for playing Hogwarts Adventure!")
            break



if __name__ == "__main__":
    main()
