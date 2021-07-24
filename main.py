import os, pygame
from game import game_characters

pygame.init()

screen_width = 800
screen_height = int(screen_width * 0.8)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()
fps = 60
game_running = True
game_background_color = (150, 220, 150)
game_ground_color = (255, 200, 200)
GRAVITY = 0.75

player = game_characters.Character('player', 200, 200, 3, 5, GRAVITY)
player_move_left = False
player_move_right = False

enemy01 = game_characters.Character('enemy', 500, 200, 3, 5, GRAVITY)


def draw_background():
    screen.fill(game_background_color)
    pygame.draw.line(screen, game_ground_color, (0, 300), (screen_width, 300))


while game_running:
    clock.tick(fps)
    draw_background()

    enemy01.draw(screen)

    player.update_animation()
    player.draw(screen)
    if player.alive:
        if player.in_air:
            player.update_action(2)
        elif player_move_left or player_move_right:
            player.update_action(1)
        else:
            player.update_action(0)
        player.move(player_move_left, player_move_right)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
            if event.key == pygame.K_a:
                player_move_left = True
            if event.key == pygame.K_d:
                player_move_right = True
            if event.key == pygame.K_w and player.alive:
                player.jump = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_move_left = False
            if event.key == pygame.K_d:
                player_move_right = False
            if event.key == pygame.K_w and player.alive:
                player.jump = False

        if event.type == pygame.QUIT:
            game_running = False

    pygame.display.update()

pygame.quit()
