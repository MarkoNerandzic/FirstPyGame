#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ivana
#
# Created:     16/01/2013
# Copyright:   (c) Ivana 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame, FirstPlayerConstants
from FirstPlayerConstants import *

class Enemy():
    area = (0,0,0,0)
    direction = 0
    powerUpActive = False
    powerUpType = 0
    powerTimeOut = 0
    powerUpStart = 0
    originalHeight = 0
    originalWidth = 0
    ticksSinceStart = 0

    def __init__(self, (leftx, topy, width, height), startingDirection):
        self.area = pygame.Rect(leftx, topy, width, height)
        self.originalHeight = height
        self.originalWidth = width
        self.direction = startingDirection

    def update(self):
        if (self.powerUpStart + self.powerTimeOut) <= self.ticksSinceStart and self.powerUpActive:
            if self.powerUpType == GROWUP:
                self.area.height = self.originalHeight
                self.area.width = self.originalWidth
            self.powerUpActive = False

        if self.direction == UP:
            if (self.area.top - ENEMYSPEED) < 0:
                self.direction = DOWN
            else:
                self.area.top -= ENEMYSPEED
        if self.direction == DOWN:
            if (self.area.bottom + ENEMYSPEED) > SCREENHEIGHT:
                self.direction = UP
                self.area.top -= ENEMYSPEED
            else:
                self.area.bottom += ENEMYSPEED

        if self.direction == LEFT:
            if (self.area.left - ENEMYSPEED) < 0:
                self.direction = RIGHT
            else:
                self.area.left -= ENEMYSPEED
        if self.direction == RIGHT:
            if (self.area.right + ENEMYSPEED) > SCREENWIDTH:
                self.direction = LEFT
                self.area.left -= ENEMYSPEED
            else:
                self.area.right += ENEMYSPEED
        self.ticksSinceStart += 1
        return self.area

    def setPowerUp(self, powerUpType, powerUpLength):
        self.powerUpType = powerUpType
        self.powerUpActive = True
        self.powerTimeOut = powerUpLength
        self.powerUpStart = self.ticksSinceStart
        if powerUpType == GROWUP:
            self.area.height = POWERUPENEMYHEIGHT
            self.area.width = POWERUPENEMYWIDTH

    def getRect(self):
        return self.area
