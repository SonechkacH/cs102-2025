import pathlib
import random
import typing as tp

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        self.rows, self.cols = size
        self.prev_generation = self.create_grid()
        self.curr_generation = self.create_grid(randomize=randomize)
        self.max_generations = max_generations
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        grid = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                if randomize:
                    cell_value = random.randint(0, 1)
                else:
                    cell_value = 0
                row.append(cell_value)
            grid.append(row)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        row, col = cell
        neighbours = []

        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                    neighbours.append(self.curr_generation[new_row][new_col])

        return neighbours

    def get_next_generation(self) -> Grid:
        new_grid = [[0] * self.cols for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                neighbours = self.get_neighbours((row, col))
                alive_neighbours = sum(neighbours)
                current_state = self.curr_generation[row][col]

                if current_state == 1:
                    if alive_neighbours in (2, 3):
                        new_grid[row][col] = 1
                    else:
                        new_grid[row][col] = 0
                else:
                    if alive_neighbours == 3:
                        new_grid[row][col] = 1
                    else:
                        new_grid[row][col] = 0

        return new_grid

    def step(self) -> None:
        self.prev_generation = [row[:] for row in self.curr_generation]
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        if self.max_generations is None:
            return False
        return self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        with open(filename, "r") as f:
            lines = [line.strip() for line in f.readlines()]

        rows = len(lines)
        cols = len(lines[0]) if rows > 0 else 0

        game = GameOfLife(size=(rows, cols), randomize=False)

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                game.curr_generation[i][j] = int(char)

        return game

    def save(self, filename: pathlib.Path) -> None:
        with open(filename, "w") as f:
            for row in self.curr_generation:
                line = "".join(str(cell) for cell in row)
                f.write(line + "\n")
