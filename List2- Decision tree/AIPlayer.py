class AIPlayer:
    def __init__(self, evaluation_function):
        self.evaluation_function = evaluation_function

    def evaluate_board(self, game):
        return self.evaluation_function(game)


def choose_evaluation_method():
    print("Choose evaluation method:")
    print("1. Based on number of pieces")
    print("2. Based on number of available moves")
    print("3. Based on number of flipped pieces")

    choice = int(input("Enter the number (1, 2 or 3): "))
    while choice not in [1, 2, 3]:
        choice = int(input("Invalid choice, enter the number (1, 2 or 3): "))

    return choice
