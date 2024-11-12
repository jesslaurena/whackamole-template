import pygame
import random

screen = pygame.display.set_mode((640, 512))

def draw_grid():
    for i in range(32, 512, 32):  # creating rows
        pygame.draw.line(
            screen,
            (66, 66, 66),
            (0, i),  # SQUARE_SIZE = 32
            (640, i),
        )
    for i in range(32, 640, 32):  # creating columns
        pygame.draw.line(
            screen,
            (66, 66, 66),
            (i, 0),
            (i, 512),
        )

def main():
    mole_x = 1
    mole_y = 1
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos  # recording where mouse click happened
                    click_x = x//32 + 1
                    click_y = y//32 + 1
                    if click_x == mole_x and click_y == mole_y:
                        mole_x = random.randrange(1, 21)
                        mole_y = random.randrange(1, 17)
            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_image.get_rect(center = ((mole_x * 32)-16, (mole_y * 32)-16)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()