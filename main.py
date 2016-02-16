# Créé par Antoine, le 15/02/2016 en Python 3.2
import pygame, math, sys
from pygame.locals import *
from math import *
from sys import *

    fps = 300

winxmax = 720
winymax = 480

epaisseurtrait = 10
barretaille = 100
offsetbarre = 25

black     = (0  ,0  ,0  )
white     = (255,255,255)


def drawarene():
    displayWin.fill(black)
    pygame.draw.rect(displayWin, white, ((0,0),(winxmax,winymax)), epaisseurtrait*2)

def drawbarre(barre):
    if barre.bottom > winymax - epaisseurtrait:
        barre.bottom = winymax - epaisseurtrait

    elif barre.top < epaisseurtrait:
        barre.top = epaisseurtrait

    pygame.draw.rect(displayWin, white, barre)

def drawballe(balle):
    pygame.draw.rect(displayWin, white, balle)

def deplacballe(balle, dirXballe, dirYballe):
    balle.x = balle.x + dirXballe
    balle.y = balle.y + dirYballe
    return balle

def checkballecolisionmur(balle,dirXballe,dirYballe):
    if balle.top == (epaisseurtrait) or balle.bottom == (winymax - epaisseurtrait):
        dirYballe = dirYballe * -1
        son.play()
    if balle.left == (epaisseurtrait) or balle.right == (winxmax - epaisseurtrait):
        dirXballe = dirXballe * -1
    return dirXballe, dirYballe

def checkballecollisionbarre(balle, barre1, barre2, dirXballe):
    if dirXballe == -1 and barre1.right == balle.left and barre1.top < balle.top and barre1.bottom > balle.bottom:
        son.play()
        return -1
    elif dirXballe == 1 and barre2.left == balle.right and barre2.top < balle.top and barre2.bottom > balle.bottom:
        son.play()
        return -1
    else:
        return 1

def displayscore(score, x):
    resultSurf = BASICFONT.render('Score = %s' %(score), True, white)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (winxmax - x, 25)
    displayWin.blit(resultSurf, resultRect)

def ending(joueur):
    str = print

def main():
    pygame.init()

    global displayWin
    global BASICFONT, BASICFONTSIZE
    global son
    global sonbut
    son = pygame.mixer.Sound("pong.ogg")
    sonbut = pygame.mixer.Sound("but.ogg")
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    fpsClock = pygame.time.Clock()
    displayWin = pygame.display.set_mode((winxmax, winymax))
    pygame.display.set_caption('Pong')

    ballex = winxmax/2 - epaisseurtrait/2
    balley = winymax/2 - epaisseurtrait/2
    ponepos = (winymax - barretaille)/2
    ptwopos = (winymax - barretaille)/2

    dirXballe = -1
    dirYballe = -1

    scorep1 = 0
    scorep2 = 0

    barre1 = pygame.Rect(offsetbarre,ponepos, epaisseurtrait,barretaille)
    barre2 = pygame.Rect(winxmax-offsetbarre,ptwopos, epaisseurtrait,barretaille)
    balle = pygame.Rect(ballex, balley, epaisseurtrait, epaisseurtrait)

    drawarene()
    drawbarre(barre1)
    drawbarre(barre2)
    drawballe(balle)


    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    barre2.y += -25
                if event.key == K_DOWN:
                    barre2.y += 25
                if event.key == K_q:
                    barre1.y += -25
                if event.key == K_a:
                    barre1.y += 25

        if balle.left == (epaisseurtrait):
            scorep1 += 1
            print("BUTTTTTTTTTT pour le joueur 1:")
            print(scorep1)
            sonbut.play()
        if balle.right == (winxmax - epaisseurtrait):
            scorep2 += 1
            print("BUTTTTTTTTTT pour le joueur 2:")
            print(scorep2)
            sonbut.play()


        drawarene()
        drawbarre(barre1)
        drawbarre(barre2)
        drawballe(balle)

        balle = deplacballe(balle, dirXballe, dirYballe)
        dirXballe, dirYballe = checkballecolisionmur(balle, dirXballe, dirYballe)
        dirXballe = dirXballe * checkballecollisionbarre(balle, barre1, barre2,dirXballe)

        displayscore(scorep1, 125)
        displayscore(scorep2, winxmax - 25)

        if scorep1 == 5 or scorep2 == 5:
             pygame.quit()
             sys.exit()


        pygame.display.flip()
        fpsClock.tick(fps)

if __name__=='__main__':
    main()

