import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 80))  # Placeholder (replace with sprite later)
        self.image.fill((255, 0, 0))  # Red rectangle as placeholder
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5
        self.is_attacking = False #track attack state
        self.attack_timer = 0 #attack animation time

    def attack(self, keys):
        if keys[pygame.K_j] and not self.is_attacking:  # Press 'J' to attack
            self.is_attacking = True
            self.attack_timer = 10  # Attack animation lasts 10 frames

    def update(self):
        if self.is_attacking:
            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.is_attacking = False  # Reset attack after animation

    def move(self, keys):
        if keys[pygame.K_LEFT]:  # Move left
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:  # Move right
            self.rect.x += self.speed
        if keys[pygame.K_UP]:  # Jump (later change to proper jump physics)
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:  # Crouch or move down
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.is_attacking:
            pygame.draw.rect(screen,
                             (255, 255, 0),
                             (self.rect.x + 50, self.rect.y + 20, 20, 10))  # Attack HitBox