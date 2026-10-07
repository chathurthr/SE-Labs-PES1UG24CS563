
from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.best_score = 0
        self.history = []

    def display(self):
        print("\n" + "+------+------+------+------+")
        for row in self.board.grid:
            print("|" + "|".join(f"{x:^6}" if x else f"{' ':^6}" for x in row) + "|")
            print("+------+------+------+------+")
        print("Score:", self.board.score, " Best:", self.best_score)

    def move(self, key):
        moves = {
            "a": self.board.move_left,
            "d": self.board.move_right,
            "w": self.board.move_up,
            "s": self.board.move_down
        }

        if key not in moves:
            return False

        # Save the state before the move.
        old_grid = [row[:] for row in self.board.grid]
        old_score = self.board.score

        changed = moves[key]()

        # Unchanged moves must not create a tile
        # or overwrite the undo state.
        if not changed:
            return False

        # Store exactly one undo state.
        self.history = [(old_grid, old_score)]

        # Successful moves create one random tile.
        self.board.add_random_tile()

        # Track the highest score reached during this run.
        self.best_score = max(self.best_score, self.board.score)

        # Task 4: determine whether this move produced a merge.
        merge_score = self.board.score - old_score

        direction = {
            "a": "left",
            "d": "right",
            "w": "up",
            "s": "down"
        }[key]

        # Exactly one feedback message for the successful move.
        if merge_score > 0:
            print(f"Moved {direction} — merged for {merge_score} points.")
        else:
            print(f"Moved {direction}.")

        return True

    def undo(self):
        if not self.history:
            return False

        old_grid, old_score = self.history.pop()

        # Restore the board and score exactly.
        self.board.grid = [row[:] for row in old_grid]
        self.board.score = old_score

        return True

    def run(self):
        print("2048 — W/A/S/D to move, U to undo, Q to quit.")

        while True:
            self.display()

            # Task 2: reaching 2048 ends the game.
            if any(2048 in row for row in self.board.grid):
                print("You reached 2048!")
                return

            # Task 2: no legal moves ends the game.
            if not self.board.can_move():
                print("No legal moves remain.")
                return

            key = input("> ").strip().lower()

            if key == "q":
                return

            if key == "u":
                if self.undo():
                    print("Undo successful.")
                else:
                    print("Nothing to undo.")
                continue

            if key not in "wasd":
                print("Use W/A/S/D.")
                continue

            self.move(key)
if __name__ == "__main__":
    Game().run()
