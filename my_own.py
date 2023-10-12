from random import *
import pygame
from pygame import mixer
from time import *
pygame.init()
window=pygame.display.set_mode((800,500))
pygame.display.set_caption('KipiLearn_Family')
pygame.display.update()
# Background Image
back1=pygame.image.load('background.jpg')
no=pygame.image.load('nor.jpg')
yes=pygame.image.load('yesr.jpg')
start=pygame.image.load('start.jpg')
exit1=pygame.image.load('exit.jpg')
snake=pygame.image.load('snake.png')
frog=pygame.image.load("frog.png")
frog2=pygame.image.load("tadpole.png")
# Background Sound
sound=mixer.Sound('eat_snake.mp3')
background_sound=mixer.Sound("background.mp3")
clicks=mixer.Sound("click.mp3")
haha=mixer.Sound("game_over1.mp3")
background_sound.play(-1)
clock=pygame.time.Clock()
def score(text,color,text_size,x,y):
    font=pygame.font.SysFont('cascadia code',text_size,bold=1)
    score_player=font.render(text,True,color)
    window.blit(score_player,[x,y])
def make_snake(window,list):
    for x,y in list:
        window.blit(snake,(x,y))
def game_start():
    #switch
    butt=2
    while True:
        # take=pygame.key.get_pressed()
        if butt==2 :
            window.blit(start,(0,0))
        for pres in pygame.event.get():
            if pres.type==pygame.QUIT:
                quit()
            if pres.type==pygame.KEYDOWN:
                if pres.key==pygame.K_LEFT:
                    window.blit(start,(0,0))
                    butt=1
                    clicks.play()
                if pres.key==pygame.K_RETURN and butt!=0:
                    game_Logic()
                if pres.key==pygame.K_RIGHT:
                    window.blit(exit1,(0,0))
                    butt=0
                    clicks.play()
                if butt==1 and pres.key==pygame.K_RETURN:
                    game_Logic()
                elif butt==0 and pres.key==pygame.K_RETURN:
                    exit()
            clock.tick(60)
            pygame.display.update()
def game_Logic():
    with open('highscore.txt','r') as f:
        high=f.read()
    #Variable Section....
    lis=[]
    snake_lenght=1
    posx=155
    game_exit=False
    game_over=False
    posy=250
    velox=0
    big=1
    foodx=randint(28,740)
    foody=randint(65,445)
    veloy=0
    speed=1
    point=0     
    fps=70
    flag=0
    but=2
    while not game_exit:
        if game_over:
            with open('highscore.txt','w') as f:
                f.write(str(high))
            if but==2:
                haha.play()
                window.blit(no,(0,0))
            for pres in pygame.event.get():
                if pres.type==pygame.QUIT:
                    game_exit=True
                if pres.type==pygame.KEYDOWN:
                    if pres.key==pygame.K_RETURN and but!=1:
                       game_Logic() 
                    if pres.key==pygame.K_RIGHT:
                        window.blit(yes,(0,0))
                        clicks.play()
                        but=1
                        clicks.play()
                    if pres.key==pygame.K_LEFT:
                        window.blit(no,(0,0))
                        clicks.play()
                        but=0
                        clicks.play()
                    if but==1 and pres.key==pygame.K_RETURN:
                        exit()
                    elif but==0 and pres.key==pygame.K_RETURN:
                        game_Logic()
                pygame.display.update()
        else:
            for avik in pygame.event.get():
                if avik.type == pygame.QUIT:
                    game_exit=True
                if avik.type == pygame.KEYDOWN:
                    if avik.key==pygame.K_RIGHT:
                        velox=speed
                        veloy=0
                    if avik.key==pygame.K_LEFT:
                        velox=-speed
                        veloy=0
                    if avik.key==pygame.K_UP:
                        veloy=-speed
                        velox=0
                    if avik.key==pygame.K_DOWN:
                        veloy=speed
                        velox=0
            if abs(foodx-posx)<=7 and abs(foody-posy)<=7:
                point+=5
                if int(high)<point:
                    high=point
                nikal=mixer.Sound('eat_snake1.mp3')
                nikal.play()
                foodx=randint(28,740)
                foody=randint(65,445)
                snake_lenght+=2
                speed+=.3
                big+=1
                if flag==1:
                    point+=50
                    if int(high)<point:
                        high=point
                    flag=0
                if big%6==0:
                    foodx=randint(28,740)
                    foody=randint(65,445)
                    flag=1
            posx+=velox
            posy+=veloy
            head=[]
            head.append(posx)
            head.append(posy)
            lis.append(head)
            if len(lis)>snake_lenght:
                del lis[0]
            if head in lis[:-1]:
                game_over=True
            if posx>750 or posx<33 or posy>455 or posy<63:
                sound.play()
                sleep(2)
                game_over=True
            window.blit(back1,(0,0))
            score('Score : '+str(point),'darkblue',25,2,5)
            score('KipiLearn Family','Red',25,600,2)
            score('Highest Score : '+ str(high),'blue',25,230,6)
            make_snake(window,lis)
            if big%6!=0:
                window.blit(frog2,(foodx,foody))
            else:
                window.blit(frog,(foodx,foody))        
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
game_start()