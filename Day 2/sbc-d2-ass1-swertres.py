import random

def get_user_numbers():
    return [int(input(f"Enter Bet number {i + 1} (0-9): ")) for i in range(3)]

def check_result(user, result):
    return "You Win!" if user == result else "Partial Win!" if sorted(user) == sorted(result) else "You lose!"

def main():
    print("Swertres!")
    user_numbers = get_user_numbers()
    result_numbers = random.sample(range(10), 3)
    print("Swertres Result:", result_numbers)
    print(check_result(user_numbers, result_numbers))

if __name__ == "__main__":
    main()

