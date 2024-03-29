﻿# The script of the game goes in this file.

##CHARACTER DEFINITIONS##

#Main Character 
define mc = Character("[mcname]", what_prefix='"', what_suffix='"') 

#Senior Designer
define ch = Character("Charlie", what_prefix='"', what_suffix='"') 

#Project Manager 
define pm = Character("Project Manager", what_prefix='"', what_suffix='"')
define joe = Character("Joe", what_prefix='"', what_suffix='"') #Project Manager but he has a name now 

#Publisher
define pub = Character("Publisher", what_prefix='"', what_suffix='"') 
define per = Character("Percy", what_prefix='"', what_suffix='"') 

#Mid-level Animator 
define ari = Character("Ariel", what_prefix='"', what_suffix='"') 

#Extras 
define ex1 = Character("Extra #1", what_prefix='"', what_suffix='"') 
define ex2 = Character("Extra #2", what_prefix='"', what_suffix='"')
define ex3 = Character("Extra #3", what_prefix='"', what_suffix='"') 
define who = Character("???", what_prefix='"', what_suffix='"') 



##Image Character Sprites ##
#Senior Designer
image charlie neutral = "./images/Characters/neutralCharlie.png"
image charlie happy = "./images/Characters/satisfiedCharlie.png"
image charlie angry = "./images/Characters/angryCharlie1.png"

#Project Manager
image pm neutral = "./Characters/PM.png"
image pm happy = "./Characters/PM.png"
image pm angry = "./Characters/angryPM.png"


#Other Senior Designer 
image janice neutral = "./Characters/JanicetheotherSeniorDesigner.png" 

#PLACEHOLDERS FOR NOW#
#Publisher 
image pub neutral = "./images/Characters/neutralPercy.png"
image pub happy = "./images/Characters/happyPercy.png"
image pub angry = "./images/Characters/angryPercy.png"

#Mid-level Animator 
image anim neutral = "./images/Characters/neutralAriel.png"
#image anim happy = "./images/Characters/carmen h.png"
#image anim angry = "./images/Characters/carmen a.png"

#Player 
image player happy = "./images/Characters/happyplayer.png"
image player neutral = "./images/Characters/neutralplayer.png"
image player sad = "./images/Characters/sadplayer.png"

##custom x coord for sprites##
transform middle:
    xalign 0.5
#transform left:
  #  xalign 0.2
#transform right:
   # xalign 0.8

#Image Backgrounds 
#https://neeka-of-obp.itch.io/office-background-pack-lite 
#the only free office VN bgs I could find
image bg letter = "./images/letter1.jpeg" #replace this with actual letter 
image bg black = "./images/black.png"
image bg lounge = "./images/lounge.jpg"
image bg meeting room = "./images/meetingroom2.jpg"
image bg office = "./images/office2.jpg"
image bg office space= "./images/officespace.jpg"
image bg workspace = "./images/workspace.jpg" 
#https://thumbs.dreamstime.com/b/people-talking-to-each-other-silhouettes-set-black-three-groups-different-standing-51963980.jpg
image bg gaslight = "./images/gaslight placeholder.jpg"
image bg gaslight dog = "./images/gaslight placeholder1.jpg"

# Characters' Stats
# To use PEOPLE dictionary: 
#   In string: "bla bla [people[key(name/role)]]"
#   In statement: $ [people['key(name/role)']
default people = {'mc': 3, 'ch': 3, 'pm': 3}
default emotion = {1: 'very angry', 2: 'angry', 3: 'normal', 4: 'happy', 5:'very happy'}
default playerStats = {'Mental Health': 1,  'Awareness': 1, 'Courage': 1, 'Kindness': 1}
default joeStats = {'Charisma': 1, 'Awareness': 1, 'Courage': 1, 'Kindness': 1}
default subordinateStats = {'Mental Health': 1, 'Work': 1, 'LoadProductiveness': 1} 


# The game starts here.
label start:
    scene bg black
    show player neutral 
    python:
        mcname = renpy.input("My name is?", length=32)
        mcname = mcname.strip()
        if not mcname: 
            mcname = "Emm Cee"
    mc "My name is [mc]."
    scene bg lounge
    hide player

label startGame:
    menu: 
        "Chapter 1":
            jump chapter_one 
        "Chapter 2":
            jump chapter_two
       

label people_options:
    menu:
        "Talk to [ch]":
            jump junior_programmer
        "Talk to [pm]":
            jump project_manager
        "End the game":
            jump end

label junior_programmer:
    #show charlie neutral
    "Talking to [ch]"
    $ value = int(people['ch'])
    $ emotion_string = emotion[value]
    "[ch]'s value is [value] aka [emotion_string]"
    menu:
        "Make [ch] angry":
            $ people['ch'] -= 1
            "[ch] is angry, lose a value by 1"
        "Make [ch] happy":
            $ people['ch'] += 1
            "[ch] is happy, gain a value by 1"
        "Do Nothing":
            pass
     
    jump people_options

label project_manager: 
    "Talking to [pm]"
    $ value = int(people['pm'])
    $ emotion_string = emotion[value]
    "[pm]'s value is [people[pm]]"
    menu:
        "Make [pm] angry": 
            $ people['pm'] -= 1
            "[pm] is angry, lose a value by 1"
        "Make [pm] happy":
            $ people['pm'] += 1
            "[pm] is happy, gain a value by 1"
        "Do Nothing":
            pass
    jump people_options





label end:
    # This ends the game.
    scene bg gaslight with fade 
    "Gaslighting occurs more often than we think..."
    "<Gaslighting description>"
    "<Gaslighting numerical cases>"
    "<Gaslighting testimonials>"
    "The End."
    #jump people_options
    return
