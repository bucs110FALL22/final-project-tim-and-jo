@@ -11,6 +11,8 @@ Come up with interfaces for 3 possible classes you think you may need for your p

## Class Interface 1

The object that the Player controls

a. class Player:
    i. attributes
        1. x
@@ -22,10 +24,26 @@ a. class Player
        1. move_hori()
        2. move_vert()
        3. interact()

        4. is_controlling()

## Class Interface 2

< add your interface >
This is almost the same as the player character, but controlled by the CPU
A catch-all class for characters that the player does not control by default (is_mind_control() gives control to the player)

a. class NPC:
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

class Monster:
  i. attributes
    1. x
    2. y
    3. image
    4. type/variant
    5. class
    6. HP
    7. SP
    8. Stat_increase #if player character is too strong stat wise or lvl wise, stats will increase to make it a challenge
  ii. method of movement
        1. move_hori()
        2. move_vert()
        3. aggro_range()
        4. RNG encounter due to movement

class Boss:
  i. attribute
1. x
2. y
3. stationary until provoked
4. image
5. Multiple health bars
6. Sp
8. Stat_increase
  ii. method of movement
1.no movement
2. static encounter/encounter when entering boss room