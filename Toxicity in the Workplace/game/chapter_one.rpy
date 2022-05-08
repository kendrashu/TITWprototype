# Implementing the dialouge from here 
#https://docs.google.com/spreadsheets/d/1U0G65mqXHQhQ_7g8A7ZLfTBbkok0qyP7RsILxaPznkk/edit#gid=0


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

    "The taciturn person, Charlie becomes my higher-up."
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
            menu:
                "Go to Charlie": 
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
                    jump gaslit
                   

        "I pretended nothing happened.": #"I pretended not to hear and hurried out of there.": 
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
                    ch "You are so pathetic, tears are worthless."
                    #Propreties:M2-1=M1 B4-1=B3 E2 -1=E1
                    "I began to doubt myself. I must have done something wrong."
                    hide charlie angry 
                    jump gaslit

label gaslit: 
    show charlie neutral
    "I can still remember Charlie patting me on the shoulder and saying," 
    show charlie happy 
    ch "Well done, you're going to do great things."
    hide charlie happy
    menu: 
        "I must have done something wrong.":
            menu: 
                "Office":
                    scene bg office with fade 
                    show charlie neutral 
                    "I began to show Charlie my weakness."
                    "I began to watch his face carefully."
                    "I get to the office earlier and leave later and later."
                    "I double-check every email again and again, even for notifications that don't matter."
                    "I change my clothes every day."
                    "However, I still make a new mistake."
                    scene bg office space with fade 
                    show charlie shock 
                    ch "You look unhappy, you should smile."
                    scene bg lounge with fade 
                    show charlie neutral 
                    ch "This colour is disgusting, why did you choose it?"
                    scene bg meeting room with fade 
                    show charlie angry
                    ch "Can you speak quickly? I have other things to do."
                    scene bg office with fade 
                    show charlie neutral
                    ch "The documentation is good, but there are some details that need to be improved. "
                    #Propreties: M1 -1=0  B3  E 0
                    "I even feel grateful. Charlie still encouraged me. I still kept this job."
                    hide charlie neutral 
                    scene bg black with fade 
                    "I can't sleep at night. I'm afraid tomorrow will come. I'm afraid I'll make new mistake."
                    "My hair is starting to fall out, handfuls of it."
                    #Propreties: M1 -1=0  B3-3=0  E 0 
                    jump worst_end

        "That's not right. That's not how it's suppose to be.":
            "I must get out of this disgusting situation."
            jump get_proof
    
        
label you_suck_response:
    menu: 
        "Sorry about the unpleasant things. I'll do it in my way.":
            "I decided to fight back."
            #Propreties:M3 +1=M4 B5 E 1
            jump get_proof


        "Great, I'm done.": 
            "I quit the job immediately."
            #Propreties: M3 +1=M4 B5 E1 +4=E5
            jump resign 

label get_proof: #Properties Checking: if M<3, execute A, prompt Warning
    "I have to prove what was said."
    "<Warning> Different options require different psychological pressures."
    menu:
        "Chat history": 
            #mental health -1
            jump evidence 

        "Mail Records":
            #mental health -1
            jump evidence 

        "Public CCTV":
            #mental health -3
            jump evidence2  

label evidence:
    menu:
        "Project Manager Office":
            scene bg office with fade 
            show pm neutral 
            "I sent all the evidence I collected to the project manager."
            "After a moment's silence."
            show pm happy 
            pm "Nice work you did."
            hide pm 
            #Properties Checking: if M<3 to i102 
            menu:
                "Good Stats":
                    jump good_end 

                "Bad Stats":
                    jump dismiss 
label evidence2:
    menu:
        "Project Manager Office":
            scene bg office with fade 
            show pm neutral 
            "I sent all the evidence I collected to the project manager."
            "After a moment's silence."
            pm "Nice work you did."
            show pm shock 
            pm "I apologize for being so presumptuous earlier."
            scene bg black with fade
            "Charlie was fired."
            "I heard after this was over that he had done the same thing before." 
            "In 6 months, I have never felt so relaxed."
            "Ending 3. Success"
            jump end 

label resign: 
    scene bg black with fade
    "Ending 2. Resign"
    jump end

label dismiss:
    menu:
        "Timeskip to Project Manager Office":
            scene bg office with fade 
            show pm neutral 
            pm "Sorry, we won't be hiring you anymore."
            hide pm 
            #Properties Checking: if E<3 to J103
            menu:
                "Good Stats":
                    scene bg black with fade 
                    "At least, I'm free now."
                    "Ending 2. Dismissed"
                    jump end 

                "Bad Stats":
                    jump worst_end


label good_end: 
    scene bg black with fade 
    "I was changed to another group."
    "In 6 months, I have never felt so relaxed."
    "Ending 3. Success"
    jump end 


label worst_end:
    "The world hates me. "
    "I'm a terrible person."
    "Ending 1. Lose it all." #changed the name 
    jump end 
