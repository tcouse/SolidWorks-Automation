# these functions are now obsolete but could be useful again later

from fractions import Fraction


def get_distance(prompt: str):
    while True:
        diameter = input(prompt)

    # verifies the user has entered a valid number
        try:
            diameter = float(Fraction(diameter))
        except ValueError:
            print('Please enter a number.')
            continue

    # verifies the user has entered a positive, non-zero diameter
        if diameter <= 0:
            print('The diameter must be a positive, non-zero number.')
            continue
        break
    return diameter


def yes_or_no(question: str):
    while True:
        # prompts the user with a yes or no question
        u_bolt = input(question)
        u_bolt = u_bolt.lower()
        # returns True for yes, False for No
        if u_bolt == 'yes' or u_bolt == 'y':
            u_bolt = True
            break
        elif u_bolt == 'no' or u_bolt == 'n':
            u_bolt = False
            break
        else:
            print('Invalid input, please answer Yes or No.')
    return u_bolt
