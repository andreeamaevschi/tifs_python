import pygame
import sys
import random
#1
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

pygame.display.set_caption("Golden Dash")

#2
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

#3
class PatrateAurii(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = 0
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - 30)
            self.rect.y = 0
            self.speed = random.randint(1, 3)

#4
class PatrateRosii(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = 0
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - 30)
            self.rect.y = 0
            self.speed = random.randint(1, 3)

#5
all_sprites = pygame.sprite.Group()
patrate_aurii = pygame.sprite.Group()
patrate_rosii = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

def show_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Scor: {score}", True, WHITE)
    WIN.blit(text, (10, 10))

def game_over():
    font = pygame.font.Font(None, 72)
    text = font.render("Ai pierdut!", True, WHITE)
    WIN.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)
    main()

def main():
    score = 0

    for _ in range(5):
        patrat_auriu = PatrateAurii()
        all_sprites.add(patrat_auriu)
        patrate_aurii.add(patrat_auriu)

    for _ in range(3):
        patrat_rosu = PatrateRosii()
        all_sprites.add(patrat_rosu)
        patrate_rosii.add(patrat_rosu)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        all_sprites.update()

        hits_golden = pygame.sprite.spritecollide(player, patrate_aurii, True)
        for hit in hits_golden:
            score += 1
            patrat_auriu = PatrateAurii()
            all_sprites.add(patrat_auriu)
            patrate_aurii.add(patrat_auriu)

        hits_red = pygame.sprite.spritecollide(player, patrate_rosii, False)
        if hits_red:
            game_over()

        WIN.fill((0, 0, 0))
        all_sprites.draw(WIN)
        show_score(score)

        pygame.display.flip()

        clock.tick(60)

main()
