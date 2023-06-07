# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("Decision Maker", color = "red")
define developer = Character("...")
define kendall = Character("Kendall")
define jan = Character("Jan")
# The game starts here.

label start:
    scene bg city
    with fade
    # The developer's beginning dialogue
    developer "Welcome, my friend."
    developer "You are invited, because we want you to make choices."
    developer "We want to know why you make these choices."
    developer "Your thought is crucial for us."
    developer "Now let's start it."

    menu:
        "Continue":
            jump Scenario_1

label Scenario_1:
    
    developer "Now the story begins. You are going to make choices for Kendall and Jan."
    $ renpy.pause() #Pause to create a gap

    scene bg cafe

    ""






