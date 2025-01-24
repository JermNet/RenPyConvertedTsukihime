
label s168:
    
    scene expression 'background/BG_32A.jpg' at bgpos
    
    "\"Does that clear it up?"
    
    "Then let's go.... Arcueid, do you have anywhere in mind?\""
    
    scene expression 'background/BG_32A.jpg' at bgpos
    
    show expression 'foreground/ARK_T03.png' as i0 at fgpos(36, 0)
    
    "\"Hmm, I don't know so I'll let you decide."
    
    "Just take me wherever?\""
    
    scene expression 'background/BG_32A.jpg' at bgpos
    
    ".... So she told me we're going somewhere and now it's this?"
    
    "Oh well--I'm not sure what kind of place she likes, but I'll take her to a good hangout place."
    
    "Well then--"
    
    menu:
        
        'Go for the usual, take her to the movie theater.':
            
            $ selected = 1
        
        "She'll probably like somewhere such as a back alley, right?":
            
            $ selected = 2
        
        "I don't really know, so let's go to the park for now.":
            
            $ selected = 3
    
    if selected == 1:
        
        jump s169
    
    if selected == 2:
        
        jump s170
    
    if selected == 3:
        
        jump s171
