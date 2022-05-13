from __future__ import division

import pygame
from math import pi

from .arena import Arena, ARENA_MARKINGS_COLOR, ARENA_MARKINGS_WIDTH

from ..markers import Token
from ..vision import MARKER_TOKEN_GOLD, MARKER_TOKEN_SILVER

from random import uniform
from random import choice

class GoldToken(Token):
    def __init__(self, arena, marker_number):
        super(GoldToken, self).__init__(arena, marker_number,
                                        marker_type=MARKER_TOKEN_GOLD, damping=10)

    @property
    def surface_name(self):
        return 'sr/token_gold_grabbed.png' if self.grabbed else 'sr/token.png'


class SilverToken(Token):
    def __init__(self, arena, marker_number):
        super(SilverToken, self).__init__(arena, marker_number,
                                          marker_type=MARKER_TOKEN_SILVER, damping=10)

    @property
    def surface_name(self):
        return 'sr/token_silver_grabbed.png' if self.grabbed else 'sr/token_silver.png'

class SunnySideUpArena(Arena):
    size = (19, 10)
    start_locations = [( -8, -4)]

    start_headings = [pi/2]

    zone_size = 1

    def __init__(self, objects=None, wall_markers=True):
        super(SunnySideUpArena, self).__init__(objects, wall_markers)

        count=0
        zone1 = [-8.5, 8.5, -4.25, -3.5]
        zone2 = [7.5, 8.5, -3.5, 3.5]
        zone3 = [2, 8.5, 3.5, 4.5]
        zone4 = [2, 3, -0.75, 4.5]
        zone5 = [-2, 2, -0.75, 0.25]
        zone6 = [-3, -2, -0.75, 3.5]
        zone7 = [-8.5, -2, 3.5, 4.5]
        zone8 = [-8.5, -7.5, -3.5, 3.5]

        for i in range(38):
                token = GoldToken(self, count)
                token.location = (-9, -4.5+i*0.25)
                self.objects.append(token)
                count+1
	
        for i in range(23):
            token = GoldToken(self, count)
            token.location = (-7, -2.75+i*0.25)
            self.objects.append(token)
            count+1
        
        #for i in range(55):
        #    token = Token(self, i, damping=10)
        #    token.location = (-6.75+i*0.25, 3)
        #    self.objects.append(token)
	
        #for i in range(71):
        #    token = Token(self, i, damping=10)
        #    token.location = (-8.75+i*0.25, 5)
        #    self.objects.append(token) 
            
        for i in range(13):
             token = GoldToken(self, count)
             token.location = (-6.75+i*0.25, 3)
             self.objects.append(token)
             count+1
	
        for i in range(29):
            token = GoldToken(self, count)
            token.location = (-8.75+i*0.25, 5)
            self.objects.append(token) 
            count+1
            
        for i in range(16):
            token = GoldToken(self, count)
            token.location = (-3.5, -1+i*0.25)
            self.objects.append(token) 
            count+1
            
        for i in range(16):
            token = GoldToken(self, count)
            token.location = (-1.5, 1+i*0.25)
            self.objects.append(token) 
            count+1
            
        
        for i in range(11):
            token = GoldToken(self, count)
            token.location = (-1.25+i*0.25, 0.75)
            self.objects.append(token)
            count+1
            
        for i in range(27):
            token = GoldToken(self, count)
            token.location = (-3.25+i*0.25, -1.25)
            self.objects.append(token)
            count+1
      
        
        for i in range(16):
            token = GoldToken(self, count)
            token.location = (3.5, -1+i*0.25)
            self.objects.append(token)
            count+1 
            
        for i in range(16):
            token = GoldToken(self, count)
            token.location = (1.5, 1+i*0.25)
            self.objects.append(token) 
            count+1
            
        for i in range(13):
             token = GoldToken(self, count)
             token.location = (3.75+i*0.25, 3)
             self.objects.append(token)
             count+1
	
        for i in range(29):
            token = GoldToken(self, count)
            token.location = (1.75+i*0.25, 5)
            self.objects.append(token)
            count+1
            
        count = 0
            
        for i in range(55):
            token = GoldToken(self, count)
            token.location = (-6.75+i*0.25, -3)
            self.objects.append(token)
            count+1
	
        for i in range(71):
            token = GoldToken(self, count)
            token.location = (-8.75+i*0.25, -4.75)
            self.objects.append(token)  
            count+1 
            
        for i in range(38):
            token = GoldToken(self, count)
            token.location = (9, -4.5+i*0.25)
            self.objects.append(token)
            count+1
	
        for i in range(23):
            token = GoldToken(self, count)
            token.location = (7, -2.75+i*0.25)
            self.objects.append(token) 
            count+1
            
        token=SilverToken(self,count)
        token.location = (uniform(zone1[0],zone1[1]), uniform(zone1[2],zone1[3]))
        self.objects.append(token) 
        count+1
    
        token=SilverToken(self,count)
        token.location = (uniform(zone2[0],zone2[1]), uniform(zone2[2],zone2[3]))
        self.objects.append(token) 
        count+1

        token=SilverToken(self,count)
        token.location = (uniform(zone3[0],zone3[1]), uniform(zone3[2],zone3[3]))
        self.objects.append(token) 
        count+1

        token=SilverToken(self,count)
        token.location = (uniform(zone4[0],zone4[1]), uniform(zone4[2],zone4[3]))
        self.objects.append(token) 
        count+1

        token=SilverToken(self,count)
        token.location = (uniform(zone5[0],zone5[1]), uniform(zone5[2],zone5[3]))
        self.objects.append(token) 
        count+1

        token=SilverToken(self,count)
        token.location = (uniform(zone6[0],zone6[1]), uniform(zone6[2],zone6[3]))
        self.objects.append(token) 
        count+1

        token=SilverToken(self,count)
        token.location = (uniform(zone7[0],zone7[1]), uniform(zone7[2],zone7[3]))
        self.objects.append(token) 
        count+1 

        token=SilverToken(self,count)
        token.location = (uniform(zone8[0],zone8[1]), uniform(zone8[2],zone8[3]))
        self.objects.append(token) 
        count+1      

    def draw_background(self, surface, display):
        super(SunnySideUpArena, self).draw_background(surface, display)

        # Corners of the inside square
        top_left     = display.to_pixel_coord((self.left + self.zone_size, self.top + self.zone_size), self)
        top_right    = display.to_pixel_coord((self.right - self.zone_size, self.top + self.zone_size), self)
        bottom_right = display.to_pixel_coord((self.right - self.zone_size, self.bottom - self.zone_size), self)
        bottom_left  = display.to_pixel_coord((self.left + self.zone_size, self.bottom - self.zone_size), self)

        # Lines separating zones
        def line(start, end):
            pygame.draw.line(surface, ARENA_MARKINGS_COLOR, \
                             start, end, ARENA_MARKINGS_WIDTH)

        line((0, 0), top_left)
        line((display.size[0], 0), top_right)
        line(display.size, bottom_right)
        line((0, display.size[1]), bottom_left)

        # Square separating zones from centre
        pygame.draw.polygon(surface, ARENA_MARKINGS_COLOR, \
                            [top_left, top_right, bottom_right, bottom_left], 2)
