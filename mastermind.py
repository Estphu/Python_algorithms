from random import randrange

def four_digit_mastermind():
    random_four_digits = []
    for i in range(4):
        random_four_digits.append(randrange(9))
    print(random_four_digits)    
    for i in range(10):
        result = []
        user_guess_nums = input('Enter your four digit guess code: ')
        user_guess_lists = list(user_guess_nums)
        user_guess_nums_len = user_guess_nums.__len__()
        if user_guess_nums_len == 4: 
            for random_four_digit in random_four_digits:
                for user_guess_num in user_guess_lists:
                    if user_guess_num == random_four_digit:
                        if user_guess_lists.index(user_guess_num) == random_four_digits.index(random_four_digit):
                            result.append('R')
                        else:
                            result.append('Y')
                    else:
                        result.append('B')
                     
        else:
            print("FOUL!!! PLEASE ENTER FOUR DIGITS")
            continue            
        print(''.join(result))               
                                    

if __name__ == '__main__':
    four_digit_mastermind()
