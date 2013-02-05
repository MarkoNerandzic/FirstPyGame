#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ivana
#
# Created:     25/12/2012
# Copyright:   (c) Ivana 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame

class SpeedUp():

    area = (0, 0, 0, 0)
    active = False

    def __init__(self, (leftx, topy, width, height)):
        self.area = pygame.Rect(leftx, topy, width, height)

    def getActive(self):
        return self.active

    def getRect(self):
        return self.area

    def setActive(self, activated):
        self.active = activated

    def setRect(self, (leftx, topy, width, height)):
        self.area = pygame.Rect(leftx, topy, width, height)