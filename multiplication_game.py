"""A simple game which asks you multiplication questions,
which gets harder till the answers are correct
"""
import random


def multiplication_game(score):
    """Asks multiplication of two numbers.

    score is integer
    length is integer
    num1 is integer
    num2 is integer
    question is string
    answer is integer
    returns question and answer
    """
    length = score//10 + 2
    num1 = int(random.random() * 10**length)
    num2 = int(random.random() * 10**length)
    question = str(num1) + 'x' + str(num2)
    answer = str(num1 * num2)

    return question, answer


def question_mode(game, score=0):
    """Calls a game with a predifined score

    game is a function
    score is integer
    """
    question, answer = game(score)

    while answer == input(question + '\n'):
        print('good job')
        score += 1
        question, answer = game(score)

    print(f'you scored {score}')

    if '1' == input('Want to try again? (yes: 1)\n'):
        question_mode(game)
    else:
        pass


if __name__ == "__main__":
    question_mode(multiplication_game)
