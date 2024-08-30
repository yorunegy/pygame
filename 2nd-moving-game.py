import pygame
import random

# Pygameを初期化
pygame.init()

# 画面サイズを設定
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 色の設定　RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# プレイヤーの設定
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# 障害物の設定
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5

# ゲームループのフラグ
running = True

# ゲームのメインループ
while running:
    # イベントの処理
    for event in pygame.event.get(): # 全イベントの取得
        if event.type == pygame.QUIT: # 閉じるボタンが押されたかどうか
            running = False

    # キー入力の処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # 障害物の移動
    obstacle_y += obstacle_speed

    # 障害物が画面外に出たら再配置
    if obstacle_y > screen_height:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, screen_width - obstacle_width)

    # プレイヤーと障害物の衝突判定
    if (player_x < obstacle_x + obstacle_width and
        player_x + player_width > obstacle_x and
        player_y < obstacle_y + obstacle_height and
        player_y + player_height > obstacle_y):
        print("Game Over!")
        running = False

    # 画面の描画（下から順番に描いていく）
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # 画面を更新
    pygame.display.flip()

    # フレームレートを設定
    pygame.time.Clock().tick(60)

# Pygameを終了
pygame.quit()
