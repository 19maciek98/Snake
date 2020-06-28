from random import randint
import pygame
from pygame import (Rect)
from sys import exit
from pygame.locals import (K_DOWN, K_ESCAPE, K_LEFT,
                           K_RIGHT, K_UP, KEYDOWN, QUIT)


class GameLogic:

    def __init__(self, windowSizeX=250, windowSizeY=250):
        self.windowSizeX = windowSizeX
        self.windowSizeY = windowSizeY
        self.gameUnitSize = 15
        if (self.windowSizeX % self.gameUnitSize != 0):
            self.windowSizeX += self.gameUnitSize - self.windowSizeX % self.gameUnitSize
        if (self.windowSizeY % self.gameUnitSize != 0):
            self.windowSizeY += self.gameUnitSize - self.windowSizeY % self.gameUnitSize
        self.window = pygame.display.set_mode(
            [self.windowSizeX, self.windowSizeY])
        pygame.display.set_caption("Snakes!")
        self.window.fill((0, 0, 0))
        pygame.font.init()
        self.font = pygame.font.SysFont("bahnschrift", 20)

        self.text = self.font.render(
            "Press any key to begin", True, (255, 255, 255))
        self.startTextRect = self.text.get_rect(
            center=(windowSizeX/2, windowSizeY/2))
        self.snake = [self.startSnake()]
        self.snake1 = [self.startSnake1()]
        self.food = self.createFood()
        self.food1 = self.createFood1()
        self.speed = 15
        self.score = 0
        self.score1 = 0
        self.scoreText = self.font.render(
            f"Score: {self.score}", True, (255, 255, 255), None)
        self.score1Text = self.font.render(
            f"Score1: {self.score1}", True, (255, 255, 255), None)
        self.snakeDirections = {
            'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}

        self.snake1Directions = {
            'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}
        
        self.previousDirection = self.snakeDirections.get('left')
        self.previousDirection1 = self.snake1Directions.get('left')
        self._readyScreen()
        self._gameLoop()
