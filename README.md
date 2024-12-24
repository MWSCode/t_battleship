# Terminal Battleship

This is the classic Battleship game in it’s simplest form, written entirely in python.  
You can read more about Battleship games here: [Battleship (game) - Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))  
You can see a running version of this code here: [Terminal Battleship](https://www.online-python.com/yBJVdlf9Iw)

## How to play:

- In this game you play against the computer. You have to sink the computer’s ships (are actually more like submarines) by guessing a row and column number.  
- You start first and the computer makes it’s guess after you.  
- You can see where your ships are placed, indicated by an “S”, but you can’t see where the computer’s ships are.  
- Missed shots are indicated by a dot. Successful hits are indicated by an “X”.  
- The winner is the player who sinks all the opponent’s battleships first.  

## Features

- Ships are randomly placed on both the player’s and computer’s board.
- Input validation:
  - You can’t enter coordinates outside the grid size.
  - You must enter numbers.  
- If you enter the same guess twice, the system will inform you about that.
- You can modify the board size and the number of ships at the beginning of the code.
### Screenshots:
![Welcome-message](https://mwresearch.github.io/t_battleship/doc/welcome-message.png)
![Boards](https://mwresearch.github.io/t_battleship/doc/boards.png)
![Game play](https://mwresearch.github.io/t_battleship/doc/game-play.png)
![Game play](https://mwresearch.github.io/t_battleship/doc/game-play2.png)
![Wrong Input](https://mwresearch.github.io/t_battleship/doc/wrong-input.png)
![You have won](https://mwresearch.github.io/t_battleship/doc/you-win.png)
![PC has won](https://mwresearch.github.io/t_battleship/doc/computer-wins.png)

## Future plans
- Allowing ships larger than 1x1


## Code validation
I have tested my code with [pep8ci.herokuapp.com](https://pep8ci.herokuapp.com) and it shows no errors.

## Deployment
My plan to deploy this code on Heroku wasn't successful so far, because of problems with the account registration.
But you can easily see this code running on [online-python.com](www.online-python.com):  
- [Terminal Battleship](https://www.online-python.com/yBJVdlf9Iw)

## Initial bugs and problems
One challenge was to copy a multi dimensional list.  Since making a copy of multi dimensional lists is not as easy as copying a variable, my code didn’t work as intended and it took a while until I figured out how to make a copy of a multi dimensional list.  
After winning, entering q didn’t quit the game. I solved this problem by using return False instead of break.

## Remaining bugs
None so far

## Credits
I developed this game using information provided by:  
Codeinstitute, W3school, Stackoverflow and myself.
