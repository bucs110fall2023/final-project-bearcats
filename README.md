[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803297&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Bearcats Dinosaur Game
## CS110 Final Project Fall, 2023

## Team Members

Jessica Zheng and Catherin Patrick 

***

## Project Description

A dinosaur is continously running and it needs to avoid objects. The player has to jump in order to avoid colliding with obstacles.
***    

## GUI Design

### Initial Design

![initial gui](assets/initialgui.png)

### Final Design

![final gui](assets/finalgui.png)

## Program Design

### Features

1. Start menu
2. Moveable dinosaur
3. Obstacles
4. Scrolling background
5. Game over / High score

### Classes

- Scroll Class:


## ATP
Team: Bearcats 
Jessica Zheng & Catherin Patrick

Test Case 1: Player Movement 
Test Description: Verify that the player moves jumps, ducks, and continuously moves forward as expected. 
Test Steps: 
Start the game 
Press the space key. 
Verify that the player has jumped. 
Press the down arrow key. 
Verify that the player’s head shifted down. 
Expected Outcome: The player should jump and duck in response to the space key and down key inputs. 

Test Case 2: Collision Detection with Cacti. 
Test Description: Ensure that the collisions between the player and cacti. 
Test Steps: 
Start the game 
Press the space key to jump over a cactus. 
Verify that no collision is detected. 
Allow the player to run into a cactus. 
Verify that the player collides with the cactus.
Expected Outcome: Player should collide correctly with the cactus. 

Test Case 3: Collision Detection with birds.  
Test Description: Ensure that the collisions between the player and birds. 
Test Steps: 
Start the game 
Press down arrow  key to duck under a bird. 
Verify that no collision is detected. 
Allow player to run into bird 
Verify that the player collides with the bird. 
Expected Outcome: Player should collide correctly with the cactus. 

Test Case 4: Menu Navigation 
Test Description: test the navigation through the game’s main menu. 
Test Steps: 
Start the game 
Navigate through the main menu options (Start Game, Settings, Quit) 
Verify that each option is selectable and leads to the expected actions. 
Expected Outcome: The main menu should allow the player to navigate through options and select them. 

Test Case 5: Game Over Condition
Test Description:  
Test Steps: 
Start the game 
Play until the player loses by colliding with a cactus or bird. 
Verify that the game displays a “Game Over” message. 
Expected Outcome: The game should display a “Game Over” message when the player loses all lives. 


