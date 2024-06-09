import pygame

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.image = pygame.Surface((16, 16))
        self.image.fill((255, 255, 255))  # White square
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type

    def apply_effect(self, pacman):
        pass

class InvincibilityPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y, "invincibility")

    def apply_effect(self, pacman):
        pacman.invincible = True
        pacman.invincibility_timer = 5  # 5 seconds of invincibility

class SpeedBoostPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y, "speed_boost")

    def apply_effect(self, pacman):
        pacman.speed += 2
        pacman.speed_timer = 5  # 5 seconds of speed boost

class ScoreBoostPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y, "score_boost")

    def apply_effect(self, pacman):
        pacman.score_multiplier = 2
        pacman.score_timer = 5  # 5 seconds of score boost