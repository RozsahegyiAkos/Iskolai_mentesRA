import pygame

WIDTH, HEIGHT = 1280, 620
BG_COLOR = (140, 137, 246)
FONT_COLOR = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 1. font objektum létrehozása
game_font = pygame.font.Font(None, 60)
# 2. a feliratot tartalmazó réteg létrehozása
text_surf = game_font.render("GAME", True, FONT_COLOR)
# 3. Rect obejktum létrehozása
text_rect = text_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

fonts = pygame.font.get_fonts()
print(len(fonts))
for f in fonts:
    print(f)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    # 4. réteg megjelenítése
    screen.blit(text_surf, text_rect)
    pygame.display.update()

pygame.quit()