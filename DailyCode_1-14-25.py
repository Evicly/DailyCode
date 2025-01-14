import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 72)

score = 0
running = True

class Bird:
    def __init__(self):
        self.y = 400
        self.velocity = 0

    def flap(self):
        self.velocity = -3

    def physics(self):
        self.velocity += 0.1
        self.y += self.velocity

    def draw(self):
        pygame.draw.rect(screen, (255,0,0), (50, self.y, 30, 30))

bird = Bird()

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, 400)
        self.gap = 150

    def move(self):
        self.x -= 2

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, 50, self.height))

        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.height + self.gap, 50, 600 - (self.height + self.gap)))

pipes = []
spawn_pipe = 0

def check_collision(bx, by, px, py):
    if bx + 30 > px and bx < px + 50 and by < py:
        return True
    if bx + 30 > px and bx < px + 50 and by + 30 > py + 150:
        return True
    return False


ticker = 0

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bird.flap()

    ticker+=1
    if ticker%10 == 0:
        ticker = 0
        score+=1

    spawn_pipe += 1
    if spawn_pipe >= 150:
        pipes.append(Pipe(800))
        spawn_pipe = 0
    for pipe in pipes:
        pipe.move()
        if check_collision(50, bird.y, pipe.x, pipe.height):
            running = False
    i = len(pipes) - 1
    while i >= 0:
        if pipes[i].x <= -50:
            pipes.pop(i)
        i -= 1

    bird.physics()

    screen.fill((0,0,0))

    score_text = font.render("Score", True, (255,255,255))
    screen.blit(score_text, (650, 20))
    score_text2 = font.render(str(score), True, (255,255,255))
    screen.blit(score_text2, (750, 20))
    bird.draw()

    for pipe in pipes:
        pipe.draw()

    pygame.display.flip()
text = font2.render("GAME OVER", True, (255,50,50))
screen.blit(text, (200,200))
pygame.display.flip()
pygame.time.delay(2000)
pygame.quit()