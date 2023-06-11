# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    import json, uuid
    user_id = str(uuid.uuid4())
    
    def save_input(text:str, scenario:str, choice:str):
        with open(config.save_directory+"user_input.json", 'a+') as f:
            data = {"Scenario":scenario, "text":text, "Choice":choice}
            json.dump(data,f)


define text = Character("[text_input]")
define participant = Character("[user_id]")
define developer = Character("...")
define kendall = Character("Kendall", image="kendall")
define jan = Character("Jan", image="jan")

# The game starts here.

label start:
    scene bg city with dissolve
    
    # The developer's beginning dialogue
    developer "Welcome, my friend."
    developer "You are invited, because we want you to make choices."
    developer "We want to know why you make these choices."
    developer "Your thought is crucial for us."
    developer "Now let's start it."

    menu:
        "Continue":
            jump cafe

label cafe:
    
    developer "Now the story begins. You are going to make choices for Kendall and Jan."
    $ renpy.pause() #Pause to create a gap
    
    scene bg cafe with dissolve
    
    '''$ text_input = renpy.input("Testing:", copypaste = False) 
    $ save_input(text_input, "Scenario_1", "Random Choice")'''
   
    #show jan beaming at truecenter
    
    "Kendall and Jan are sitting in a cozy café, enjoying a cup of coffee together."

    kendall "Jan, these past few months have been incredible. I can't believe how much we've grown together. I think our relationship is getting really serious."
    jan "Kendall, I feel the same way. I've never connected with someone on such a deep level before. It's like we're meant to be."

    "How would Kendall feel about this?"
    menu:
        "Feeling In Love":
            jump feeling_in_love

        "Angry":
            jump angry

label feeling_in_love:
    kendall "(blushing) Yes, Jan, I'm completely in love with you. You make me feel like the luckiest person in the world. I want to cherish every moment we spend together."
    jan "(smiling warmly) Kendall, you have my heart too. Our love is something truly special, and I can't wait to see where it takes us."
    
    "(Kendall stands up to do the dishes while Jan goes into her room. Some time passes)"

    scene bg kitchen with move #(Scene: Kendall is in the kitchen, pondering his next move.)

    kendall " (thinking) I wonder if Jan has found a date for the upcoming dance. I should go and talk to her about it."

    "What will Kendall want to do next?"
    menu:
        "Talk to Jan":
            jump jan_room
        "Clean Her Home":
            jump clean_her_home

label angry:
    kendall "(Kenadll sits down, looking frustrated)"
    kendall "Jan, we need to talk."
    jan "(concerned) What's wrong, Kendall? You seem upset."
    kendall "(angry) I can't help but feel angry about our relationship. It's getting serious, and I thought we were on the same page, but it feels like you're holding back."
    jan "(surprised) Kendall, I'm sorry if it seems that way. I care about you deeply, but I might have some reservations."
    kendall "(frustrated) Reservations? After all this time together? What's holding you back?"
    jan "(taking a deep breath) Kendall, it's not about you. I've been hurt in the past, and it's made it difficult for me to fully open up and trust someone again."
    "(Scene: Jan faints in Kendall's arms, causing concern and worry.)"

    $ renpy.pause(1.0)
    "Question: What happen to Jen?"

    menu:
        "Jan is getting better":
            jump ending_5
        "Jan appreciates what Kendall does":
            jump ending_6 

label jan_room:

    scene janroom with move

    "(Kendall enters Jan's room, noticing she is sleeping on her stomach.)"
    kendall "(softly) Jan looks so peaceful sleeping like that. I want to make sure she stays warm."
    "(Kendall tries to pull Jan's covers over her body)"

    $ renpy.pause(1.0)
    "How would Jan feel about Kendall's action?"
    menu:
        "Being Ignored":
            jump ending_1
        "Being Loved":
            jump ending_2

label clean_her_home:
    scene bg room with dissolve
    "(Kendall decides to clean Jan's home while she is busy.)"

    kendall "(thinking to himself) Jan has been occupied lately, and I know she has a lot on her plate. I'll take this opportunity to clean her home and help lighten her load."
    "Kendall starts cleaning, tidying up the living room and organizing the kitchen."

    kendall "(focused on cleaning, muttering to himself) I want Jan to come back to a clean and cozy home. She deserves a relaxing space after her busy day."
    "(Kendall looks at the overflowing shelves and the small living room.)"
    kendall "I have to find a bigger home for us so we can live comfortably."

    "(Kendall finds a big villa that is suitable for both him and Jen)"
    "How will Kendall feel?"
    $ renpy.pause(1.0)
    menu:
        "Being Loved":
            jump ending_3
        "Feeling Detached":
            jump ending_4



