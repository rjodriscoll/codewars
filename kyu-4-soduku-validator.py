def valid_solution(board):
    def validate_segment(input):
        cond_1 = len(set(input)) == len(input)
        cond_2 = min(input) == 1
        cond_3 = max(input) == 9

        if cond_1 and cond_2 and cond_3:
            return True
        else:
            return False

    def get_to_validate(board):
        to_validate = []
        for row in board:
            to_validate += [row]
        for i in range(9):
            to_validate += [[row[i] for row in board]]

        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                cell = [
                    board[col][row : row + 3],
                    board[col + 1][row : row + 3],
                    board[col + 2][row : row + 3],
                ]
                to_validate += [[item for sublist in cell for item in sublist]]

        return to_validate

    to_validate = get_to_validate(board)

    for row in to_validate:
        valid = validate_segment(row)
        if not valid:
            return False
    return True