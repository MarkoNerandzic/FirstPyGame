#-------------------------------------------------------------------------------
# Name:        FirstPoint
# Purpose:     This is the file that handles the point objects and defines the Point class
#
# Author:      Marko Nerandzic
#
# Created:     16/01/2013
# Copyright:   (c) Marko Nerandzic 2013
# Licence:      This work is licensed under the Creative Commons Attribution-
#               NonCommercial-NoDerivs 3.0 Unported License. To view a copy of
#               this license, visit http://creativecommons.org/licenses/by-nd/3.0/.
#-------------------------------------------------------------------------------


import pygame

class Point():
    area = (0,0,0,0)

    #Initializes the location of the point object
    def __init__(self, (leftx, topy, width, height)):
        self.area = pygame.Rect(leftx, topy, width, height)

    #Returns the location
    def getRect(self):
        return self.area

    #Makes the location change when the player collides with it
    def setRect(self, (leftx, topy, width, height)):
        self.area = pygame.Rect(leftx, topy, width, height)