# Checkerboard Race
My first SimpleGE game

## Overview
Use the cards in your hand to nmove your checker and reach the other corner of the board before your opponent.

## Technical Overview
This is a 2D game in which the user controls where they move their checker by choosing cards that correspond to the amount of movement they may take. Three face-up cards are shown on the screen in addition to a face-down deck. To begin the game, the user clicks on the deck, which then displays three face-up cards to the player. The user then selects one of these cards to select the amount of movement they will take, but the movement must land them on a square of the same color as the card. Then the other player performs the same action with their hand.

## Primary Sprites
### Square
Each square on the checkerboard is its own sprite. The square is a subclass of the simpleGE sprite. Squares will be used to detect collision with the checker for placement and know whether they are connected to other squares. Each square is 50x50 pixels and is either a png of a red square or black square, which is determined by the self.color variable. The squares remain on screen for the entire game and have a boundary condition of continue because, although they remain in a fixed position, if they are placed so that they are partially off screen they should continue to be rendered. On collision with a checker, the square's state changes to signify that the square is occupied.

### Checker
Each checker is its own sprite, which is a subclass of the simpleGE sprite. The checker image is a basic checker png from Kenney's assets. Checkers move based on the movement points alloted by the card selected and can only move to adjacent squares that are in the same row or column as them. Movement is determined by player input on the arrow keys. Each checker is 40x40 pixels and is bounded by the checkerboard boundaries. The checkers remain on screen for the entire game.

### Card
The card is a simpleGE sprite that takes on the image of one of 52 cards from a standard deck or a card back from the Kenney cards pack, sized at 100x100 pixels. Cards have a fixed position at the bottom of the screen and face-up cards are hidden until the deck is pressed. Each card has a value that determines how much movement the player can take. The color of the card represents which color tile the player must land on.

## The Game Class
### Initialization
The primary class is the game class, which has the following elements:
- cards - a list of card sprites
- onScreenCards - a list of card slots for visible cards
- checkerboard - a list of lists of square sprites arranged in a checkerboard pattern
- redChecker - an instance of the checker

### Sprite Groups
The redChecker, onScreenCards, and the checkerboard are add to the Game class sprite list.

### The ProcessEvent Method
The processEvent method checks for key presses to move the checker around the checkerboard. On every key press, the following is checked:
- which key was pressed? (up, down, left, right)
- if a key was pressed, is there aan available square in that direction that the checker can move to?
- if the move is legal, move the position of the checker to the corresponding square and change the current square to the new square

## Asset list
The game uses the following assets, which are either original or have a Creative Commons CC0 license
- cards - Kenney: https://www.kenney.nl/assets/playing-cards-pack
- checkers - Kenney: https://www.kenney.nl/assets/boardgame-pack
- squares - made in Krita

## Milestone plan
- Initialize a screen and player sprite
- Create a checkerboard of individual square sprites
- Add a checker piece that can be positioned on a particular square
- Check for interactivity with individual squares by checking for mouse input
- Check for interactivity with the checker piece by checking for response to mouse input
- Add a way for individual square sprites to recognize whether they have neighbors
- Add way for checker to move to a new square based on whether one exists and is accessible in that direction
- Add keyboard input to checker to allow movement

### Stretch Goals
- Determine movement based on selected card
- Add second player
- Add way to check if checker has reached goal
- Add intro and winner screens