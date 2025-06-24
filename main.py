import pygame
import pygame.gfxdraw
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

circle_center = (WIDTH // 2, HEIGHT // 2)
circle_radius = 250

class Ball:
    def __init__(self):
        self.radius = 20
        angle = random.uniform(0, 2*math.pi)
        r = random.uniform(0, circle_radius - self.radius)
        self.x = circle_center[0] + r * math.cos(angle)
        self.y = circle_center[1] + r * math.sin(angle)
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.vel_x = random.uniform(-4, 4)
        self.vel_y = random.uniform(-8, -4)
        self.gravity = 0
        self.bounce_factor = 1

    def update(self):
        self.vel_y += self.gravity
        self.x += self.vel_x
        self.y += self.vel_y

        dx = self.x - circle_center[0]
        dy = self.y - circle_center[1]
        dist = math.hypot(dx, dy)

        if dist + self.radius > circle_radius:
            overlap = dist + self.radius - circle_radius
            nx = dx / dist
            ny = dy / dist
            self.x -= nx * overlap
            self.y -= ny * overlap

            vn = self.vel_x * nx + self.vel_y * ny
            self.vel_x -= 2 * vn * nx * self.bounce_factor
            self.vel_y -= 2 * vn * ny * self.bounce_factor

    def draw(self, surface):
        pygame.gfxdraw.aacircle(surface, int(self.x), int(self.y), self.radius, self.color)
        pygame.gfxdraw.filled_circle(surface, int(self.x), int(self.y), self.radius, self.color)

balls = [Ball() for _ in range(7)]

running = True
while running:
    screen.fill((30, 30, 30))

    pygame.draw.circle(screen, (40, 40, 40), circle_center, circle_radius)
    pygame.draw.circle(screen, (200, 200, 200), circle_center, circle_radius, 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for ball in balls:
        ball.update()
        ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
