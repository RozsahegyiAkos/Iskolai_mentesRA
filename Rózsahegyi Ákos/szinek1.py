import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Színek")
  
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      
    # ablak háttérszínének beállítása sztringgel
    screen.fill('yellow')
    # RGB értékkel tuple-ként megadva
    # screen.fill((125, 125, 0))
      
    pygame.display.update()
  
pygame.quit()