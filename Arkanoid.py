import pygame
import math
import random
pygame.init()

def ply_act(x_ply):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        if x_ply < 340:
            x_ply+=5
    if pressed[pygame.K_LEFT] and x_ply > 0:
        x_ply-=5
    return x_ply
def draw_rect(rows,columns,x,y,hit):
    pos_x = 0
    pos_y = 100
    for j in range(rows):
        pos_x = 0
        for i in range(columns):
            pos_list = (columns*j)+i
            if not hit[pos_list]:
                pygame.draw.rect(screen,(255,255,255), pygame.Rect(pos_x,pos_y,x,y),1)
            pos_x+=x
        pos_y+=y
def mov_ball(x_ball,y_ball,x_speed,y_speed):
    x_ball+=x_speed
    y_ball+=y_speed
    return int(x_ball),int(y_ball)
def wall_check(x_ball,y_ball,x_speed,y_speed):
    if x_speed > 0 and (x_ball + 4 < 0 or x_ball + 4 > 400):
            x_speed = -x_speed
    if x_speed < 0 and (x_ball - 4 < 0 or x_ball - 4 > 400):
            x_speed = -x_speed
    if y_ball < 0:
            y_speed = -y_speed
    return x_speed,y_speed
def rect_check(x_ball,y_ball,y_speed,rows,columns,hit,x,y):
    pos_x = 0
    pos_y = 100
    for j in range(rows):
        pos_x = 0
        for i in range(columns):
            pos_list = (columns*j)+i
            if ((pos_x < x_ball  and (pos_x + x) > x_ball  and (pos_y + y + 2) > y_ball and (pos_y + y - 3) < y_ball) or ((pos_x < x_ball  and (pos_x + x) > x_ball  and (pos_y + 2) > y_ball and (pos_y - 3) < y_ball))) and not hit[pos_list]:
                y_speed = -y_speed
                hit[pos_list] = True
            pos_x+=x
        pos_y+=y
    return y_speed,hit
def ply_check(x_ball,y_ball,x_ply,x_speed,y_speed):
    if y_ball < 562 and y_ball > 557 and x_ball > x_ply and x_ball < x_ply + 60:
        speed = 5
        l = 30
        d_origin = (x_ball-x_ply)
        angle = ((d_origin/l)*pi/4+(pi/4))*random.uniform(0.5,1.5)
        x_speed = -cos(angle)*speed
        y_speed = -sin(angle)*speed
    return x_speed,y_speed
def out_check(x_ball,y_ball,x_speed,y_speed,done,lives,x_ply):
    if y_ball > 600:
        lives-=1
        x_ball = 198
        y_ball = 558
        x_speed=5*math.sqrt(2)/2
        y_speed=-5*math.sqrt(2)/2
        x_ply=170
    if lives == 0:
        done = True
    return x_ball,y_ball,x_speed,y_speed,done,lives,x_ply
def side_check(x_ball,y_ball,x_speed,rows,columns,hit,x,y):
    pos_x = 0
    pos_y = 100
    for j in range(rows):
        pos_x = 0
        for i in range(columns):
            pos_list = (columns*j)+i
            if ((pos_x - 2 < x_ball  and (pos_x + 3) > x_ball  and (pos_y + y) > y_ball and (pos_y) < y_ball) or ((pos_x + x - 2 < x_ball  and (pos_x + x + 3) > x_ball  and (pos_y + y) > y_ball and (pos_y) < y_ball))) and not hit[pos_list]:
                x_speed = -x_speed
                hit[pos_list] = True
            pos_x+=x
        pos_y+=y
    return x_speed,hit
screen = pygame.display.set_mode((400,600))
done = False
clock = pygame.time.Clock()
pi = math.pi
cos = math.cos
sin = math.sin
x = 50
y = 15
pos_x = 0
pos_y = 100
lives = 3
columns=10
rows=10
x_ply=170
x_ball = 198
y_ball = 558
x_speed=5*math.sqrt(2)/2
y_speed=-5*math.sqrt(2)/2
hit=[]
for i in range(rows*columns):
    hit.append(False)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    x_ply = ply_act(x_ply)
    x_speed,y_speed = wall_check(x_ball,y_ball,x_speed,y_speed)
    y_speed,hit = rect_check(x_ball,y_ball,y_speed,rows,columns,hit,x,y)
    x_speed,hit = side_check(x_ball,y_ball,x_speed,rows,columns,hit,x,y)
    x_speed,y_speed = ply_check(x_ball,y_ball,x_ply,x_speed,y_speed)
    x_ball,y_ball,x_speed,y_speed,done,lives,x_ply = out_check(x_ball,y_ball,x_speed,y_speed,done,lives,x_ply)
    x_ball,y_ball = mov_ball(x_ball,y_ball,x_speed,y_speed)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255), pygame.Rect(x_ply,560,60,10))
    draw_rect(rows,columns,x,y,hit)
    pygame.draw.circle(screen, (255,255,255), (x_ball,y_ball), 4)
    for i in range(lives):
    	pygame.draw.circle(screen, (255,255,255), (i*15+15, 15), 4)
    pygame.display.flip()
    clock.tick(100)
