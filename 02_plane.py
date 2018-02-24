import pygame
import time
import random
from pygame.locals import *


class PBullet(object):
    def __init__(self, screen, x, y, who):
        self.screen = screen
        self.who = who
        if self.who == "player":
            self.bulletImageFile = "./img/bullet-3.gif"
            self.x = x + 40
            self.y = y - 18
        elif self.who == "enemy":
            self.bulletImageFile = "./img/bullet-1.gif"
            self.x = x + 20
            self.y = y + 18

        self.bullet = pygame.image.load(self.bulletImageFile).convert()

    def display(self):
        self.screen.blit(self.bullet, (self.x, self.y))

    def checkY(self):
        return self.y

    def judgeOut(self):
        if self.checkY() > 820 or self.checkY() < 1:
            return True
        else:
            return False

    def move(self):
        if self.who == "player":
            self.y -= 7
        elif self.who == "enemy":
            self.y += 7


class Plane(object):
    def __init__(self, screen, who):
        self.x = 230
        self.y = 600
        self.screen = screen
        self.who = who
        self.planeImageFile = "./img/hero.gif"
        self.plane = pygame.image.load(self.planeImageFile).convert()
        self.bulletList = []

    def display(self):
        self.screen.blit(self.plane, (self.x, self.y))
        time.sleep(0.01)
        tempBulletList = []

        for needRemove in self.bulletList:
            if needRemove.judgeOut():
                tempBulletList.append(needRemove)

        for tmp in tempBulletList:
            self.bulletList.remove(tmp)

        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def shoot(self):
        self.b = PBullet(self.screen, self.x, self.y, self.who)
        self.bulletList.append(self.b)


class Player(Plane):
    def __init__(self, screen, who):
        self.plane = pygame.image.load(self.planeImageFile).convert()
    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10


class Enemy(Plane):
    def __init__(self,screen,who):
        self.x = 230
        self.y = 0
        self.planeImageFile = "./img/enemy-1.gif"
        self.direction = "left"

    def checkX(self):
        return self.x

    def move(self):
        if self.direction == "right":
            self.x += 3
        elif self.direction == "left":
            self.x -= 3

        if self.checkX() > 440:
            self.direction = "left"
            print(self.direction)
        elif self.checkX() < 0:
            self.direction = "right"
            print(self.direction)

    def shoot(self):
        num = random.randint(1, 20)
        if num == 10:
            super().shoot()
