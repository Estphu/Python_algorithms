import random 

def four_digit_mastermind():
    random_four_digits = list(map(str, random.sample(range(0,9),4)) )
    print('''
            *** WELCOME TO MASTERMIND *** \n
            GUESS THE FOUR DIGITS \n
            ---MANUAL---\n
            NUMBERS ARE BETWEEN 0 to 9\n
            EACH NUMBER IS UNIQUE\n
            THREE CHARACTERS AGAINST YOUR GUESSED NUMBER MEANINGS:\n
            B ----> YOU GUESSED IT WRONG\n
            Y ----> YOU GUESSED THE NUMBER RIGHT BUT IT'S IN WRONG PLACE\n
            R ----> YOU GUESSED THE NUMBER RIGHT AND IT'S IN RIGHT PLACE\n
            *** GOOD LUCK *** YOU GOT EIGHT TRIES
     ''')
    for i in range(8):
        result = ['B','B','B','B']
        user_guess_nums = input('Enter your four digit guess code: ')
        user_guess_lists = list(user_guess_nums)
        user_guess_nums_len = len(user_guess_nums)
        if user_guess_nums_len == 4:     
            for user_index, user_guess_num in enumerate(user_guess_lists):
                for guess_index, random_four_digit in enumerate(random_four_digits):
                    if user_guess_num == random_four_digit:
                        if user_index == guess_index:
                            result[user_index] = 'R'
                        else:
                            result[user_index] = 'Y'

            print(result)
            if result == ['R','R','R','R']:
                print(''.join(result))
                print('>>> CONGRATULATIONS IT MATCHED <<<')
                break
        else:
            print("FOUL!!! PLEASE ENTER FOUR DIGITS")
            continue

if __name__ == '__main__':
    four_digit_mastermind()
