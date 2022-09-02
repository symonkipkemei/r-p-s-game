

def get_hand_user(number: int) -> str:
    """Pick a number from the user and return string representation of the hand

    Args:
        number (int): Number by the user

    Returns:
        str: The string representation of the hand
    """

    values = {0 : "rock", 1: "paper",2:"scissorr"}

    for key,value  in values.items():
        if number == key:
            return value


def get_hand_computer() -> str:
    """Randomly pick a number and return a string of the same

    Returns:
        str: _description_
    """
    import random

    number = random.randint(0,2)

    values = {0 : "rock", 1: "paper",2:"scissorr"}

    for key,value  in values.items():
        if number == key:
            return value


def determine_winner(user_hand: str, comp_hand:str) -> str:
    """Establishes if the user won, drew or lost the game

    Args:
        user_hand (str): entry by the use
        comp_hand (str): entry by the computer

    Returns:
        str: The winner
    """
    #options referred by numbers for accuracy/consistancy
    options = {1:"won",2:"lost",3:"drew"}

    #store the possibilities for the user
    game_outcome = " "

    # User Winning probabilities

    if user_hand == "scissorr" and comp_hand == "paper":
        game_outcome =options[1]
        
    elif user_hand == "paper" and comp_hand == "rock":
        game_outcome =options[1]
       
    elif user_hand == "rock" and comp_hand == "scissor":
        game_outcome =options[1]
       
    elif user_hand == "rock" and comp_hand == "rock":
        game_outcome =options[3]
        
    elif user_hand == "scissor" and comp_hand == "scissor":
        game_outcome =options[3]
        
    elif user_hand == "paper" and comp_hand == "paper":
        game_outcome =options[3]
    
    else:
         game_outcome = options[2]

    return game_outcome

def ask_option() -> int:
    """Displays the game options for the user, and ask the user to select an option

    Returns:
        int: returns a keypair of what was selected by the user
    """
    while True:
        print("_____________ROCK, PAPER SCISSOR GAME !___________________")

        print("select one option:")
        values = {0 : "rock", 1: "paper",2:"scissorr"}
        for key,value in values.items():
            print(f"{key}:{value}")
        print("_________________________________________________________")
        option = input("Insert your option: ")

        if option.isdigit():
            option = int(option)
            if option > 2 or option < 0:
                print("Input out of range, try again:")
            else:
                break            
        else:
            print("You entered a text and not a number, try again:")
            
    return option
        

def main():
    """Compiles code into one
    """
    number = ask_option()
    user_option =get_hand_user(number)
    comp_option = get_hand_computer()

    winner =determine_winner(user_option,comp_option)
    print("\n__________________OUTCOME______________________________")
    print(f"User_hand:{user_option}\ncomputer_hand:{comp_option}")
    print("_________________________________________________________")
    print(f"User:{winner}")

main()