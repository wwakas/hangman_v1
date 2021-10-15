# Modules section

# Functions definition
def hello_statement():
    return print('H A N G M A N')


def word_check(guessed_word, right_word):
    if guessed_word == right_word:
        return True


def encryptor(right_word):
    temp_string = ''
    for i in range(0, len(right_word)):
        temp_string += '*'
    return temp_string


def comparator(right_word, guessed, user_input):
    temp_string = ''
    temp_list = list(guessed)
    for i in range(0, len(right_word)):
        if right_word[i] == user_input:
            temp_list[i] = user_input
        elif guessed[i] == '*':
            temp_list[i] = '*'
    for j in temp_list:
        temp_string += j
    return temp_string


def true_or_false(right_word, user_input):
    if user_input not in right_word:
        return True
    else:
        return False


# Main block of program
counter = 0  # counter of misses -> if counter > 7 player loose the game
hello_statement()
winning_word = input('Input the word to guess: > ')
print('\n'*100)
already_guessed = encryptor(winning_word)
print(already_guessed)

while ('*' in already_guessed):
    user_guessed_input = input('Guess the word/char: > ')
    already_guessed = comparator(winning_word, already_guessed, user_guessed_input)
    if word_check(user_guessed_input, winning_word):
        print('Bingo!')
        break
    print(already_guessed)
    if true_or_false(winning_word, user_guessed_input):
        counter += 1
        print('Wrong char / word! Your current count of misses: ', counter)
    if counter >= 7:
        print('You lost!')
        break
    if (len(user_guessed_input) >= 2) and (user_guessed_input != winning_word):
        print('Please type one char or complete word!')