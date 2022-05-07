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
        "Talk to Junior Programmer":
            jump junior_programmer
        "Talk to Lead Designer":
            jump lead_designer
        "Chapter 1":
            jump chapter_one 
        "End the game":
            jump end

label junior_programmer:
    "Talking to Junior Programmer"
    jump people_options

label lead_designer:
    "Talking to Lead Designer"
    jump people_options

label chapter_one:
    scene bg letter 

    "Dear [mc],"
    "Congratulations!"
    "You are employed by our company as the first place in the interview!"
    "Welcome to join our {b}Zoopany{/b}!"

    scene bg office space with fade 
    "Choose your Senior Designer."
    menu: 
        "A serious looking one":
            "However, the other new employee was assigned to this Designer."
            jump senior_designer
        "A taciturn but smiling one":
            jump senior_designer 

label senior_designer:

    "The taciturn person, Charlie become my higher-up."
    "The first day at work, I find there is already a cup of coffee on my table and Charlie looks up at me and raise the coffee cup to me."
    show charlie happy 
    ch "Welcome."
    hide charlie happy

    #INSERT STATS 
    #Propreties: M3+1=M4 B3+1=B4 E5
    menu:
        "Go to office":
            jump office1

label office1:
    scene bg office with fade 
    show charlie happy
    "The day's work is over, and I get up to go home. The work environment let me feel comfortable, and everyone is kind there."
    
    "As for Charlie, although Charlie looks indifferent, is considerate of others."
    mc "This is going to be the perfect job."
    "I told myself." 
    hide charlie happy 

    #Propreties: M4+1=M5 B4 E5
    menu: 
        "Go to meeting room":
            jump meetingroom1 


label meetingroom1:
    scene bg meeting room with fade 
    "There is a seminar today, and I will responsible for taking notes of all the suggestions made at the meeting."
    "Everything went well, except for a few disagreements over a design of a particular feature, but it worked out well."
    
    show charlie neutral 
    "After the meeting, Charlie wants to review my minutes of the seminar, then a strange thing happened."
    "Charlie edited some contents, while saying something with a hint of anger."
    show charlie angry 
    ch "This is really unprofessional." 
    "Charlie said and pushed the computer back to me without any explanation."

    mc "I feel vaguely weird,"
    hide charlie angry

    #Propreties: M5-1=M4 B5 E5 -1=E4
    menu:
        "and I report this thing to the project manager.":
        
            jump everything_changed 

        "But I act like nothing happened and submitted the minutes.":
            menu:
                "Timeskip to office":
                    scene bg office with fade 
                    "Everything goes well and this project is given approbation."
                    #Propreties: M5 B4 +1=5 E5
                    "Until one day, the project is delivered to the investor."
                    "The representative stated that the expected feature in the delivered project was not implemented."
                    "I immediately realize, the missing feature is which Charlie edited at the beginning of the project, after that seminar."
                    "I suddenly realized what Charlie said in that day. The original design is piece of sh*t."
                    show pm angry
                    "At the end of the email, the project manager asks to talk with me."
                    "I tell the truth about what happened on that day."
                    "The Project Manager looks at me with disbelief and disapproval in his eyes."
                    pm "Charlie told me everything, you should be honest, [mcname]."
                    
                    "I stood there, my hands and feet cold, unable to say a word."
                    hide pm angry 
                    #Propreties: M5-1=M4 B5 E5 -1=E4 
                    jump everything_changed 


label everything_changed: 
    scene bg black with fade
    "Then everything changed."
    scene bg office 
    show charlie neutral 
    "Charlie seems become critical of my work."
    "Scores below five started popping up frequently on my performance reviews."
    "Charlie sometimes ignores what I said at everyday meeting." 
    #I know, Charlie knows what I did.(for A. Reporting) 
    "I don't know what happened."
    #Propreties: M4-1=M3 B5 E4-1=E3
    "Everything tells me something's wrong."
    "But I'm not sure what's going to happen."
    "Because Charlie still treats me like he used to and gives me some great advice about my work."
    "But I kind of don't want to go to my company. " 
    hide charlie angry 

    menu: 
        "I think I was treated badly.":
            #A: Propreties:M3 B5 E3 -1=E2 
            jump feel_terrible 

        "Maybe I'm just being overly sensitive":
            menu: 
                "Go to Lounge":
                    scene bg lounge with fade 
                    "\"[mcname] slacks off at work. They are so stupid and always makes mistakes.\""
                    "I recognized that is Charlie's voice."
                    #Propreties:M3-1=M2 B5-1=B4 E3 -1=E2
                    jump feel_terrible 

label feel_terrible:
    "I feel terrible." 
    menu: 
        "I decided to talk to Charlie.":
            show charlie angry 
            ch "You are too young. You don't know what's behind it, all things are about business."
            ch "You screwed everything up, [mcname]."
            hide charlie angry 

            menu:
                "But it is not my mistake.":

                    show charlie neutral
                    "Charlie looks me straight into my eyes."
                    show charlie angry 
                    ch "You suck."
                    ch "I wondered why the HR team gave this job to you."
                    hide charlie angry
                    #Propreties: M3 B5 E2 -1=E1
                    jump you_suck_response 

                "...could you please give me one more chance?":
                    show charlie happy
                    "Charlie smiled."
                    #Propreties: M3 -1=2 B5 E2+1=E3
                    ch "Of course, you deserve it."
                    "Charlie is so kind I think."
                    "I began to doubt myself. I must have done something wrong."
                    "I can still remember Charlie patting me on the shoulder and saying," 
                    ch "Well done, you're going to do great things."
                    hide charlie happy
                    "insert other options here "#COEM BACK TO THIS
                    jump end


        "I pretended not to hear and hurried out of there.": #"I pretended there is nothing happened.":
            menu: 
                "Workspace":
                    scene bg workspace with fade 
                    "Worse things start to happen."
                    "My colleagues began to distance themselves from me."
                    "Charlie even accuses me of not dressing well enough today."
                    "I broke down and burst into tears."
                    "There is only apathy in the workplace."
                    show charlie neutral 
                    "Charlie looks at me."
                    show charlie angry 
                    ch "You are so pathetic, tears are worthless"
                    #Propreties:M2-1=M1 B4-1=B3 E2 -1=E1
                    "I began to doubt myself. I must have done something wrong."
                    hide charlie angry 
                    "insert other options here "#COEM BACK TO THIS
                    jump end


    
        
label you_suck_response:
     menu: 
        "Sorry about the unpleasant things. I'll do it in my way.":
            "I decided to fight back."
            #Propreties:M3 +1=M4 B5 E 1
            "insert other options here "#COEM BACK TO THIS
            jump end


        "Great, I'm done.": 
            "I quit the job immediately."
            #Propreties: M3 +1=M4 B5 E1 +4=E5
            jump resign 



label resign: 
    scene bg black with fade
    "Ending 2. Resign"
    jump end


label end:
    # This ends the game.
    "Ending the game"
    return
