
label s158:
    
    scene expression 'background/BG_32D.jpg' at bgpos
    
    play music 'sound/06.mp3'
    
    ".... I go up the residential hill and arrive at the outskirts of the mansion."
    
    "It's around two in the morning."
    
    "As expected, I'm totally assailed by sleepiness."
    
    "\".... I wonder if she's going to be okay.\""
    
    "I'm concerned about how she seemed when we parted."
    
    "It seemed like it wasn't pain from her wound, but---"
    
    "\"Hm.... crap, the front gate is locked.\""
    
    "It's only natural, but it's still locked."
    
    ".... If I climb over the wall like yesterday, alarms will probably go off."
    
    "\".... Dang.... does this mansion have a rear entrance or something?\""
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    scene expression 'background/BG_47.jpg' at bgpos
    
    ".... I walk around the mansion perimeter."
    
    "Anyway, there is something like a rear entrance, but it's locked so I can't get in."
    
    "It's probably not possible to force my way through to the garden."
    
    "\".... Dang."
    
    "If this keeps up I'll have to spend the night out here....\""
    
    "I want to avoid that if possible."
    
    "People don't really go by the mansion, so after the sun sets it's just a deep darkness around here."
    
    "Walking around during these hours sends chills down my spine."
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    scene expression 'background/BG_47.jpg' at bgpos
    
    "\"Hm?\""
    
    "What is that?"
    
    "It feels like there's someone lurking in the shadows not illuminated by the streetlights."
    
    scene expression 'background/IMA_11B.jpg' at bgpos
    
    scene expression 'background/BG_47.jpg' at bgpos
    
    "---Thu,mp."
    
    "My heart stops my breath."
    
    "My blood rushes through my body, this sensation---"
    
    "Certainly, there's someone standing there."
    
    "The figure gets closer and closer."
    
    "Footsteps."
    
    "The sound of dry footsteps reaches my ears."
    
    "----Thu, mp."
    
    "I have a bad feeling about this."
    
    "Chills race up my spine."
    
    "\"----\""
    
    "The figure draws near."
    
    "Suddenly----the streetlights shatter loudly."
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    "The moon is hidden by the clouds."
    
    "The whole world instantly turns to darkness."
    
    "\"!\""
    
    "----Thump......!"
    
    "My heartbeat skips, as if warning me of death."
    
    "Perhaps I was tired after having walked the perimeter of the mansion for so long."
    
    "My body gave an all-too-sluggish reaction as I tried to leap backwards."
    
    scene expression 'background/IMA_11B.jpg' at bgpos
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    "A knife running through the dark."
    
    "The sound of the flesh over my heart being sliced."
    
    scene expression 'background/IMA_13.jpg' at bgpos
    
    "\"Ah---eh?\""
    
    "---I don't, understand."
    
    "Just.. that.. there's a knife, sticking through my chest."
    
    scene expression 'background/BG_47.jpg' at bgpos
    
    scene expression 'background/BG_47.jpg' at bgpos
    
    show expression 'foreground/ROA_T07B.png' as i0 at fgpos(14, 0)
    
    scene expression 'background/BG_47.jpg' at bgpos
    
    "The clouds part for a brief moment and illuminates the dark figure."
    
    "\"Ah----\""
    
    "An eerie figure wrapped entirely in bandages."
    
    "That's.. the last thing I see."
    
    stop music
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    scene expression 'background/END.jpg' at bgpos
    
    "Will you take 'Ciel-sensei's lesson'?"
    
    menu:
        
        'Yes.':
            
            $ selected = 1
        
        'No.':
            
            $ selected = 2
    
    if selected == 1:
        
        jump s515
    
    if selected == 2:
        
        jump start
