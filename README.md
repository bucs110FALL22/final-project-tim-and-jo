:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# A Ripoff of Fire Emblem But Seriously it is
## CS 110 Final Project
### Fall Semester, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

[repl](#)](https://replit.com/join/mdpcukgnro-jo-cheungcheung)

<< [link to demo presentation slides](#12) >>

### Team: 12
#### Jo Cheung Wong, Tim Zheng
***

## Project Description

<<Title Screen is where the user gets to deside the player's name and start the game. The game is really simple, using the arrow keys to move the player character to the monsters to attempt to fight it. Fighting will result in the monster losing HP till it dies and you move onto the demon lord to beat the game and you name will be recorded in a mini Hall of Fame.>>

***    

## User Interface Design

- **Initial Concept**
  - << Menu screen: user decides their name of the player that will be listed in Hall of Fame before starting game.

    >>
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design
Our design would be similar to JRPG games mixed in with turn based attack/turns where you can explore areas of the map to complete objectives, fighting monsters along the way that block your path or ambush you. We are planning on using sprites to represent the player moving on a background map and entering a specific area will open up a new map where monsters and items will appear. 
* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
    * << You should have a list of each of your classes with a description. >>

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * << all of your python files should go here >>
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.

## Testing

* << Describe your testing strategy for your project. >>

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
