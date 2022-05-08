# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen", what_prefix='"', what_suffix='"')
define mc = Character("[mcname]", what_prefix='"', what_suffix='"') #main Character 
define ch = Character("Charlie", what_prefix='"', what_suffix='"')
define pm = Character("Project Manager", what_prefix='"', what_suffix='"')

#PLACEHOLDERS FOR NOW#

#Image Character Sprites 
#replace him with an animal
#Senior Designer
image charlie neutral = "./images/Characters/win d.png"
image charlie happy = "./images/Characters/win h.png"
image charlie shock = "./images/Characters/win s.png"
image charlie angry = "./images/Characters/win a.png"

#Project Manager
image pm neutral = "./Characters/bp rock d.png"
image pm angry = "./Characters/bp rock a.png"
image pm happy = "./Characters/bp rock h.png"

#Image Backgrounds 
#https://neeka-of-obp.itch.io/office-background-pack-lite 
#the only free office VN bgs I could find
image bg letter = "./images/letter.jpg" #replace this with actual letter 
image bg black = "./images/black.png"
image bg lounge = "./images/lounge.jpg"
image bg meeting room = "./images/meetingroom2.jpg"
image bg office = "./images/office2.jpg"
image bg office space= "./images/officespace.jpg"
image bg workspace = "./images/workspace.jpg" 
#https://thumbs.dreamstime.com/b/people-talking-to-each-other-silhouettes-set-black-three-groups-different-standing-51963980.jpg
image bg gaslight = "./images/gaslight placeholder.jpg"

# Characters' Stats
# To use PEOPLE dictionary: 
#   In string: "bla bla [people[key(name/role)]]"
#   In statement: $ [people['key(name/role)']
default people = {'mc': 3, 'ch': 3, 'pm': 3}
default emotion = {1: 'very angry', 2: 'angry', 3: 'normal', 4: 'happy', 5:'very happy'}


# The game starts here.
label start:
    scene bg black
    python:
        mcname = renpy.input("My name is?", length=32)
        mcname = mcname.strip()
        if not mcname: 
            mcname = "Rob Boss"
    mc "My name is [mc]."
    scene bg room
       

label people_options:
    menu:
        "Talk to [ch]":
            jump junior_programmer
        "Talk to [pm]":
            jump project_manager
        "Chapter 1":
            jump chapter_one 
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
            #show charlie angry 
            $ people['ch'] -= 1
            "[ch] is angry, lose a value by 1"
        "Make [ch] happy":
            #show charlie happy 
            $ people['ch'] += 1
            "[ch] is happy, gain a value by 1"
        "Do Nothing":
            pass
    #hide charlie 
    jump people_options

label project_manager:
    #show pm neutral 
    "Talking to [pm]"
    $ value = int(people['pm'])
    $ emotion_string = emotion[value]
    "[pm]'s value is [people[pm]]"
    menu:
        "Make [pm] angry":
            #show pm angry 
            $ people['pm'] -= 1
            "[pm] is angry, lose a value by 1"
        "Make [pm] happy":
            #show pm happy 
            $ people['pm'] += 1
            "[pm] is happy, gain a value by 1"
        "Do Nothing":
            pass
    #hide pm 
    jump people_options





label end:
    # This ends the game.
    scene bg gaslight with fade 
    "Gaslighting occurs more often than we think..."
    "<Gaslighting description>"
    "<Gaslighting numerical cases>"
    "<Gaslighting testimonials>"
    "The End."

    return
