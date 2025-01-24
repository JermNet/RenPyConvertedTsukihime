
label s129:
    
    scene expression 'background/BG_01A.jpg' at bgpos
    
    "----I arrive thirty minutes earlier than usual."
    
    "The figures of students around the school gate are sparse."
    
    "It seems I'm the only one who's arrived at this odd time."
    
    scene expression 'background/BG_03A.jpg' at bgpos
    
    "On the school grounds, the athletic clubs are holding their practices."
    
    ".... I'm not in any clubs right now, but truthfully, I like to move around a lot."
    
    "I know that I have some athletic ability, at least enough to be proud of."
    
    "But, I can't join any clubs."
    
    "My body always has this recurring anemia so I would just be a bother----and my doctor has told me that I should not exercise frequently."
    
    "Since middle school, I've been asked more than a few times to join a club."
    
    "But I always have to say \"it's not my thing\" and refuse."
    
    "Every time I refused----I felt a sense of separation."
    
    "That might have been.."
    
    "a subconscious wall that told me I will never be able to mix in with the people on the other side."
    
    "\"........\""
    
    "Ah, that's enough."
    
    "This really isn't my thing."
    
    "I'll stop thinking such thoughts and hurry on to the classroom."
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    scene expression 'background/BG_06A.jpg' at bgpos
    
    play music 'sound/03.mp3'
    
    "\"Huh----?\""
    
    "I thought I was the first one, but it seems like some of my classmates are already here."
    
    "\"Yo, you're early Tohno.\""
    
    "\"Morning."
    
    "This class seems to have a lot of people with spare time.\""
    
    "\"Nah."
    
    "Our practice just got over with."
    
    "Those that come here this early who aren't in clubs are usually only those with daily duties.\""
    
    "I see."
    
    "That does makes sense, now that he mentions it."
    
    "Greeting those around me, I take my seat."
    
    "It's half an hour before homeroom."
    
    "It's not a bad idea to just watch my classmates arrive."
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    scene expression 'background/BG_06A.jpg' at bgpos
    
    "The classroom starts to get busy around seven fifty."
    
    "\"----Huh?\""
    
    "I think I saw Senpai in the hallway."
    
    "\"She's down at the first year hallway again----what is she doing?\""
    
    "Maybe she came to see me?"
    
    "Then----"
    
    menu:
        
        "I'll go into the hallway and talk to her.":
            
            $ selected = 1
        
        "No, it probably doesn't concern me so I'll just watch from here.":
            
            $ selected = 2
        
        "An opening! I'll surprise her from behind!":
            
            $ selected = 3
    
    if selected == 1:
        
        jump s130
    
    if selected == 2:
        
        jump s131
    
    if selected == 3:
        
        jump s132
