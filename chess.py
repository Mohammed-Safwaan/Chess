import pygame
import sys
from board import Board
from home import home_screen


# Initialize pygame
pygame.init()

WIDTH, HEIGHT = 640, 640
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

def load_images():
    pieces = ["w_pawn", "w_rook", "w_knight", "w_bishop", "w_queen", "w_king",
              "b_pawn", "b_rook", "b_knight", "b_bishop", "b_queen", "b_king"]
    images = {}
    for piece in pieces:
        images[piece] = pygame.transform.scale(
            pygame.image.load(f"assets/images/{piece}.png"), (80, 80)
        )
    return images

# Load images
images = load_images()

# Create board
board = Board()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                board.handle_click(pos)

        SCREEN.fill((0, 0, 0))
        board.draw(SCREEN, images)
        pygame.display.flip()

if __name__ == "__main__":
    names = home_screen()  # Get player names from home screen
    print(f"Player 1: {names[0]}, Player 2: {names[1]}")  # For debugging (optional)
    main() 