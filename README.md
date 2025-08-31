# Checkerboard Race
My first SimpleGE game

## Overview
Use the cards in your hand to nmove your checker and reach the other corner of the board before your opponent.

## Technical Overview
This is a 2D game in which the user controls where they move their checker by choosing cards that correspond to the amount of movement they may take. Three face-up cards are shown on the screen in addition to a face-down deck. To begin the game, the user clicks on the deck, which then displays three face-up cards to the player. The user then selects one of these cards to select the amount of movement they will take, but the movement must land them on a square of the same color as the card. Then the other player performs the same action with their hand.

## Primary Sprites
### Square
Each square on the checkerboard is its own sprite. The square is a subclass of the simpleGE sprite. Squares will be used to detect collision with the checker for placement and know whether they are connected to other squares. 

### Checker
The checker