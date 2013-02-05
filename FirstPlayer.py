#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ivana
#
# Created:     24/12/2012
# Copyright:   (c) Ivana 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame, FirstPlayerConstants
from FirstPlayerConstants import *

class Player():
    area = (1,1,1,1)
    placeGoingTo = (1, 1, 1, 1)
    powerUp = False
    powerUpType = 1
    timeWhenPowerUpEnds = 0
    ticksSinceStart = 0
    speed = 0
    score = 0

    def __init__(self, (leftx, topy, width, height), speed):
        self.area = pygame.Rect(leftx, topy, width, height)
        self.placeGoingTo = pygame.Rect(leftx, topy, width, height)
        self.speed = speed

    def update(self):
        if self.powerUp:
            if self.timeWhenPowerUpEnds <= self.ticksSinceStart:
                self.powerUp = False
                if self.powerUpType == SPEEDUP:
                    self.speed = 2
                elif self.powerUpType == GROWUP:
                    self.area.width = 50
                    self.area.height = 50
                    self.placeGoingTo.width = 50
                    self.placeGoingTo.height = 50

        distanceNeededToTravelx = abs(self.placeGoingTo.centerx - self.area.centerx)
        if distanceNeededToTravelx >= self.speed:
            if self.placeGoingTo.centerx > self.area.centerx:
                self.area.centerx += self.speed
            elif self.placeGoingTo.centerx < self.area.centerx:
                self.area.centerx -= self.speed
        else:
            self.area.centerx = self.placeGoingTo.centerx

        distanceNeededToTravely = abs(self.placeGoingTo.centery - self.area.centery)
        if distanceNeededToTravely >= self.speed:
            if self.placeGoingTo.centery > self.area.centery:
                self.area.centery += self.speed
            elif self.placeGoingTo.centery < self.area.centery:
                self.area.centery -= self.speed
        else:
            self.area.centery = self.placeGoingTo.centery
        self.ticksSinceStart += 1
        return self.area

    def moveUp(self, distance):
        if (self.placeGoingTo.top - distance) < 0:
            self.placeGoingTo.top = 0
        else:
            self.placeGoingTo.centery = self.placeGoingTo.centery - distance

    def moveDown(self, distance):
        if (self.placeGoingTo.bottom + distance) > SCREENHEIGHT:
            self.placeGoingTo.bottom = SCREENHEIGHT
        else:
            self.placeGoingTo.centery = self.placeGoingTo.centery + distance

    def moveLeft(self, distance):
        if (self.placeGoingTo.left - distance) < 0:
            self.placeGoingTo.left = 0
        else:
            self.placeGoingTo.centerx = self.placeGoingTo.centerx - distance

    def moveRight(self, distance):
        if (self.placeGoingTo.right + distance) > SCREENWIDTH:
            self.placeGoingTo.right = SCREENWIDTH
        else:
            self.placeGoingTo.centerx = self.placeGoingTo.centerx + distance

    def setPowerUp(self, typeOfPowerUp, duration):
        self.powerUp = True
        self.timeWhenPowerUpEnds = self.ticksSinceStart + duration
        self.powerUpType = typeOfPowerUp
        if typeOfPowerUp == SPEEDUP:
            self.speed = 5
        elif typeOfPowerUp == GROWUP:
            self.area.width = 70
            self.area.height = 70
            self.placeGoingTo.width = 70        #Place going to is also updated because collisions work better like this
            self.placeGoingTo.height = 70

    def addPoints(self, numOfPoints):
        self.score += numOfPoints

    def printValues(self):
        print 'The current speed is', self.speed
        print 'The rect is', self.area

    def getRect(self):
        return self.area

    def getMovingVertically(self):
        if self.area.centery != self.placeGoingTo.centery:
            return True
        else:
            return False

    def getMovingHorizontally(self):
        if self.area.centerx != self.placeGoingTo.centerx:
            return True
        else:
            return False

    def getScore(self):
        return self.score
