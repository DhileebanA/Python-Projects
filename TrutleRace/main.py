import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    word_guessed = False

    print("Welcome to Hangman!")
    
    while attempts > 0 and not word_guessed:
        print("\n" + display_word(word, guessed_letters))
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()
       
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1
        
        
        word_guessed = all(letter in guessed_letters for letter in word)
    
    if word_guessed:
        print("Congratulations! You've guessed the word", word)
    else:
        print("Game over! The word was:",word)
hangman()
