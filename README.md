![Battleship](https://mwresearch.github.io/t_battleship/doc/battleship-teaser.webp)  

# Terminal Battleship

This is the classic Battleship game in it’s simplest form, written entirely in python.  
You can read more about Battleship games here: [Battleship (game) - Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))  
You can see a running version of this code here: [Terminal Battleship](https://terminal-battleship-97f847223817.herokuapp.com/)

## How to play:
- In this game you play against the computer. You have to sink the computer’s ships (are actually more like submarines) by guessing a row and column number.  
- You start first and the computer makes it’s guess after you.  
- You can see where your ships are placed, indicated by an “S”, but you can’t see where the computer’s ships are.  
- Missed shots are indicated by a dot. Successful hits are indicated by an “X”.  
- The winner is the player who sinks all the opponent’s battleships first.  

## Design and Terminal modifications
I didn’t create the terminal software (The command prompt window that shows the running python code), therefore I don’t have full control over it. But I modified it to give it a more pleasant look.  
I changed the font size, improved the spacings, reduced the column size to 45, and since there is nothing more awkward than white text on pitch black background, I changed the background color to blue.  
I created a responsive layout so that this game is playable on both mobile devices with small screens and desktop devices with large screens.  

## Features
- Ships are randomly placed on both the player’s and computer’s board.
- Input validation:
  - You can’t enter coordinates outside the grid size.
  - You must enter numbers.  
- If you enter the same guess twice, the system will inform you about that.
- You can modify the board size and the number of ships in run.py at the beginning of the code.
![variables](https://mwresearch.github.io/t_battleship/doc/initial-vars.png)  

### Screenshots:
![Welcome-message](https://mwresearch.github.io/t_battleship/doc/welcome-message.png)  
The game boards:  
![Boards](https://mwresearch.github.io/t_battleship/doc/boards.png)  
Game play:  
![Game play](https://mwresearch.github.io/t_battleship/doc/game-play.png)
![Game play](https://mwresearch.github.io/t_battleship/doc/game-play2.png)  
(Wrong input) warnings:  
![Wrong Input](https://mwresearch.github.io/t_battleship/doc/wrong-input.png)  
Game Won:  
![You have won](https://mwresearch.github.io/t_battleship/doc/you-win.png)
![PC has won](https://mwresearch.github.io/t_battleship/doc/computer-wins.png)

## Future plans
- Allowing ships larger than 1x1


## Code validation
I have tested my code with [pep8ci.herokuapp.com](https://pep8ci.herokuapp.com) and it shows no errors.

## Deployment
I deployed this python game on Heroku, the cloud application platform. 
You can see a running version of this code here: [Terminal Battleship](https://terminal-battleship-97f847223817.herokuapp.com/)

## Initial bugs and problems
One challenge was to copy a multi dimensional list.  Since making a copy of multi dimensional lists is not as easy as copying a variable, my code didn’t work as intended and it took a while until I figured out how to make a copy of a multi dimensional list.  
After winning, entering q didn’t quit the game. I solved this problem by using return False instead of break.

## Remaining bugs
None so far

## Credits
I developed this game using information provided by:  
Codeinstitute, W3school, Stackoverflow and myself.
