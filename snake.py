import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
x=0
y=0
i=0
r=0
g=225
b=75
rnd_x = 10*random.randint(0,39)
rnd_y = 10*random.randint(0,29)
length = 1
position_x=[]
position_y=[]
for i in range(length):
    position_x.append(0)
    position_y.append(0)
up = False
down = False
right = False
left = False
clock = pygame.time.Clock()

while not done:
    if up:
        y-=10
    if down:
        y+=10
    if right:
        x+=10
    if left:
        x-=10
    position_x.append(x)
    position_y.append(y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            r=random.randint(25,200)
            g=random.randint(25,200)
            b=random.randint(25,200)
    screen.fill((0,0,0))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        up = True
        down = False
        left = False
        right = False
    if pressed[pygame.K_DOWN]:
        down = True
        up = False
        left = False
        right = False
    if pressed[pygame.K_LEFT]:
        left = True
        up = False
        down = False
        right = False
    if pressed[pygame.K_RIGHT]:
        right = True
        up = False
        down = False
        left = False

    if x == rnd_x and y == rnd_y:
        length+=3
        rnd_x = 10*random.randint(0,39)
        rnd_y = 10*random.randint(0,29)
        for i in range(1,length+1):
            while rnd_x == position_x[-i] and rnd_y == position_y[-i]:
                rnd_x = 10*random.randint(0,39)
                rnd_y = 10*random.randint(0,29)

    if len(position_x) > 2*length:
        for i in range(1,length):
            if x == position_x[-i-1] and y == position_y[-i-1]:
                done = True

    if x > 390 or x < 0 or y > 290 or y < 0:
        done = True

    color = (r,g,b)
    pygame.draw.rect(screen,(255,0,0), pygame.Rect(rnd_x,rnd_y,10,10))
    for i in range(length):
        pygame.draw.rect(screen,color, pygame.Rect(position_x[-i-1],position_y[-i-1],10,10))

    pygame.display.flip()
    clock.tick(12)
