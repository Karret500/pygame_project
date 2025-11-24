import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos, *groups) -> None:
        super().__init__(*groups)
        self.original_image = pygame.image.load("creature.png")
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self):
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_w]):
            self.rect.y -= 1
        if(keys[pygame.K_a]):
            self.rect.x -= 1
        if(keys[pygame.K_s]):
            self.rect.y += 1
        if(keys[pygame.K_d]):
            self.rect.x += 1
