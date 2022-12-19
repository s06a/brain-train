"""A simple game which asks you multiplication questions,
which gets harder till the answers are correct
"""
import random


def multiplication_game(length):
    """Asks multiplication of two numbers.

    length is integer
    num1 is integer
    num2 is integer
    question is string
    answer is integer
    returns question and answer
    """
    num1 = int(random.random() * 10**length)
    num2 = int(random.random() * 10**length)
    question = str(num1) + 'x' + str(num2)
    answer = str(num1 * num2)

    return question, answer


if __name__ == "__main__":

    question, answer = multiplication_game(2)

    while answer == input(question):
        print('good job')
        question, answer = multiplication_game(2)

    print('maybe next time')
