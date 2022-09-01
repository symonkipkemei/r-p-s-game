
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
    """Establishes who won the rock paper scissor game

    Args:
        user_hand (str): entry by the use
        comp_hand (str): entry by the computer

    Returns:
        str: The winner
    """
    #options
    options = {1:"win",2:"lose",3:"draw"}

    # possibilities
    possibilities = {"user" : "","comp":""}

    
    # User probabilities

    if user_hand == "scissorr" and comp_hand == "paper":
        possibilities["user"] =options[1]
        possibilities["comp"] =options[2]

    elif user_hand == "paper" and comp_hand == "rock":
        possibilities["user"] =options[1]
        possibilities["comp"] =options[2]
    
    elif user_hand == "rock" and comp_hand == "scissor":
        possibilities["user"] =options[1]
        possibilities["comp"] =options[2]

    elif user_hand == "rock" and comp_hand == "rock":
        possibilities["user"] =options[3]
        possibilities["comp"] =options[3]
    
    elif user_hand == "scissor" and comp_hand == "scissor":
        possibilities["user"] =options[3]
        possibilities["comp"] =options[3]
    
    elif user_hand == "paper" and comp_hand == "paper":
        possibilities["user"] =options[3]
        possibilities["comp"] =options[3]

    # Computer probabilities

    elif comp_hand == "scissorr" and user_hand == "paper":
        possibilities["user"] =options[2]
        possibilities["comp"] =options[1]

    elif comp_hand == "paper" and user_hand == "rock":
        possibilities["user"] =options[2]
        possibilities["comp"] =options[1]
    
    elif comp_hand == "rock" and user_hand == "scissor":
        possibilities["user"] =options[2]
        possibilities["comp"] =options[1]

    elif user_hand == "rock" and comp_hand == "rock":
        possibilities["user"] =options[3]
        possibilities["comp"] =options[3]
    
    elif user_hand == "scissor" and comp_hand == "scissor":
        possibilities["user"] =options[3]
        possibilities["comp"] =options[3]
    
    elif user_hand == "paper" and comp_hand == "paper":
        possibilities["user"] =options[3]
        possibilities["comp"] =options[3]

    for key, value in possibilities.items():
        if value == "win":
            print(key,"won")
            return key

def ask_option() -> int:
    """Displays the game options for the user

    Returns:
        int: returns a keypair of what was selected by the user
    """
    print("select one option:")
    values = {0 : "rock", 1: "paper",2:"scissorr"}
    for key,value in values.items():
        print(f"{key}:{value}")
    
    option = int(input("Insert option: "))
    return option



def main():
    """Compiles code into one
    """
    number = ask_option()
    user_option =get_hand_user(number)
    comp_option = get_hand_computer()

    winner =determine_winner(user_option,comp_option)

    print(f"User_hand:{user_option}\ncomputer_hand:{comp_option}\nWinner:{winner}")


main()