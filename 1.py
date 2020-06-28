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









    def startSnake(self):
        snakeNodeX = self.window.get_width() / 2 - self.gameUnitSize
        if (snakeNodeX % self.gameUnitSize != 0):
            snakeNodeX -= snakeNodeX % self.gameUnitSize
        snakeNodeY = self.window.get_height() / 2 - self.gameUnitSize
        if (snakeNodeY % self.gameUnitSize != 0):
            snakeNodeY -= snakeNodeY % self.gameUnitSize
        snakeNodeRectangle = Rect(
            (snakeNodeX, snakeNodeY), (self.gameUnitSize, self.gameUnitSize))
        return snakeNodeRectangle
    
    def startSnake1(self): 
        snake1NodeX = self.window.get_width() / 2 - self.gameUnitSize
        if (snake1NodeX % self.gameUnitSize != 0):
            snake1NodeX -= snake1NodeX % self.gameUnitSize
        snake1NodeY = self.window.get_height() / 2 - self.gameUnitSize
        if (snake1NodeY % self.gameUnitSize != 0):
            snake1NodeY -= snake1NodeY % self.gameUnitSize
        snake1NodeRectangle = Rect(
            (snake1NodeX, snake1NodeY), (self.gameUnitSize, self.gameUnitSize))
        return snake1NodeRectangle

    def createFood(self):
        foodX = randint(0, self.window.get_width() - self.gameUnitSize)
        if (foodX % self.gameUnitSize != 0):
            foodX -= foodX % self.gameUnitSize
        foodY = randint(0, self.window.get_height() - self.gameUnitSize)
        if (foodY % self.gameUnitSize != 0):
            foodY -= foodY % self.gameUnitSize
        foodRectangle = Rect(
            (foodX, foodY), (self.gameUnitSize, self.gameUnitSize))
        return foodRectangle
    
    def createFood1(self):
        food1X = randint(0, self.window.get_width() - self.gameUnitSize)
        if (food1X % self.gameUnitSize != 0):
            food1X -= food1X % self.gameUnitSize
        food1Y = randint(0, self.window.get_height() - self.gameUnitSize)
        if (food1Y % self.gameUnitSize != 0):
            food1Y -= food1Y % self.gameUnitSize
        food1Rectangle = Rect(
            (food1X, food1Y), (self.gameUnitSize, self.gameUnitSize))
        return food1Rectangle

    def moveFood(self):
        self.food.x = randint(0, self.window.get_width() - self.gameUnitSize)
        if (self.food.x % self.gameUnitSize != 0):
            self.food.x -= self.food.x % self.gameUnitSize
        self.food.y = randint(0, self.window.get_height() - self.gameUnitSize)
        if (self.food.y % self.gameUnitSize != 0):
            self.food.y -= self.food.y % self.gameUnitSize
            
    def moveFood1(self):
        self.food1.x = randint(0, self.window.get_width() - self.gameUnitSize)
        if (self.food1.x % self.gameUnitSize != 0):
            self.food1.x -= self.food1.x % self.gameUnitSize
        self.food1.y = randint(0, self.window.get_height() - self.gameUnitSize)
        if (self.food1.y % self.gameUnitSize != 0):
            self.food1.y -= self.food1.y % self.gameUnitSize

    def createSnake(self):
        snakeNodeX = randint(0, self.window.get_width())
        if (snakeNodeX % self.gameUnitSize != 0):
            snakeNodeX -= snakeNodeX % self.gameUnitSize
        snakeNodeY = randint(0, self.window.get_height())
        if (snakeNodeY % self.gameUnitSize != 0):
            snakeNodeY -= snakeNodeY % self.gameUnitSize
        snakeNodeRectangle = Rect(
            (snakeNodeX, snakeNodeY), (self.gameUnitSize, self.gameUnitSize))
        return snakeNodeRectangle
    
    def createSnake1(self):
        snake1NodeX = randint(0, self.window.get_width())
        if (snake1NodeX % self.gameUnitSize != 0):
            snake1NodeX -= snake1NodeX % self.gameUnitSize
        snake1NodeY = randint(0, self.window.get_height())
        if (snake1NodeY % self.gameUnitSize != 0):
            snake1NodeY -= snake1NodeY % self.gameUnitSize
        snake1NodeRectangle = Rect(
            (snake1NodeX, snake1NodeY), (self.gameUnitSize, self.gameUnitSize))
        return snake1NodeRectangle

    def appendSnake(self):
        # add node to tail
        newSnakeLink = Rect((self.snake[len(self.snake) - 1].x, self.snake[len(
            self.snake) - 1].y), (self.gameUnitSize, self.gameUnitSize))
        self.snake.append(newSnakeLink)

    def appendSnake1(self):
        # add node to tail
        newSnake1Link = Rect((self.snake1[len(self.snake1) - 1].x, self.snake1[len(
            self.snake1) - 1].y), (self.gameUnitSize, self.gameUnitSize))
        self.snake1.append(newSnake1Link)
        
    def moveSnake(self, direction):
        x = 0
        y = 1
        self.snake[len(self.snake) - 1].x = self.snake[0].x + \
            direction[x] * self.speed
        self.snake[len(self.snake) - 1].y = self.snake[0].y + \
            direction[y] * self.speed
        self.snake.insert(0, self.snake.pop())
        self.previousDirection = direction
        
    def moveSnake1(self, direction):
        x = 0
        y = 1
        self.snake1[len(self.snake1) - 1].x = self.snake1[0].x + \
            direction[x] * self.speed
        self.snake1[len(self.snake1) - 1].y = self.snake1[0].y + \
            direction[y] * self.speed
        self.snake1.insert(0, self.snake1.pop())
        self.previousDirection1 = direction

    def intersect(self):
        if self.snake[0].x == self.food.x and self.snake[0].y == self.food.y:
            return True
        if self.snake[0].x == self.food1.x and self.snake[0].y == self.food1.y:
            return True
        
    def intersect1(self):
        if self.snake1[0].x == self.food.x and self.snake1[0].y == self.food.y:
            return True
        if self.snake1[0].x == self.food1.x and self.snake1[0].y == self.food1.y:
            return True

    def snakeCollidingWithWall(self):
        if self.snake[0].x >= self.windowSizeX or self.snake[0].x < 0 or self.snake[0].y >= self.windowSizeY or self.snake[0].y < 0:
            return True
        return False
    
    def snake1CollidingWithWall(self):
        if self.snake1[0].x >= self.windowSizeX or self.snake1[0].x < 0 or self.snake1[0].y >= self.windowSizeY or self.snake1[0].y < 0:
            return True
        return False

    def snakeCollidingWithSelf(self):
        for link in self.snake:
            if (self.snake[0] is not link):
                if self.snake[0].x == link.x and self.snake[0].y == link.y:
                    return True
        return False
    
    def snake1CollidingWithSelf(self):
        for link in self.snake1:
            if (self.snake1[0] is not link):
                if self.snake1[0].x == link.x and self.snake1[0].y == link.y:
                    return True
        return False

    def killSnake(self):
        self._gameOverScreen()
        
    def killSnake1(self):
        self._gameOverScreen()

    def _update(self):
        self.window.fill((0, 0, 0))

        if (self.intersect() == True):
            self.appendSnake()
            self.moveFood()
            self.moveFood1()
            self.score += 1
        elif (self.snakeCollidingWithWall() == True or self.snakeCollidingWithSelf() == True):
            self.killSnake()

        for link in self.snake:
            pygame.draw.rect(self.window, (255, 255, 25), link)
        pygame.draw.rect(self.window, (102, 255, 51), self.food)
        pygame.draw.rect(self.window, (102, 255, 51), self.food1)
        
        if (self.intersect1() == True):
            self.appendSnake1()
            self.moveFood()
            self.moveFood1()
            self.score1 += 1
        elif (self.snake1CollidingWithWall() == True or self.snake1CollidingWithSelf() == True):
            self.killSnake1()

        for link in self.snake1:
            pygame.draw.rect(self.window, (25, 255, 255), link)
        pygame.draw.rect(self.window, (102, 255, 51), self.food)
        pygame.draw.rect(self.window, (102, 255, 51), self.food1)

        self.scoreText = self.font.render(
            f"Score_yellow: {self.score}", True, (255, 255, 255))
        self.scoreTextRect = self.scoreText.get_rect(center=(70, 10))
        self.window.blit(self.scoreText, self.scoreTextRect)
        
        self.score1Text = self.font.render(
            f"Score_blue: {self.score1}", True, (255, 255, 255))
        self.score1TextRect = self.score1Text.get_rect(center=(70, 40))
        self.window.blit(self.score1Text, self.score1TextRect)

        pygame.display.update()

    def _input(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
        keys = pygame.key.get_pressed()
        if (keys[K_LEFT] and self.previousDirection != self.snakeDirections.get('right')):
            self.moveSnake(self.snakeDirections.get('left'))
        elif (keys[K_RIGHT] and self.previousDirection != self.snakeDirections.get('left')):
            self.moveSnake(self.snakeDirections.get('right'))
        elif (keys[K_UP] and self.previousDirection != self.snakeDirections.get('down')):
            self.moveSnake(self.snakeDirections.get('up'))
        elif (keys[K_DOWN] and self.previousDirection != self.snakeDirections.get('up')):
            self.moveSnake(self.snakeDirections.get('down'))
        else:
            self.moveSnake(self.previousDirection)
            
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] and self.previousDirection1 != self.snake1Directions.get('right')):
            self.moveSnake1(self.snake1Directions.get('left'))
        elif (keys[pygame.K_d] and self.previousDirection1 != self.snake1Directions.get('left')):
            self.moveSnake1(self.snake1Directions.get('right'))
        elif (keys[pygame.K_w] and self.previousDirection1 != self.snake1Directions.get('down')):
            self.moveSnake1(self.snake1Directions.get('up'))
        elif (keys[pygame.K_s] and self.previousDirection1 != self.snake1Directions.get('up')):
            self.moveSnake1(self.snake1Directions.get('down'))
        else:
            self.moveSnake1(self.previousDirection1)

    def _readyScreen(self):
        while True:
            self.window.blit(self.text, self.startTextRect)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
            keys = pygame.key.get_pressed()
            if (keys[K_LEFT]):
                self.previousDirection = self.snakeDirections.get('left')
                break
            if (keys[K_RIGHT]):
                self.previousDirection = self.snakeDirections.get('right')
                break
            if (keys[K_UP]):
                self.previousDirection = self.snakeDirections.get('up')
                break
            if (keys[K_DOWN]):
                self.previousDirection = self.snakeDirections.get('down')
                break
            pygame.display.update()
            
            keys = pygame.key.get_pressed()
            if (keys[K_LEFT]):
                self.previousDirection = self.snake1Directions.get('left')
                break
            if (keys[K_RIGHT]):
                self.previousDirection = self.snake1Directions.get('right')
                break
            if (keys[K_UP]):
                self.previousDirection = self.snake1Directions.get('up')
                break
            if (keys[K_DOWN]):
                self.previousDirection = self.snake1Directions.get('down')
                break
            pygame.display.update()

    def _gameOverScreen(self):
        while True:
            self.window.fill((0, 0, 0))
            self.text = self.font.render(
                f"Game Over, Score_yellow: {self.score}, Score_blue: {self.score1}", True, (255, 255, 255))
            self.startTextRect = self.text.get_rect(
                center=(self.windowSizeX/2, self.windowSizeY/2))
            self.window.blit(self.text, self.startTextRect)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
            pygame.display.update()

    def _gameLoop(self):
        while True:
            pygame.time.delay(100)
            self._input()
            self._update()








class LeaderBoard:

    def __init__(self):
        
        file = open("C:\git\hmt\Learning\leaderboard.txt", "r")
        self.leaderboard = []
        i = 0
        while i < 5:
            chunk = file.readline()
            if (chunk == ''):
                break
            LeaderBoard.insert(0, chunk.splitlines())
            i += 1
        file.close()
        self.leaderboard.reverse()

    
    def addToLeaderboard(self, name, newScore):
        i = 0
        for score in self.leaderboard:
            if newScore > score:
                self.leaderboard.remove(score)
                self.leaderboard.insert(i, newScore)
            i += 1
        file = open("C:\git\hmt\Learning\leaderboard.txt", "w")
        
        file.close()


def main():
    
    game = GameLogic(800, 800)


main()