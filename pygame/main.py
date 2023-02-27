import pygame
import random


# Classes

class Player:

    def __init__(self, x, y, width, height, velocity, jump_strength=0.3):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.jumping = False
        self._jump_factor = 10
        self.jump_strength = jump_strength
        self.left = False
        self.right = True
        self.walk_count = 0
        self.is_moving = False
        self.health = 90

    def rect(self):
        return self.x, self.y, self.width, self.height

    def position(self):
        return self.x, self.y

    def begin_frame(self):
        self.is_moving = False

    def move_left(self):
        self.x = max(self.x - self.velocity, 0)
        self.left = True
        self.right = False
        self.is_moving = True

    def move_right(self, window):
        self.x = min(self.x + self.velocity, window.width - self.width)
        self.left = False
        self.right = True
        self.is_moving = True

    def jump(self):
        self.jumping = True
        if self._jump_factor >= -10:
            neg = 1
            if self._jump_factor < 0:
                neg = -1
            self.y -= (self._jump_factor ** 2) * self.jump_strength * neg
            self._jump_factor -= 2
        else:
            self.jumping = False
            self._jump_factor = 10

    def draw(self, win):
        if self.is_moving:
            if self.walk_count >= 18:
                self.walk_count = 0
            if self.left:
                win.blit(walk_left[self.walk_count // 6], self.position())
                self.walk_count += 1
            elif self.right:
                win.blit(walk_right[self.walk_count // 6], self.position())
                self.walk_count += 1
        else:
            self.walk_count = 0
            if self.left:
                win.blit(walk_left[self.walk_count // 6], self.position())
            elif player.right:
                win.blit(walk_right[self.walk_count // 6], self.position())
        self.hitbox = (self.x + 2, self.y + 5, self.width - 4, self.height - 10)
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 5))
        pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50 / 100) * (100 - self.health)), 5))



class Win:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def size(self):
        return self.width, self.height


class Worm:
    walk_left = [pygame.image.load('worm1.png'), pygame.image.load('worm2.png'), pygame.image.load('worm3.png'),
                 pygame.image.load('worm4.png'), pygame.image.load('worm5.png'), pygame.image.load('worm6.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walk_count = 0
        self.vel = -4
        self.path = [self.x, self.end]
        self.has_ended = False

    def position(self):
        return self.x, self.y

    def rect(self):
        return self.x, self.y, self.width, self.height

    def draw(self, win):
        win.blit(self.walk_left[self.walk_count // 3], self.position())
        self.hitbox = (self.x, self.y, self.width / 2 + 5, self.height / 2)

    def move(self):
        self.walk_count += 1
        if self.walk_count >= 18:
            self.walk_count = 0
        if self.x < self.end:
            self.has_ended = True
        self.x += self.vel


# Pygame Setup

pygame.init()

p_win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

window = Win(p_win.get_width(), p_win.get_height())
player = Player(0, window.height - 32, 50, 32, 8)

font = pygame.font.Font('PTM55FT.ttf', 30)

pygame.display.set_caption("Badger")

score = 0

walk_right = [pygame.image.load('badger4.png'), pygame.image.load('badger5.png'), pygame.image.load('badger6.png')]
walk_left = [pygame.image.load('badger1.png'), pygame.image.load('badger2.png'), pygame.image.load('badger3.png')]
bg = pygame.image.load('background.png')

worms = []

clock = pygame.time.Clock()


# Game loop

def draw():
    p_win.blit(bg, (0, 0))
    player.draw(p_win)
    text = font.render(str(score), 1, (255, 255, 255))
    p_win.blit(text, (10, 10))
    for w in worms:
        w.draw(p_win)
    pygame.display.update()


def generate_worm():
    rand = random.randint(0, 10000)
    if 0 <= rand <= 200:
        if len(worms) < 5:
            worms.append(Worm(window.width, window.height - 14, 45, 27.5, 0))


def rect_clips(rect1, rect2):
    start_1_x = rect1[0]
    finish_1_x = rect1[0] + rect1[2]
    start_2_x = rect2[0]
    finish_2_x = rect2[0] + rect2[2]

    start_1_y = rect1[1]
    finish_1_y = rect1[1] + rect1[3]
    start_2_y = rect2[1]
    finish_2_y = rect2[1] + rect2[3]

    in_x = finish_1_x >= start_2_x and finish_2_x >= start_1_x
    in_y = finish_1_y >= start_2_y and finish_2_y >= start_1_y

    return in_x and in_y


run = True

while run:
    clock.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for w in worms:
        if w.has_ended:
            worms.pop(worms.index(w))
        else:
            w.move()
            if rect_clips(w.hitbox, player.hitbox):
                worms.pop(worms.index(w))
                score += 1

    player.begin_frame()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_LEFT]:
        player.move_left()
    elif keys[pygame.K_RIGHT]:
        player.move_right(window)
    if keys[pygame.K_UP] or player.jumping:
        player.jump()

    # generate things
    generate_worm()

    # drawing
    draw()

pygame.quit()
