from random_words import get_random_words
from random import choice
from validations import get_user_letter, validate_letter_in

def main():
    
    print(f'\n{'Welcome to the Word Guessing game'.center(50, '-')}\n')
    
    print('You have 12 turns to guess the word, good luck!\n')
    
    random_words = get_random_words()
    random_word = choice(random_words)
    print(random_word)
    
    print('The word was selected:')
    hidden_word = '_'*len(random_word)
    print(hidden_word)
    
    attemps = 12
    
    while attemps > 0:
        user_letter = get_user_letter()
        
        hidden_word, success = validate_letter_in(random_word=random_word, user_letter=user_letter, hidden_word=hidden_word)
        
        if success:
            
            print(hidden_word)
            print()
            print(f'You\'re right! the letter {user_letter} is part of the word\n')
            attemps -= 1
            print(f'You have {attemps} attempts left\n')
        else:
            print(hidden_word)
            print()
            print('Oh no, the letter a is not found in the hidden word.')
            attemps -= 1
            print(f'You have {attemps} attempts left\n')
        
        if not '_' in hidden_word:
            print(f'Congratulations, you got the word!')
            break
    
    if attemps == 0:
        print('You have lost, you have no more attempts left. Better luck next time!')
        print(f'The word was "{random_word}"')

main()