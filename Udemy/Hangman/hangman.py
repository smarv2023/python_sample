import random
from hangman_art import logo, stages
from hangman_words import word_list


end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
life = len(stages) - 1

# Testing code
print(f'Pssst, the solution is {chosen_word}.')
print(f"{logo}\n{stages[life]}")
# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # Check guessed letter
    if guess in display:
        print(f"You've already guessed {guess}.")
    elif guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        print(f"{guess} is not in the word. You lose a life")
        life -= 1

    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    # Check if user does not have life left
    print(f"{stages[life]}")
    if life == 0:
        end_of_game = True
        print(f'You lose, the word is: "{chosen_word}"')
