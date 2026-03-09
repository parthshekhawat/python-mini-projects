import random
from book import word_list

chosen_word = random.choice(word_list)


#placeholder
placeholder = ""

for i in range(len(chosen_word)):
    placeholder += "-"

print(placeholder)


guessed_letters = []
lives = 6
gameover = False

#take guess

while not gameover:
    print(f"\n********************** - LIVES = {lives}/6 - *************************\n")
    
    display = ""
    
    guess = input("guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already guessed '{guess}'.\n")
        continue
        #tells user if they have already guessed a letter
        
    for letter in chosen_word:
        
        if letter == guess:
            display += letter
            
            
        elif letter in guessed_letters:
            display += letter #since letter is already in guessed_letters, it gets added as well
            
        else:            
            display += "-"

    print(f"\n{display}\n")

    if guess not in chosen_word:
        print(f"Your guess was '{guess}', it is not in the word.")
        
        lives -= 1
        if lives == 0:
            gameover = True
            print("\n************************* YOU LOSE! ********************************")        
            print(f"The word was {chosen_word}. \nBetter luck next time.\n")
            
    
    
    if "-" not in display:
        print("\n************************* YOU WIN! ********************************")        
        gameover = True

input("\n\n\nENTER")

print("done")
