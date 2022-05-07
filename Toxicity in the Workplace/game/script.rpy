# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # --------------------------------

    # Create stats for characters
    # To use PEOPLE dictionary: 
    #   In string: "bla bla [people[key(name/role)]]"
    #   In statement: $ [people['key(name/role)']
    $ people = {'junior_programmer': 3, 'lead_designer': 3}
    $ emotion = {1: 'very angry', 2: 'angry', 3: 'normal', 4: 'happy', 5:'very happy'}
    

label people_options:
    menu:
        "Talk to Junior Programmer":
            jump junior_programmer
        "Talk to Lead Designer":
            jump lead_designer
        "End the game":
            jump end

label junior_programmer:
    "Talking to Junior Programmer"
    $ value = int(people['junior_programmer'])
    $ emotion_string = emotion[value]
    "His value is [value] aka [emotion_string]"
    menu:
        "Make him angry":
            $ people['junior_programmer'] -= 1
            "He is angry, lose a value by 1"
        "Make him happy":
            $ people['junior_programmer'] += 1
            "He is happy, gain a value by 1"
        "Do Nothing":
            pass
    jump people_options

label lead_designer:
    "Talking to Lead Designer"
    "Her value is [people[lead_designer]]"
    menu:
        "Make her angry":
            $ people['lead_designer'] -= 1
            "She is angry, lose a value by 1"
        "Make her happy":
            $ people['lead_designer'] += 1
            "She is happy, gain a value by 1"
        "Do Nothing":
            pass
    jump people_options


label end:
    # This ends the game.
    "Ending the game"
    return
