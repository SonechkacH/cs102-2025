import curses
import time
from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        screen.addch(0, 0, "+")
        screen.addch(0, self.life.cols + 1, "+")
        screen.addch(self.life.rows + 1, 0, "+")
        screen.addch(self.life.rows + 1, self.life.cols + 1, "+")

        for x in range(1, self.life.cols + 1):
            screen.addch(0, x, "-")
            screen.addch(self.life.rows + 1, x, "-")

        for y in range(1, self.life.rows + 1):
            screen.addch(y, 0, "|")
            screen.addch(y, self.life.cols + 1, "|")

    def draw_grid(self, screen) -> None:
        for y in range(self.life.rows):
            for x in range(self.life.cols):
                if self.life.curr_generation[y][x] == 1:
                    screen.addch(y + 1, x + 1, "█")
                else:
                    screen.addch(y + 1, x + 1, " ")

    def run(self) -> None:
        screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        screen.keypad(True)
        curses.curs_set(0)

        try:
            while True:
                screen.clear()

                self.draw_borders(screen)

                self.draw_grid(screen)

                screen.addstr(0, self.life.cols + 3, f"Gen: {self.life.generations}")
                screen.addstr(1, self.life.cols + 3, "Q - выход")

                if self.life.is_max_generations_exceeded or not self.life.is_changing:
                    screen.addstr(self.life.rows + 3, 0, "GAME OVER")
                    screen.refresh()
                    time.sleep(2)
                    break

                screen.refresh()

                screen.timeout(500)
                key = screen.getch()

                if key == ord("q") or key == ord("Q"):
                    break

                self.life.step()

        finally:
            curses.nocbreak()
            screen.keypad(False)
            curses.echo()
            curses.endwin()
