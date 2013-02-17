#-------------------------------------------------------------------------------
# Name:        FirstEnemy
# Purpose:     This is the file that stores the enemy class
#
# Author:      Marko Nerandzic
#
# Created:     16/01/2013
# Copyright:   (c) Marko Nerandzic 2013
# Licence:      This work is licensed under the Creative Commons Attribution-
#               NonCommercial-NoDerivs 3.0 Unported License. To view a copy of
#               this license, visit http://creativecommons.org/licenses/by-nd/3.0/.
#-------------------------------------------------------------------------------


import pygame, FirstPlayerConstants
from FirstPlayerConstants import *

class Enemy():
    #Declares & defines all required variables
    area = (0,0,0,0)
    direction = 0
    powerUpActive = False
    powerUpType = 0
    powerTimeOut = 0
    powerUpStart = 0
    originalHeight = 0
    originalWidth = 0
    ticksSinceStart = 0

    #Initializes location and size and direction it moves
    def __init__(self, (leftx, topy, width, height), startingDirection):
        self.area = pygame.Rect(leftx, topy, width, height)
        self.originalHeight = height
        self.originalWidth = width
        self.direction = startingDirection


    def update(self):
        #Checks if powerup effect has expired in which case it reverts to it's normal size
        if (self.powerUpStart + self.powerTimeOut) <= self.ticksSinceStart and self.powerUpActive:
            if self.powerUpType == SHRINK_ENEMIES:
                self.area.height = self.originalHeight
                self.area.width = self.originalWidth
            self.powerUpActive = False

        #Checks if the direction is vertical and if it is in contact with a wall before moving vertically
        if self.direction == UP:
            if (self.area.top - ENEMY_SPEED) < 0:
                self.direction = DOWN
            else:
                self.area.top -= ENEMY_SPEED
        if self.direction == DOWN:
            if (self.area.bottom + ENEMY_SPEED) > SCREEN_HEIGHT:
                self.direction = UP
                self.area.top -= ENEMY_SPEED
            else:
                self.area.bottom += ENEMY_SPEED

        #Checks if the direction is horizontal and if it is in contact with a wall before moving horizontally
        if self.direction == LEFT:
            if (self.area.left - ENEMY_SPEED) < 0:
                self.direction = RIGHT
            else:
                self.area.left -= ENEMY_SPEED
        if self.direction == RIGHT:
            if (self.area.right + ENEMY_SPEED) > SCREEN_WIDTH:
                self.direction = LEFT
                self.area.left -= ENEMY_SPEED
            else:
                self.area.right += ENEMY_SPEED
        #Increments the total ticks since start and returns the updated location and size
        self.ticksSinceStart += 1
        return self.area

    #Called when the player collides with a shrinking powerup and sets the new size and duration of the powerup
    def setPowerUp(self, powerUpType, powerUpLength):
        self.powerUpType = powerUpType
        self.powerUpActive = True
        self.powerTimeOut = powerUpLength
        self.powerUpStart = self.ticksSinceStart
        if powerUpType == SHRINK_ENEMIES:
            self.area.height = SHRUNKEN_ENEMY_HEIGHT
            self.area.width = SHRUNKEN_ENEMY_WIDTH

    #Returns location and size
    def getRect(self):
        return self.area
