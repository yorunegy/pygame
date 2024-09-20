import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600)) # 画面つくる
pygame.display.set_caption('Pygame Introduction') # 画面トップのタイトル

# ver2 色の設定　RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ver2 背景色の変更
    screen.fill(WHITE)
    pygame.display.flip()

pygame.quit()
