import random
import time

def create_board(size):
    """Create a board with pairs of cards."""
    cards = list(range(1, (size * size) // 2 + 1)) * 2
    random.shuffle(cards)
    return [cards[i:i + size] for i in range(0, len(cards), size)]

def display_board(board, revealed):
    """Display the board with revealed cards."""
    print("\n".join(" ".join(str(board[i][j]) if revealed[i][j] else "*" for j in range(len(board[i]))) for i in range(len(board))))

def check_win(revealed):
    """Check if all cards are revealed."""
    return all(all(row for row in revealed) for revealed in revealed)

def memory_game(size=4, time_limit=60):
    board = create_board(size)
    revealed = [[False] * size for _ in range(size)]
    attempts = 0
    start_time = time.time()

    while time.time() - start_time < time_limit:
        display_board(board, revealed)
        print(f"Time left: {time_limit - int(time.time() - start_time)} seconds")
        try:
            first_pick = input("Select first card (row,col): ")
            x1, y1 = map(int, first_pick.split(","))
            if revealed[x1][y1]:
                print("Card already revealed. Try again.")
                continue

            second_pick = input("Select second card (row,col): ")
            x2, y2 = map(int, second_pick.split(","))
            if revealed[x2][y2] or (x1, y1) == (x2, y2):
                print("Card already revealed or same card. Try again.")
                continue

            revealed[x1][y1] = True
            revealed[x2][y2] = True
            attempts += 1

            if board[x1][y1] != board[x2][y2]:
                print("Not a match!")
                revealed[x1][y1] = False
                revealed[x2][y2] = False
            else:
                print("It's a match!")
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid coordinates.")
        
        if check_win(revealed):
            print("Congratulations! You've matched all pairs!")
            break
    else:
        print("Time's up! Game Over!")

    display_board(board, [[True] * size for _ in range(size)])
    print(f"Total attempts: {attempts}")

if __name__ == "__main__":
    memory_game()