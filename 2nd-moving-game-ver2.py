##### BGM追加
##### 画像切替
##### SE追加

import pygame
import random

# Pygameを初期化
pygame.init()

# ver2 BGM追加
pygame.mixer.init()  # ミキサーを初期化

# BGMをロードして再生
pygame.mixer.music.load("bgm.mp3")  # BGMファイルをロード
pygame.mixer.music.play(-1)  # ループ再生（-1は無限ループ）


# ver2 効果音のロード
obstacle_sound = pygame.mixer.Sound("se.mp3")

# ver2 画像のロード
# player_image = pygame.image.load("player.png")

player_images = [
    pygame.image.load("player1.png"),
    pygame.image.load("player2.png"),
    pygame.image.load("player3.png"),
]
obstacle_image = pygame.image.load("energyball.png")

# ver2 障害物のサイズを変更
obstacle_image = pygame.transform.scale(obstacle_image, (50, 50))  # 50x50ピクセルに縮小

# ver2 画像を90度回転
rotated_obstacle = pygame.transform.rotate(obstacle_image, 90)


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

# ver2 アニメーション用
player_index = 0  # 最初のフレームのインデックス
animation_speed = 0.2  # アニメーションの速さ
frame_count = 0  # フレームカウンター

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
        
        # ver2 障害物が登場するたびに効果音を再生
        obstacle_sound.play()

    # プレイヤーと障害物の衝突判定
    if (player_x < obstacle_x + obstacle_width and
        player_x + player_width > obstacle_x and
        player_y < obstacle_y + obstacle_height and
        player_y + player_height > obstacle_y):
        print("Game Over!")
        running = False


    # 画面の描画（下から順番に描いていく）
    screen.fill(WHITE)
    # pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))
    # pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # ver2 画像の描画
    # フレームカウンターを更新
    frame_count += animation_speed
    if frame_count >= len(player_images):
        frame_count = 0  # フレームをループさせる

    # ver2 現在のフレームを描画
    player_index = int(frame_count)  # フレームカウンターを整数に変換してインデックスを更新
    screen.blit(player_images[player_index], (player_x, player_y))
    # screen.blit(player_image, (player_x, player_y))
    screen.blit(rotated_obstacle, (obstacle_x, obstacle_y))
    
    # 画面を更新
    pygame.display.flip()

    # フレームレートを設定
    pygame.time.Clock().tick(60)

# Pygameを終了
pygame.quit()
