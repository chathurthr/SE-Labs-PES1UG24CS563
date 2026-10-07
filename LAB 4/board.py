import random

SIZE = 4


class Board:
    def __init__(self):
        self.grid = [[0] * SIZE for _ in range(SIZE)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        empty = [
            (r, c)
            for r in range(SIZE)
            for c in range(SIZE)
            if self.grid[r][c] == 0
        ]

        if empty:
            r, c = random.choice(empty)
            self.grid[r][c] = 4 if random.random() < 0.1 else 2

    @staticmethod
    def slide_line(line):
        values = [x for x in line if x]
        result = []
        i = 0

        while i < len(values):
            if i + 1 < len(values) and values[i] == values[i + 1]:
                result.append(values[i] * 2)
                i += 2
            else:
                result.append(values[i])
                i += 1

        return result + [0] * (SIZE - len(result))

    def move_left(self):
        changed = False

        for r in range(SIZE):
            old = self.grid[r][:]
            self.grid[r] = self.slide_line(old)

            if old != self.grid[r]:
                changed = True

                # Add points for each merge in this row.
                old_values = [x for x in old if x]
                new_values = [x for x in self.grid[r] if x]

                i = 0
                j = 0

                while i < len(old_values):
                    if (
                        i + 1 < len(old_values)
                        and old_values[i] == old_values[i + 1]
                    ):
                        self.score += old_values[i] * 2
                        i += 2
                    else:
                        i += 1

        return changed

    def move_right(self):
        changed = False

        for r in range(SIZE):
            old = self.grid[r][:]
            reversed_old = list(reversed(old))
            new = list(reversed(self.slide_line(reversed_old)))

            self.grid[r] = new

            if old != new:
                changed = True

                old_values = [x for x in reversed_old if x]

                i = 0
                while i < len(old_values):
                    if (
                        i + 1 < len(old_values)
                        and old_values[i] == old_values[i + 1]
                    ):
                        self.score += old_values[i] * 2
                        i += 2
                    else:
                        i += 1

        return changed

    def move_up(self):
        changed = False

        for c in range(SIZE):
            old = [self.grid[r][c] for r in range(SIZE)]
            new = self.slide_line(old)

            for r in range(SIZE):
                self.grid[r][c] = new[r]

            if old != new:
                changed = True

                old_values = [x for x in old if x]

                i = 0
                while i < len(old_values):
                    if (
                        i + 1 < len(old_values)
                        and old_values[i] == old_values[i + 1]
                    ):
                        self.score += old_values[i] * 2
                        i += 2
                    else:
                        i += 1

        return changed

    def move_down(self):
        changed = False

        for c in range(SIZE):
            old = [self.grid[r][c] for r in range(SIZE)]
            reversed_old = list(reversed(old))
            new = list(reversed(self.slide_line(reversed_old)))

            for r in range(SIZE):
                self.grid[r][c] = new[r]

            if old != new:
                changed = True

                old_values = [x for x in reversed_old if x]

                i = 0
                while i < len(old_values):
                    if (
                        i + 1 < len(old_values)
                        and old_values[i] == old_values[i + 1]
                    ):
                        self.score += old_values[i] * 2
                        i += 2
                    else:
                        i += 1

        return changed

    def can_move(self):
        if any(0 in row for row in self.grid):
            return True

        for r in range(SIZE):
            for c in range(SIZE):
                if c + 1 < SIZE and self.grid[r][c] == self.grid[r][c + 1]:
                    return True

                if r + 1 < SIZE and self.grid[r][c] == self.grid[r + 1][c]:
                    return True

        return False
