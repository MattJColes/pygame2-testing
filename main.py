import sys, os, pygame
from game import level_loader


pygame.init()

sprites_dir = os.path.join('assets', 'sprites')

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

character = pygame.image.load(os.path.join(sprites_dir, 'player16.png'))
character_rect = character.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    character_rect = character_rect.move(speed)
    if character_rect.left < 0 or character_rect.right > width:
        speed[0] = -speed[0]
    if character_rect.top < 0 or character_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(character, character_rect)
    pygame.display.flip()
    clock.tick(60)