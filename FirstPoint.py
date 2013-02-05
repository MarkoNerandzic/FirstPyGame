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

import pygame

class Point():
    area = (0,0,0,0)

    def __init__(self, (leftx, topy, width, height)):
        self.area = pygame.Rect(leftx, topy, width, height)

    def getRect(self):
        return self.area

    def setRect(self, (leftx, topy, width, height)):
        self.area = pygame.Rect(leftx, topy, width, height)