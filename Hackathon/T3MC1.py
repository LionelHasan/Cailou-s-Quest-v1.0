import os
from pickle import FALSE, TRUE
from tkinter.messagebox import QUESTION
from turtle import update
import pygame
from pygame import mixer
import random

from pygame import MOUSEBUTTONDOWN, key

pygame.font.init()
pygame.mixer.init() # load audio portion of pygame


WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
WIDTH, HEIGHT = 1700, 900
CAILOU_WIDITH = 150
CAILOU_HEIGHT = 150
COIN_HEIGHT = 50
COIN_WIDITH = 75
SQUARE_WIDITH = 30
SQUARE_HEIGHT = 30
CAILOU_VEL_X = 5
CAILOU_VEL_Y = 5
QUESTION_FONT =  pygame.font.SysFont("times new roman",55)
MC_FONT = pygame.font.SysFont("times new roman",40)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BACK_MAIN = pygame.transform.scale(pygame.image.load(os.path.join('Sounds and Images','cailou house.jpg')),(WIDTH, HEIGHT))

BACK_MC = pygame.transform.scale(pygame.image.load(os.path.join('Sounds and Images','mc.jpg')),(WIDTH, HEIGHT))


VICTORY_SCREEN = pygame.transform.scale(pygame.image.load(os.path.join('Sounds and Images','Victory.jpg')),(WIDTH, HEIGHT))

mixer.music.load('theme.wav')
mixer.music.play(-1)

WRONG_ANWSER = pygame.mixer.Sound(os.path.join('Sounds and Images','wrong anwser.wav'))

RIGHT_ANWSER = pygame.mixer.Sound(os.path.join('Sounds and Images','right anwser.wav'))

COIN_SOUND = pygame.mixer.Sound(os.path.join('Sounds and Images','coin.wav'))


CAILOU_NON_SCALE = pygame.image.load(os.path.join('Sounds and Images','cailou.png'))   # Load Liam in 
CAILOU = pygame.transform.scale(CAILOU_NON_SCALE,(CAILOU_HEIGHT,CAILOU_WIDITH))


COIN_NON_SCALE = pygame.image.load(os.path.join('Sounds and Images','Mario coin.PNG'))
COIN = pygame.transform.scale(COIN_NON_SCALE,(COIN_HEIGHT,COIN_WIDITH))

COIN_REACHED = pygame.USEREVENT + 1

FPS = 60
cailou_char = pygame.Rect(100,10, CAILOU_WIDITH, CAILOU_HEIGHT)
coin_obj = pygame.Rect(900,500, COIN_WIDITH, COIN_HEIGHT)
a = pygame.Rect(10,145, SQUARE_WIDITH, SQUARE_HEIGHT)
b = pygame.Rect(10,295, SQUARE_WIDITH, SQUARE_HEIGHT)
c = pygame.Rect(10,495, SQUARE_WIDITH, SQUARE_HEIGHT)
d = pygame.Rect(10,695, SQUARE_WIDITH, SQUARE_HEIGHT)

