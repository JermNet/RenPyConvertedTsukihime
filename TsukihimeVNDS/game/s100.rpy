
label s100:
    
    scene expression 'background/BG_29C.jpg' at bgpos
    
    ".... Still, still too early."
    
    "There's about ten meters in between me and Nrvnqsr."
    
    "I need a more definite opening before I can draw close without him realizing me."
    
    "\"------\""
    
    "I gulp."
    
    "A little more----a little more, something----"
    
    "\".... I do not understand.\""
    
    "Muttering."
    
    "As if speaking to the moon above, Nrvnqsr mutters aloud."
    
    "\"It is displeasing to be faced by such unsightly enmity, but I cannot think this is one of the Princess's familiars."
    
    "Is that just trash?\""
    
    "\"------!"
    
    "Shiki, run away!\""
    
    "Arcueid's composed voice."
    
    "\"...... Eh?\""
    
    "But, I can't understand in time."
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    "My legs start to sink in something."
    
    "The firm ground beneath me is like quicksand."
    
    "\"Ah------\""
    
    "The ground is full of something pitch-black."
    
    "My body collapses."
    
    "My ankles which sunk into the black puddle are attached to nothing."
    
    "\"------\""
    
    "I fall with a splash into the puddle."
    
    ".... There's no bottom."
    
    "This black puddle transforms into a mouth of a large animal and compresses my body-----"
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    scene expression 'background/END.jpg' at bgpos
    
    "Will you take 'Ciel-sensei's lesson'?"
    
    menu:
        
        'Yes.':
            
            $ selected = 1
        
        'No.':
            
            $ selected = 2
    
    if selected == 1:
        
        jump s514
    
    if selected == 2:
        
        jump start
