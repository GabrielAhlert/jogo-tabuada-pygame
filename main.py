import pygame, random
#Let's import the Player Class
from player import Player
from barrier import Barrier

pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 100, 100)
DARKRED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
DARKBLUE = (0, 0, 255)

speed = 1
barrierSpeed = 20
posibleRange = (1,5)
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)


SCREENWIDTH=800
SCREENHEIGHT=600

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Player Racing")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()


playerPlayer1 = Player(DARKBLUE, 60, 80, 70)
playerPlayer1.rect.x = 130
playerPlayer1.rect.y = SCREENHEIGHT - 100

playerPlayer2 = Player(DARKRED, 60, 80, 70)
playerPlayer2.rect.x = 530
playerPlayer2.rect.y = SCREENHEIGHT - 100

Barrier1 = Barrier(random.choice(colorList), 60, 80, barrierSpeed, 1)
Barrier1.rect.x = 50
Barrier1.rect.y = -100

Barrier2 = Barrier(random.choice(colorList), 60, 80, barrierSpeed, 1)
Barrier2.rect.x = 130
Barrier2.rect.y = -100

Barrier3 = Barrier(random.choice(colorList), 60, 80, barrierSpeed, 1)
Barrier3.rect.x = 210
Barrier3.rect.y = -100

Barrier4 = Barrier(random.choice(colorList), 60, 80, barrierSpeed, 1)
Barrier4.rect.x = 290
Barrier4.rect.y = -100

Barrier5 = Barrier(random.choice(colorList), 60, 80, barrierSpeed, 1)
Barrier5.rect.x = 450
Barrier5.rect.y = -100

Barrier6 = Barrier(random.choice(colorList), 60, 80, barrierSpeed, 1)
Barrier6.rect.x = 530
Barrier6.rect.y = -100

Barrier7 = Barrier(random.choice(colorList), 60, 80, barrierSpeed, 1)
Barrier7.rect.x = 610
Barrier7.rect.y = -100

Barrier8 = Barrier(random.choice(colorList), 60, 80, barrierSpeed, 1)
Barrier8.rect.x = 690
Barrier8.rect.y = -100


# Add the Player to the list of objects
all_sprites_list.add(playerPlayer1)
all_sprites_list.add(playerPlayer2)
all_sprites_list.add(Barrier1)
all_sprites_list.add(Barrier2)
all_sprites_list.add(Barrier3)
all_sprites_list.add(Barrier4)
all_sprites_list.add(Barrier5)
all_sprites_list.add(Barrier6)
all_sprites_list.add(Barrier7)
all_sprites_list.add(Barrier8)

all_coming_BarriersLeft = pygame.sprite.Group()
all_coming_BarriersLeft.add(Barrier1)
all_coming_BarriersLeft.add(Barrier2)
all_coming_BarriersLeft.add(Barrier3)
all_coming_BarriersLeft.add(Barrier4)

all_coming_BarriersRight = pygame.sprite.Group()
all_coming_BarriersRight.add(Barrier5)
all_coming_BarriersRight.add(Barrier6)
all_coming_BarriersRight.add(Barrier7)
all_coming_BarriersRight.add(Barrier8)

numbersLeft = []
numbersRight = []

for Barrier in all_coming_BarriersLeft:
    number = random.randint(posibleRange[0],posibleRange[1])
    Barrier.setNumber(number)
    numbersLeft.append(number)

for Barrier in all_coming_BarriersRight:
    number = random.randint(posibleRange[0],posibleRange[1])
    Barrier.setNumber(number)
    numbersRight.append(number)

anwser = random.choice(numbersLeft) * random.choice(numbersRight)


#Allowing the user to close the window...
PlayerryOn = True
clock=pygame.time.Clock()

while PlayerryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                PlayerryOn=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    playerPlayer1.moveRight(80)
                elif event.key==pygame.K_a:
                    playerPlayer1.moveLeft(80)
                elif event.key==pygame.K_LEFT:
                    playerPlayer2.moveLeft(80)
                elif event.key==pygame.K_RIGHT:
                    playerPlayer2.moveRight(80)

        for Barrier in all_coming_BarriersLeft:
            Barrier.moveForward(speed)
            if Barrier.rect.y > SCREENHEIGHT:
                numbersLeft = []
                for barrier in all_coming_BarriersLeft:
                    number = random.randint(posibleRange[0],posibleRange[1])
                    numbersLeft.append(number)
                    barrier.repaint(random.choice(colorList))
                    barrier.rect.y = -200
                    barrier.setNumber(number)
                numbersRight = []
                for barrier in all_coming_BarriersRight:
                    number = random.randint(posibleRange[0],posibleRange[1])
                    numbersRight.append(number)
                    barrier.repaint(random.choice(colorList))
                    barrier.rect.y = -200
                    barrier.setNumber(number)
                numberleft = random.choice(numbersLeft)
                numberright = random.choice(numbersRight)
                anwser = numberleft * numberright
                print("anwser: " + str(anwser))
                print("left: " + str(numberleft))
                print("right: " + str(numberright))

        
        for Barrier in all_coming_BarriersRight:
            Barrier.moveForward(speed)
            
        # #Game Logic
        # for Barrier in all_coming_BarriersLeft:
        #     Barrier.moveForward(speed)
        #     if Barrier.rect.y > SCREENHEIGHT:
        #         #Barrier.changeSpeed(random.randint(barrierSpeed, 100))
        #         Barrier.repaint(random.choice(colorList))
        #         Barrier.rect.y = -200
        #         Barrier.setNumber(random.randint(1,10))


        # for Barrier in all_coming_BarriersRight:
        #     Barrier.moveForward(speed)
        #     if Barrier.rect.y > SCREENHEIGHT:
        #         #Barrier.changeSpeed(random.randint(barrierSpeed, 100))
        #         Barrier.repaint(random.choice(colorList))
        #         Barrier.rect.y = -200
        #         Barrier.setNumber(random.randint(1,10))

        all_sprites_list.update()

        #Drawing on Screen
        screen.fill(GREEN)

        #Draw The Road
        pygame.draw.rect(screen, GREY, [40,0, 320,SCREENHEIGHT])
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [120,0],[120,SCREENHEIGHT],5)
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [200,0],[200,SCREENHEIGHT],5)
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [280,0],[280,SCREENHEIGHT],5)

        #Draw The Second Road
        pygame.draw.rect(screen, GREY, [440,0, 320,SCREENHEIGHT])
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [520,0],[520,SCREENHEIGHT],5)
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [600,0],[600,SCREENHEIGHT],5)
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [680,0],[680,SCREENHEIGHT],5)

        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)

        # Draw the score and top score  
        pygame.draw.rect(screen, (0,0,0), [0,0, SCREENWIDTH,80])
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Score: " + str(10),True,WHITE)
        screen.blit(text, [20, 10])
        text = font.render("Top Score: " + str(10),True,WHITE)
        screen.blit(text, [20, 40])

        
        # Draw Rules to win match
        font = pygame.font.SysFont('Calibri', 40, True, False)
        text = font.render("       X        = " + str(anwser),True,WHITE)
        screen.blit(text, (288, 20))
        pygame.draw.rect(screen, DARKBLUE, [300,20, 40,40])
        pygame.draw.rect(screen, DARKRED, [380,20, 40,40])

        #Refresh Screen
        pygame.display.flip()

        #Number of frames per secong e.g. 60
        clock.tick(60)

pygame.quit()