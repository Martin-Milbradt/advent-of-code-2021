from modules import DataManager

data = DataManager(__file__).get_data_string()


def bingo_score(draw_order, input):
    # Convert draw order and boards to integers
    draw_order = list(map(int, draw_order.split(",")))
    boards = []
    for row in input:
        if not row:
            boards.append([])
        else:
            boards[-1].append(list(map(int, row.split())))

    for num in draw_order:
        for board in boards:
            # Mark the number on the board
            for i in range(5):
                for j in range(5):
                    if board[i][j] == num:
                        board[i][j] = -1  # Use -1 to mark the number

            # Check if the board has a winning row or column
            for i in range(5):
                if all(board[i][j] == -1 for j in range(5)) or all(
                    board[j][i] == -1 for j in range(5)
                ):
                    # Calculate the score of the winning board
                    score = sum(
                        board[i][j]
                        for i in range(5)
                        for j in range(5)
                        if board[i][j] != -1
                    )
                    return score * num

    return None


print(bingo_score(data[0], data[1:]))
