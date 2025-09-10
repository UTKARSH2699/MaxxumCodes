import random

def hangman():
    words = ['apple', 'banana', 'cherry', 'orange', 'grape']
    word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    
    while incorrect_guesses < max_incorrect:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("\nWord: " + ' '.join(display_word))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1
        
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
