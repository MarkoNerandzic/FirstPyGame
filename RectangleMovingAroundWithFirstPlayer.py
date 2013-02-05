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

import FirstPlayer, FirstPowerUp, FirstPlayerConstants, FirstInputs, FirstEnemy, FirstPoint, pygame, random
from pygame.locals import *
from FirstPlayerConstants import *

def main():
    endGame = False
    gameOver = False
    numOfTicks = 0
    last2Types = [0, 0]

    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Rectangles moving around with First Player!")

    fontObj = pygame.font.Font('freesansbold.ttf', 12)
    scoreSurface = fontObj.render('Score: ', True, BLACK, WHITE)
    scoreNumSurface = fontObj.render('0', True, BLACK, WHITE)
    textScoreNumRect = scoreNumSurface.get_rect()
    textScoreRect = scoreSurface.get_rect()
    textScoreNumRect.right = SCREENWIDTH
    textScoreNumRect.top = 0
    textScoreRect.right = textScoreNumRect.left
    textScoreRect.top = 0

    gameOverFont = pygame.font.Font('freesansbold.ttf', 64)
    gameOverSurface = gameOverFont.render('GAME OVER', True, BLACK, WHITE)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.center = (SCREENWIDTH/2, (SCREENHEIGHT/2) - 50)

    gameOverScoreFont = pygame.font.Font('freesansbold.ttf', 32)

    player = FirstPlayer.Player(((SCREENWIDTH-SQUAREWIDTH)/2, (SCREENHEIGHT - SQUAREHEIGHT)/ 2, SQUAREWIDTH, SQUAREHEIGHT), SQUARESPEED)
    enemies = []
    points = FirstPoint.Point(newRectNotAtObject(player.getRect(), POINTWIDTH, POINTHEIGHT))
    powerUp = FirstPowerUp.PowerUp((0, 0, 0, 0))
    inputs = FirstInputs.Inputs()

    while not endGame and not gameOver:
        DISPLAYSURF.fill(WHITE)

        inputs.update()

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

        counter = 0
        while counter < len(enemies):
            if player.getRect().colliderect(enemies[counter].getRect()) == 1:
                gameOver = True
            counter += 1

        if player.getRect().colliderect(points.getRect()) == 1:
            player.addPoints(1)
            tempRect = newRectNotAtObject(player.getRect(), POINTWIDTH, POINTHEIGHT)
            points.setRect(tempRect)
            tempRect = newRectNotAtObject(player.getRect(), ENEMYWIDTH, ENEMYHEIGHT)
            enemies.append(FirstEnemy.Enemy(tempRect, random.randint(1,2)))

        if player.getRect().colliderect(powerUp.getRect()) == 1 and powerUp.getActive():
            powerUp.setActive(False)
            if powerUp.getType() == SPEEDUP:
                player.setPowerUp(powerUp.getType(), POWERUPDURATION)
            elif powerUp.getType() == GROWUP:
                counter = 0
                while counter < len(enemies):
                    enemies[counter].setPowerUp(powerUp.getType(), POWERUPDURATION)
                    counter += 1

        if numOfTicks % POWERUPRESPAWNTICKS == 0 and not powerUp.getActive():
            powerUp.setActive(True)
            powerUp.setRect(newRectNotAtObject(player.getRect(), SPEEDWIDTH, SPEEDHEIGHT))
            randomNum = random.randint(1, 2)    #Because all of the powerups are numbers between 1 to 2
            while randomNum == last2Types[0] and randomNum == last2Types[1]:    #If randomNum was the last 2 types, pick a new one
                randomNum = random.randint(1, 2)
            powerUp.setType(randomNum)
            last2Types[0] = last2Types[1]
            last2Types[1] = randomNum

        scoreNumSurface = fontObj.render(str(player.getScore()), True, BLACK, WHITE)
        textScoreNumRect = scoreNumSurface.get_rect()
        textScoreRect = scoreSurface.get_rect()
        textScoreNumRect.right = SCREENWIDTH
        textScoreNumRect.top = 0
        textScoreRect.right = textScoreNumRect.left
        textScoreRect.top = 0

        if powerUp.getActive():
            pygame.draw.rect(DISPLAYSURF, powerUpColours[powerUp.getType()], powerUp.getRect())

        pygame.draw.rect(DISPLAYSURF, BROWN, points.getRect())

        counter = 0
        while counter < len(enemies):
            pygame.draw.rect(DISPLAYSURF, PURPLE, enemies[counter].update())
            counter += 1

        pygame.draw.rect(DISPLAYSURF, RED, player.update())

        DISPLAYSURF.blit(scoreSurface, textScoreRect)
        DISPLAYSURF.blit(scoreNumSurface, textScoreNumRect)

        pygame.display.update()
        FPSCLOCK.tick(FPS)
        numOfTicks += 1


    if gameOver:
        scoreNumSurface = gameOverScoreFont.render(str(player.getScore()), True, BLACK, WHITE)
        scoreSurface = gameOverScoreFont.render('Score: ', True, BLACK, WHITE)
        textScoreNumRect = scoreNumSurface.get_rect()
        textScoreRect = scoreSurface.get_rect()
        textScoreNumRect.right = (textScoreRect.width + textScoreNumRect.width + SCREENWIDTH)/2
        textScoreNumRect.top = SCREENHEIGHT/ 2
        textScoreRect.right = textScoreNumRect.left
        textScoreRect.top = SCREENHEIGHT/ 2

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(gameOverSurface, gameOverRect)
        DISPLAYSURF.blit(scoreSurface, textScoreRect)
        DISPLAYSURF.blit(scoreNumSurface, textScoreNumRect)
        pygame.display.update()
        while not inputs.getQuit():
            inputs.update()


    pygame.quit()
    pass

def newRectNotAtObject(avoidRect, createWidth, createHeight):
    newRectNotAtPlayer = False
    while not newRectNotAtPlayer:
        newRect = pygame.Rect((random.randint(0, (SCREENWIDTH - createWidth)), random.randint(0, (SCREENHEIGHT - createHeight)), createWidth, createHeight))
        if avoidRect.colliderect(newRect) != 1:
            if abs((newRect.centerx + newRect.width/2) - (avoidRect.centerx + avoidRect.width/2)) > MINXDISTANCE and abs((newRect.centery + newRect.height/2) - (avoidRect.centery + avoidRect.height/2)) > MINYDISTANCE:
                newRectNotAtPlayer = True
    return newRect

if __name__ == '__main__':
    main()
