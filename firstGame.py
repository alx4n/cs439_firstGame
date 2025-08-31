import pygame, simpleGE, random

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.player = Player(self)
        self.sprites = [self.player]

class Player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()