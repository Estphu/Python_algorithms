import random
import string

def generate_random_alphabets(sentence):
    sentence_alphabets = list(sentence)
    matched_alphabets = []

    while matched_alphabets != sentence_alphabets:  
        for sentence_alphabet in sentence_alphabets:
            if sentence_alphabet == ' ':
                matched_alphabets.append(' ')
                continue
            alphabet = ''
            while sentence_alphabet != alphabet:
                alphabet = random.choice(string.ascii_letters)
                print('MONKEY GOING CRAZY: '+alphabet)
                if sentence_alphabet == alphabet:
                    matched_alphabets.append(alphabet)
                          

    return f"MONKEY CATCHES YOUR SENTENCE\n"+''.join(matched_alphabets)     


if __name__ == '__main__':
    sentence = input('Enter sentence to get matched by monkey (only letters)\n')
    print(generate_random_alphabets(sentence))    
