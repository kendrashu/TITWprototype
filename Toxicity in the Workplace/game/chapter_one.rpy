# Implementing the dialouge from here 
#https://docs.google.com/spreadsheets/d/1U0G65mqXHQhQ_7g8A7ZLfTBbkok0qyP7RsILxaPznkk/edit#gid=0


label chapter_one:

    scene bg letter 

    "Dear [mc],"
    "Congratulations!"
    "We have decided that you'll be a great fit for our team and are excited to offer you a job at our company."
    "Welcome to {b}Zoopany{/b}!" 


    scene bg black with fade  
    show player happy with fade
    "You are a newly-hired executive designer."
    "Your job is to assist your senior designer and to implement all design-related features."
    hide player
    scene bg office space with fade 
    show janice neutral at left
    show charlie happy at right
    "As you arrive at the office, you see two employees welcoming the new hires."
    "I hope my new boss is..."


    menu:
        "the one who looks like a tough cookie":
        #"The serious looking one":
            show janice neutral
            hide charlie
            show janice neutral at middle with move 
            "However, the other new hire is already to this Designer."
            hide janice 
            jump senior_designer

        "the one who looks like an oyster but with a kind smile":
            hide janice
            show charlie happy at middle with move 
        #"The uptight but smiling one":
            jump senior_designer 

label senior_designer:
    #scene bg office space with fade 
    show charlie happy
    "The smiling one, Charlie becames my higher-up."
    hide charlie 
    #INSERT STATS 
    #Propreties: M3+1=M4 B3+1=B4 E5
    menu:
        "Go to Team Office":           
            scene bg workspace with fade 
            #show charlie neutral 
            "On the first day at work, I find there is already a cup of coffee on my desk."
            "Charlie looks up at me and raises his own cup as a toast."
            show charlie happy
            ch "Welcome."
            hide charlie happy
            jump office1


label office1:
    #scene bg office with fade 
    scene bg black with fade
    "I spend the day working."
    scene bg workspace with fade 
    "The day's work is over, and I get up to go home."
    "The work environment is comfortable and most of my coworkers are kind."
    show charlie happy
    "Although Charlie looks indifferent, he is considerate towards others."
    show player happy 
    mc "This is going to be the perfect job."
    #"I told myself." 
    hide charlie happy 
    hide player 

    #Propreties: M4+1=M5 B4 E5
    menu: 
        "End Day":
            jump meetingroom1 


label meetingroom1:
    scene bg black with fade 
    "1 month later..."
    menu:
        "Go to Meeting Room": 
            #scene bg office space with fade 
            scene bg meeting room with fade
            "There is a seminar today and I am responsible for taking notes of all the suggestions made during the meeting."
            "Other than a few disagreements over the design of a particular feature, everything worked out well."
            
            show charlie neutral 
            "After the meeting, Charlie wants to review my minutes of the seminar, then something strange happened."

            #scene bg meeting room with fade 
            "Charlie edited a portion of the notes in a huff."
            show charlie angry 
            ch "This is really unprofessional." 
            "Charlie pushed the computer back to me without any explanation."

            "I feel weird."
            hide charlie angry

            #Propreties: M5-1=M4 B5 E5 -1=E4
            menu:
                "and I report this incident to the project manager.":
                
                    jump everything_changed 

                "But I act like nothing happened and submitted the minutes.":
                    #scene bg black with fade 
                    menu:
                        "Timeskip to Team Office":
                            scene bg workspace with fade 
                            #Propreties: M5 B4 +1=5 E5
                            "Everything goes well and this project is approved."
                            "Until one day, the project is delivered to the investor."
                            "The representative stated that the expected feature in the delivered project was not implemented."
                            "I recieved an email from the project manager, asking to speak to me about the issue."
                            "As I read the email, I immediately realized that the missing feature was edited out from the notes by Charlie after that seminar."
                            "I now understand why Charlie said those angry words that day." 
                            "He was never going to agree with the design decided at that seminar."
                            menu: 
                                "Go to Project Manager Office":
                                    scene bg office with fade 
                                    show pm angry
                                    "I tell the truth about what happened on the day of the seminar."
                                    "The project manager looks at me with disbelief and disapproval in his eyes."
                                    pm "Charlie told me everything, you should be honest, [mcname]."
                                    
                                    "I stood there, my hands and feet cold, unable to say a word."
                                    hide pm angry 
                                    #Propreties: M5-1=M4 B5 E5 -1=E4 
                                    jump everything_changed 


label everything_changed: 
    scene bg black with fade
    "Then everything changed."
    scene bg office space
    show charlie neutral 
    "Charlie has become critical of my work."
    "Low scores start popping up frequently on my performance reviews."
    "Charlie sometimes ignores what I say during daily meeting." 
    #I know, Charlie knows what I did.(for A. Reporting) 
    "I don't know what happened."
    #Propreties: M4-1=M3 B5 E4-1=E3
    "Everything tells me that something's wrong."
    "But I'm not sure what's going to happen."
    "Because Charlie is still occasionally considerate towards me and gives me some great advice about my work."
    "But I don't feel comfortable at this company anymore." 
    hide charlie 

    menu: 
        "I think I was treated badly.":
            #A: Propreties:M3 B5 E3 -1=E2 
            jump feel_terrible 

        "Maybe I'm just being overly sensitive":
            "I need to go to the private meeting room to speak with QA this afternoon."
            menu: 
                "Pass by the Lounge":
                    scene bg lounge with fade 
                    who "\"[mcname] slacks off at work. [mcname] is so stupid and always makes mistakes.\""
                    "Listening closely, I recognize Charlie's voice."
                    "It sounds like he's talking about me..."
                    #Propreties:M3-1=M2 B5-1=B4 E3 -1=E2
                    jump feel_terrible 