class GameState():
    def __init__(self):
        self.state = 'main_game'
    
    def main_game(self):

        for event in pygame.event.get():    # check if the user quits
            if event.type == pygame.QUIT:
                pygame.quit() 
     

        def draw_window(cailou_char, coin_obj):
            WIN.blit(BACK_MAIN, (0,0))
            WIN.blit(CAILOU, (cailou_char.x, cailou_char.y))
            WIN.blit(COIN,(coin_obj.x,coin_obj.y))
            pygame.display.update()

        def movement(cailou_char, coin_obj):
            keys_pressed = pygame.key.get_pressed()
            coin_vel1 = 10
            coin_vel2 = 10
            coin_vel3 =10
            coin_vel4 = 10
            coin_vel1 = coin_vel1 + random.randint(-20,20)
            coin_vel2 = coin_vel2 + random.randint(-20,20)
            coin_vel3 = coin_vel3 + random.randint(-20,20)
            coin_vel4 = coin_vel4 + random.randint(-20,20)

            if keys_pressed[pygame.K_a] and cailou_char.x >= 0:    #for moving left
                cailou_char.x -= CAILOU_VEL_X 
            
            if keys_pressed[pygame.K_d] and cailou_char.x <= WIDTH - CAILOU_WIDITH:    #for moving right
                cailou_char.x += CAILOU_VEL_X 
            
            if keys_pressed[pygame.K_w] and cailou_char.y >= 0:    #for moving up
                cailou_char.y -= CAILOU_VEL_Y 
            
            if keys_pressed[pygame.K_s] and cailou_char.y <= HEIGHT - CAILOU_HEIGHT:    #for moving down
                cailou_char.y += CAILOU_VEL_Y

            if  coin_obj.x >= 0:    #for moving left
                coin_obj.x -= coin_vel1 
            
            if  coin_obj.x <= WIDTH - COIN_WIDITH - 100:    #for moving right
                coin_obj.x += coin_vel2 
            
            if  coin_obj.y >= 0:    #for moving up
                coin_obj.y -= coin_vel3 
            
            if  coin_obj.y <= HEIGHT - COIN_HEIGHT - 100:     #for moving down
                coin_obj.y += coin_vel4

        def coin_reached(cailou_char, coin_obj):
            if cailou_char.colliderect(coin_obj):
                COIN_SOUND.play()
                coin_obj.x = 50000  
                coin_obj.y = 50000
                self.state = "multiple_choice"
               
        movement(cailou_char, coin_obj) 
        draw_window(cailou_char, coin_obj)    
        coin_reached(cailou_char, coin_obj)
    
    def multiple_choice(self):
        point = pygame.mouse.get_pos()
        for event in pygame.event.get():    # check if the user quits  
            pygame.display.update() 
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if c.collidepoint(point):
                    RIGHT_ANWSER.play()
                    self.state = 'password' 
                if a.collidepoint(point):
                    color = RED
                    WRONG_ANWSER.play()
                    pygame.draw.rect(WIN, color, a)
                    pygame.display.update()
                if b.collidepoint(point):
                    color2 = RED
                    WRONG_ANWSER.play()
                    pygame.draw.rect(WIN, color2, b)
                    pygame.display.update()
                if d.collidepoint(point):
                    color3 = RED
                    WRONG_ANWSER.play()
                    pygame.draw.rect(WIN, color3, d)
                    pygame.display.update()

        collide = a.collidepoint(point)
        collide1 = b.collidepoint(point)
        collide2 = c.collidepoint(point)
        collide3 = d.collidepoint(point)

        color = GREEN if collide else BLACK  
        color1 = GREEN if collide1 else BLACK
        color2 = GREEN if collide2 else BLACK
        color3 = GREEN if collide3 else BLACK

        WIN.blit(BACK_MAIN, (0,0))
        pygame.draw.rect(WIN, color, a)
        pygame.draw.rect(WIN, color1, b)
        pygame.draw.rect(WIN, color2, c)
        pygame.draw.rect(WIN, color3, d)
        question_text = QUESTION_FONT.render('When will an else statement be executed?', 1,BLACK)
        a_text = MC_FONT.render('a.) When the if statement has been executed, but none of the elif statement(s)', 1,BLACK)
        b_text = MC_FONT.render('b.) When neither the if or elif statements have been executed', 1,BLACK)
        c_text = MC_FONT.render('c.) When both the if and elif statements have been executed', 1,BLACK)
        d_text = MC_FONT.render('d.) When the elif statement(s) has been executed, but none of the if statements', 1,BLACK)
        WIN.blit(question_text, (10,10))
        WIN.blit(a_text,(50,130))
        WIN.blit(b_text, (50,280))
        WIN.blit(c_text,(50,480))
        WIN.blit(d_text, (50,685))                
        
    def password(self):
        for event in pygame.event.get():    # check if the user quits
            if event.type == pygame.QUIT:
                pygame.quit()  

        def draw_password():
            WIN.blit(VICTORY_SCREEN, (0,0))
            password_text = MC_FONT.render('Password: q3eVnS', 1, BLACK)
            WIN.blit(password_text,(730,380))
            pygame.display.update()
        
        draw_password()

    def state_manager(self):
        if self.state == "main_game":
            self.main_game()
        if self.state == "multiple_choice":
            self.multiple_choice()
        if self.state == "password":
            self.password()
    
def main():
    game_state = GameState()
    clock = pygame.time.Clock()
    run = True
    while run:  # loops to check for different events in game
        game_state.state_manager()
        clock.tick(FPS) # Cap frame rate

if __name__ == "__main__":
    main()


    

