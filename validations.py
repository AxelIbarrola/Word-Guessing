def get_user_letter():
    
    while True:
        
        user_letter = input('\nEnter an alphabetical letter: ')
        
        if not user_letter.isalpha():
            print('You must enter an alphabetic value')
        elif not len(user_letter) == 1:
            print('You must enter a single letter')
        else:
            break
    
    return user_letter
        
def validate_letter_in(user_letter, random_word, hidden_word):
    
    hidden_word = list(hidden_word)
    
    while True:
        if user_letter in hidden_word:
            print('That letter has already been selected, try again')
            user_letter = get_user_letter()
        else:
            break
        
    for i in range(len(random_word)):
        
        if user_letter == random_word[i]:
        
            hidden_word[i] = user_letter
        
    hidden_word = ''.join(hidden_word)
    
    if user_letter in random_word:    
        return hidden_word, True
    
    return hidden_word, False