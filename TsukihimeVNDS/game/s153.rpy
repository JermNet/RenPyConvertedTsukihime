
label s153:
    
    stop music
    
    scene expression 'background/BG_06B.jpg' at bgpos
    
    ".... As expected, the debate over what to do for the Culture Festival is a stormy one."
    
    "Since everyone's opinions are different, the decision gets postponed till next week."
    
    "By the time it's over, it's late in the afternoon."
    
    "Everyone gets up tiredly from their chairs and leaves the classroom."
    
    "\"----Well then.\""
    
    "There's nothing to do in the classroom."
    
    "I should get ready for tonight and go back to the mansion---"
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    scene expression 'background/BG_32B.jpg' at bgpos
    
    play music 'sound/01.mp3'
    
    "I don't swing by anywhere else and head right back to the mansion."
    
    "The sun hasn't quite set so Akiha probably isn't back yet."
    
    "\"That Akiha."
    
    "I wonder if she's still mad like this morning....\""
    
    ".... Well, that can't be helped either."
    
    "I can't tell her the truth, so I'll probably just continue to be hated as a terrible older brother."
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    scene expression 'background/BG_33B.jpg' at bgpos
    
    scene expression 'background/BG_33B.jpg' at bgpos
    
    show expression 'foreground/HIS_T01.png' as i0 at fgpos(62, 0)
    
    "\"Welcome back, Shiki-sama.\""
    
    "Hisui bows as I enter the mansion."
    
    "\".... Yeah, I'm back."
    
    "Thanks for greeting me, Hisui.\""
    
    "---It's been a week since I've come back, but I'm not used to this yet."
    
    "\"Um, Akiha isn't back yet?\""
    
    "\"No."
    
    "She told me to tell you she would be back especially late tonight so please eat dinner on your own, Shiki-sama.\""
    
    scene expression 'background/BG_33B.jpg' at bgpos
    
    ".... I knew she'd still be angry from this morning."
    
    "\"----Sigh.\""
    
    "I slump my shoulders as I start to walk to my room."
    
    "---And then,"
    
    scene expression 'background/BG_33B.jpg' at bgpos
    
    show expression 'foreground/HIS_T01.png' as i0 at fgpos(62, 0)
    
    "\"Shiki-sama.\""
    
    "Hisui looks around the lobby before she speaks again."
    
    "\"Forgive me for asking an awkward question, but will you be leaving tonight again, Shiki-sama?\""
    
    "\"Eh----?\""
    
    "She fixates her emotionless eyes on me."
    
    "I think she simply wants to know what time I'll be back because she's so dedicated of a servant, but letting her know means Akiha would know."
    
    "I should---"
    
    scene expression 'background/BG_33B.jpg' at bgpos
    
    menu:
        
        "Still, I'll tell Hisui the truth.":
            
            $ selected = 1
        
        "No, I can't let anyone know.":
            
            $ selected = 2
    
    if selected == 1:
        
        jump s154
    
    if selected == 2:
        
        jump s155
