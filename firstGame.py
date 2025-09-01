import pygame, simpleGE, random, csv

""" 
Asset Attributions:

cards - Kenney: https://www.kenney.nl/assets/playing-cards-pack

"""

class Game(simpleGE.Scene):
    def __init__(self, size = (640, 640)):
        super().__init__()
        self.screen = pygame.display.set_mode(size)
        self.background = pygame.Surface(self.screen.get_size())
        pygame.Surface.fill(self.background, (0, 128, 255))
        self.checkerboard = []
        self.ROWS = 8
        self.COLS = 8
        self.loadCheckerboard()
        
        self.redChecker = Checker(self)
        self.redChecker.setColor(self.redChecker.RED)
        self.redChecker.position = self.checkerboard[0][7].position
        self.sprites = [self.checkerboard, self.redChecker]

    def process(self):
        for row in self.checkerboard:
            for square in row:
                square.isTouchingSide()
                    
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
                newSquare.row = row
                newSquare.col = col
                self.checkerboard[row].append(newSquare)

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
        self.row = 0
        self.col = 0
        self.isTouchingLeft = False
        self.isTouchingRight = False
        self.isTouchingBottom = False
        self.isTouchingTop = False

    def setState(self, state):
        self.state = state
        self.copyImage(self.images[state])
        self.setSize(50,50)
    
    def changeState(self, state):
        if state == self.RED:
            self.copyImage(self.images[self.BLACK])
            self.setSize(50,50)
        else:
            self.copyImage(self.images[self.RED])
            self.setSize(50,50)

    def isTouchingSide(self):
        if (self.col + 1) < self.scene.COLS:
            if self.scene.checkerboard[self.row][self.col + 1]:
                self.isTouchingLeft = True
        if self.scene.checkerboard[self.row][self.col - 1]:
            self.isTouchingRight = True
        if self.scene.checkerboard[self.row - 1][self.col]:
            self.isTouchingTop = True
        if (self.row + 1) < self.scene.ROWS:
            if self.scene.checkerboard[self.row + 1][self.col] != None:
                self.isTouchingBottom = True       

class Checker(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = [
            pygame.image.load("redChecker.png"),
            pygame.image.load("blackChecker.png")
        ]
        self.RED = 0
        self.BLACK = 1
        self.state = self.RED
        self.setSize(40,40)
        self.setBoundAction(self.CONTINUE)

    def setColor(self, state):
        self.state = state
        self.copyImage(self.images[self.state])

class Card(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("card images/card_back.png")
        self.setSize(100,100)
        self.position = (100, 500)
        self.images = []
        with open('card images/_cards.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.images.append(pygame.image.load("card images/" + row['card_name']))
       

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()