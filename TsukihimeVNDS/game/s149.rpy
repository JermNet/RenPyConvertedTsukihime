
label s149:
    
    scene expression 'background/BG_06A.jpg' at bgpos
    
    play music 'sound/03.mp3'
    
    "Fourth period class is about modern society."
    
    "The mood in the classroom is somewhat lighter than usual before lunch."
    
    "Today is Wednesday, so there's one less hour of classes than usual."
    
    "After lunch, there's homeroom and an hour of deciding what to do for the Culture Festival."
    
    "What's more, tomorrow is a school holiday, so after this fourth period is over, it's practically vacation already."
    
    "It's only natural for everyone to be waiting for the end-of-class bell to ring."
    
    "\"----Sleepy.\""
    
    "I give a big yawn."
    
    "The class is completely unchanged, the whole day progresses with nothing out of the ordinary."
    
    "Come to think of it, I've been through so many strange experiences, I almost feel odd just sitting in class."
    
    "And after classes are over and night falls, I'll have to go out once more with Arcueid."
    
    "Thinking of that, I really don't have the time to be fooling around here."
    
    "I look at my reflection in the window glass."
    
    "Tohno Shiki's face seems to be happy for some reason."
    
    "\"----Grr.\""
    
    "I tighten my expression."
    
    "It's not like roaming the streets with Arcueid is fun, so why am I acting like this?"
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    scene expression 'background/event/ARK_E09.jpg' at bgpos
    
    scene expression 'background/BG_06A.jpg' at bgpos
    
    "\".... Arcueid....\""
    
    "There's really, something wrong."
    
    "Looking out the window and into the rear courtyard, I can see an illusion of her aacing her hand at me and saying \"Hey\"."
    
    "----Hey, wait a minute....!"
    
    scene expression 'background/event/ARK_E09.jpg' at bgpos
    
    "\"Wha, wha, wha----\""
    
    "I push myself onto the window and look down."
    
    "I can only see the very edge of the rear courtyard,"
    
    "but without a doubt,"
    
    "Arcueid, in her usual manner, is at my school."
    
    "\"!!!!!\""
    
    "I look around the classroom."
    
    "----Fortunately, there's no one who noticed the strange foreigner aacing to me."
    
    "\"What is she thinking....!?\""
    
    "I moan to myself as I clutch my head."
    
    "But, complaining does me no good."
    
    ".... There's about twenty minutes till lunch."
    
    "What are you going to do Shiki?"
    
    "If you leave her alone, who knows what she'll do....!?"
    
    menu:
        
        'Go to the courtyard now.':
            
            $ selected = 1
        
        "Pray she doesn't do anything until classes are over.":
            
            $ selected = 2
        
        "I don't care":
            
            $ selected = 3
    
    if selected == 1:
        
        jump s150
    
    if selected == 2:
        
        jump s151
    
    if selected == 3:
        
        jump s152
