#-------------------------------------------------------------------------------
# Name:        FirstPowerUp
# Purpose:     This is the file that handles the power ups and stores the PowerUp class
#
# Author:      Marko Nerandzic
#
# Created:     25/12/2012
# Copyright:   (c) Marko Nerandzic 2012
# Licence:      This work is licensed under the Creative Commons Attribution-
#               NonCommercial-NoDerivs 3.0 Unported License. To view a copy of
#               this license, visit http://creativecommons.org/licenses/by-nd/3.0/.
#-------------------------------------------------------------------------------


import pygame

class PowerUp():
    #Definition of all required variables
    area = (0, 0, 0, 0)
    active = False
    typeOfPowerUp = 0

    #Initialization of location
    def __init__(self, (leftx, topy, width, height)):
        self.area = pygame.Rect(leftx, topy, width, height)

    #If active is True, the player can collide with it to get a powerup effect and it is shown on the screen
    def getActive(self):
        return self.active

    def getRect(self):
        return self.area

    #Returns if the powerup is a speedup or shrink powerup
    def getType(self):
        return self.typeOfPowerUp

    #Called when it is time for the powerup to become active and displayed again
    def setActive(self, activated):
        self.active = activated

    #Called when it is time for the powerup to become active and displayed again in a different location
    def setRect(self, (leftx, topy, width, height)):
        self.area = pygame.Rect(leftx, topy, width, height)

    #Called when it is time for the powerup to become active and displayed again
    def setType(self, powerUpType):
        self.typeOfPowerUp = powerUpType
