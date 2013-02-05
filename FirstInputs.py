#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      321599755
#
# Created:     08/01/2013
# Copyright:   (c) 321599755 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame
from pygame.locals import *

class Inputs():

    exit = QUIT
    quitGame = False
    upKeyPressed = False
    downKeyPressed = False
    leftKeyPressed = False
    rightKeyPressed = False

    def __init__(self, upKey = K_UP, downKey = K_DOWN, leftKey = K_LEFT, rightKey = K_RIGHT):
        self.moveUpKey = upKey
        self.moveDownKey = downKey
        self.moveLeftKey = leftKey
        self.moveRightKey = rightKey

    def update(self):
        for event in pygame.event.get():
            if event.type == self.exit:
                self.quitGame = True
            if event.type == KEYDOWN:
                if event.key == self.moveUpKey:
                    self.upKeyPressed = True
                elif event.key == self.moveDownKey:
                    self.downKeyPressed = True
                elif event.key == self.moveLeftKey:
                    self.leftKeyPressed = True
                elif event.key == self.moveRightKey:
                    self.rightKeyPressed = True
            elif event.type == KEYUP:
                if event.key == self.moveUpKey:
                    self.upKeyPressed = False
                elif event.key == self.moveDownKey:
                    self.downKeyPressed = False
                elif event.key == self.moveLeftKey:
                    self.leftKeyPressed = False
                elif event.key == self.moveRightKey:
                    self.rightKeyPressed = False

    def getUpKeyPressed(self):
        return self.upKeyPressed

    def getDownKeyPressed(self):
        return self.downKeyPressed

    def getLeftKeyPressed(self):
        return self.leftKeyPressed

    def getRightKeyPressed(self):
        return self.rightKeyPressed

    def getQuit(self):
        return self.quitGame