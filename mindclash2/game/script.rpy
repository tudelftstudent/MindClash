# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define skylar = Character("Skylar")
define friend = Character("Skylar's friend")
define leader = Character("Team leader")
define members = Character("Team members")



# # The game starts here.
#
# label start:
#
#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.
#
#     scene bg room
#
#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.
#
#     show eileen happy
#
#     # These display lines of dialogue.
#
#     e "You've created a new Ren'Py game."
#
#     e "Once you add a story, pictures, and music, you can release it to the world!"
#
#     # This ends the game.
#
#     return

label start:
    scene girl_room with dissolve
    skylar "I really like sports, sports make me relax. but playing alone is kind of boring."
    skylar "Maybe join the local soccer team can make it more interesting!"

    "What would Skylar do next?"
    menu:
        "show up in practice directly":
            jump practice
#         "connect with the local team leader":
#             jump

label practice:

    skylar "Hey guysss! I am Skylar and I would like to join the local soccer team!"
    members "(turn their head and stare at Skylar) ………"

    "How will Skylar feel next?"
    menu:
        "Embarassed":
            jump embarassed
        "Confident":
            jump confident
label embarassed:
    scene football with dissolve
    skylar "Hmmm.. Can I join you guys?"
    members "Well, the local soccer team is already full. Besides this, we don’t want to accept a new member who doesn't have a strong physique."

    "How would Skylar  feel as a result?"
    menu:
        "feel inferior"
            jump inferior

label confident: