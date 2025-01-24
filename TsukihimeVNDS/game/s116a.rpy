
label s116a:
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    "........ My body is exhausted."
    
    "But, I can't fall into a deep sleep."
    
    "The wounds all around my body sting and wake up my mind as it tries to sleep."
    
    "I look at the clock as I lie in bed."
    
    "It's past three o'clock in the morning----already five hours of unsatisfactory rest."
    
    "\"...... Damn it, I can't sleep.\""
    
    "Not being able to sleep when I want to.. it's like torture."
    
    "Tick, tick, tick."
    
    "The sound of the clock's second hand gets on my nerves."
    
    "Tick, tick, tick, tick, tick, creak, tick, tick, tick, tick----"
    
    "\"Eh--?\""
    
    "I think I heard something mixed in with the ticking."
    
    "It sounded like the door opening, but who would be coming at this hour?"
    
    "Tap, tap, tap."
    
    "No, there's no mistake."
    
    "Someone came into the room and is coming near me."
    
    "\"----\""
    
    "Who is it?"
    
    ".... If someone was to come this late at night, it would be---"
    
    if persistent.cleared != 0:
        
        jump s117
    
    menu:
        
        'It might be Arcueid.':
            
            $ selected = 1
        
        'It might be Ciel-Senpai.':
            
            $ selected = 2
        
        'It might be Akiha.':
            
            $ selected = 3
    
    if selected == 1:
        
        jump s118
    
    if selected == 2:
        
        jump s119
    
    if selected == 3:
        
        jump s120
