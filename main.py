from games.multiplication_game import multiplication_game


def question_mode(game, score=0):
    """Calls a game with a predifined score

    game is a function
    score is integer
    """
    question, answer = game(score)

    while answer == input(question):
        print('nice job\n')
        score += 1
        question, answer = game(score)

    print(f'you scored {score}\n')

    if '1' == input('Want to try again? (yes: 1)\n'):
        question_mode(game)
    else:
        pass


if __name__ == "__main__":
    question_mode(multiplication_game)
