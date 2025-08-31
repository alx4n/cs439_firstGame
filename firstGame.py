import pygame, simpleGE, random

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.player = Player(self)
        pygame.Surface.fill(self.background, (0, 128, 255))
        self.checkerboard = []
        self.ROWS = 8
        self.COLS = 8
        startingX = 200
        startingY = 25
        self.loadCheckerboard()
        self.sprites = [self.player, self.checkerboard]

    def _process(self):
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.checkerboard[i][j].clicked:
                    self.checkerboard[i][j].state = 0
                    
    
    def loadCheckerboard(self):
        map = [
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0]
        ]

        for row in range(self.ROWS):
            self.checkerboard.append([])
            for col in range(self.COLS):
                currentVal = map[row][col]
                newSquare = Square(self)
                newSquare.setState(currentVal)
                newSquare.position = (150 + (50 * row), 25 + (50 * col))
                self.checkerboard[row].append(newSquare)

class Player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)

class Square(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = [
            pygame.image.load("red-square.png"),
            pygame.image.load("black-square.png")
        ]
        self.setSize(50,50)
        self.RED = 0
        self.BLACK = 1
        self.state = self.RED
        self.setBoundAction(self.HIDE)

    def setState(self, state):
        self.state = state
        self.copyImage(self.images[state])
        self.setSize(50,50)

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()