while True:
    word = input("Enter word: ")
    normalized_word = word.lower().replace(" ", "")
    reversed_word = normalized_word[::-1]
    if normalized_word == reversed_word:
        print("This is palindrome")
    else:
        print("Not palindrome")