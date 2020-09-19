import random 

word_list = ['trash','visual','code','test']

def get_word():
    word = random.choice(word_list)
    return word.upper()

def hangman_try(tries):
    stages = [
        '1 wrong 5 change left',
        '2 wrong 4 change left',
        '3 wrong 3 change left',
        '4 wrong 2 change left',
        '5 wrong 1 change left',
        '6 wrong sorry ',
    ]
    return stages [tries]

def play(word):
    word_completion = "_" * len(word)
    guessed = False 
    guessed_letters = []
    guessed_wods = []
    tries = 6 

    print("let's play hangman")
    print(hangman_try(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0 :
        guess = input("let me see your word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters : 
                print("you already guessed the letter", guess)
            elif guess not in word : 
                print(guess, "is not in the word")
                tries -= 1 
                guessed_letters.append(guess)
            else:
                print("good job",guess, "is in the word")
                guessed_letters.append(guess)
                word_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_list[index] = guess

def main():
    word = get_word ()
    play(word)
    
    if input("Play again ? (y/n)") == "y" :
            word = get_word ()
            play(word)

if __name__ == "__main__":
    main()