#-------------------------------------------------------------------------------
# Name:        FirstPlayer
# Purpose:     This is the file that handles the user's character and defines the Player class
#
# Author:      Marko Nerandzic
#
# Created:     25/12/2012
# Copyright:   (c) Marko Nerandzic 2012
# Licence:      This work is licensed under the Creative Commons Attribution-
#               NonCommercial-NoDerivs 3.0 Unported License. To view a copy of
#               this license, visit http://creativecommons.org/licenses/by-nd/3.0/.
#-------------------------------------------------------------------------------


import pygame, FirstPlayerConstants
from FirstPlayerConstants import *

class Player():
    #Definition of all variables the Player class needs
    area = (1,1,1,1)
    placeGoingTo = (1, 1, 1, 1)
    powerUp = False
    powerUpType = 1
    timeWhenPowerUpEnds = 0
    ticksSinceStart = 0
    speed = 0
    score = 0

    #Initialization of relevant variables at the time
    def __init__(self, (leftx, topy, width, height), speed):
        self.area = pygame.Rect(leftx, topy, width, height)
        self.placeGoingTo = pygame.Rect(leftx, topy, width, height)
        self.speed = speed

    def update(self):
        #Checks if powerUp should run out in which case it resets the relevaant variables to their initial values
        if self.powerUp:
            if self.timeWhenPowerUpEnds <= self.ticksSinceStart:
                self.powerUp = False
                if self.powerUpType == SPEED_UP:
                    self.speed = 2
                elif self.powerUpType == SHRINK_ENEMIES:
                    self.area.width = 50
                    self.area.height = 50
                    self.placeGoingTo.width = 50
                    self.placeGoingTo.height = 50

        #Moves the player in the x direction based on where it should be due to user inputs
        distanceNeededToTravelx = abs(self.placeGoingTo.centerx - self.area.centerx)
        if distanceNeededToTravelx >= self.speed:
            if self.placeGoingTo.centerx > self.area.centerx:
                self.area.centerx += self.speed
            elif self.placeGoingTo.centerx < self.area.centerx:
                self.area.centerx -= self.speed
        else:
            self.area.centerx = self.placeGoingTo.centerx

        #Moves the player in the y direction according to where it should be due to user inputs
        distanceNeededToTravely = abs(self.placeGoingTo.centery - self.area.centery)
        if distanceNeededToTravely >= self.speed:
            if self.placeGoingTo.centery > self.area.centery:
                self.area.centery += self.speed
            elif self.placeGoingTo.centery < self.area.centery:
                self.area.centery -= self.speed
        else:
            self.area.centery = self.placeGoingTo.centery

        #Increments the amount of times called since start and returns the rectangle where the player is
        self.ticksSinceStart += 1
        return self.area

    #This function informs the player to where it should move up and checks for collisions with the walls if the application
    def moveUp(self, distance):
        if (self.placeGoingTo.top - distance) < 0:
            self.placeGoingTo.top = 0
        else:
            self.placeGoingTo.centery = self.placeGoingTo.centery - distance

    #This function informs the player to where it should move down and checks for collisions with the walls if the application
    def moveDown(self, distance):
        if (self.placeGoingTo.bottom + distance) > SCREEN_HEIGHT:
            self.placeGoingTo.bottom = SCREEN_HEIGHT
        else:
            self.placeGoingTo.centery = self.placeGoingTo.centery + distance

    #This function informs the player to where it should move left and checks for collisions with the walls if the application
    def moveLeft(self, distance):
        if (self.placeGoingTo.left - distance) < 0:
            self.placeGoingTo.left = 0
        else:
            self.placeGoingTo.centerx = self.placeGoingTo.centerx - distance

    #This function informs the player to where it should move right and checks for collisions with the walls if the application
    def moveRight(self, distance):
        if (self.placeGoingTo.right + distance) > SCREEN_WIDTH:
            self.placeGoingTo.right = SCREEN_WIDTH
        else:
            self.placeGoingTo.centerx = self.placeGoingTo.centerx + distance

    #When the player touches a powerup, this function adjusts the variables based on the type of powerup and sets the duration of the powerup's effect
    def setPowerUp(self, typeOfPowerUp, duration):
        self.powerUp = True
        self.timeWhenPowerUpEnds = self.ticksSinceStart + duration
        self.powerUpType = typeOfPowerUp
        if typeOfPowerUp == SPEED_UP:
            self.speed = 5
        elif typeOfPowerUp == SHRINK_ENEMIES:
            self.area.width = 70
            self.area.height = 70
            self.placeGoingTo.width = 70        #Place going to is also updated to make sure movement is still accurate
            self.placeGoingTo.height = 70

    #Increments the number of points by 1, called when the player collides with the point object
    def addPoints(self, numOfPoints):
        self.score += numOfPoints

    def getRect(self):
        return self.area

    #Returns a boolean value based on whether the player is currently moving in the y direction
    def getMovingVertically(self):
        if self.area.centery != self.placeGoingTo.centery:
            return True
        else:
            return False

    #Returns a boolean value based on whether the player is currently moving in the x direction
    def getMovingHorizontally(self):
        if self.area.centerx != self.placeGoingTo.centerx:
            return True
        else:
            return False

    #Returns the current player score
    def getScore(self):
        return self.score

    #Resets the player to it's original location
    def reset(self, newLeftX, newTopY, newSpeed):
        self.speed = newSpeed
        self.score = 0
        self.area.left = newLeftX
        self.area.top = newTopY
        self.placeGoingTo.left = newLeftX
        self.placeGoingTo.top = newTopY
