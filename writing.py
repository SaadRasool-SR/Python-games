#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:52:59 2019

@author: Saad
"""
'''
cities = ["Calgary","Edmonton","lloydminster","Rainbow lake"]

with open("cities.txt",'w') as city_file:
     for city in cities:
         print(city, file = city_file)
         
cities = []
 
with open("cities.txt",'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

print(cities)


for city in cities:
    print(city)


with open("times.txt",'w') as times_file:
    for x in range(1,13):
        for y in range(1,13):
            answer = x*y 
            print(str(y) + ' times ' + str(x) + ' is ' + str(answer), file=times_file)
        print('-' * 40, file=times_file)

with open("binary",'bw') as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))
        

with open("binary",'br') as Bin_file:
    for num in Bin_file:
        print(num)'''
        

#import pickle 
 

'''imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          ((1,'Pulling The Rug'),
          (2,'Psycho'),
          (3,'Mayhem'),
          (4,'Kentish Town Waltz'))) 

with open("Imdela.pickle","wb") as pickle_file:
     pickle.dump(imelda, pickle_file) '''
     
        

'''with open("Imdela.pickle","rb") as pickle_file:
    lines = pickle.load(pickle_file)

print(lines)'''

import shelve

with shelve.open("shelftest") as fruit:
    fruit['orange'] = "Cirlce orange in colour"
    fruit['apple'] = "Cirlce red in colour"
    fruit['bannana'] = "Long yellow in colour"
    fruit['Mango'] = "from pakistan, yellow in colour"
    
    print(fruit["orange"])
    print(fruit["Mango"])
    
    
    
 

    

    
  