label ending_1: #Ending: Clean Her Home
    #(Scene: Kendall leaves the room without disturbing Jan's sleep. However, unbeknownst to Kendall, Jan wakes up briefly and notices his presence.)
    "Kendall leaves the room without disturbing Jan's sleep. However, unbeknownst to Kendall, Jan wakes up briefly and notices his presence."

    scene bg breakfast table with dissolve
    show jan hesitate at truecenter
    jan "Kendall, can we talk about something?"
    hide jan
    show kendall concerned at truecenter
    kendall "Of course, Jan. What's on your mind?"
    hide kendall
    show jan hesitate at truecenter
    jan "Last night, when I woke up for a moment, I noticed you were in my room. I appreciate your intention to keep me warm, but it made me feel a bit ignored as if you didn't want to disturb me."
    hide jan
    show kendall frustrated at truecenter
    kendall "Jan, I'm so sorry if I gave you that impression. I truly didn't want to disrupt your sleep, thinking it would be better to let you rest peacefully. I never meant for you to feel ignored."
    hide kendall
    show jan sad at truecenter
    jan "Kendall, it's not just about that one incident. Lately, I've been feeling like our connection has dissolved. We seem to have different priorities and our communication has suffered. I think it might be best if we go our separate ways."
    hide jan
    show kendall concerned at truecenter
    kendall "Jan, I didn't realize you felt this way. I'm devastated to hear that you want to end our relationship, but I respect your decision."
    hide kendall
    show jan tear eyed at truecenter
    jan "Kendall, it's not an easy decision for me either. We had some beautiful moments together, but it feels like we've grown apart. It's time for both of us to find our own happiness."
    return 

label ending_2:
    #(Scene: Kendall's act of pulling the covers over Jan reflects his care and love for her. 
    # Their relationship deepens as they continue to nurture their connection.)
    scene bg breakfast table with dissolve
    "(Kendall's act of pulling the covers over Jan reflects his care and love for her. Their relationship deepens as they continue to nurture their connection.)"

    #(Scene: Kendall and Jan spend quality time together, strengthening their bond.)
    scene bg warm home with dissolve
    "(Kendall and Jan spend quality time together, strengthening their bond.)"
    show kendall happy at truecenter
    kendall "Jan, I wanted to make sure you felt warm and comfortable. Your well-being means everything to me."
    hide kendall
    show jan smile at truecenter
    jan "Kendall, your thoughtfulness never fails to touch my heart. It's moments like these that remind me how lucky I am to have you in my life."
    hide jan smile
    show kendall affective smile at truecenter
    kendall "Jan, being with you feels like home. You bring so much joy and warmth into my life. I can't imagine my days without you by my side."
    hide kendall
    show jan blushing at truecenter
    jan "Kendall, you make me feel cherished and loved. The way you care for me and pay attention to the little details fills me with happiness. I'm grateful for our deep connection."

    #Consequence: (Scene: Kendall and Jan's relationship continues to flourish, 
    #filled with love, understanding, and mutual respect. 
    #They create a harmonious life together, supporting each other's dreams and aspirations. 
    #As time passes, their commitment deepens, 
    #and they decide to take their relationship to the next level.)


    #(Scene: Kendall and Jan celebrate their engagement,
    #surrounded by love and the promise of a lifelong partnership. 
    #They embark on a beautiful journey together, building a life filled with warmth, trust, 
    #and unwavering love.)
    scene bg wedding with dissolve
    "Kendall and Jan celebrate their engagement, surrounded by love and the promise of a lifelong partnership.
    They embark on a beautiful journey together, building a life filled with warmth, trust, 
    #and unwavering love."

    return
    


