##### ver2 BGM追加
##### ver2 画像切替
##### ver2 SE追加

##### ver3 避けるたびにスコア増える
##### ver3 難易度増加（障害物のスピード増   
##### ver3 障害物が同時に複数登場

import pygame
import random

# Pygameを初期化
pygame.init()

# 色の設定　RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# ver2 BGM追加
pygame.mixer.init()  # ミキサーを初期化

# BGMをロードして再生
pygame.mixer.music.load("bgm.mp3")  # BGMファイルをロード
pygame.mixer.music.play(-1)  # ループ再生（-1は無限ループ）

# ver2 効果音のロード
obstacle_sound = pygame.mixer.Sound("se.mp3")

# プレイヤー画像のロード
player_images = [
    pygame.image.load("player1.png"),
    pygame.image.load("player2.png"),
    pygame.image.load("player3.png"),
]
obstacle_image = pygame.image.load("energyball.png")

# ver2 障害物のサイズを変更
obstacle_image = pygame.transform.scale(obstacle_image, (50, 50))  # 50x50ピクセルに縮小
obstacle_image = pygame.transform.rotate(obstacle_image, 90)

# 画面サイズを設定
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 色の設定　RGB
WHITE = (255, 255, 255)

# プレイヤーの設定
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# アニメーション用
player_index = 0  # 最初のフレームのインデックス
animation_speed = 0.2  # アニメーションの速さ
frame_count = 0  # フレームカウンター

# ver3 複数の障害物をリストで管理
obstacles = []
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5

# ver3 障害物を追加する関数
def add_obstacle():
    obstacle_x = random.randint(0, screen_width - obstacle_width)
    obstacle_y = -obstacle_height
    obstacles.append({'x': obstacle_x, 'y': obstacle_y, 'speed': obstacle_speed})

# ver3 最初の障害物を1つ追加
add_obstacle()

# ver3 新しい障害物を追加するためのタイマー
obstacle_timer = 0
obstacle_interval = 100  # 障害物を追加する間隔（フレーム単位）

### スコア
score = 0
font = pygame.font.SysFont(None, 55)
score_rank = 5  # スコアのしきい値
speed_increase_amount = 1  # スピードアップ幅
speed_up = ""

frame_count = 0

# ゲームループのフラグ
running = True

# ゲームのメインループ
while running:
    # イベントの処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キー入力の処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # ver3 障害物の追加
    obstacle_timer += 1
    if obstacle_timer > obstacle_interval:
        add_obstacle()
        obstacle_timer = 0

    # ver3 各障害物の移動
    for obstacle in obstacles:
        obstacle['y'] += obstacle['speed']
        if obstacle['y'] > screen_height:
            obstacles.remove(obstacle)
            score += 1

        # 衝突判定
        if player_x < obstacle['x'] + obstacle_width and player_x + player_width > obstacle['x'] and player_y < obstacle['y'] + obstacle_height and player_y + player_height > obstacle['y']:
            running = False  # ゲームオーバー

    # ver3 フレーム数に応じて障害物の追加間隔を変化させる（逆数関数）
    obstacle_interval = int(100 / (1 + 1 * score))  # 逆数関数で障害物の追加間隔を制御

    # 背景色の設定
    screen.fill(WHITE)

    # プレイヤーの描画
    screen.blit(player_images[int(player_index)], (player_x, player_y))

    # アニメーションフレームの更新
    frame_count += 1
    if frame_count >= 10:
        player_index += animation_speed
        if player_index >= len(player_images):
            player_index = 0
        frame_count = 0

    # ver3 障害物の描画
    for obstacle in obstacles:
        screen.blit(obstacle_image, (obstacle['x'], obstacle['y']))

    # スコアの描画
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    obstacle_interval_text = font.render(f"obs: {obstacle_interval}", True, BLACK)
    screen.blit(obstacle_interval_text, (300, 10))


    # ゲーム画面を更新
    pygame.display.flip()

    # フレームレートを設定
    pygame.time.Clock().tick(60)

# Pygameを終了
pygame.quit()
