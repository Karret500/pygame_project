import pygame
import player


class Level():
    def __init__(self) -> None:
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        # Add the player
        self.player = player.Player((200, 200), self.all_sprites)
        

    def draw(self,screen):
        self.all_sprites.draw(screen)                    
    def update(self):
        self.all_sprites.update()
