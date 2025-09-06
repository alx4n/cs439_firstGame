import pygame, simpleGE, random, csv

""" 
Asset Attributions:

cards - Kenney: https://www.kenney.nl/assets/playing-cards-pack
checkers - Kenney: https://www.kenney.nl/assets/boardgame-pack
squares - made in Krita

"""

class Game(simpleGE.Scene):
    def __init__(self, size = (640, 640)):
        super().__init__(size)
        pygame.Surface.fill(self.background, (0, 128, 255))
        
        self.cards = []
        with open('assets/card images/_cards.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            for row in reader:
                newCard = CardStruct(row['card_name'], row['movement_points'], row['color'], row['placement'], pygame.image.load('assets/card images/' + row['card_name'] + '.png'))
                self.cards.append(newCard)
        self.onScreenCards = []
        for i in range(4):
            newCard = Card(self)
            newCard.position = (150 + (i * 100), 500)
            newCard.hide()
            self.onScreenCards.append(newCard)
        self.onScreenCards[0].show()
        
        self.checkerboard = []
        self.ROWS = 8
        self.COLS = 8
        self.loadCheckerboard()
        self.row = 8
        self.col = 1
        self.currentSquare = self.checkerboard[self.row][self.col]
        
        self.redChecker = Checker(self)
        self.redChecker.setColor(self.redChecker.RED)
        self.redChecker.position = self.currentSquare.position
        self.sprites = [self.checkerboard, self.redChecker, self.onScreenCards]

    def process(self):
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

    def processEvent(self, event):
        self.currentSquare.isTouchingSide(self.currentSquare.row, self.currentSquare.col)
        if self.isKeyPressed(pygame.K_LEFT):
            if self.currentSquare.isTouchingLeft:
                print(self.currentSquare.isTouchingLeft)
                if self.checkerboard[self.currentSquare.row][self.currentSquare.col - 1].color != 2:
                    self.redChecker.position = self.checkerboard[self.currentSquare.row][self.currentSquare.col - 1].position
                    self.checkerboard[self.currentSquare.row][self.currentSquare.col - 1].checkCollision()
                    print(self.currentSquare.row, self.currentSquare.col)
            else:
                print(self.currentSquare.isTouchingLeft)
                print(self.currentSquare.row, self.currentSquare.col)
        if self.isKeyPressed(pygame.K_RIGHT):
            if self.currentSquare.isTouchingRight:
                print(self.currentSquare.isTouchingRight)
                if self.checkerboard[self.currentSquare.row][self.currentSquare.col + 1].color != 2:
                    self.redChecker.position = self.checkerboard[self.currentSquare.row][self.currentSquare.col + 1].position
                    self.checkerboard[self.currentSquare.row][self.currentSquare.col + 1].checkCollision()
                    print(self.currentSquare.row, self.currentSquare.col)
            else:
                print(self.currentSquare.isTouchingRight)
                print(self.currentSquare.row, self.currentSquare.col)
        if self.isKeyPressed(pygame.K_UP):
            if self.currentSquare.isTouchingTop:
                print(self.currentSquare.isTouchingTop)
                if self.checkerboard[self.currentSquare.row - 1][self.currentSquare.col].color != 2:
                    self.redChecker.position = self.checkerboard[self.currentSquare.row - 1][self.currentSquare.col].position
                    self.checkerboard[self.currentSquare.row - 1][self.currentSquare.col].checkCollision()
                    print(self.currentSquare.row, self.currentSquare.col)
            else:
                print(self.currentSquare.isTouchingTop)
                print(self.currentSquare.row, self.currentSquare.col)
        if self.isKeyPressed(pygame.K_DOWN):
            if self.currentSquare.isTouchingBottom:
                print(self.currentSquare.isTouchingBottom)
                if self.checkerboard[self.currentSquare.row + 1][self.currentSquare.col].color != 2:
                    self.redChecker.position = self.checkerboard[self.currentSquare.row + 1][self.currentSquare.col].position
                    self.checkerboard[self.currentSquare.row + 1][self.currentSquare.col].checkCollision()
                    print(self.currentSquare.row, self.currentSquare.col)
            else:
                print(self.currentSquare.isTouchingBottom)
                print(self.currentSquare.row, self.currentSquare.col)
            
    def loadCheckerboard(self):
        map = [
            [2,2,2,2,2,2,2,2,2,2],
            [2,0,1,0,1,0,1,0,1,2],
            [2,1,0,1,0,1,0,1,0,2],
            [2,0,1,0,1,0,1,0,1,2],
            [2,1,0,1,0,1,0,1,0,2],
            [2,0,1,0,1,0,1,0,1,2],
            [2,1,0,1,0,1,0,1,0,2],
            [2,0,1,0,1,0,1,0,1,2],
            [2,1,0,1,0,1,0,1,0,2],
            [2,2,2,2,2,2,2,2,2,2]
        ]

        for row in range(self.ROWS + 2):
            self.checkerboard.append([])
            for col in range(self.COLS + 2):
                currentVal = map[row][col]
                newSquare = Square(self)
                newSquare.setColor(currentVal)
                newSquare.position = (100 + (50 * col), 0 + (50 * row))
                newSquare.row = row
                newSquare.col = col
                self.checkerboard[row].append(newSquare)

class Square(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = [
            pygame.image.load("assets/red-square.png"),
            pygame.image.load("assets/black-square.png"),
            pygame.image.load("assets/transparent-square.png")
        ]
        self.setSize(50,50)
        # color of square
        self.RED = 0
        self.BLACK = 1
        self.TRANSPARENT = 2
        self.color = self.RED

        # state of square
        self.EMPTY = 0
        self.OCCUPIED = 1
        self.state = self.EMPTY

        self.setBoundAction(self.CONTINUE)

        self.isTouchingLeft = False
        self.isTouchingRight = False
        self.isTouchingBottom = False
        self.isTouchingTop = False

    def process(self):
        pass
        
    def checkCollision(self):
        if self.collidesWith(self.scene.redChecker):
            self.state = self.OCCUPIED
            self.scene.currentSquare = self

    def setColor(self, color):
        self.color = color
        self.copyImage(self.images[color])
        self.setSize(50,50)

    def isTouchingSide(self, row, col):
        if (col - 1) > 0:
            if self.scene.checkerboard[row][col - 1]:
                self.isTouchingLeft = True
        if (col + 1) < self.scene.COLS + 1:
            if self.scene.checkerboard[row][col + 1]:
                self.isTouchingRight = True
        if (row - 1) > 0:
            if self.scene.checkerboard[row - 1][col]:
                self.isTouchingTop = True
        if (row + 1) < self.scene.ROWS + 1:
            if self.scene.checkerboard[row + 1][col]:
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
        self.currentSquare = self.scene.currentSquare

    def setColor(self, state):
        self.state = state
        self.copyImage(self.images[self.state])

class CardStruct():
    def __init__(self, name, value, color, placement, image):
        self.name = name
        self.value = value
        self.color = color
        self.placement = placement
        self.image = image

class Card(simpleGE.Sprite):
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