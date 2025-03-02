import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 800  # Increased height for more space
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2 Jug Problem")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)  # Light blue for buttons
DARK_BLUE = (0, 0, 139)       # Darker blue for button borders
GREEN = (0, 255, 0)           # Color for win message

# Jug capacities and target
jug1_capacity = 4
jug2_capacity = 3
target = 2

# Current amount of water in jugs
jug1_current = 0
jug2_current = 0

# Font
font = pygame.font.SysFont(None, 40)

# Jug dimensions and positions
jug_width, jug_height = 100, 300
jug1_x, jug1_y = 100, 50
jug2_x, jug2_y = WIDTH - 200, 50

# Button dimensions and positions
button_width, button_height = 200, 50
button_spacing = 15
jug1_buttons_x = jug1_x  # X coordinate for Jug 1 buttons
jug2_buttons_x = jug2_x  # X coordinate for Jug 2 buttons
button_y_start = jug1_y + jug_height + 20  # Y coordinate for buttons just below the jugs

def draw_jugs():
    # Jug 1
    pygame.draw.rect(screen, BLUE, (jug1_x, jug1_y, jug_width, jug_height), 5)
    pygame.draw.rect(screen, BLUE, (jug1_x, jug1_y + jug_height - jug_height * (jug1_current / jug1_capacity), jug_width, jug_height * (jug1_current / jug1_capacity)))
    jug1_label = font.render(f"Jug 1: {jug1_current}/{jug1_capacity}", True, BLACK)
    screen.blit(jug1_label, (jug1_x, jug1_y - 40))

    # Jug 2
    pygame.draw.rect(screen, BLUE, (jug2_x, jug2_y, jug_width, jug_height), 5)
    pygame.draw.rect(screen, BLUE, (jug2_x, jug2_y + jug_height - jug_height * (jug2_current / jug2_capacity), jug_width, jug_height * (jug2_current / jug2_capacity)))
    jug2_label = font.render(f"Jug 2: {jug2_current}/{jug2_capacity}", True, BLACK)
    screen.blit(jug2_label, (jug2_x, jug2_y - 40))

def draw_buttons():
    # Define button labels and their positions for Jug 1
    jug1_buttons = [
        ("FillJug1", jug1_buttons_x, button_y_start),
        ("EmptyJug1", jug1_buttons_x, button_y_start + button_height + button_spacing),
        ("Jug1->Jug2", jug1_buttons_x, button_y_start + 2 * (button_height + button_spacing)),
    ]
    
    # Define button labels and their positions for Jug 2
    jug2_buttons = [
        ("FillJug2", jug2_buttons_x, button_y_start),
        ("EmptyJug2", jug2_buttons_x, button_y_start + button_height + button_spacing),
        ("Jug2->jug1", jug2_buttons_x, button_y_start + 2 * (button_height + button_spacing)),
    ]
    
    # Draw Jug 1 buttons
    for label, x, y in jug1_buttons:
        pygame.draw.rect(screen, LIGHT_BLUE, (x, y, button_width, button_height))
        pygame.draw.rect(screen, DARK_BLUE, (x, y, button_width, button_height), 2)  # Button border
        text = font.render(label, True, BLACK)
        screen.blit(text, (x + 10, y + 10))
    
    # Draw Jug 2 buttons
    for label, x, y in jug2_buttons:
        pygame.draw.rect(screen, LIGHT_BLUE, (x, y, button_width, button_height))
        pygame.draw.rect(screen, DARK_BLUE, (x, y, button_width, button_height), 2)  # Button border
        text = font.render(label, True, BLACK)
        screen.blit(text, (x + 10, y + 10))

def handle_click(x, y):
    global jug1_current, jug2_current

    # Determine button clicked based on x, y position
    if y >= button_y_start and y <= button_y_start + 3 * (button_height + button_spacing):
        if x >= jug1_buttons_x and x <= jug1_buttons_x + button_width:
            if y < button_y_start + button_height:
                jug1_current = jug1_capacity
            elif y < button_y_start + 2 * (button_height + button_spacing):
                jug1_current = 0
            else:
                pour_amount = min(jug1_current, jug2_capacity - jug2_current)
                jug1_current -= pour_amount
                jug2_current += pour_amount
        elif x >= jug2_buttons_x and x <= jug2_buttons_x + button_width:
            if y < button_y_start + button_height:
                jug2_current = jug2_capacity
            elif y < button_y_start + 2 * (button_height + button_spacing):
                jug2_current = 0
            else:
                pour_amount = min(jug2_current, jug1_capacity - jug1_current)
                jug2_current -= pour_amount
                jug1_current += pour_amount

def check_win():
    return jug1_current == target or jug2_current == target

def main():
    global jug1_current, jug2_current

    running = True
    while running:
        screen.fill(WHITE)
        draw_jugs()
        draw_buttons()

        if check_win():
            win_label = font.render("You Win!", True, GREEN)
            screen.blit(win_label, (WIDTH // 2 - 50, 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not check_win():
                    handle_click(*event.pos)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
