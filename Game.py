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
    window = Window('Game Name',500,500)
    Game_instructions= 'Hello'
    window.draw_string(Game_instructions,0,0)
    
    
    
main()
