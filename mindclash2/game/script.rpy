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
    play music "cheerful.mp3" fadein 0.4 fadeout 0.4 volume 0.3
    show skylar grinning at truecenter
    skylar "I really like sports, sports make me relax. but playing alone is kind of boring."
    hide skylar grinning at truecenter
    show skylar thinking at truecenter
    skylar "Maybe join the local soccer team can make it more interesting!"

    "What would Skylar do next?"
    menu:
        "show up in practice directly":
            jump practice
        "connect with the local team leader":
            jump connect

label practice:
    scene football with dissolve
    play music "cheerful.mp3" if_changed
    show skylar excited at truecenter
    skylar "Hey guysss! I am Skylar and I would like to join the local soccer team!"
    hide skylar
    members "(turn their head and stare at Skylar) ………"

    "How will Skylar feel next?"
    menu:
        "Embarassed":
            jump embarassed
        "Confident":
            jump confident
label embarassed:
    scene football with dissolve
    play music "tense.mp3" fadein 0.4 fadeout 0.4 volume 0.3
    show skylar embarassed at truecenter
    skylar "Hmmm.. Can I join you guys?"
    hide skylar
    members "Well, the local soccer team is already full. Besides this, we don’t want to accept a new member who doesn't have a strong physique."

    "How would Skylar  feel as a result?"
    menu:
        "feel inferior":
            jump inferiorE
        "furious":
            jump furiousE

label confident:
    scene football with dissolve
    play music "cheerful.mp3" if_changed
    show skylar confident at truecenter
    skylar "I'm really skilled at soccer!"
    hide skylar
    show leader grinning at truecenter
    leader "That's great to hear! We actually need one more player. Are you up for showing us what you've got?"
    hide leader
    show skylar confident
    skylar "Absolutely! I'm ready to give it my all and show you my skills."
    hide skylar
    "What would Skylar do next?"
    menu:
        "Feel elated for being accepted":
            jump acceptedE
        "Experience nervousness about showcasing his abilities":
            jump nervousnessE

label acceptedE:
    scene football with dissolve
    play music "cheerful.mp3" if_changed
    show skylar excited at truecenter
    skylar "Thank you all for accepting me! I'm so thrilled to be a part of this team."
    hide skylar
    show leader smiling at truecenter
    leader "Welcome aboard, Skylar! We're glad to have you. Get ready to show us your skills in the upcoming practice sessions."
    return
label nervousnessE:
    scene football with dissolve
    play music "nervous.mp3" fadein 0.4 fadeout 0.4 volume 0.3
    show skylar nervously at truecenter
    skylar "I hope I can live up to everyone's expectations. I'm feeling a bit anxious about showing my abilities."
    hide skylar
    show leader supportive at truecenter
    leader "Don't worry, Skylar. Just be yourself and play the way you know. We're here to support and help you improve. Give it your best shot."
    return

label inferiorE:
    scene football with dissolve
    play music "sad.mp3" fadein 0.4 fadeout 0.4 volume 0.3
    show skylar tearing at truecenter
    skylar "Well...alright..."
    hide skylar
    hide football
    scene girl_room with dissolve
    show skylar tearing at truecenter
    skylar "I never thought they would say I'm not strong enough. Their words hurt..."
    hide skylar
    show friend sad-smile at truecenter
    friend "Hey, don't let their negativity get to you. You have an amazing talent for soccer, Skylar. It's their loss for not recognizing it."
    hide friend
    show skylar tearing at truecenter
    skylar "Do you really think I'm a good player?"
    hide skylar
    show friend smile at truecenter
    friend "Absolutely! You're the best soccer player I've ever seen. Come on, let's go out there and show them what you're made of."
    hide friend
    show skylar tear-grinning at truecenter
    skylar "Thank you! Your words mean a lot to me. Let's go play soccer and prove them wrong!"
    return

label furiousE:
    scene football with dissolve
    play music "sad2.mp3" fadein 0.4 fadeout 0.4 volume 0.3
    show skylar angry at truecenter
    skylar "What did you just say?"
    hide skylar
    show leader contemptuously at truecenter
    leader "I said you're not strong enough to join our team. This isn't the right place for you. Did I make myself clear?"
    hide leader
    show skylar angry-blush at truecenter
    skylar "You'll regret saying that. I'll show you just how strong I am."
    hide skylar
    hide football
    scene street with dissolve
    show skylar angry at truecenter
    skylar "(angry)"
    hide skylar
    show leader contemptuously at truecenter
    leader "Oh, here comes the hot-headed player."
    hide leader
    show skylar angry at truecenter
    skylar "You think you can belittle me? Well, I'm not backing down. Let's settle this right here, right now."
    hide skylar
    show leader surprised at truecenter
    leader "Are you challenging me to a fight?"
    hide leader
    show skylar determined at truecenter
    skylar "Yes, I am. I'll prove to you and everyone else that I'm stronger than you think."
    hide skylar
    "The two engage in a physical confrontation, showcasing Skylar's resilience and determination. Eventually, Skylar's display of strength and skill impresses not only the team leader but also the onlookers, gaining the respect and recognition Skylar deserves."
    return




label connect:
    scene cafe with dissolve
    play music "modern.mp3" fadein 0.4 fadeout 0.4 volume 0.3
    show skylar excited at truecenter
    skylar "Hi there! My name is Skylar, and I'm really passionate about soccer. Can I join your local team?"
    hide skylar
    show leader smiling at truecenter
    leader "Of course! But before you join the team, there's something I need you to prepare for me."
    hide leader
    show skylar confused at truecenter
    skylar "What do you mean? What kind of things?"
    hide skylar
    show leader smiling
    leader "Well, I'm looking for some financial support or other personal advantages."

    "What will Skylar do next?"
    menu:
        "Surprised, but still consider paying the money":
            jump surprisedE
        "Angry, and decide to report the team leader for bribery":
            jump angryE

label surprisedE:
    scene cafe with dissolve
    play music "sad3.mp3" fadein 0.4 fadeout 0.4 volume 0.3
    show skylar surprised at truecenter
    skylar "I didn't expect this condition, but I'm really passionate about joining the team. I'll consider paying the money, although it feels unusual."
    hide skylar
    show leader satisfied at truecenter
    leader "Great decision, Skylar. Your commitment is appreciated. Welcome to the team!"
    return
label angryE:
    scene cafe with dissolve
    play music "sad3.mp3" fadein 0.4 fadeout 0.4 volume 0.3
    show skylar determined at truecenter
    skylar "I won't tolerate this kind of behavior. It goes against fair play and the integrity of the game. I'm going to report you to the appropriate authorities."
    hide skylar
    show leader nervously at truecenter
    leader "You can't prove anything! Don't try to ruin my reputation. You're not welcome on this team anymore."
    return
