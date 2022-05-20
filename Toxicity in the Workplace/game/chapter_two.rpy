label chapter_two:
    scene bg office space with fade 
    show pm neutral 
    "You are Joe, the project manager."
    "You are responsible for delegating tasks and delivering communication between your team and the publisher."
    hide pm
    menu:
        "Project Manager Office":
            scene bg office with fade 
            show pm neutral 
            "It's Friday morning, which means that I'm due for a meeting with the publisher soon."
            "I gather up my meeting notes, take one last sip of coffee, and check my watch."
            joe "I still have some time..." 
            "{i}(Exploration break){/i}"
            "I murmer to myself, straightening my suit."
            joe "Gotta head to the meeting room before Percy gets here." 
            menu: 
                "Go to Team Meeting Room":
                    scene bg meeting room with fade 
                    "Not long after I've taken a seat, the publisher's spokesperson promptly strides through the door and takes the seat across from me."
                    show pub happy
                    per "Good morning, Joe." 
                    "He smiles, extending a hand in greeting."
                    joe "Good morning, Percy. "
                    #"I reply,"
                    hide pub 
                    menu: 

                        "Smiling in kind and grasping his hand in a handshake.":
                            $ joeStats['Charisma'] += 2
                            $ joeStats['Kindness'] += 2
                            "Charisma increase by 2, Kindness increase by 2"
                            jump handshake 

                        "Curtly nodding and grasping his hand in a firm handshake.":
                            $ joeStats['Awareness'] += 2
                            "Awareness increase by 2"
                            jump handshake 

                        "Giving a goofy grin and eagerly shaking his hand.":
                            $ joeStats['Kindness'] += 1
                            "Kindess increase by 1"
                            jump handshake

                        "Making solid eye contact with him as I shake his hands once.":
                            $ joeStats['Awareness'] += 1
                            $ joeStats['Charisma'] += 1
                            "Charisma increase by 2, Awareness increase by 1"
                            jump handshake

label handshake:
    show pub happy 
    per "Well then, let's get down to business, shall we?" 
    show pub neutral 
    "I agree, flipping open my notebook and uncapping my pen. "
    per "The deadline for this new character is rolling up in just two weeks. Have all of the sprint goals been met so far?" 
    
    joe "Yes! In fact, with how the remaining tasks are scheduled, we currently have no outstanding problems with releasing the character by the deadline." 
    show pub happy 
    per "Perfect!" 
    "Percy's eyes light up and he clasps his hands together with approval."
    show pub neutral 
    per "I'll just need you to make a few adjustments to the moveset and add in a couple of new animations for the character then." 
    per "We're really banking on getting these changes in since the character feels a little too weak and has less of a personality compared to the rest of the roster." 
    per "It's imperative that we get these changes. It's super important for player engagement." 
    hide pub
    menu: 
        "Accept the request.":
            $ joeStats['Awareness'] -= 2
            $ joeStats['Charisma'] += 2
            " Awareness decrease by 2, charisma increase by 2"
            jump accept_pub

        "Propose a middle-ground solution.":
            $ joeStats['Awareness'] += 1
            $ joeStats['Charisma'] += 1
            $ joeStats['Courage'] -= 1
            "Courage increase by 1, Courage decrease by 1, Charisma increase by 1"
            jump middle_pub

        "Decline the request.":
            $ joeStats['Courage'] += 2
            $ joeStats['Awareness'] += 2
            $ joeStats['Charisma'] -= 2
            "Courage increase by 2, Awareness increase by 2, Charisma decrease by 2"
            jump decline_pub

label accept_pub:
    show pub neutral
    "Well, if it's a request coming directly from our publisher, who am I to say no?"
    joe "Yes, of course," 
    "I nod," 
    joe "I'll move some things around on the schedule to make sure that gets done."
    show pub happy 
    "Percy beams," 
    per "Wonderful, I will eagerly anticipate your update next week!"
    hide pub
    
    jump schedule

label middle_pub:
    show pub neutral
    "It seems a bit much to finish within two weeks with everything else going on."
    " I should probably try to bargain this a little bit..."
    joe "Which of the two features is more important to increasing player engagement?" 
    per "Making the character stronger than the rest of the roster will definitely be important for hooking players into buying them." 
    joe "Alright, then how about we try to implement that first and see if we can get to the animations at a later date?" 
    show pub angry 
    "Percy's brow slightly furrows."
    per "Definitely not ideal." 
    joe "I agree, it's not ideal. But having too many changes will jeopardize getting the character released on time." 
    "Percy sighs."
    per "Fine, I'll check back with you next week then. The moveset better be satisfyingly strong by then." 
    hide pub 
    
    jump schedule 

label decline_pub:
    show pub neutral 
    joe "I'm afraid that I'll have to politely decline. Our team will already be working all the way up until the deadline with our current schedule." 
    show pub happy 
    "The corners of Percy's lips curve up into a sarcastic smile." 

    per "And I'm afraid that you have no say in the matter."
    per "Our board has decided that these features will be vital for sales, so we'll need these features in when the character releases." 
    per "I expect to hear good news about your progress on the matter next week." 
    hide pub

    jump schedule

