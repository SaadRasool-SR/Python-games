#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:06:15 2019

@author: Saad
"""
# frictionloss calculations in a pipe 

import math 

def User_Inputs():
    Pipe_Length = float(input('Please enter the length of the pipe (m)' + '\n'))
    Pipe_Inner_Diamter= float(input('Please enter the inner diameter of the pipe (m)'+ '\n'))
    Pipe_Roughness = float(input('Please enter the roughness of the pipe (E) (m)'+ '\n'))
    Fluid_Density = float(input('Please enter the density of the transport fluid in the pipe (kg/m3)'+ '\n'))
    Fluid_Viscoisty = float(input('Please enter the viscosity of the fluid (Pa * s)'+ '\n'))
    Q = float(input('Please enter the volumetric flow rate (m3/s)'+ '\n'))  
    V = Fluid_Velocity(Q,Pipe_Inner_Diamter)
    Re = Reynolds_Number(V,Fluid_Viscoisty,Fluid_Density,Pipe_Inner_Diamter,Pipe_Roughness,Pipe_Length)
    
    
    
def Fluid_Velocity(Q, ID):
    A = math.pi * 0.25 * math.pow(ID,2)
    V = Q/A
    print('Outputs')
    print('/n' str(V) + ' m/s')
    return V

def Reynolds_Number(V,u,p,ID,Pipe_Roughness,Pipe_Length):
    
    re = (p* V * ID)/u
    
    if re > 4000:
        print('Turbulent Flow ' + str(re))
        Friction_Factor_Turbulent(re,ID,Pipe_Roughness,Pipe_Length,V,p)
    elif re < 2100:
        print('Laminar Flow ' + str(re))
        Friction_Factor_Laminar(re,ID,Pipe_Roughness,Pipe_Length,V,p)
        
    else:
        print('Reynold number ' + str(re) + ' Transitional Flow ')
        
def Friction_Factor_Turbulent(re,ID,E,L,V,p):  # using Clerbrook formula to calculate friction factor
    guess = 0.01
    x = True 
    while x :
        srt_g = math.sqrt(guess)
        E_D = E/ID
        Re_srt = E_D/3.7 + 2.51/(re * srt_g)
        log_T = -2 * math.log10(Re_srt)
        f = 1/log_T
        guess_2 = math.pow(f,2)
        error = (guess_2 - guess)/(guess_2)
        if error < 0.0001:
            x = False
            Friction_Loss(guess_2,ID,V,L,p)
        else:
            guess = guess_2
            
        
def Friction_Factor_Laminar(re,ID,E,L,V,p):
    f = 64/re
    print('Laminar friction factor is ' + str(f))
    Friction_Loss(f,ID,V,L,p)
    
def Friction_Loss(f,ID,V,L,p):
    lw = (f * L * math.pow(V,2)) / (2 * ID)
    losses = (lw * p) / 1000
    
    print(str(losses) + ' kPa frictional losses' )

User_Inputs()



    
    
