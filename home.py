import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game - Home")

FONT = pygame.font.SysFont("arial", 32)
SMALL_FONT = pygame.font.SysFont("arial", 24)

input_boxes = []
player_names = ["", ""]

active_input = [False, False]

def draw_home(hover_start_button):
    SCREEN.fill((50, 50, 50))  # Background color

    # Gradient Background
    pygame.draw.rect(SCREEN, (0, 0, 0), (0, 0, WIDTH, HEIGHT // 2))
    pygame.draw.rect(SCREEN, (0, 50, 255), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    # Player Input Labels
    for i in range(2):
        label = SMALL_FONT.render(f"Player {i+1} Name:", True, (255, 255, 255))
        SCREEN.blit(label, (150, 120 + i * 80))

        color = (255, 255, 255) if active_input[i] else (200, 200, 200)
        pygame.draw.rect(SCREEN, color, input_boxes[i], 2)

        name_surface = SMALL_FONT.render(player_names[i], True, (255, 255, 255))
        SCREEN.blit(name_surface, (input_boxes[i].x + 5, input_boxes[i].y + 5))

    # Styled Start Button with Hover Effect
    start_button = pygame.Rect(WIDTH // 2 - 80, 350, 160, 50)
    button_color = (0, 200, 0) if not hover_start_button else (0, 255, 0)
    pygame.draw.rect(SCREEN, button_color, start_button)
    start_text = SMALL_FONT.render("Start Game", True, (255, 255, 255))
    SCREEN.blit(start_text, (start_button.x + 20, start_button.y + 10))

    pygame.display.flip()
    return start_button

def home_screen():
    global input_boxes, active_input, player_names

    input_boxes = [pygame.Rect(300, 115 + i * 80, 200, 40) for i in range(2)]
    clock = pygame.time.Clock()

    # Animation Variables (no title to animate now)
    hover_start_button = False
    while True:
        start_button = draw_home(hover_start_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, box in enumerate(input_boxes):
                    active_input[i] = box.collidepoint(event.pos)
                if start_button.collidepoint(event.pos):
                    return player_names

            elif event.type == pygame.MOUSEMOTION:
                hover_start_button = start_button.collidepoint(event.pos)

            elif event.type == pygame.KEYDOWN:
                for i in range(2):
                    if active_input[i]:
                        if event.key == pygame.K_RETURN:
                            active_input[i] = False
                        elif event.key == pygame.K_BACKSPACE:
                            player_names[i] = player_names[i][:-1]
                        else:
                            if len(player_names[i]) < 12:
                                player_names[i] += event.unicode

        clock.tick(30)