label feel_terrible:
    "I feel terrible." 
    menu: 
        "I decide to talk to Charlie.":
            #menu:
             #   "Go to Charlie": 
            show charlie angry 
            ch "You are too young. You don't know what goes on in the background. All things are about business."
            ch "You screwed everything up, [mcname]."
            hide charlie angry 

            menu:
                "But it is not my mistake.":

                    show charlie neutral
                    "Charlie looks me straight into my eyes."
                    show charlie angry 
                    ch "You know nothing."
                    ch "I wonder why the HR team gave this job to you."
                    show charlie neutral 
                    ch "But, it's ok. Everyone makes mistakes."
                    ch "You have to talk to me first if you do not know how to make a decision."
                    ch "I'll always be there for you."
                    ch "You just need time to learn more."
                    hide charlie 
                    #Propreties: M3 B5 E2 -1=E1
                    jump you_suck_response 

                "...could you please give me one more chance?":
                    show charlie happy
                    "Charlie smiled."
                    #Propreties: M3 -1=2 B5 E2+1=E3
                    ch "Of course, you deserve it."
                    "Charlie is so kind."
                    "I began to doubt myself. I must have done something wrong."
                    jump gaslit
                   

        "I pretended that nothing happened.": #"I pretended not to hear and hurried out of there.": 
            menu: 
                "Team Office":
                    scene bg workspace with fade 
                    "Worse things start to happen."
                    "My colleagues began to distance themselves from me."
                    show charlie angry
                    "Charlie even accused me of not dressing well enough today."
                    hide charlie angry 
                    show player sad 
                    mc "But, everyone dresses casually here..."
                    hide player 
                    show charlie angry 
                    ch "Not to the point of wearing sandals to work. Put on proper shoes next time."
                    "I break down and burst into tears."
                    "There is only apathy in the workplace."
                    show charlie neutral 
                    "Charlie looks at me."
                    show charlie angry 
                    ch "You are so pathetic. Tears are worthless. Especially over a pair of sandals."
                    #Propreties:M2-1=M1 B4-1=B3 E2 -1=E1
                    "I began to doubt myself. I must have done something wrong."
                    hide charlie angry 
                    jump gaslit

label gaslit: 
    show charlie neutral
    "I can still remember Charlie patting me on the shoulder and saying," 
    #scene bg workspace with fade 
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
                    "I start to arrive at the office earlier and leave later than everyone else."
                    "I double-check every email again and again, even for notifications that don't matter."
                    "I change my clothes every day."
                    "However, Charlie always finds something that needs improvement."
                    scene bg office space with fade 
                    show charlie neutral
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
                    "I feel grateful."
                    "Charlie still encourages me."
                    "I still kept this job."
                    hide charlie neutral 
                    scene bg black with fade 
                    "I can't sleep at night."
                    "I'm afraid tomorrow will come."
                    "I'm afraid I'll make new mistakes."
                    "My hair is starting to fall out, handfuls of it."
                    #Propreties: M1 -1=0  B3-3=0  E 0 
                    jump worst_end

        "That's not right. That's not how it's suppose to be.":
            "I must get out of this disgusting situation."
            jump get_proof
    
        
label you_suck_response:
    menu: 
        "Sorry about the unpleasant things. I'll do it in my way.":
            "I decide to fight back."
            #Propreties:M3 +1=M4 B5 E 1
            jump get_proof


        "Great, I'm done.": 
            "I quit the job immediately."
            #Propreties: M3 +1=M4 B5 E1 +4=E5
            jump resign 

label get_proof: #Properties Checking: if M<3, execute A, prompt Warning
    #scene bg workspace
    "I have to prove that I told the truth."
    #"<Warning> Different options require different psychological pressures."
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
        "Go to Project Manager Office":
            scene bg office with fade 
            #show pm neutral 
            show pm angry
            "I sent all the evidence I collected to the project manager."
            "After a moment's silence."
            show pm neutral
            pm "Nice work you did."
            hide pm 
            #Properties Checking: if M<3 to i102 

        #STATS STUFF
        #replace this with an if statement? 
            menu:
                "Good Stats":
                    jump good_end 

                "Bad Stats":
                    jump dismiss 
label evidence2:
    menu:
        "Go to Project Manager Office":
            scene bg office with fade 
            #show pm neutral 
            show pm angry
            "I sent all the evidence I collected to the project manager."
            "After a moment's silence."
            show pm neutral
            pm "Nice work you did."
            pm "I apologize for being so presumptuous earlier."
            scene bg black with fade
            "Charlie was fired."
            "I later heard that he had done the same thing before." 
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
            "A couple days later..."
            #show pm neutral 
            show pm angry
            pm "Sorry, we won't be hiring you anymore."
            hide pm 
            #Properties Checking: if E<3 to J103
        #STATS STUFF
        #replace this with an if statement? 
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
    "I was transferred to another team."
    "In 6 months, I have never felt so relaxed."
    "Ending 3. Success"
    jump end 


label worst_end:
    scene bg black with fade 
    "The world hates me. "
    "I'm a terrible person."
    "Ending 1. Lose it all." #changed the name 
    jump end 
