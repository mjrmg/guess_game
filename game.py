import random


def get_user_range():
    print('Podaj min zakresu: ')
    min_d = int(input())
    print('Podaj max zakresu: ')
    max_d = int(input())

    return min_d, max_d


def get_random_number_from_range(min_d, max_d):
    return random.randint(min_d, max_d)


def guess_number(drawn, min_d, max_d):
    counter = 0

    print(f'Zgadnij liczbę z zakresu {min_d}-{max_d}')

    while True:
        user_guess = int(input())
        counter += 1
        if user_guess > drawn: print('za dużo')
        elif user_guess < drawn: print('za mało')
        else:
            print(f'Zgadłeś liczbę {drawn}, za {counter} razem.')
            break

def start_game():
    min_nr, max_nr = get_user_range()
    random_nr = get_random_number_from_range(min_nr, max_nr)
    guess_number(random_nr, min_nr, max_nr)

start_game()
