
# CS110 Project Proposal

# A Ripoff of Fire Emblem But Seriously it is

## CS 110 Final Project

### Fall Semester, 2022

### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

[Repl](https://replit.com/join/mdpcukgnro-jo-cheungcheung)

[Demo Slides](https://docs.google.com/presentation/d/1EzJeEtMkL8QF2dRZl_swCZaoDkbE_AoH3_Oo4zgj4_s/edit?usp=sharing)

### Team: 12

#### Jo Cheung Wong, Tim Zheng

***

## Project Description

Title Screen is where the user gets to deside the player's name and start the game. The game is really simple, using the arrow keys to move the player character to the monsters to attempt to fight it. Fighting will result in the monster losing HP till it dies and you move onto the demon lord to beat the game and you name will be recorded in a mini Hall of Fame.

***

## User Interface Design

- **Initial Concept**
  - Menu screen: user decides their name of the player that will be listed in Hall of Fame before starting game.
  - ![Menu Screen](assets/Menu.PNG)
    Game screen: movement of player character around map to collide with monsters to fight them and kill them.
  - ![Game Screen](assets/GameScreen.PNG)
- **Final GUI**
  - Final versions of GUI
    ![Menu Screen](assets/Menu.PNG)

    ![Game Screen](assets/GameScreen.PNG)

***

## Program Design

Our design is similar to Fire Emblem the Sacred Stones as we pulled sprites and a map from the game. We designed it to where the user would move the hero around the map to fight the monster and eventually the demon lord and when they win, their name would recorded into the Hall of Fame.

- Non-Standard libraries
  - None

- Class Interface Design
   ![class diagram](assets/Class_Diagram.jpeg)

- Classes
  - Player: the Hero that the User controls, has movement with the arrow keys and has an objective to kill all monsters. Has an attack and speed stat to determine how far it moves when arrow keys are pressed and how much damage it can do to monsters when colliding with them
  - Enemy: the boss monster and regular Monster that threatens the Hero. Stationary and has HP stat and attack stat. Takes damage when colliding with Hero and pushs them back a random distance when countering. Boss monster is just a bigger and stronger version of the regular monster
  - Background: the Map and the Menu screen of the program and kind of measures where the character and Monsters are
  - Controller: the code that runs all the behind the scene actions like damage taken during collision, collision tracking, movement of each character and what pulls the needed information from each file to keep the game running.

## Project Structure and File List

The Project is broken down into the following file structure:

- main.py

- src
  - Background.py,Enemy.py,Player.py,Controller.py

- assets
  - RecordofPersons.json, Mlord sprite.png, Game Boy Advance - Fire Emblem The Sacred Stones - Map Sprites.png, Boss_dialouge.json, Cyclope sprite.png, DLord sprite.png, fe8map6.png, Game Boy Advance - Fire Emblem The Sacred Stones - Chapter 14 Eirika.png, Map 1 sprite.png
- etc
  - Class_Diagram.jpeg, GameScreen.png, Menu.png, milestone2.md

***

## Tasks and Responsibilities

  Tim Zheng - Subloop management and design
  Jo Cheung Wong - PNGS and Models
  Both - Everything else not credited to one person

## Testing

Our testing strategy was fairly simple - implement one feature, test that feature, and repeat.

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|1|Start Program |Menu Screen appears where name can be entered, the game can be played, and the game can be quit|
|2|Press the down arrow key once, then press the Enter key| changes to game screen where user assumes control of the Hero|
|3|Arrow up to move up, arrow left to move left, arrow down to move down, arrow right to move right | moves Hero in corrisponding direction of arrow key pressed|
|4|Using the arrow keys, charge towards the smaller of the two monsters| Player is knocked back |
|5|Repeatedly bash into the monster| The monster dies/disappears |
|6|Repeat steps 4-5 except with the bigger monster| The big monster dies, but his ghost gives a great speech. Control is taken away from the player|
|7|Wait while your name is being recorded in the Hall of Fame| pygame exits and the program ends|
