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
        
        self.cards = []
        with open('assets/card images/_cards.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            for row in reader:
                newCard = Card(row['card_name'], row['movement_points'], row['color'], row['placement'], pygame.image.load('assets/card images/' + row['card_name'] + '.png'))
                self.cards.append(newCard)
        self.onScreenCards = []
        for i in range(4):
            newCard = CardSprite(self)
            newCard.position = (150 + (i * 100), 500)
            newCard.hide()
            self.onScreenCards.append(newCard)
        self.onScreenCards[0].show()
        
        self.checkerboard = []
        self.ROWS = 8
        self.COLS = 8
        self.loadCheckerboard()
        self.row = 0
        self.col = 7
        self.currentSquare = self.checkerboard[self.row][self.col]
        
        self.redChecker = Checker(self)
        self.redChecker.setColor(self.redChecker.RED)
        self.redChecker.position = self.currentSquare.position
        self.sprites = [self.checkerboard, self.redChecker, self.onScreenCards]

    def process(self):
        for row in self.checkerboard:
            for square in row:
                square.isTouchingSide()
        if self.onScreenCards[1].visible == False:
            if self.onScreenCards[0].clicked:
                for i in range(1,4):
                    self.onScreenCards[i].drawCard()
                    self.onScreenCards[i].show()
        for i in range(1,4):
            if self.onScreenCards[i].clicked:
                index = self.onScreenCards[i].value
                print("You can move " + str(self.cards[index].value) + " space(s)")
                self.redChecker.moveSpaces()
                self.onScreenCards[i].drawCard()
            
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
            pygame.image.load("assets/red-square.png"),
            pygame.image.load("assets/black-square.png")
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
        if self.scene.checkerboard[self.row][self.col - 1]:
            self.isTouchingLeft = True   
        if (self.col + 1) < self.scene.COLS:
            if self.scene.checkerboard[self.row][self.col + 1]:
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
            pygame.image.load("assets/redChecker.png"),
            pygame.image.load("assets/blackChecker.png")
        ]
        self.RED = 0
        self.BLACK = 1
        self.state = self.RED
        self.setSize(40,40)
        self.setBoundAction(self.CONTINUE)

    def setColor(self, state):
        self.state = state
        self.copyImage(self.images[self.state])
    
    def process(self):
        self.moveSpaces()
                
    def moveSpaces(self):
        if self.isKeyPressed(pygame.K_LEFT):
        self.image = image

class CardSprite(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("assets/card images/card_back.png")
        self.setSize(100,100)
        self.position = (100, 500)
        self.images = []
        self.index = 0
        for i in range(0,53):
            self.images.append(self.scene.cards[i].image)
            self.images[i] = pygame.transform.scale(self.images[i], (100,100))

    def drawCard(self):
        self.value = random.randint(2,53)
        self.index = self.value
        self.copyImage(self.images[self.value])

    def getMovement(self, index):
        self.card = self.cardNames[index]
        self.movement = int(self.dict[self.card])
        return self.movement

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()