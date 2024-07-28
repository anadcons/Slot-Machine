import pygame
import random

class Button:
    def __init__(self, x, y, width, height, text, font, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)
            if click[0] == 1 and self.action:
                self.action()
        else:
            pygame.draw.rect(surface, self.color, self.rect)
        
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

class SlotMachine:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Slot Machine')

        # Colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)

        # Load background image
        self.background = pygame.image.load('/Users/anadcons/Project/backgroundd.jpeg')
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        # Load symbols (make sure they are PNGs with transparent backgrounds)
        self.symbols = [
            pygame.image.load('/Users/anadcons/Project/belll.png').convert_alpha(),
            pygame.image.load('/Users/anadcons/Project/7.png').convert_alpha(),
            pygame.image.load('/Users/anadcons/Project/cherry2.png').convert_alpha()
        ]

        # Symbol size
        self.symbol_width = 80
        self.symbol_height = 80
        self.symbols = [pygame.transform.scale(symbol, (self.symbol_width, self.symbol_height)) for symbol in self.symbols]

        # Font
        self.font = pygame.font.SysFont(None, 48)

        # Initial balance
        self.balance = 1000
        self.spin_cost = 10
        self.win_reward = 50

        self.result = self.spin_reels()
        self.game_started = False

        # Start button
        self.start_button = Button(self.width // 2 - 100, self.height // 2 - 50, 200, 100, 'Start', self.font, self.green, self.red, self.start_game)

        # Slot coordinates (adjust these based on your background image)
        self.slot_coords = [
            (220, 175),  # First slot
            (330, 175),  # Second slot
            (444, 175)   # Third slot
        ]

        # Text box coordinates and dimensions
        self.text_box = pygame.Rect(0, 0, self.width, 100)

    def draw_text(self, text, font, color, surface, rect):
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center=rect.center)
        surface.blit(text_surf, text_rect)

    def spin_reels(self):
        return [random.choice(self.symbols) for _ in range(3)]

    def check_win(self, result):
        return result[0] == result[1] == result[2]

    def start_game(self):
        self.game_started = True

    def play(self):
        running = True
        while running:
            self.window.blit(self.background, (0, 0))  # Draw the background image
            
            if not self.game_started:
                self.start_button.draw(self.window)
            else:
                # Display the slot machine symbols
                for i in range(3):
                    x, y = self.slot_coords[i]
                    self.window.blit(self.result[i], (x, y))

                # Display instructions and balance
                self.draw_text('Press SPACE to spin', self.font, self.black, self.window, self.text_box)
                self.draw_text(f'Balance: ${self.balance}', self.font, self.black, self.window, pygame.Rect(0, 100, self.width, 50))
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.game_started:
                        if self.balance >= self.spin_cost:
                            self.balance -= self.spin_cost
                            self.result = self.spin_reels()
                            if self.check_win(self.result):
                                self.balance += self.win_reward

        pygame.quit()

if __name__ == "__main__":
    game = SlotMachine()
    game.play()