label schedule:
    "{i}(Exploration Break){/i}"

    menu: 
        "Head back to Project Manager Office":
            scene bg office with fade
            "Well, I better get cracking on this schedule..."
            menu: 
                "Call an emergency meeting with involved parties":
                    $ joeStats['Awareness'] += 3
                    $ joeStats['Courage'] += 1
                    $ joeStats['Charisma'] += 2
                    "Awareness increase by 3, Courage increase by 1, Charisma incease by 2"
                    jump chose_what 

                "Call an emergency meeting with the whole team":
                    $ joeStats['Awareness'] += 3
                    $ joeStats['Courage'] += 1
                    "Awareness increase by 1, Courage increase by 1"
                    jump chose_what 

                "Reschedule tasks on your own":
                    $ joeStats['Awareness'] -= 3
                    $ joeStats['Charisma'] -= 2
                    "Awareness decrease by 3, Charisma decrease by 2"
                    jump reschedule_tasks 

label chose_what:
    #STATS STUFF - change this menu into if statement 
    menu: 
        "You had Accepted/Declined the request":
        #A. Call an emergency meeting with involved parties AND either Accepted the request (A) OR Declined the request (C)
            jump emergencyAC 
        
        #A. Call an emergency meeting with involved parties AND Proposed a middle-ground solution (B)
        "You picked the middle ground option":
            jump emergencyB 


label emergencyAC:
    "Delegation's my job, but without the proper expertise, rescheduling tasks last minute on my own is only going to drag everyone else down."
    "A few minutes pass and Ariel peeks her head in, lightly rapping on my office door."
    show anim neutral 
    ari "Hello Joe! Sorry, my team leader is currently busy so they sent me in their stead. Is that okay?" 
    joe "Of course," 
    #"I nod," 
    joe "This is a very spontaneous meeting so it's understandable."
    show anim neutral at left with move
    show charlie neutral at offscreenright 
    "As Ariel quickly takes a seat and Charlie strides in soon after."
    show charlie happy at right with move
    ch "Hey man, you called?" 
    joe "Yeah, I just need some insight on how long these new tasks from the publisher might take "
    joe "and how we can cut some of our current tasks short to accommodate for the extras." 
    scene bg black with fade 
    hide anim
    hide charlie
    "The meeting continues for another hour."
    scene bg office with fade 
    "It's too bad we lost 15 minutes of lunch break, "
    "but I have a much clearer idea of how to distribute these tasks and assign realistic deadlines for these next two weeks."
    menu: 
        "Go to Team Meeting Room":
            scene bg meeting room with fade
            joe "Welcome, everyone, to our sprint review where we'll be going over completed work and additional changes."
            joe "I have some updates to share with everyone based on the meeting I had with our publisher this morning."
            "I give everyone a concise rundown of the publisher's requests and the modified sprint schedule."
            ex1 "More features?"
            ex2 "Really?? Not crunch time again..."
            ex3 "I'll have to let my wife know to save a portion of dinner for me for the next two weeks."
            "Several unsatisfied murmers float through the air."
            "But who wouldn't be unhappy with crunch time?"
            "Such is the life of a game developer. Weekends are a luxury."
            jump ch2_end 

label emergencyB:
    "Delegation's my job, but without the proper expertise, rescheduling tasks last minute on my own is only going to drag everyone else down."
    show charlie happy at offscreenright
    "Charlie strides in soon after receiving the message I sent him on Sloth."
    show charlie happy at middle with move
    ch "Hey man, you called?"
    joe "Yeah, I just need some insight on how long these new tasks from the publisher might take" 
    joe "and how we can cut some of our current tasks short to accommodate for the extras."
    scene bg black with fade 
    "The meeting continues for another 45 minutes."
    scene bg office with fade
    "We luckily ended right before lunch break."
    "I have a much clearer idea of how to distribute these tasks and assign realistic deadlines for these next two weeks!"
    
    menu: 
        "Go to Meeting Room":
            scene bg meeting room with fade
            joe "Welcome, everyone, to our sprint review."
            joe "I have some updates to share with everyone based on the meeting I had with our publisher this morning."
            "I give everyone a concise rundown of the publisher's requests and the modified sprint schedule."
            ex1 "Scaling numbers? That doesn't seem too bad"
            ex2 "Well, reasonable enough..."
            "A few unsatisfied, yet optimistic murmers float through the air."
            "Good, looks like we'll be able to make the deadline without using too much overtime. "
            "You gotta cut what you gotta cut. Scope is important and feature creeping will be the downfall of all of us."
            jump ch2_end 

label reschedule_tasks:
    "Delegation's my job and everyone else is currently busy finishing up their sprint."
    "I can't bother them with something that they don't need to worry about until Monday. "
    "I spend the next 2 hours reordering all tasks to accommodate for the publisher's requests."
    "I'm pretty confident that our team can still meet all of the new sprint goals in time for the character's release."
    "I missed out on lunch break for this, but I'm feeling pretty satisfied for a job well done!"
    "Now that the schedule changes are complete, it's time to hold the Sprint Review in the meeting room."
    menu: 
        "Go to Meeting Room":
            scene bg meeting room with fade
            joe "Welcome, everyone, to our sprint review."
            joe "I have some updates to share with everyone based on the meeting I had with our publisher this morning."
            "I give everyone a concise rundown of the publisher's requests and the modified sprint schedule."
            ex1 "More features?"
            ex2 "Wait, there's NO way I can get this done in two days."
            ex3 "I'll have to let my wife know that I'll be sleeping over at the company for the next two weeks..."
            ex3 "Gee, I hope she won't think that I'm cheating on her..."
            "Audible chatter of discontent and worrying comments start to grow louder even as team members start filing out of the room."
            "After hearing that, I'm not very confident in my scheduling anymore, either."
            "All I can do for now is to hope that everything will be okay and cater to any questions or concerns to the best of my ability."
            jump ch2_end 

label ch2_end:
    scene bg black with fade 
    "To be continued."
    return
