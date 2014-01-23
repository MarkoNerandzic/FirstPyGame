#-------------------------------------------------------------------------------
# Name:        FirstInputs
# Purpose:     This is the file that handles with the inputs through the Inputs class
#
# Author:      Marko Nerandzic
#
# Created:     08/01/2013
# Copyright:   (c) Marko Nerandzic 2013
# Licence:      This work is licensed under the Creative Commons Attribution-
#               NonCommercial-NoDerivs 3.0 Unported License. To view a copy of
#               this license, visit http://creativecommons.org/licenses/by-nd/3.0/.
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *

class Inputs():
    #Declares all of the required variables and the event type for quiting
    exit = QUIT
    quitGame = False
    upKeyPressed = False
    downKeyPressed = False
    leftKeyPressed = False
    rightKeyPressed = False
    mouseEvents = []

    #Initializes the move keys
    def __init__(self, upKey = K_UP, downKey = K_DOWN, leftKey = K_LEFT, rightKey = K_RIGHT):
        self.moveUpKey = upKey
        self.moveDownKey = downKey
        self.moveLeftKey = leftKey
        self.moveRightKey = rightKey

    #Resets the inputs to their default state
    def resetInputs(self):
        self.quitGame = False
        self.upKeyPressed = False
        self.downKeyPressed = False
        self.leftKeyPressed = False
        self.rightKeyPressed = False
        self.mouseEvents = []

    #Goes through all of the events that happened since last called and sets the appropriate variables to signal the change
    def update(self):
        self.mouseEvents = []
        for event in pygame.event.get():
            #If the quit event occured, set the quitGame variable to be True
            if event.type == self.exit:
                self.quitGame = True
            #If a key was pressed down, register it as being pressed
            if event.type == KEYDOWN:
                if event.key == self.moveUpKey:
                    self.upKeyPressed = True
                elif event.key == self.moveDownKey:
                    self.downKeyPressed = True
                elif event.key == self.moveLeftKey:
                    self.leftKeyPressed = True
                elif event.key == self.moveRightKey:
                    self.rightKeyPressed = True
            #If a key was released, register it as not being pressed
            elif event.type == KEYUP:
                if event.key == self.moveUpKey:
                    self.upKeyPressed = False
                elif event.key == self.moveDownKey:
                    self.downKeyPressed = False
                elif event.key == self.moveLeftKey:
                    self.leftKeyPressed = False
                elif event.key == self.moveRightKey:
                    self.rightKeyPressed = False
            elif event.type == MOUSEBUTTONUP:
                self.mouseEvents.append(event)

    #Returns the information about any variable
    def getUpKeyPressed(self):
        return self.upKeyPressed

    def getDownKeyPressed(self):
        return self.downKeyPressed

    def getLeftKeyPressed(self):
        return self.leftKeyPressed

    def getRightKeyPressed(self):
        return self.rightKeyPressed

    def getMouseEvents(self):
        return self.mouseEvents

    def getQuit(self):
        return self.quitGame