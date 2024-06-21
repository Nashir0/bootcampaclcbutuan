import random

# Function to get user input for three numbers
def get_user_numbers():
    return [int(input(f"Enter Bet number {i + 1} (0-9): ")) for i in range(3)]

# Function to check the result against user input
def check_result(user, result):
    # Check if user's numbers match exactly with result
    if user == result:
        return "You Win!"
    # Check if user's numbers match result in any order (partial win)
    elif sorted(user) == sorted(result):
        return "Partial Win!"
    # If no matches, user loses
    else:
        return "You lose!"

# Main function to run the game
def main():
    print("Swertres!")  # Print game title
    user_numbers = get_user_numbers()  # Get user's three numbers
    result_numbers = random.sample(range(10), 3)  # Generate random result numbers
    print("Swertres Result:", result_numbers)  # Print the result numbers
    print(check_result(user_numbers, result_numbers))  # Print the result of the game

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
