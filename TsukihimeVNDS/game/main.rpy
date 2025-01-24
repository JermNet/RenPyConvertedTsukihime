
label start:
    
    if persistent.clear_kohaku != 0:
        
        scene expression 'background/TITLE2.jpg' at bgpos
    
    if persistent.clear_kohaku == 0:
        
        scene expression 'background/TITLE1.jpg' at bgpos
    
    play music 'sound/08.mp3'
    
    if persistent.clear_kohaku != 0:
        
        menu:
            
            'Watch Opening':
                
                $ selected = 1
            
            'Start Game':
                
                $ selected = 2
            
            '"Eclipse"':
                
                $ selected = 3
    
    if persistent.clear_kohaku == 0:
        
        menu:
            
            'Watch Opening':
                
                $ selected = 1
            
            'Start Game':
                
                $ selected = 2
    
    if selected == 1:
        
        stop music
        
        jump opening
    
    if selected == 2:
        
        stop music
        
        jump s20
    
    if selected == 3:
        
        stop music
        
        jump eclipse