label ending_3:
    #(Scene: Kendall and Jan move into their new home.)
    scene bg villa inside with dissolve
    
    "(Kendall and Jan move into their new home.)"
    $ renpy.pause()
    show kendall excited at left
    kendall "(looking around with excitement) Jan, we did it! This place is perfect for us. I'm so glad I put our way of navigating into practice."
    show jan beaming at right
    jan "(beaming) Kendall, I'm amazed at how you found this gem of a home. You truly have a knack for creating a beautiful and comfortable space."
    show kendall accomplished at left
    kendall "(feeling loved and accomplished) Jan, your words mean the world to me. I wanted us to have a place we can truly call home, and seeing your happiness makes it all worthwhile."
    #Consequence: 
    #(Scene: Kendall and Jan settle into their new home, surrounded by love, warmth, 
    #and the fruits of their shared navigation. 
    #The space becomes a sanctuary where their love flourishes, 
    #creating lasting memories and a solid foundation for their future together. 
    #Kendall feels a deep sense of fulfillment, 
    #knowing they were able to provide a great place for their shared happiness to thrive.)






label ending_4:
    #(Scene: Kendall and Jan struggle to find a suitable place to live.)
    scene bg city street with dissolve
    show kendall frustrated at left
    kendall "(frustrated and detached) Jan, I thought I could find us a great home, but it's not working out as I hoped. I feel detached from the whole process."
    show jan supportive at right
    jan "(Supportive) Kendall, it's okay. Finding a home can be challenging, but we're in this together. Let's not get disheartened."
    show kendall concerned at left
    kenadll " (reflective) Jan, I appreciate your understanding. I've realized that my navigation skills alone may not be enough. We should approach this as a team and seek professional guidance to find the perfect place."

    #(Scene: Kendall and Jan regroup, 
    #seeking assistance from a real estate agent. 
    #Through their joint effort and the support they provide each other, 
    #they eventually find a suitable home. 
    #Kendall learns the importance of relying on others and working together, 
    #leading to a stronger bond and a sense of shared responsibility in their journey.)





label ending_5:
    scene bg house3 with dissolve
    kendall "(panicked) Jan! Jan, wake up! Can you hear me?"
    $ renpy.pause(2.0)
    jan "(slowly regaining consciousness) What... happened?"
    kendall "(relieved) You fainted, Jan. I was so worried. Are you feeling better now?"
    $ renpy.pause(0.5)
    jan "(slowly regaining consciousness) What... happened?"
    kendall " (relieved) You fainted, Jan. I was so worried. Are you feeling better now?"
    $ renpy.pause(0.3)
    jan "(weakly) I think so. I'm sorry for causing you concern."
    kendall "(softly) Jan, I care deeply about you. Seeing you in distress worried me, and I wanted to make sure you were okay."
    jan "(smiling weakly) It means a lot to me, Kendall. Your kindness and support remind me that I have someone who genuinely cares about me."
    kendall "(gently) You deserve to be cared for, Jan. I want to be the person who supports you and makes you feel loved."
    jan " (reflective) I've been guarded because of my past, but your actions and words show me that I can trust you. I want us to continue building our relationship."
    kendall "(grateful) Jan, I'm here for you, and I want us to grow together. Let's work through any challenges that come our way and create a future filled with love and happiness."

    #Consequence: 
    #(Scene: Jan's appreciation for Kendall's kindness deepens their connection, 
    #and they continue to nurture their relationship with care and understanding. 
    #The experience strengthens their bond, 
    #allowing them to overcome Jan's past reservations and build a loving and trusting partnership.)
    



label ending_6:
    #(Scene: Jan's gratitude and appreciation for Kendall's actions deepen their connection.)
    scene bg house2 with dissolve
    jan "(softly) Kendall, I want you to know how much I appreciate what you did for me. Your care and kindness mean the world to me."
    kendall "(smiling) Jan, seeing you happy and feeling appreciated is all I could ask for. I'm here for you, through thick and thin."
    jan "(reflective) I never expected to find someone as caring and understanding as you, Kendall. You've shown me what it means to be loved and supported."
    kendall "(tenderly) Jan, you deserve nothing less than love and support. I want to be the one who provides that for you, now and in the future."
    jan "(grateful) With you by my side, I feel like I can overcome any challenges that come our way. Together, we can create a beautiful and fulfilling relationship."

    #Consequence: 
    #(Scene: Jan's gratitude deepens their bond, 
    #and they continue to nurture their relationship with care, 
    #understanding, and unconditional love. 
    #Their shared appreciation and commitment to each other create a strong foundation, 
    #allowing their love to grow and flourish. 
    #Kendall's dedication to Jan's happiness fosters a sense of security and happiness, 
    #making their relationship a source of joy and fulfillment for both of them.)

