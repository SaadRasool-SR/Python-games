#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 21:26:33 2019

@author: Saad
"""

from uagame import Window 
import pygame , time
from pygame.locals import *
import math, random 


def main():
    display_width = 800
    display_height = 800
    window = Window('Snake Game',display_width,display_height)
    Game_instructions= ''
    window.draw_string(Game_instructions,0,0)
    window.set_auto_update(False)
    game = Game(window)
    game.play()
    window.close()

class Game:
    
    def __init__(self,window):
        self.window = window
        self.bg_colour = pygame.Color('Black')
        self.close_clicked = False
        self.continue_game = True
        self.window_width = self.window.get_width()
        self.window_height = self.window.get_height()
        self.ball_radius = 5
        self.center = [self.window_width//2,self.window_height//2]
        self.Ball = ball(self.window.get_surface(),'white',[self.center[0],self.center[1]],self.ball_radius)
        self.Snake_Corrd  = [self.window_width//4, self.window_height//4]
        self.Snake_length = 10
        self.Snake_width = 10
        self.set_speed()
        self.Snake_speed_x = 0
        self.Snake_speed_y = 0
        self.Snake_list = []
        self.Snake = snake(self.window.get_surface(), 'Yellow', self.Snake_speed_x, self.Snake_speed_y,self.Snake_actual_speed, self.Snake_list, self.Snake_Corrd[0], self.Snake_Corrd[1], self.Snake_width, self.Snake_length)
        self.ending_string = "YOU LOSE !!!, Would you like to play again (Y/N) ? "
        self.current_font_size = self.window.get_font_height()
        self.curent_colour = self.window.get_font_color()
        self.Score = score(self.window.get_surface(), self.window,self.current_font_size, self.curent_colour)
         
        
        
    def set_speed(self):
        display_string = 'Pick snake speed, between 1 (slow) - 10 (really fast) '
        
        while True:
            try:
                self.user_input = int(self.window.input_string(display_string, 250 , self.center[0]))
                if self.user_input > 10:
                    self.user_input = 10
                    self.Snake_actual_speed = self.user_input
                    break
                elif  self.user_input <= 10:
                    self.Snake_actual_speed = self.user_input
                    break
            except:
                self.window.draw_string('Please enter a integer between 1-10', 250, self.center[0]+30)

        
        
    
    def play(self):
       while not self.close_clicked:
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.handle_event()
            self.draw()
        

    
    def handle_event(self):
        event = pygame.event.poll()
        if event.type == QUIT:
            self.close_clicked = True
    
    def draw(self):
        self.window.clear()
        self.Ball.draw()
        self.Snake.draw()
        self.Score.draw_score()
        self.replay()
        self.window.update()
            
    
    def update(self):
        self.Snake.move()
        if self.Snake.Sn_rect.collidepoint(self.Ball.center[0] - self.ball_radius, self.Ball.center[1] - self.ball_radius):
            self.Snake.grow()
            self.Ball.move()
            self.Score.update_score()
        elif self.Snake.Sn_rect.collidepoint(self.Ball.center[0] + self.ball_radius, self.Ball.center[1] + self.ball_radius):
            self.Snake.grow()
            self.Ball.move()
            self.Score.update_score()
        elif self.Snake.Sn_rect.collidepoint(self.Ball.center[0] - self.ball_radius,self.Ball.center[1]): 
            self.Snake.grow()
            self.Ball.move()
            self.Score.update_score()
        elif self.Snake.Sn_rect.collidepoint(self.Ball.center[0] + self.ball_radius,self.Ball.center[1]):
            self.Snake.grow()
            self.Ball.move()
            self.Score.update_score()
    
    def decide_continue(self):
        if self.Snake.Collide():
            self.continue_game = False
            
    def replay(self):
        if self.Snake.Collide():
            self.window.set_font_color(self.curent_colour)
            time.sleep(1)
            self.window.clear()
            event = pygame.event.poll()
            user_input = self.window.input_string(self.ending_string,250,self.center[1])
            if user_input.upper() == 'Y':
                main()
            elif user_input.upper() == 'N':
                self.window.clear()
                self.close_clicked = True
                
                
class snake:
    
    def __init__(self, surface, colour, speed_x, speed_y, speed_actual, snake_list, x_coord, y_coord, width, length):
        self.surface = surface
        self.colour = pygame.Color(colour)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.actual_speed = speed_actual
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.length = length
        self.Sn_rect = Rect(self.x_coord, self.y_coord, self.width, self.length)
        self.size = self.surface.get_size()
        self.Sn_list = snake_list
        self.Sn_head = []
        self.Snake_list_len = 20
        
    def draw (self):     
        for XnY in self.Sn_list:
            pygame.draw.rect(self.surface, self.colour, [XnY[0], XnY[1], self.length, self.width])
            
    def move(self):
        self.Sn_head = []
        self.Sn_rect = Rect(self.x_coord, self.y_coord, self.width, self.length)
        key_list = pygame.key.get_pressed()
        if key_list[K_RIGHT] == True:
            self.speed_x = self.actual_speed
            self.speed_y = 0
        elif key_list[K_LEFT] == True:
            self.speed_x = -self.actual_speed
            self.speed_y = 0
        elif key_list[K_UP] == True:
            self.speed_y = -self.actual_speed
            self.speed_x = 0
        elif key_list[K_DOWN] == True:
            self.speed_y = self.actual_speed
            self.speed_x = 0
        self.x_coord += self.speed_x
        self.y_coord += self.speed_y 
        self.Sn_head.append(self.x_coord)
        self.Sn_head.append(self.y_coord)
        self.Sn_list.append(self.Sn_head)
        self.Sn_rect = Rect(self.x_coord, self.y_coord, self.width, self.length)
        
        if len(self.Sn_list) > self.Snake_list_len:
            del self.Sn_list[0]
    
    def Collide(self):  
        if self.x_coord <= 0 or self.x_coord + self.width >= self.size[0]:
            return True   
        if self.y_coord <= 0 or self.y_coord + self.length >= self.size[1]:
            return True     
        if self.Sn_head in self.Sn_list[:-20]:
            return True

    def grow(self):
        self.Snake_list_len += 10
        
        
class ball:
    def __init__(self,surface,colour,center,radius):
        self.surface = surface
        self.colour = pygame.Color(colour)
        self.center = center
        self.radius = radius
        self.size = self.surface.get_size()
    
    def draw(self):
        pygame.draw.circle(self.surface, self.colour, self.center, self.radius)
    
    def move(self):
        x = random.randint(0 + 10,self.size[0] - 10)
        y = random.randint(0 + 24,self.size[1] - 10)
        self.center = [x,y]
        
    
class score:
    def __init__(self, surface, window, font, colour):
        self.surface = surface 
        self.score_is = 0
        self.window = window
        self.window.set_font_size(24)
        self.window.set_font_color('White')
        self.font = font
        self.colour = colour
    
    def update_score(self):
        self.score_is += 10
        
    
    def draw_score(self):
        self.window.draw_string('Score : ' + str(self.score_is),10,10)   

        

main()
