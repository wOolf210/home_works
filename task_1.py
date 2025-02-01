class ChessPieceException(Exception):
    pass


def queen_move(start, end):
    try:
        x1, y1 = start
        x2, y2 = end

        if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            return True
        else:
            return False
    except ValueError:
        raise ChessPieceException("Ошибка: неправильные координаты!")


def knight_move(start, end):
    try:
        x1, y1 = start
        x2, y2 = end

        if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
            return True
        else:
            return False
    except ValueError:
        raise ChessPieceException("Ошибка: неправильные координаты!")


if __name__ == "__main__":
    try:
        start_queen = (1, 1)
        end_queen = (1, 8)
        print(f"Ферзь может попасть: {queen_move(start_queen, end_queen)}")

        start_knight = (1, 1)
        end_knight = (3, 2)
        print(f"Конь может попасть: {knight_move(start_knight, end_knight)}")
    except ChessPieceException as e:
        print(e)
