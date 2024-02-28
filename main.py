import pygame
import random
from os import path
blue =  (18,10,143)
black = (0,0,0)
green = (0,255,0)
white = (255,255,255)
dis_width = 800
dis_height = 600
pygame.init()
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()
FPS = 3


snake_list = []
x1 = dis_width /2
y1 = dis_height /2

snake_block = 30
snake_step = 30

x1_change = 0
y1_change = 0
length = 1

img_dir= path.join(path.dirname(__file__), "img")
music_dir= path.join(path.dirname(__file__), "music")
bg = pygame.image.load(path.join(img_dir, "фон_столкновение_светлый.jpg")).convert()
bg = pygame.transform.scale(bg, (dis_width,dis_height))
bg_rect=bg.get_rect()
win_sound=pygame.mixer.Sound(path.join(music_dir,"звук_съедания.ogg"))
win_sound.set_volume(0.5)
pygame.mixer.music.load(path.join(music_dir,"музыка_пыяла.mp3"))
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
run= True

head_images = [pygame.image.load(path.join(img_dir, "HeadR.png")).convert(),
               pygame.image.load(path.join(img_dir, "HeadL.png")).convert(),
               pygame.image.load(path.join(img_dir, "HeadB.png")).convert(),
               pygame.image.load(path.join(img_dir, "HeadT.png")).convert()]

snake_tail_img = [pygame.image.load(path.join(img_dir, "tailright.png")).convert(),
               pygame.image.load(path.join(img_dir, "tailleft.png")).convert(),
               pygame.image.load(path.join(img_dir, "taildown.png")).convert(),
               pygame.image.load(path.join(img_dir, "tailup.png")).convert()]

def draw_head (i,snake_list):
    snake_head_img_now = head_images[i]
    snake_head = pygame.transform.scale(snake_head_img_now, (snake_block, snake_block))
    snake_head.set_colorkey(black)
    snake_head_rect = snake_head.get_rect(x=snake_list[-1][0], y=snake_list[-1][1])
    dis.blit(snake_head, snake_head_rect)

def draw_tail (i,snake_list):
    snake_tail_img_now = snake_tail_img[i]
    snake_tail = pygame.transform.scale(snake_tail_img_now, (snake_block, snake_block))
    snake_tail.set_colorkey(white)
    snake_tail_rect = snake_tail.get_rect(x=snake_list[0][0], y=snake_list[0][1])
    dis.blit(snake_tail, snake_tail_rect)

def eating_check(xcor, ycor, foodx, foody):
    if foodx - snake_block <= xcor <= foodx + snake_block:
       if foody - snake_block <= ycor <= foody + snake_block:
           return True
    else:
        return False
foodx = random.randrange(50,500)
foody = random.randrange(50,500)

food_img = [pygame.image.load(path.join(img_dir,"Sweets1.png")).convert(),
            pygame.image.load(path.join(img_dir,"Sweets2.png")).convert(),
            pygame.image.load(path.join(img_dir,"Sweets3.png")).convert(),
            pygame.image.load(path.join(img_dir,"Sweets4.png")).convert(),
            pygame.image.load(path.join(img_dir,"Sweets5.png")).convert(),
            pygame.image.load(path.join(img_dir,"Sweets6.jpg")).convert()]
food = pygame.transform.scale(random.choice(food_img),( 70,70))
food.set_colorkey(white)
food_rect = food.get_rect(x=foodx, y=foody)
i = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_step
                y1_change = 0
                i = 1
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_step
                y1_change = 0
                i=0
            elif event.key == pygame.K_UP:
                y1_change = -snake_step
                x1_change = 0
                i=3
            elif event.key == pygame.K_DOWN:
                y1_change = snake_step
                x1_change = 0
                i=2

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        run=False
    x1 += x1_change
    y1 += y1_change

    dis.fill(blue)
    dis.blit(bg, bg_rect)
    dis.blit(food,food_rect)
    # pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
    snake_head = [x1,y1]
    snake_list.append(snake_head)
    if len(snake_list)> length:
        del snake_list[0]
    for x in snake_list[1:-1]:
        if x == snake_head:
            run = False
    for x in snake_list[1:]:
        snake_img = pygame.image.load(path.join(img_dir, "body3.png")).convert()
        snake = pygame.transform.scale(snake_img, (snake_block, snake_block))
        snake.set_colorkey(white)
        dis.blit(snake, (x[0], x[1]))
    for x in snake_list[1:-1]:
         if x == snake_head:
            run = False

    draw_head(i, snake_list)
    draw_tail(i, snake_list)
    pygame.display.update()
    if eating_check(x1,y1,foodx,foody) :
        foodx = random.randrange(50, 500)
        foody = random.randrange(50, 500)
        food_img = [pygame.image.load(path.join(img_dir, "Sweets1.png")).convert(),
                    pygame.image.load(path.join(img_dir, "Sweets2.png")).convert(),
                    pygame.image.load(path.join(img_dir, "Sweets3.png")).convert(),
                    pygame.image.load(path.join(img_dir, "Sweets4.png")).convert(),
                    pygame.image.load(path.join(img_dir, "Sweets5.png")).convert(),
                    pygame.image.load(path.join(img_dir, "Sweets6.jpg")).convert()]

        food = pygame.transform.scale(random.choice(food_img), (70, 70))
        food.set_colorkey(white)
        food_rect = food.get_rect(x=foodx, y=foody)
        length += 1
        win_sound.play()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
quit()

