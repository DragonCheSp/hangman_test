import random 

word_list = ['trash','visual','code','test']

def get_word():
    word = random.choice(word_list)
    return word.upper()

def hangman_try(tries):
    stages = [
        '1','2','3','4','5','6',
    ]
    return stages [tries]

def play(word):
    guess = False 
    tries = 6 

    print("let's play hangman")
    print(hangman_try(tries))

def main():
    word = get_word ()
    play(word)
    
    if input("play again ? (y/n)") == "y" :
            word = get_word ()
            play(word)

if __name__ == "__main__":
    main()