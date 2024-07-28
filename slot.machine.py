import pygame
import random

pygame.init()
#game_window
width=800
height=600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Slot Machine')
#colors
black=(0, 0, 0)
white=(255,0,0)
#images
symbols=[
    pygame.image.load(''),
    pygame.image.load(''),
    pygame.image.load('')
]
#symbol size
symbol_width=100
symbol_height=100
symbols = [pygame.transform.scale(symbol, (symbol_width, symbol_height)) for symbol in symbols]
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
font = pygame.font.SysFont(None, 48)
def spin_reels():
    return [random.choice(symbols) for _ in range(3)]
result = [random.choice(symbols) for _ in range(3)]
run=True
while run:
    for i in range(3):
        window.blit(result[i], (150 + i * (symbol_width + 20), 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                result = spin_reels()
draw_text('Press SPACE to spin', font, black, window, 200, 50)
pygame.display.update()
pygame.quit()