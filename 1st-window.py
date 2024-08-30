import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600)) # 画面つくる
pygame.display.set_caption('Pygame Introduction') # 画面トップのタイトル

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()
