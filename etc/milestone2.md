milestone 2 template
======================================================================

# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

The object that the Player controls

a. class Player
    i. attributes
        1. x
        2. y
        3. image
        4. HP
        5. MP/SP
    ii. methods
        1. move_hori()
        2. move_vert()
        3. interact()
        4. is_controlling()
        
## Class Interface 2

This is almost the same as the player character, but controlled by the CPU
A catch-all class for characters that the player does not control by default (is_mind_control() gives control to the player)

a. class NPC
    i. attributes
        1. x
        2. y
        3. image
        4. type
        4. HP
        5. MP/SP
    ii. methods
        1. move_hori()
        2. move_vert()
        3. interact()
        4. is_mind_control()

## Class Interface 3

< add your interface >

======================================================================
