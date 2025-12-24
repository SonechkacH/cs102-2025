import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed

        self.width = self.life.cols * cell_size
        self.height = self.life.rows * cell_size

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("darkgray"), (x, 0), (x, self.height)
            )
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("darkgray"), (0, y), (self.width, y)
            )

    def draw_grid(self) -> None:
        # Copy from previous assignment
        self.screen.fill(pygame.Color("black"))

        for y in range(self.life.rows):
            for x in range(self.life.cols):
                # Определяем цвет клетки
                if self.life.curr_generation[y][x] == 1:
                    color = pygame.Color("green")
                else:
                    color = pygame.Color("white")

                rect = pygame.Rect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size - 1,
                    self.cell_size - 1,
                )

                pygame.draw.rect(self.screen, color, rect)
        self.draw_lines()
        font = pygame.font.Font(None, 36)
        text = font.render(
            f"Generation: {self.life.generations}", True, (255, 255, 255)
        )
        self.screen.blit(text, (10, 10))

        if self.life.is_max_generations_exceeded or not self.life.is_changing:
            font = pygame.font.Font(None, 48)
            text = font.render("GAME OVER", True, (255, 0, 0))
            text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(text, text_rect)

    def run(self) -> None:
        running = True
        paused = False

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        paused = not paused
                    elif event.key == K_r:
                        self.life.curr_generation = self.life.create_grid(
                            randomize=True
                        )
                        self.life.generations = 1
                    elif event.key == K_ESCAPE:
                        running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        cell_x = x // self.cell_size
                        cell_y = y // self.cell_size
                        if (
                            0 <= cell_x < self.life.cols
                            and 0 <= cell_y < self.life.rows
                        ):
                            self.life.curr_generation[cell_y][cell_x] = (
                                1 - self.life.curr_generation[cell_y][cell_x]
                            )
            if not paused:
                self.life.step()

            self.draw_grid()

            pygame.display.flip()

            self.clock.tick(self.speed)

        pygame.quit()
