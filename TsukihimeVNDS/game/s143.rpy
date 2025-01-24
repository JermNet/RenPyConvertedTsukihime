
label s143:
    
    if flg7 >= 1:
        
        jump s144
    
    if flg8 >= 1:
        
        jump s145
    
    scene expression 'background/CMO_05.jpg' at bgpos
    
    "Back then, the whole mansion was like a giant playground."
    
    "The garden, a deep forest."
    
    "The house, a tall castle."
    
    "We played in our own little world, which would take days to explore."
    
    "Every day was fun."
    
    "No one thought about ever growing up,"
    
    "and we believed that days and nights would always be the same."
    
    "It was just a childhood spent playing like puppies."
    
    "We got along wonderfully, and were the best of playmates."
    
    "Whenever I turned back, Akiha would be there, aacing her hands and hiding shyly."
    
    "Yes, always the same."
    
    "At that time, the mansion was a giant playground."
    
    "The garden, a deep forest."
    
    "The house, a tall castle."
    
    "We played in our own little world, which would take days to explore."
    
    scene expression 'background/IMA_11.jpg' at bgpos
    
    "I slowly awaken and open my eyes."
    
    "The morning light wraps around me and my sleepiness starts to lift."
    
    "As the last vestiges clear,"
    
    "I sense that I had a very nostalgic dream."
    
    scene expression 'background/BG_40E.jpg' at bgpos
    
    "\"-------\""
    
    "As soon as I open my eyes, I start to see those terrible things jump into my vision."
    
    "My head stabs with pain."
    
    "\"Gg----\""
    
    "I scramble for the glasses by my pillow and put them on."
    
    scene expression 'background/BG_40A.jpg' at bgpos
    
    play music 'sound/02.mp3'
    
    "I take in some air."
    
    "After taking a few deep breaths, I manage to calm down."
    
    "\"Why did I----so early..\""
    
    "See those lines so clearly this early in the morning?"
    
    "It's difficult to see the lines of death in buildings."
    
    "It's usually hard to see them, and seeing them so clearly like I just did now is rare."
    
    "\"........\""
    
    "What's more, I even saw those \"points\"."
    
    "I think my headache is getting worse too."
    
    "Sensei said these eyes would attract things that weren't good."
    
    "I think Arcueid and these vampires are certainly not good."
    
    "So, maybe it's all affecting my eyes and making them stronger."
    
    "\"----Can't be.\""
    
    "I'm probably just tired."
    
    "\"Huh----?\""
    
    "Come to think of it, Hisui isn't here."
    
    "It's already past seven."
    
    "Normally she would have already come in and woke me up."
    
    "\".... Maybe Hisui slept in.\""
    
    "But I see my freshly prepared uniform on my desk."
    
    "\"What's this?"
    
    "Maybe she had some other duties.\""
    
    "I'm a little curious, but I guess it doesn't concern me."
    
    "I don't have time this morning, so I should just hurry up, change and go to the sitting room."
    
    scene expression 'background/IMA_10.jpg' at bgpos
    
    scene expression 'background/BG_34A.jpg' at bgpos
    
    stop music
    
    "\"------Ah.\""
    
    "As I go from the lobby towards the sitting room, I realize I forgot something terribly important."
    
    "I open the door and stand there, without taking a single step forward."
    
    scene expression 'background/BG_34A.jpg' at bgpos
    
    show expression 'foreground/AKI_T01A.png' as i0 at fgpos(40, 0)
    
    "Akiha is in the sitting room."
    
    "Kohaku-san is nearby and the two of them are drinking tea silently."
    
    scene expression 'background/BG_34A.jpg' at bgpos
    
    "Normally she would say,"
    
    "\"Good morning, Nii-san,\""
    
    "no matter how angry she might be, but she doesn't even look at me this morning."
    
    "\"Ah...... uh.\""
    
    "It goes without saying."
    
    "Arcueid's coming here last night has some very lasting repercussions."
    
    "Akiha's irritation is permeating the air."
    
    "You could practically cut the tension with a knife."
    
    play music 'sound/02.mp3'
    
    scene expression 'background/BG_34A.jpg' at bgpos
    
    show expression 'foreground/KOHA_T01A.png' as i0 at fgpos(52, 0)
    
    "\"Good morning, Shiki-san.\""
    
    ".... Well, it seems like she's remained unaffected, at least."
    
    "\"Ah.. yeah, good morning Kohaku-san.\""
    
    "Raising a hand to Kohaku-san, I enter the sitting room."
    
    scene expression 'background/BG_34A.jpg' at bgpos
    
    scene expression 'background/BG_34A.jpg' at bgpos
    
    show expression 'foreground/AKI_T03A.png' as i0 at fgpos(40, 0)
    
    "Akiha glares at me as I shuffle into the sitting room."
    
    "---Ugh, I'm not going to succumb to this silent pressure!"
    
    scene expression 'background/BG_34A.jpg' at bgpos
    
    menu:
        
        'I should smooth things over with a cheerful greeting.':
            
            $ selected = 1
        
        "I won't do something stupid, so just greet her normally.":
            
            $ selected = 2
        
        'No, no':
            
            $ selected = 3
    
    if selected == 1:
        
        jump s146
    
    if selected == 2:
        
        jump s147
    
    if selected == 3:
        
        jump s148
