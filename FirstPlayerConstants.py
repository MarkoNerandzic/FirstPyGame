#-------------------------------------------------------------------------------
# Name:        FirstPlayerConstants
# Purpose:     This is the file that defines all of the constants used in the game
#
# Author:      Marko Nerandzic
#
# Created:     25/12/2012
# Copyright:   (c) Marko Nerandzic 2012
# Licence:      This work is licensed under the Creative Commons Attribution-
#               NonCommercial-NoDerivs 3.0 Unported License. To view a copy of
#               this license, visit http://creativecommons.org/licenses/by-nd/3.0/.
#-------------------------------------------------------------------------------

#Constants for power up types
SPEED_UP = 1
SHRINK_ENEMIES = 2

#Constants regarding the display
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 500
FPS = 30

#Constants regarding the player
PLAYER_HEIGHT = 50
PLAYER_WIDTH = 50
PLAYER_SPEED = 2
DISTANCEPERMOVE = 10

#Constants regarding the powerup object
POWERUP_HEIGHT = 30
POWERUP_WIDTH = 30
POWERUP_DURATION = 300
POWERUP_RESPAWN_TICKS = 900

#Constants regarding the points object
POINT_WIDTH = 15
POINT_HEIGHT = 15

#Constants concerning enemies
ENEMY_SPEED = 2
ENEMY_WIDTH = 80
ENEMY_HEIGHT = 80

#Constants for height and width for enemies after player gets shrinking powerup
SHRUNKEN_ENEMY_HEIGHT = 40
SHRUNKEN_ENEMY_WIDTH = 40

#Colour constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (233, 0, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 13)
BLACK = (0, 0, 0)

#Array holding which colour refers to which powerup type
powerUpColours = [0]

powerUpColours.append(BLUE)
powerUpColours.append(GREEN)

#Direction Constants
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

#Minimum distance a object can be created or moved from the player
MIN_X_DISTANCE = 30
MIN_Y_DISTANCE = 30