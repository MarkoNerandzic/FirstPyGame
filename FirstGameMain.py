#-------------------------------------------------------------------------------
# Name:        FirstGameMain
# Purpose:     This is the main file of the game, it handles the game state
#
# Author:      Marko Nerandzic
#
# Created:     25/12/2012
# Copyright:   (c) Marko Nerandzic 2012
# Licence:     This work is licensed under the Creative Commons Attribution-
#              NonCommercial-NoDerivs 3.0 Unported License. To view a copy of
#              this license, visit http://creativecommons.org/licenses/by-nd/3.0/.
#-------------------------------------------------------------------------------


import FirstPlayer, FirstPowerUp, FirstPlayerConstants, FirstInputs, FirstEnemy, FirstPoint, pygame, random
from pygame.locals import *
from FirstPlayerConstants import *

def main():
    #Initialization of the game variables
    endGame = False
    gameOver = False
    numOfTicks = 0
    last2Types = [0, 0]

    #Initization of PyGame
    pygame.init()

    #Display setup
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption("First PyGame!")

    #Initialization of clock used for delay to achieve 30 frames per second
    FPSCLOCK = pygame.time.Clock()

    #Initialization of all text in the game
    fontObj = pygame.font.Font('freesansbold.ttf', 12)
    scoreSurface = fontObj.render('Score: ', True, BLACK, WHITE)
    scoreNumSurface = fontObj.render('0', True, BLACK, WHITE)
    textScoreNumRect = scoreNumSurface.get_rect()
    textScoreRect = scoreSurface.get_rect()
    textScoreNumRect.right = SCREEN_WIDTH
    textScoreNumRect.top = 0
    textScoreRect.right = textScoreNumRect.left
    textScoreRect.top = 0

    #Initialization of game over text images
    gameOverFont = pygame.font.Font('freesansbold.ttf', 64)
    gameOverSurface = gameOverFont.render('GAME OVER', True, BLACK, WHITE)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.center = (SCREEN_WIDTH/2, (SCREEN_HEIGHT/2) - 50)

    gameOverScoreFont = pygame.font.Font('freesansbold.ttf', 32)

    #Initialization of the player object the user controls
    player = FirstPlayer.Player(((SCREEN_WIDTH-PLAYER_WIDTH)/2, (SCREEN_HEIGHT - PLAYER_HEIGHT)/ 2, PLAYER_WIDTH, PLAYER_HEIGHT), PLAYER_SPEED)
    #Definition of an array to hold all of the enemies in the game, whose number increases
    enemies = []
    #Initialization of the point object
    points = FirstPoint.Point(newRectNotAtObject(player.getRect(), POINT_WIDTH, POINT_HEIGHT))
    #Initialization of the power up object that shrinks the enemies or increases the player's speed
    powerUp = FirstPowerUp.PowerUp((0, 0, 0, 0))
    #Initialization of the object that will handle user inputs
    inputs = FirstInputs.Inputs()

    while not endGame and not gameOver:
        #Resets the display
        DISPLAYSURF.fill(WHITE)

        #Updates the state of the inputs based on the user's actions since last called
        inputs.update()

        #Interprets the inputs from the player and updates accordingly
        if inputs.getQuit():
            endGame = True
        elif inputs.getUpKeyPressed() and not player.getMovingVertically():
            player.moveUp(DISTANCEPERMOVE)
        elif inputs.getDownKeyPressed() and not player.getMovingVertically():
            player.moveDown(DISTANCEPERMOVE)
        elif inputs.getLeftKeyPressed() and not player.getMovingHorizontally():
            player.moveLeft(DISTANCEPERMOVE)
        elif inputs.getRightKeyPressed() and not player.getMovingHorizontally():
            player.moveRight(DISTANCEPERMOVE)

        #This loop checks the player position against the position of all enemies to check for collisions
        #If a collision is detected, the gameOver variable is set True to exit the loop
        counter = 0
        while counter < len(enemies):
            if player.getRect().colliderect(enemies[counter].getRect()) == 1:
                gameOver = True
            counter += 1

        #Checks if there is a collision between the player and the point
        #If there is a collision, the point moves somewhere else, a point is added to the player's score and a new enemy is created
        if player.getRect().colliderect(points.getRect()) == 1:
            player.addPoints(1)
            tempRect = newRectNotAtObject(player.getRect(), POINT_WIDTH, POINT_HEIGHT)
            points.setRect(tempRect)
            tempRect = newRectNotAtObject(player.getRect(), ENEMY_WIDTH, ENEMY_HEIGHT)
            enemies.append(FirstEnemy.Enemy(tempRect, random.randint(1,2)))

        #Checks if there is a collision between the player and the powerup object
        #If there is a collision and the power up is shown on the screen, the player or enemies get adjusted based on the type of powerup
        if player.getRect().colliderect(powerUp.getRect()) == 1 and powerUp.getActive():
            powerUp.setActive(False)
            if powerUp.getType() == SPEED_UP:
                player.setPowerUp(powerUp.getType(), POWERUP_DURATION)
            elif powerUp.getType() == SHRINK_ENEMIES:
                counter = 0
                while counter < len(enemies):
                    enemies[counter].setPowerUp(powerUp.getType(), POWERUP_DURATION)
                    counter += 1

        #If the powerup is not shown on the screen and it is time for it to be active
        #It generates a new location and type for the powerup and sets it to be active
        if numOfTicks % POWERUP_RESPAWN_TICKS == 0 and not powerUp.getActive():
            powerUp.setActive(True)
            powerUp.setRect(newRectNotAtObject(player.getRect(), POWERUP_WIDTH, POWERUP_HEIGHT))
            randomNum = random.randint(1, 2)                                    #Because all of the powerup types are numbers between 1 to 2
            while randomNum == last2Types[0] and randomNum == last2Types[1]:    #If randomNum is equal to the last 2 numbers generated, pick a new one
                randomNum = random.randint(1, 2)
            powerUp.setType(randomNum)
            last2Types[0] = last2Types[1]
            last2Types[1] = randomNum

        #Recalulates the score and text object required and position of the text objects and renders them
        scoreNumSurface = fontObj.render(str(player.getScore()), True, BLACK, WHITE)
        textScoreNumRect = scoreNumSurface.get_rect()
        textScoreRect = scoreSurface.get_rect()
        textScoreNumRect.right = SCREEN_WIDTH
        textScoreNumRect.top = 0
        textScoreRect.right = textScoreNumRect.left
        textScoreRect.top = 0

        #If the powerup is active, it draws it to the screen
        if powerUp.getActive():
            pygame.draw.rect(DISPLAYSURF, powerUpColours[powerUp.getType()], powerUp.getRect())

        #Draws the point object to the screen
        pygame.draw.rect(DISPLAYSURF, BROWN, points.getRect())

        #Draws all of the enemies to the screen
        counter = 0
        while counter < len(enemies):
            pygame.draw.rect(DISPLAYSURF, PURPLE, enemies[counter].update())
            counter += 1

        #Draws the player to the screen
        pygame.draw.rect(DISPLAYSURF, RED, player.update())

        #Draws the text objects to the screen
        DISPLAYSURF.blit(scoreSurface, textScoreRect)
        DISPLAYSURF.blit(scoreNumSurface, textScoreNumRect)

        #Updates the screen
        pygame.display.update()
        #Delays the loop to have create 30 frames per second
        FPSCLOCK.tick(FPS)
        #Increments the number of times looped since the start of the game
        numOfTicks += 1


    if gameOver:
        #Renders and calculates the position of the game over text
        scoreNumSurface = gameOverScoreFont.render(str(player.getScore()), True, BLACK, WHITE)
        scoreSurface = gameOverScoreFont.render('Score: ', True, BLACK, WHITE)
        textScoreNumRect = scoreNumSurface.get_rect()
        textScoreRect = scoreSurface.get_rect()
        textScoreNumRect.right = (textScoreRect.width + textScoreNumRect.width + SCREEN_WIDTH)/2
        textScoreNumRect.top = SCREEN_HEIGHT/ 2
        textScoreRect.right = textScoreNumRect.left
        textScoreRect.top = SCREEN_HEIGHT/ 2

        #Resets the screen to white
        DISPLAYSURF.fill(WHITE)
        #Draws the text objects  to the screen
        DISPLAYSURF.blit(gameOverSurface, gameOverRect)
        DISPLAYSURF.blit(scoreSurface, textScoreRect)
        DISPLAYSURF.blit(scoreNumSurface, textScoreNumRect)
        #Updates the screen
        pygame.display.update()
        #Waits until the user presses the quit button
        while not inputs.getQuit():
            inputs.update()

    #Exits pygame
    pygame.quit()
    pass

#This function makes sure that the object that is being created or moved is not at the same position as the rectangle to avoid
def newRectNotAtObject(avoidRect, createWidth, createHeight):
    newRectNotAtPlayer = False
    while not newRectNotAtPlayer:
        newRect = pygame.Rect((random.randint(0, (SCREEN_WIDTH - createWidth)), random.randint(0, (SCREEN_HEIGHT - createHeight)), createWidth, createHeight))
        if avoidRect.colliderect(newRect) != 1:
            if abs((newRect.centerx + newRect.width/2) - (avoidRect.centerx + avoidRect.width/2)) > MIN_X_DISTANCE and abs((newRect.centery + newRect.height/2) - (avoidRect.centery + avoidRect.height/2)) > MIN_Y_DISTANCE:
                newRectNotAtPlayer = True
    return newRect

if __name__ == '__main__':
    main()
