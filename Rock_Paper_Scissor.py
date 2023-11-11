import random

class Move:
    def __init__(self, user_choice, computer_choice):
        self.user_choice = user_choice
        self.computer_choice = computer_choice
        self.next = None

def create_move(user_choice, computer_choice):
    return Move(user_choice, computer_choice)

def push_move(stack, user_choice, computer_choice):
    move = create_move(user_choice, computer_choice)
    move.next = stack
    return move

def pop_move(stack):
    if stack is None:
        return None
    move = stack
    stack = move.next
    return move

def display_move(user_choice, computer_choice):
    choices = ["Rock", "Paper", "Scissors"]
    print(f"You chose: {choices[user_choice - 1]}")
    print(f"Computer chose: {choices[computer_choice - 1]}")

def main():
    move_stack = None

    while True:
        print("Welcome to Rock, Paper, Scissors!")
        print("Choose your move:")
        print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")
        user_choice = int(input("Enter your choice (1/2/3/4): "))

        if user_choice == 4:
            break

        if user_choice < 1 or user_choice > 3:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
            continue

        # Generate a random choice for the computer (1 = Rock, 2 = Paper, 3 = Scissors)
        computer_choice = random.randint(1, 3)

        display_move(user_choice, computer_choice)

        # Push the move onto the stack
        move_stack = push_move(move_stack, user_choice, computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print("You win!")
        else:
            print("Computer wins!")

    # Display the game history
    print("Game history:")
    while move_stack is not None:
        move = pop_move(move_stack)
        display_move(move.user_choice, move.computer_choice)

if __name__ == "__main__":
    main()
