#-------------------------------------------------------------------------------
# Name:         Button.py
# Purpose:      To create a button class to be used for the menu and game over
#               screen.
#
# Author:       Marko Nerandzic
#
# Created:      31/05/2013
# Copyright:    (c) Marko Nerandzic 2013
# Licence:      This work is licensed under the Creative Commons Attribution-
#               NonCommercial-NoDerivs 3.0 Unported License. To view a copy of
#               this license, visit http://creativecommons.org/licenses/by-nd/3.0/.
#-------------------------------------------------------------------------------

import pygame

class Button():
    area = None
    colour = None
    message = None

    #Initializes the button
    def __init__(self, initArea, initColour, initMessage):
        self.area = pygame.Rect(initArea)
        self.colour = initColour
        self.message = initMessage

    #Returns the area and colout
    def getRectToDraw(self):
        return [self.area, self.colour]

    #Returns the message
    def getMessage(self):
        return self.message

    #Returns the area
    def getArea(self):
        return self.area

    #Returns the colour
    def getColour(self):
        return self.colour


