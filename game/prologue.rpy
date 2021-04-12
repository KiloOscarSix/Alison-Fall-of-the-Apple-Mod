
label start:
    image jessimation = Movie(play="Jessimation.webm")

    image jessimation2 = Movie(play="Jessimation2.webm")

    image meliwalk = Movie(play="Meliwalker.webm")

    image mcall = Movie(play="mcall.webm")

    image kittypat = Movie(play="patdatkitty.webm")

    image kittyblink = Movie(play="kittyblink.webm")

    image kittytears = Movie(play="kittytears.webm")

    image aliwalk = Movie(play="Aliwalker.webm")

    image shakedatbootay = Movie(play="Shakeitgirl.webm")

    image yoga1 = Movie(play="yoga1.webm")

    image yoga2 = Movie(play="yoga2.webm")

    image yoga3 = Movie(play="yoga3.webm")

    stop music

    scene black
    "This visual novel is intended for adults only and includes images that are sexual in nature."
    "May contain graphic violence, blood, sexual content and strong language."
    "All digital playable characters depicted in this game are at least 18 years old."
    "If you are under the age of 18, or if it is illegal to view such content in your country, please exit now."
    menu:
        "Are you 18 years old or above?"
        "I confirm that I am 18+ and that I can handle lots of TEXT!":


            jump legalage
        "I'm not 18+ and I love TEXT! Can we make a deal?!":


            jump not18



    return

label legalage:


    jump prologue_start



label prologue_start:
    $ mc = renpy.input("What is your name?")

    $ mc = mc.strip()

    if mc == "":
        $ mc="Michael"

    show text "PROLOGUE. REMASTER." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "2038. New York City aka The Big Apple." with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)


    menu:
        "The option to 'Skip to 3 route choice' is for those who have played previously and want to skip the prologue."
        "Normal game (Remastered Prologue)":

            jump IagreeSenpai
        "Skip to 3 route choice":
            jump FixMuhSavesBruh

label IagreeSenpai:
    scene black
    show text "2038. New York City. Alison." with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)
    scene alr01
    with dissolve
    A "Somebody help me, please!"
    scene alr02
    with dissolve

    A "(Maybe I managed to lose them?)"

    A "(No, I can hear footsteps.)"

    A "(I need to find a way out of here, or at least somewhere to hide for now.)"
    scene black
    show text "[mc] and his rookie \"Gunter\"" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)
    scene alr03
    with dissolve
    G "Hey, [mc]?"

    M "Yes, Gunter?"

    G "Tell me again, why do you keep choosing these lame ass traffic jobs?"

    M "We've already had this conversation. Focus on driving and stop nagging like an ex-wife."

    G "Hahaha. Yes, sir."
    scene black
    show text "The evil thugs. Ronny and Kenny." with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)
    scene alr05
    with dissolve
    play music "Fear.ogg" fadein 5
    k "Hey, Ronny. You hear that? Silence!"

    r "Hehehe. I think she wants to play hide and seek."

    k "Should we have some fun with the little princess first?"
    scene alr06
    with dissolve
    r "*Twisted smile* Oh, yes. Just make sure not to kill her, little brother."

    r "The boss said to bring her back alive."

    k "Yeah, I hear the little bitch is special."

    r "I can't wait to find out for myself, just how special she is."
    scene alr07
    with dissolve
    k "Well, let the games begin!"

    r "Oh, yes. Come here little bunny! I won't hurt you... much. Hahahaha!"

    k "Yeah, what he said! I promise, I'll only make it hurt for the night!"

    A "(Coming here was a big mistake. I really need to find a way back out there.)"
    scene alr08
    with dissolve
    r "Come out, come out, wherever you are!"

    k "You don't really think that is going to work on her, do you bro?"

    r "No, you idiot. It just sounded cool, you know, like in the movies?"
    scene alr09
    with dissolve
    k "Hehehe. Well, I'm going this way, you check the other side."

    r "Don't tell me what to do!"

    r "You go that way, I'll check this side."

    k "I just said that."
    scene alr10
    with dissolve
    r "Just shut your face and go find her."

    k "Yeah, yeah. I heard you the first time."

    r "Remember, I go first this time okay? And don't kill her!"

    scene alr11
    with dissolve
    k "Come here little bunny, I promise to be gentle if you let me catch you first."

    k "If you make me work, I'll make it hurt! Hehehehe."

    "Guy hiding behind the box" "(What the hell is going on here?)"

    "Guy hiding behind the box" "(First that crazy bitch screaming and now these two punks.)"
    scene alr12
    with dissolve
    A "(It looks like I was right. They want me alive... So, he sent them.)"

    A "(I'm not so sure that matters to me right now.)"

    A "(I need to figure out a way to get past them and back outside somehow.)"
    scene alr13
    with dissolve
    A "(Oh no! He's coming this way! What do I do, what do I do?!)"

    A "(Oh god. Please, somebody help me. *Sobs softly*)"

    r "Come out, come out, wherever you are!"

    r "You are starting to piss me off! Come out or I will make you suffer!"

    r "You hear?!"
    scene alr14
    with dissolve
    k "Hehehehe. What's the matter bro, the little bunny making you want to stab her in the face?!"

    r "Shut the fuck up [k], and find that little bitch!"

    k "Temper temper. Looks like somebody needs to get some. Hehehehe."

    r "I would shoot you if you were not my brother."
    scene alr15
    with dissolve

    k "Well, too bad. Cuz I am. Hehehehe."

    "Guy sneaking away from his box" "(Okay, these two fucking morons are armed and dangerous.)"

    "Guy sneaking away from his box" "(I think it is time I evict myself from this mansion.)"

    r "Did you find her yet?!"
    scene alr16
    with dissolve
    k "Found her! She's making a run for the stairs!"

    k "Stop her bro!"
    scene alr17
    with dissolve
    k "Well, I'll be damned. You sure she was a girl [r]?"
    play sound "9mmglock.ogg"

    r "What the fuck are you doing?! You almost shot me you retard!"

    k "I'm telling pa you called me that name again, and that's a dude that ran past you."
    stop music fadeout 2
    scene alr18
    with dissolve
    G "Hey, [mc], did you hear that sound?"

    M "Yeah, it sounded like a gunshot."

    G "Does that mean we're going to check it out?"

    M "It means we are going to call it in."
    scene alr19
    with dissolve
    M "Kid, don't be in such a hurry to die, okay?"

    M "I'm sure we'll find you lots of action when you are more experienced."

    G "You know why I became a cop sir."

    M "Yeah, I know. You want to change the world."
    scene alr20
    with dissolve
    G "You don't believe it's possible, do you [mc]?"

    M "Honestly? No, I don't. Now eyes front and watch the road."

    G "Yeah, sorry."
    scene alr21
    with dissolve
    M "Watch it!"

    G "Fuck!"
    scene alr22
    pause(.2)
    scene alr23
    with vpunch
    pause(.2)
    scene alr24
    with dissolve
    M "Well, it looks like he is in a hurry."

    G "Yeah, maybe it has something to do with that gunshot?"

    M "Let's find out. Just remember, stay to my right and behind me a few steps."

    G "I got your back."
    scene alr25
    with dissolve
    M "Turn those off."
    scene alr26
    with dissolve
    M "Are you okay sir?"

    "Barefoot dude" "Help me! They took my home!"

    M "Calm down and take it from the top."
    scene alr27
    with dissolve
    M "Who took your home?"

    M "Can you stand?"
    scene alr28
    with dissolve
    "Barefoot dude" "Uh, yeah!"

    M "Okay. Now, what's your name?"

    "Barefoot dude" "My name is Thomas."

    M "Thomas. Start from the begining. What happened, why are you running barefoot?"
    scene alr29
    with dissolve
    "Thomas" "Those thugs. They invaded my home. They shot me!"

    M "Where is your home?"

    "Thomas" "Uh, well, I'm homeless."

    G "Is this guy drunk?"

    M "Gunter. Don't be rude."

    "Thomas" "Listen to me! There was a girl who started screaming for help."

    G "A girl? Why the hell didn't you start with that first, man? Where is she?!"

    scene alr30
    with dissolve
    M "Calm down, [G]."

    "Thomas" "Man, I don't care about no girl! These two thugs with guns came into my home and shot me!"

    "Thomas" "Now do your job for once, and go get them out of my house!"

    M "(It doesn't look like he is under the influence of anything.)"

    M "Okay, we should call this in and get some backup."
    scene alr31
    with dissolve
    G "Man, screw backup, I'm not sitting idle while a woman gets abused! Never again."

    M "[G]! Don't go in there alone!"

    M "God damn it, kid!"

    M "(I have to call for back up and get this guy an ambulance quickly before that moron gets himself killed.)"

    M "(Fuck it. I'll have to lock this guy in the car until they arrive.)"
    scene alr32
    with dissolve
    r "Stop struggling bitch! I'm going to ruin that pretty face of yours if you keep this up."

    k "Hehehehe. I say we cut her a little first."

    r "Shut the fuck up [k], and hold this whore down already!"

    A "Let go of me! Help! Somebody help me, please!"
    scene alr33
    with dissolve
    G "(He was right. By the sound of it, there's two of them.)"

    G "NYPD! Come out with your hands up."

    r "You stupid bitch. Now, the little piggy has to die."
    scene alr34
    with dissolve
    r "Take care of it [k]."

    k "With pleasure, bro."

    r "I'm going to make you suffer for this, bitch."
    scene alr35
    with dissolve
    k "Okay! I'm coming out policeman sir."

    k "I don't want no trouble."
    scene alr36
    with dissolve
    G "You, back there. Let go of that woman, right fucking now!"

    G "And you, show me your hands, now!"

    r "Fuck you pig. Come and make me. This whore is mine!"
    scene alr37
    with dissolve
    G "This is your last warning, show me your fucking hands, now!"

    r "Do as the man says [k]. Show him your hands while I cut this bitch."

    k "Sure thing, bro."

    A "Let me go!"
    scene alr38
    with hpunch
    pause(.3)
    G "Huh?"
    scene alr39
    with dissolve
    G "(Was that just a kick? From her?!)"
    scene alr40
    with dissolve
    r "(What the fuck just happened?!)"

    k "Die pig!"

    M "[G]!"
    play sound "9mmglock.ogg"
    pause(.3)
    scene alr41
    with dissolve
    play sound "9mmglock.ogg"
    pause(.3)
    scene alr42
    with dissolve
    M "(God damn it, kid. Why the fuck did you have to rush in?)"

    A "(Oh no!)"

    M "You are as good as dead now, asshole."

    r "You're the one who is going to die here, pig! You bastard, you killed Kenny!"

    M "You're a cop killer. I am going to give you only one chance, asshole."
    scene alr43
    with dissolve
    A "Watch out! He's hiding."

    M "(Yeah, no shit, lady. But thanks I suppose.)"

    r "You're lucky I need you alive, bitch. But, don't worry, I'll make you scream for this."
    scene alr44
    with dissolve
    M "Drop the gun and come out with your hands up. There is no escape for you."

    M "Backup is already on its way."

    r "Oh, yeah? Then come and get me pig!"
    scene alr45
    with dissolve
    M "(Fuck. He's dead.)"

    M "(It looks like this asshole is hiding at roughly my two o'clock.)"

    M "(In that case.)"
    scene alr46
    with dissolve
    play sound "Glock9mm.ogg"
    pause(.4)
    scene alr47
    r "(Fuck! This pig is starting to make me angry.)"
    scene alr48
    with dissolve
    r "(I need to get out of here. I must avenge my brother, I can't do that if I'm dead.)"

    r "(I can always get that little whore back later.)"
    play sound "9mmglock.ogg"

    r "(This pig is not going to give me an opening. I need to think.)"
    scene alr49
    with dissolve
    M "(I'm sure I can take him out, but that girl should be my priority right now.)"

    M "(That fool gave his life for her.)"
    play sound "9mmglock.ogg"
    M "(I'll just keep him pinned down until they arrive.)"
    scene alr50
    with dissolve
    play sound "9mmglock.ogg"
    M "(I think he switched sides.)"
    scene alr51
    with dissolve
    M "(I see you asshole.)"
    scene alr52
    with hpunch
    play sound "Glock9mm.ogg"
    r "Fucking pig! Die already!"
    scene alr53
    with vpunch
    r "(Mother fucker! He is no ordinary little piggy. Likely ex military, like pops.)"

    r "(Okay, I'll just have to kill the power and make a run for it.)"

    r "(This piggy is too cautious for me, and I'm running out of time.)"

    A "Are you okay?"

    M "Move over a little."
    scene alr54
    with dissolve
    A "*Breathes shakily*"

    M "Don't worry, I'll get you out of here safely."

    r "Awww. You two already making promises? I can't wait to gut you, pig!"

    r "I'm going to make her watch, just so you know. Hahahahaha."
    play sound "9mmglock.ogg"
    scene alr55
    with dissolve
    r "Die pig!"
    play sound "Glock9mm.ogg"

    A "*Trembles* Please, don't die."
    scene alr56
    with dissolve
    stop sound
    M "(Fuck, I'm out and so are the lights.)"
    play sound "Glock9mm.ogg"
    pause(2)
    stop sound
    r "Fuck you, pig!"
    scene alr57
    pause(.3)
    play sound "reloading.ogg"
    pause(2)
    scene alr58
    pause(3)
    scene alr59
    with dissolve
    M "(He must have shot the fusebox. Lucky fuck.)"
    stop sound
    stop music
    scene alr60
    with dissolve
    M "Stay where you are, I'll be right back."

    A "*Sobs* Please! Don't leave me alone!"
    scene alr61
    with dissolve
    M "(What the fuck are you doing [mc]?)"

    M "(I don't have time for a personal vendetta right now.)"

    M "(I should make sure she is okay.)"
    scene alr62
    with dissolve
    A "*Breaks down in tears*"

    M "(Oh, fuck. The one thing I can't handle.)"
    scene alr63
    with dissolve
    play music "siren_arriving.ogg"
    M "I'm right here, okay?"

    M "I'm not going to leave you alone."

    A "*Sobs softly*"

    M "What's your name?"
    scene alr64
    with dissolve
    A "Al... *trembles* Alison."

    M "I'm [mc], Alison. Don't be scared."

    M "I'm not going to let anything happen to you."

    A "You... You promise?"
    scene alr65
    with dissolve
    A "*Gasps*"

    M "I promise. Now, breathe in slowly, and exhale."

    A "*Inhales and exhales slowly*"
    scene alr66
    with dissolve
    M "There you go. That's a good girl."

    M "You're in shock, so it's normal to be scared and a little shaky."

    M "I don't think you are any less brave than I am right now."
    scene alr67
    pause(.2)
    scene alr66
    pause(.2)
    A "(He is the first person who was ever nice to me from the start.)"

    A "(Maybe he can help me.)"
    scene alr67
    pause(.2)
    scene alr66
    pause(.2)
    M "Do you think you can stand?"

    A "*Nods gently*"

    M "Okay, let's try and stand up together, slowly, okay?"
    scene alr68
    with dissolve
    M "There you go. Just stay right here, I'll go and get you something to put on."

    M "I bet you're freezing."

    A "(He is so nice. I wonder if he is just pretending.)"
    scene alr69
    with dissolve
    A "Okay."

    M "I won't be gone long, I promise."

    A "Okay. *Shivers from the cold*"

    M "(I have no idea what those fucks wanted with her...)"

    M "(But, I do know that they wanted her alive for certain.)"
    scene alr70
    with dissolve
    A "(I really hope he is someone who can help me.)"
    stop music fadeout 2

    M "Hey, Alison?"
    scene alr71
    with dissolve
    A "Y-yes?"

    M "Put this on."
    scene black
    with fade
    "" "A few seconds later."
    scene alr72
    with vpunch
    M "Okay, I got you. You can lean on me, okay?"

    A "*Exhales relieved*"

    M "The ambulance is just outside. I'll make sure you get to the hospital safely."

    A "Thank you."

    M "(I can't imagine what she has gone through...)"

    M "(...but she looks like she'll be okay, with a little care.)"

    M "I'll make sure you are well taken care of. You have my word, okay?"

    A "*Sniffles* Thank you."
    play music "Alison.ogg" fadein 5
    scene black
    with Pause(1)


    show text "Made with Ren'Py Visual novel engine." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    scene black
    with Pause(1)

    show text "Created by OneManVN. Alison fall of the apple \"Remastered\"" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
label Hospital:
    scene black
    "" "A few hours later."
    scene alr73
    with dissolve
    M "(Time to go check and see how she is doing.)"

    M "(I can't help but think of Jessica, after meeting Alison.)"

    M "(Then Michelle, practically forces me to bring her some clothes.)"
    scene alr74
    with dissolve
    M "(Still can't believe that Gunter is dead.)"

    M "(When I find the asshole who got away, I am going to make him hurt...)"

    M "(...until I know why they were after her.)"
    scene alr75
    with dissolve
    M "(Apparently she is the daughter of some rich dude with some serious pull.)"

    M "(I have no idea what she is involved in, but my job here is almost done.)"
    scene alr76
    with dissolve
    stop music fadeout 5
    M "Excuse me."

    "Nurse" "*Hums a random tune*"

    M "Hello?!"
    scene alr77
    with vpunch
    "Nurse" "Oh! Hi, I'm sorry!"

    M "Don't worry about it, there's no need to panic."

    M "It smells lovely by the way."

    "Nurse" "Huh?!"

    M "The perfume. (Oh, brother.)"

    "Nurse" "Right, of course! Thank you."

    M "I'm here to see Alison, the doctor called for me."
    scene alr78
    with dissolve
    "Nurse" "Right. The cute and feisty one."

    "Nurse" "She is at the end of the hall, last door on the right."

    "Nurse" "Can't miss it, another officer is standing outside the door."

    M "Okay, thank you."

    M "(Cute one, yeah she is. Feisty though?)"
    scene alr79
    with dissolve
    M "(Suddenly I feel like I'm coming down with something, or is that up?)"
    scene alr80
    with dissolve
    "Hot doctor" "I can see why she would only speak with you."

    M "(Huh? I guess I'll take that as a compliment.)"

    M "Hello. You must be doctor Lin?"

    lin "Yes, and you must be [mc]."

    M "That's me."
    scene alr81
    pause(.2)
    scene alr80
    pause(.2)
    M "So, doc. What's happening with her?"

    lin "Well, where to begin."

    M "The short version, will do."
    scene alr81
    pause(.2)
    scene alr80
    pause(.2)
    lin "The young lady you brought in, she won't eat and she won't work with me."

    lin "She is crying. She is also insisting that she speaks with you."

    M "(I guess that explains the feisty part.)"

    M "Sorry, doc. I don't know what to tell you."
    scene alr81
    pause(.2)
    scene alr80
    pause(.2)
    scene alr82
    with dissolve
    lin "*Chuckles softly* I'm not blaming you or anything."

    lin "Just please go see her and help us out as much as you can."

    lin "Her father is one of our biggest benefactors, so we want to make sure she is well taken care of."

    M "I see. In that case, I'll do everything I can to help you out."
    scene alr81
    pause(.2)
    scene alr80
    pause(.2)
    scene alr82
    lin "Thank you."

    lin "Her father should be arriving in the next hour or so."

    M "Alright, doc. I'll go and see her right now."
    scene alr83
    with dissolve
    lin "Try to keep it short. She needs to rest and hopefully eat something first."

    M "Yeah, I'll try. Thanks, doc."
    scene alr84
    with dissolve
    M "(Now I understand why she is getting the VIP treatment with two guards and all.)"

    M "(I wonder who her father is and why did he fail so miserably to keep his daughter safe?)"
    scene alr85
    with dissolve
    "Random cop 98" "Oh, hello [mc]. Are you here to see the girl?"

    M "Yeah, the doc asked for me."

    "Random cop 98" "Oh, right. Sorry, she mentioned it as she went past me."

    "Random cop 98" "Go right ahead."

    M "Thanks."
    scene alr86
    with dissolve
    play sound "Rain.ogg" fadein 3
    A "*Sobs quietly* Oh, mom. How I miss you."
    play music "walkaway.ogg" fadein 3

    A "*Sniffles* Why is this happening to me?"

    M "(Oh, god. I can't take this shit.)"

    M "(Poor girl. I need to do something.)"

    M "(Here goes nothing.)"
    scene alr87
    with dissolve
    M "Hiding under that blanket will not make your troubles go away."
    scene alr88
    with dissolve
    M "Alison?"

    A "[mc]?!"
    scene alr89
    with dissolve
    A "It is you!"

    M "Yeah, it's me. The doctor called me in."

    M "She said you wanted to see me."

    A "Yes, I really need to get out of here."

    M "Your father should be here shortly. I'm sure he can get you out of here."
    scene alr90
    with dissolve
    A "(It's already too late then.)"

    M "What's the matter?"
    scene alr91
    pause(.2)
    scene alr90
    pause(.2)
    A "I need to get out of here now."

    A "Please, get me out of here."
    scene alr91
    pause(.2)
    scene alr90
    pause(.2)

    M "(She looks like she is about to start crying.)"

    M "(Is he abusive?)"
    scene alr92
    with dissolve
    "" "You sense fear in her eyes."

    M "I'm sorry, I didn't mean to frighten you."

    "" "As you were about to pull your hand away."
    scene alr93
    with dissolve
    "" "She reaches out, placing her hand on top of yours without a word."

    M "(She's trembling. What could possibly make her feel so scared?)"

    M "Alison, why do you want to get out of here?"
    scene alr94
    pause(.2)
    scene alr93
    pause(.2)
    scene alr94
    play sound "ringtone.ogg"
    M "Sorry. I have to take this."
    scene alr95
    with dissolve
    A "Okay."
    scene alr96
    with dissolve
    stop sound
    M "Hello?"

    Mls "[mc]. Just listen and do as I say. A warrant for your arrest has been issued."

    Mls "Gunter was confirmed dead by your gun and I know this was not your doing."

    Mls "All this happened the moment that girl was located."

    Mls "She is the daughter of someone with some serious pull."

    Mls "The commissioner himself called the chief. Time is up. Get out of there now."

    Mls "Swat is likely going to be on the way in the next 5 minutes or less."

    Mls "I'll meet you at {b}{i}her place.{/i}{/b}"

    M "(What the fuck was that all about? Guess Jess's old place is the safest option.)"

    M "Alison, change of plans."
    label galleryScene8:
    scene alr97
    with dissolve
    M "How would you... (Oh, fuck. Okay, let's not make her feel even worse now.)"

    M "If you want to get out of here, now is your chance."

    M "I brought some clothes as you can see. Please put them on and let's go."

    A "Okay, yes!"
    scene alr98
    with dissolve
    M "(So, she believes the girl is the source of all this.)"

    M "(Over here we have a girl whose expression suddenly changes from joy to near terror at the mention of her father.)"

    M "(And now she is more than happy to leave the hospital with me.)"
    scene alr98
    with dissolve
    M "(That could only mean one thing.)"

    M "(She escaped from home and does not wish to be found by her father.)"
    scene alr99
    with dissolve
    M "(Why did she run away from home, what is she hiding?)"

    M "(That's the question now.)"
    scene alr100
    with dissolve
    M "(I don't believe the girl is dangerous.)"

    M "(And I doubt she could kill anyone, I've looked into the eyes of killers before and she's no killer.)"
    $ renpy.end_replay()
    scene alr101
    with dissolve
    M "(Overthinking this is getting me nowhere.)"

    M "(I'll just wait and see if she'll open up to me once we are out of here.)"

    A "I'm ready."
    scene alr102
    with dissolve
    M "(Wow. She looks incredible.)"

    M "I'm glad they fit you."
    scene alr103
    with dissolve
    A "Thank you for doing this, [mc]."
    stop music fadeout 2

    M "You can thank me by explaining to me what's going on when we get out of here."
    play music "Stomachgrowl.ogg"

    A "*Blushes*"
    stop music

    M "Haha."
    scene alr104
    with dissolve
    M "That's what you get for refusing to eat."

    M "Let's get out of here. Follow my lead and try to act normal."

    M "I'll get you some food soon."

    A "Okay. (Act normal?)"
    scene alr105
    with dissolve
    "Random cop 98" "Is the girl being taken somewhere else?"

    M "Yeah, her father is expecting her downstairs with the doctor."

    M "You know how it is with daddy's who can buy the whole hospital."

    A "(How do I act normal?!)"
    scene alr106
    with dissolve
    "Random cop 98" "Okay, well, she's your responsibility now."

    M "Understood."
    scene alr107
    with dissolve
    M "Alison, don't forget to breathe."

    A "*Takes a deep breath*"

    M "There we go. Now just follow me and you'll be fine."
    scene alr108
    with dissolve
    "Nurse" "(Hmmm. Isn't that the cutie from 207?)"

    "Nurse" "(I wonder if she is being taken in for questioning or something.)"

    M "I'll need to change. First we hit the garage and then we take a cab."

    A "Okay."
    "" "A cab ride and 20 minutes later."
    scene alr109
    with dissolve
    play music "modernrock.ogg" fadein 3
    R "Look what the cat dragged in!"

    R "If it isn't \"Uncle [mc].\""
    scene alr110
    with dissolve
    M "Hey, old timer."

    R "Still a wise guy, I see."

    R "Who is that cutie behind you, and what is she doing with a guy like you?"
    scene alr111
    with dissolve
    M "Man, you never change, do you?"

    R "Change is hard and expensive, brother."
    scene alr112
    with dissolve
    M "Well, meet Alison."
    scene alr113
    with dissolve
    R "Welcome to my house, Alison."

    A "Hi. Thank you."

    R "She sure is a shy one."

    R "Listen, Alison. Don't get too attached to this guy."

    R "He is a troublemaker."
    scene alr114
    with dissolve
    M "Really? Did you just say I'm the trouble maker?!"

    R "It's too late [mc], she is already smiling."

    R "She knows I'm right."

    A "*Chuckles softly*"
    scene alr115
    with dissolve
    M "And you, I can't believe you would betray me like that."

    M "Just for that, no food for you."

    M "Little traitor."
    scene alr116
    with dissolve

    A "I'm sorry?"

    R "Hah. That's not going to work [mc]."
    stop music fadeout 3
    R "Michelle is bringing the food as we speak."
    scene alr117
    with dissolve
    play music "REAL BAD GIRL.ogg" fadein 3
    m "Ugh! You two bullies better stop that right now!"

    R "(Oh shit.)"

    M "(Busted.)"

    "Both [mc] and [R]" "He did it!"

    A "Umm."
    scene alr118
    with dissolve
    A "I'm sorry?"

    m "You poor thing. These two bullies should be sorry, not you."

    m "Grow up you two and stop playing those same old tricks on girls."

    R "Worked on you, didn't they?"

    M "Why fix it if it ain't broke."
    scene alr119
    with dissolve
    m "*In awe* A girl that blushes in this day and age! Can I keep her?!"

    M "What the?! Hey, don't threaten to keep her. She's been through enough already."

    M "You trying to give her a heart attack?"
    scene alr120
    with dissolve
    M "Alison, meet [m]. [m], Alison."

    m "Hi sweetie. By the way, you look adorable."

    A "*Blushes even more* Um. Thank you."

    R "(Well, the girl is the real deal. There is no acting involved there.)"

    m "I bet you're hungry."
    scene alr121
    with dissolve
    m "Come with me hon."

    A "Okay."

    M "I'll be right here Alison."

    A "Okay."

    R "(She is clearly struggling to socialize, but she's trying.)"
    scene alr122
    with dissolve
    R "Come over here for a sec [mc]."

    m "Right here sweetheart, have a seat."


    A "Thank you."
    scene alr123
    with dissolve
    m "(Poor thing. It breaks my heart.)"

    R "I know that look. You have already made up your mind and I've seen it before."

    M "Yeah, I have. She is no ordinary girl, I have a feeling she is involved..."

    M "...in something she has no idea how to get out of."

    R "Look, I can't deny the fact that she looks like her but you need to remember she is not Jessica."

    M "I'm not blind [R], I can see that."

    R "I'm not so sure [mc]. You just met her, and here you are fighting her wars."

    R "You need to look after yourself, also, I got some bad news on her staying here."
    scene alr124
    with dissolve
    R "What's the matter babe?"

    m "I need you to promise me [mc], promise me that you will do everything in your power..."

    m "...to help that sweet little girl."

    M "He tells me to stay out of it and now you want me to promise I do the oppossite?"

    m "Only what I say matters here hon, haven't you learned that by now?"
    scene alr125
    with vpunch
    R "She's making the face, isn't she?"

    M "Yup. She sure is."

    R "Well, I'm sorry brother. This is out of my hands now."

    R "You know I'd fight a war with you, but I can't win against that face."

    R "You're on your own."

    M "Man, you really suck."
    scene alr126
    with dissolve
    M "Alright, you have my word."

    R "You are as evil as ever, I see."

    m "Did you say something baby?"

    R "Nope, not a thing my love."

    m "That's what I thought."
    scene alr126
    with dissolve
    R "Are you sure that was a good idea?"

    m "Yes, baby. He needs this, and she needs him."

    m "Didn't you see how taken she is with him already?"

    M "Hey, Alison. Did you enjoy your burger?"
    scene alr128
    with dissolve
    A "*Blushes and smiles* Y-yes! (He is so close!)"

    M "I'm happy to hear that."

    M "Now, let's talk about where you will be staying."
    scene alr129
    with dissolve
    A "*Nods shyly*"

    M "You can stay with me, or..."

    A "I'll stay with you. Please?"

    m "*Chuckles from a distance* Ahem."

    M "(Well, that's that I suppose.)"

    M "Okay, let's get going."
    scene alr129
    with dissolve
    m "You take good care of her, you hear?"

    M "Yeah, yeah, I heard you the first time."

    R "Good luck [mc], you'll need it brother."
    scene alr130
    with dissolve

    M "*Scoffs*"

    m "I hope to see you again soon Alison. Goodbye sweetheart."

    A "Thank you [m], [R], and goodbye."
    scene alr131
    with dissolve

    M "(What a day this has been. Well, no point complaining about it.)"

    M "(I guess I'll let her rest first and then find out what the fuck is going on.)"
    scene black
    stop music fadeout 3
    "" "A cab ride and 20 minutes later."
    scene alr132
    with dissolve

    M "Here we are. Welcome to Casa del [mc]."
    play music "drivinghome.ogg" fadein 5

    scene alr133
    with dissolve

    A "(Huh?)"

    M "(And now I need to figure out what to do with her...)"

    M "(I really need to speak with Melissa, and soon.)"

    scene alr134
    with dissolve

    A "Is this your house?"

    scene alr135
    with dissolve

    M "Yes, that's what I said earlier. (No need to get into that right now.)"

    A "Oh. Okay."

    M "Lights on."

    A "What?"

    scene alr136
    with dissolve

    A "Oh, wow. So, your lights come on if you speak to them?"

    M "It's nothing special. It's almost a standard in most houses these days."

    M "But, back to your question, yes, they're voice activated."

    scene alr138
    with dissolve

    A "(Well, I didn't know.)"

    M "Let me show you around the place first."

    A "Mhm."

    scene alr139
    with dissolve

    M "This is the kitchen, obviously."

    A "(Obviously.)"

    M "Next up..."

    scene alr140
    with dissolve

    M "Your room."

    A "(Creepy creatures up there... They look scary.)"

    A "Okay."

    scene alr141
    with dissolve

    M "This is the bathroom. If you want to take a shower now or later, feel free to do so."

    A "Okay."

    M "Your face looks tired, are you a mass effect fan by any chance?"

    A "What?"

    M "Never mind. Next."

    scene alr142
    with dissolve

    A "This must be where you sleep?"

    M "Bingo!"

    M "This is my room and also where you can find some clothes to change into."

    M "You can go sit down in the living room for now while I look out some clothes for you to sleep in."

    A "Okay."

    scene alr143
    with dissolve
    stop music fadeout 3

    A "(*Sighs* What am I going to do...)"

    A "(He seems nice and all, but I don't know if I can trust him.)"

    A "(What if he turns me in for a reward or something?)"
    scene alr144
    with dissolve

    M "Are you listening to me?"

    M "(I wonder why she went quiet so suddenly.)"

    A "(Maybe I should just leave right now? But where would I go?)"

    scene alr145
    with dissolve

    M "(She looks deep in thought and possibly depressed... *Sigh*)"

    M "(I guess I'll keep the questioning light for now. She needs to rest tonight.)"

    A "(With my luck, I would probably end up in another mess... He saved my life.)"

    scene alr146
    with dissolve

    A "(Perhaps I should try trusting him? Oh, what other choice do you have!)"

    M "Hey, are you okay?"

    scene alr147
    with dissolve

    A "*Startled* Y-yeah... I uh, I'm fine."

    A "I'm sorry, I was just thinking."

    M "Yeah, that much is obvious. The question is, what has you so worked up."

    scene alr148
    with dissolve

    menu:
        "You can trust me, you know?":
            jump ShouldItrusthim
        "Leave her be for now.":
            jump LeaveMeBe






label ShouldItrusthim:

    A "*Gasps* (Is he a mind reader? No way... I guess he's just good at his job.)"

    A "(Maybe that's another reason to trust him?)"

    A "I'm sorry I don't mean to be ungrateful, especially after everything you've done."

    M "I don't expect you to trust me overnight, just don't do anything rash is all I ask."

    scene alr149
    with dissolve
label LeaveMeBe:

    A "Um..."

    M "Listen, Alison. Honestly, I was going to take you to a shelter and move on with my life."

    M "I have had my share of trouble, enough of it to last three lifetimes..."

    M "But, when I saw how scared you were, I just couldn't bring myself to leave you alone."

    M "So, if anything, trust that I mean you no harm and that I only wish to protect you."

    A "(Protect me?)"

    M "Now come with me, I want to show you where you can change before bedtime."


    scene alr150
    with dissolve

    A "(I guess I have no choice but to trust him, for now at least.)"

    M "Feel free to try out some of the stuff, I'm sure you'll find something."

    A "Okay, thank you [mc]."

    scene alr151
    with dissolve

    M "And here we go."

    M "Someone... Someone I used to know left these here."

    M "She won't be needing them anymore."

    scene alr152
    with dissolve

    A "(He sounded so sad saying that... I wonder who that person was.)"

    M "I'll wait for you in the living room."

    A "Okay."

    scene alr153
    with dissolve

    M "(Man, what the fuck am I going to do with her?)"

    M "(Melissa better have a flawless explanation for why I'm being set up like this.)"

    M "(She looks like a great kid, but man is she troubled.)"

    scene alr154
    pause(.2)
    scene alr153

    M "(I really don't need this shit right now, I've had enough of women in trouble.)"

    "" "You sigh deeply, realizing that the source of your anger is a certain missing redhead."

    M "(She reminds me so much of her... Is that why I decided to help her?)"

    M "(I don't even know anymore... Fuck it, what's done is done.)"

    scene alr155
    with dissolve

    A "Um."

    M "Hey. You look good, I mean those look good on you."

    A "Thank you."

    scene alr156
    with flash

    j "Thank you baby."

    M "Jessica?!"

    scene alr157
    with dissolve

    A "(He is staring! Oh my god, I am so nervous, what do I do?!)"

    M "(Fuck. This is messing with my head.)"

    M "Sorry, I'm tired, don't mind me."

    scene alr158
    with dissolve

    A "Okay. (Jessica? Is that the person he was so sad over?)"

    M "Yes?"

    A "Um... You called me Je- never mind, it's nothing, sorry."

    M "(It's probably a good idea to just leave it at that for now.)"

    M "Right. I have a few questions for you, Alison. Let's take a seat."

    scene alr159
    with dissolve

    A "Did I do something wrong?"

    M "No. So stop looking so worried already."

    M "I just want to ask you some questions."

    scene alr160
    with dissolve

    A "(I thought I made him angry for a moment there.)"

    M "Why were those two after you, I mean really, why?"

    scene alr161
    pause(.2)
    scene alr160

    A "(What do I do, what do I do?)"

    scene alr162
    with dissolve

    A "My father paid them I believe. He has people hunting for me."

    M "But why? Did you do something, or is there something you're not telling me?"

    M "Look I need to know what is going on in order to help you."

    M "I can't help you if you won't tell me what the problem is."

    scene alr163
    with dissolve

    M "(And she pouts... Fuck my life.)"

    M "You really don't want to talk about any of this, do you?"

    scene alr164
    with dissolve

    A "(No, not really.)"

    M "(She looks even more depressed than before. Best not to push her any further.)"

    M "Okay. That's enough with the questions for tonight..."

    M "I think some rest will do you good."

    scene alr165
    with dissolve

    M "I'll go change and prepare your room."

    A "*Sighs relieved*"

    scene alr166
    with dissolve

    M "(I can't fucking believe how badly my mind is fucking with me.)"

    M "(After all these years I see her face clearly once more.)"

    M "(This girl may be more than I can handle, I think it's best I just hand her over to Melissa.)"

    scene black
    "" "While you were changing, the troubled girl had fallen asleep..."

    scene alr167
    with dissolve

    "" "On the floor of all places."

    scene alr168
    with dissolve

    M "Alison?"

    scene alr169
    with dissolve
    play music "Quiet.ogg" fadein 5

    M "(I can't even imagine what she must have gone through.)"

    scene alr170
    with dissolve

    M "(More like you don't want to imagine what she has gone through...)"

    M "(If you're going to be a fucking coward at least be an honest one, [mc].)"

    M "(Fuck!)"

    scene alr171
    with dissolve

    M "(You don't need this [mc]...)"

    scene alr156
    with flash
    pause(1)

    scene alr172
    with dissolve

    "" "Anger and frasturation continues to build up within you, as you struggle with the image in front of you."

    M "(Just take her to her room [mc]. That's all you need to do, it's just for one night.)"

    M "(Tomorrow you let Melissa handle this. She is a great cop and soon to be a fine detective.)"

    "" "Yes, just let someone else handle it, you don't need this."

    scene alr173
    with dissolve

    M "(She'll take care of her better than you can.)"

    M "(Yeah... She will take care of you better than I ever could.)"

    "" "You've already failed her once..."

    M "(That's right, I did. And I don't want to go through that again.)"

    "" "Coward."



    scene alr186
    with flash

    j "You know, every single time I ask you to stay with me, you find some excuse."

    j "I'm starting to think you love your job and your cause more than me and this baby."

    M "Baby? Wait, you mean to tell me..."

    scene alr174
    with dissolve

    M "(No, no, no. We're not doing that [mc]. We are not going down that path tonight.)"

    M "(I knew this girl would be trouble from the moment I laid eyes on her.)"

    "" "You sigh deeply."

    scene alr175
    with dissolve

    M "(Well, it's just one night... What else could go wrong?)"

    scene alr176
    with dissolve

    A "I love you mom."

    "" "You shrug."

    M "(I am not your mom... Jesus Christ, this girl is killing me.)"

    M "(I need to get out of here.)"


    scene alr177
    with dissolve

    M "Man, what a fucking night this turned out to be."

    M "(More like a nightmare!)"

    "" "Frustrated you growl and decide to go to bed."

    scene alr178
    with dissolve

    M "(Am I avoiding responsibility once again, or am I doing the right thing for once?)"

    M "(I don't even know what the right fucking thing is anymore!)"

    scene alr179
    with dissolve

    M "(I should try to get some sleep.)"

    M "(Maybe Melissa has some answers...)"

    scene black
    with fade

    "" "You finally fall asleep, and the dreams you had nearly forgotten, return once again."
    stop music fadeout 4
    label galleryScene14:
    scene alr180
    with dissolve

    "" "Nearly 5 years ago... Happier times, happier you and {i}her{/i}"

    j "Baby?!"

    scene alr181
    with dissolve

    play music "nexus.ogg" fadein 4

    M "Kitten!"

    j "Oh, my god! [mc]! Baby, you're back!"

    scene alr182
    with vpunch

    j "Mwah, mwah, mwah, mwah."

    M "Ummmm!"

    j "Mwah! Oh, I'm sorry, I forgot you need to breathe sometimes."

    scene alr183
    with dissolve

    M "Hahaha. Yeah, I do need to breathe sometimes."

    M "Now, why exactly were you naked?"

    M "It's not as if you knew I was coming today, did you?"

    j "Well, no... But, you know."

    scene alr184
    with vpunch

    M "No, I do not know."

    j "*Moans* A girl needs to take care of her urges too. I was just about to play with BoB."

    M "I see... Well, seeing as you are already naked..."

    j "Just put it in already and stop talking!"

    scene alr185
    with dissolve

    M "My, my... Somebody sure is feisty today."

    j "I'm sorry baby. Please put your cock inside me?"

    M "That's a little bit better."

    scene alr184
    with dissolve
    pause(.5)
    scene alr185
    pause(.5)

    j "Please daddy, put your big fat cock inside my tight little pussy."

    scene alr186
    with dissolve

    M "Okay, you win!"

    j "I had no doubts... Today is a special day for me."

    j "I want you to become a real daddy."

    M "Wait, you mean?!"

    M "Are you serious?"

    j "Yes, and today is the perfect day for it... It's as if it was meant to be."

    M "Look..."

    scene alr187
    with dissolve

    j "*Pouts*"

    M "Oh, man."

    M "Okay baby... whatever you want."

    scene alr186
    with dissolve

    j "You are the only one for me [mc]!"

    j "It's time for you to give me a baby."

    M "Yes ma'am!"

    show jessimation

    j "Oh, baby. I missed you so much."

    j "*Moans* Oh, god, yes! Fuck me baby!"

    M "Wow, you sure did miss me, huh? You're going to make me cum even quicker than I thought."

    M "Your pussy is so freaking tight right now I'm losing my mind."

    j "It's okay baby. You can cum inside me as many times as you can handle."

    M "I bet that's what you want."

    j "Yes! Now just fuck me and fill me with your seed!"

    M "I'm starting to feel like a field plower."

    j "Stop complaining and plow my tight little field!"

    M "You are so going to pay for this..."

    M "I swear, that little ass of yours, will suffer later."

    j "Oh, fuck! Yes, yes, yes! Fuck me baby, and once you cum inside my pussy, my ass is yours."

    M "Oh, fuck! You know just what to say don't you? You are such a bad girl."

    j "Aaaaah! *Moans* Yes, I've been a very bad girl! Punish me daddy, please!"

    M "Oh, fuck I'm gonna cum if you keep squeezing my dick like that."

    j "Cum for me daddy, please cum inside me, I want to feel it."

    j "Oh, god I have really missed you."

    menu:
        "Nut inside her now.":
            jump letsNutInside
        "Keep plowing her field.":

            jump FucksomEmore

label letsNutInside:
    show jessimation2

    j "Oh, yes! I can feel your cock throbbing inside me!"

    j "Fuck me daddy, fuck me! I want your cream inside me."

    j "Please don't waste a single drop of it. Fill me up and shove it deep!"

    j "Cum for me baby, please cum for me... Oh, god you are breaking my mind!"

    scene alr188nut
    with vpunch
    pause(1)
    scene alr188nut
    with flash
    pause(.5)
    scene alr188nut
    with flash
    j "*Unintelligible nonsense*"

    M "Oh, fuck! I came so hard I think I broke you."

    M "That look suits you though."

    M "I think I should pin you down in this state and hammer you for the rest of the day."

    j "Yesh, ah, ah... *Moans*"

    A "Noooo! Leave me alone!"
    $ renpy.end_replay()
    scene alr189
    with dissolve
    stop music fadeout 3

    M "(Oh, fuck me!)"

    M "(I guess she's having a nightmare?)"

    M "(The question is, what do I do? Should I go and check on her, or just leave her be?)"

    menu:
        "Leave her be, or go check on her?"
        "Leaving her to suffer through it, is almost criminal (Go to her.)":

            jump GoCheckOnAlisonsNightMare
        "I don't need this. (Don't go.)":

            jump LetHerSufferCoward


label FucksomEmore:
    show jessimation
    "" "Hit H to hide text and watch the loop. Click again to continue and end the loop."
    menu:
        "Ready yet?"
        "Yes, I want to nut now!":

            jump letsNutInside
        "No, I want to plow some more!":
            jump FucksomEmore







label GoCheckOnAlisonsNightMare:
    scene alr189

    M "(If I was going to let her deal with her own nightmares...)"

    M "(I should have left her at that hospital then.)"

    M "(Time to be honest with yourself [mc].)"
    jump AlisonsNigHtMarE

label LetHerSufferCoward:
    scene alr189

    M "(I don't want to get involved any more than I already am.)"

    "" "That's right, you don't need this... You couldn't handle it then, and you can't now."

    M "(I don't give a fuck about what you think.)"

    M "(Great, I am back to talking to myself.)"

    M "(Fuck... What am I doing? Regardless of how I feel, this is cruel.)"

    M "(She doesn't deserve this.)"

label AlisonsNigHtMarE:
    scene alr190
    with dissolve
    play sound "distantthunder03.ogg"

    M "Alison?"

    play music "rainwindow02.ogg" fadein 3

    "" "You whisper her name as you enter the room."

    M "(Man, she's on the floor again.)"

    M "(Well, here goes nothing.)"

    "" "As you make your way towards her..."
    scene alr191
    with dissolve

    A "Why do I have to stay in here, Mom?"

    A "Have I done something wrong?"

    "" "You hear her talking to herself and start to understand just how damaged this girl truly is."

    scene alr192
    with dissolve

    M "(What the hell have they done to her?)"

    M "(Well, I'll put you on that bed as many times as it takes, until you stay there!)"

    scene alr193
    with dissolve

    "" "Determined to put an end to her sleeping on the floor habit, you pick her up gently."

    A "Please, don't put me in the cage again *sobs*"

    M "(Cage?)"

    "" "You feel an overwhelming anger take over you, briefly."

    M "I'm not putting you in any cage, Alison."

    M "I'm going to put you on your bed. You'll be safe here, I promise."

    scene alr194
    with dissolve

    A "You promise?"
    menu:
        "Repeat it.":
            scene alr194
            "" "Overwhelmed by emotions, you briefly let you guard down and answer her honestly."

            M "I promise. I'll make sure you're safe. No one will ever hurt you again."

            scene alr195
            with dissolve

            "" "You can see a smile on her face as she closes her eyes once more."
            jump PlaceHerOnThatbed
        "Just stay quiet.":
            scene alr194

            M "(She is talking to herself, I'll just leave her be.)"

            "" "You decide to just put her on the bed instead."

label PlaceHerOnThatbed:
    scene alr196
    with dissolve

    M "(Well, she calmed down at least.)"

    M "(I should probably stay with her... In case she has another nightmare.)"

    scene alr197
    with dissolve

    "" "As you sat there trying to figure out what to do... Her hand touches you."

    M "(Huh?)"

    "" "She starts mumbling again in her sleep... Something about hating thunder."

    M "(Fuck my life.)"

    menu:
        "Do you hold her hand?"
        "Hold her hand through the night.":


            scene alr198
            with dissolve

            M "I'm right here, kitten."

            M "(Kitten? Man, get your head screwed on right.)"

            scene black
            stop music fadeout 5

            "" "As you dozed off for a few hours, the rain had stopped and the sun was up."

            scene alr199
            with dissolve

            "" "The first thing you noticed was her hand still firmly holding onto yours."

            "" "And a smile on her face."

            M "(Well, what do you know... She can smile.)"

            scene alr200
            with dissolve

            "" "You greet her with a smile as she seems to be waking up."

            M "Good morning."

            scene alr201
            with dissolve

            A "*Surprised gasp* [mc]?"

            A "(He is holding my hand! Was he here the whole night?!)"

            scene alr202
            with dissolve

            "" "Partly embarrassed, partly guilty, she pulls her hand away swiftly."

            label IstaredTheWholeNight:
                scene alr202

            A "Um... Good morning. Were you here the whole night?"

            M "Well, most of the night at least."

            scene alr203
            with dissolve

            A "Please forgive me, I am so sorry."

            M "Calm down. You didn't force me to be here."

            M "I just heard your voice and came to check on you."

            scene alr204
            with dissolve

            A "*Smiles brightly* (He came to check on me?)"

            A "(I feel bad for making him sleep there...)"

            A "(But I am very grateful.)"

            scene alr205
            pause(.5)
            scene alr204

            M "You snore by the way."

            scene alr203
            with dissolve

            A "W-what?!"

            M "I'm just messing with you."

            scene alr204
            with dissolve

            A "Haha. I see."

            M "(Progress was made... She actually laughed, for a moment, but still counts.)"

            M "How about some breakfast?"

            A "Yes, please!"

            M "Okay, I'll go get things started while you wake up."

            A "Okay."
            jump BreakFasttime
        "Nah, I'll just sit here and stare.":
            scene alr194
            stop music fadeout 3
            scene black
            "" "You fell asleep for a few hours and awoke to find her talking to you."
            jump IstaredTheWholeNight

label BreakFasttime:
    scene alr206
    with dissolve

    "" "Feeling a little better today, you decided to impress her with your master-dish."

    "" "Bacon and eggs, nothing is better... At least that's what you tell yourself."
    scene alr207
    with dissolve

    M "(Hmmm. I haven't cooked for myself in awhile...)"

    M "(But, thankfully, these eggs are still good.)"

    M "(Time for some bacon and eggs then.)"

    scene alr208
    with dissolve

    "" "Without realizing it, you had began to whistle this morning."

    "" "Something you used to do once upon a time."

    scene alr209
    with dissolve

    M "(Well, what do you know... Here I am whistling again.)"

    M "(What is wrong with me today? Or is it what is right with me today?)"

    "" "While you were busy trying to decide what to name todays condition..."

    "" "Alison came in."

    scene alr210
    with dissolve

    A "*Softly* [mc]?"

    M "Yes, kitten?"

    scene alr211
    with dissolve

    A "(Kitten?)"

    M "I mean, Alison. Sorry, I-"

    A "It's okay, really. You don't need to apologize."

    A "I actually like it."
    scene alr212
    with dissolve

    M "(Well, thanks for the save.)"

    "" "Realizing what she had just admitted to, she began to blush and shy away."

    M "(She looks cute when she get's all shy. Focus, [mc], focus.)"

    M "What did you want Alison?"

    scene alr213
    with dissolve

    A "Can I take a shower, please?"

    M "Of course. Go right ahead, just don't drown in there, okay?"

    A "I won't. Thank you."
    scene alr214
    with dissolve

    M "(She actually took that drowning part seriously.)"

    "" "You softly facepalm."

    scene black

    "" "While you were playing chef in the kitchen, she was headed for the shower."

    scene alr215
    with dissolve

    A "(I can't even remember the last time I had a real shower.)"

    A "(Between that and how nice he has been to me...)"
    label galleryScene9:
    scene alr216
    with dissolve

    A "(This is really starting to feel good.)"

    A "(But I shouldn't let my guard down. Everyone starts nice.)"

    scene alr217
    with dissolve

    A "(I wonder how Caroline is doing.)"

    scene black
    "" "Meanwhile back at the Chef Rams-It kitchen."

    scene alr218
    with dissolve

    M "Those look \"fucking delicious\""

    M "(This was always her favorite.)"

    M "..."

    scene alr219
    with dissolve

    M "(I should go and check on her, she's been gone for over 20 minutes.)"

    scene alr220
    with dissolve

    play music "Frank Nora.ogg" fadein 5

    A "Hahaha. Mmmm."

    A "This is so good!"

    scene alr221
    with dissolve

    M "(What is she doing?)"
    menu:
        "Look and see?"
        "I should make sure she is okay. (Look)":

            scene alr222
            with dissolve

            M "(Wow! Okay, I didn't expect that.)"

            M "(Well, I did, but not that kind of... Oh, just fucking stop.)"

            scene alr222
            with dissolve

            "" "She is humming a song softly while playing in the shower."

            scene alr223
            with dissolve

            A "*Giggles*"

            M "(Did she just giggle? Who does that for just a shower?)"

            M "(I am really starting to worry about her.)"

            M "(I should probably say something, she'll-)"

            scene alr224
            with dissolve

            "" "Before you could finish your thought, she was staring right at you."

            M "l... *Ahem* I was worried about you, it's been almost half an hour."

            M "Uhh... Breakfast's ready."
            $ renpy.end_replay()
            scene black

            "" "With that said, you turned tail and fled back to the kitchen."
            stop music fadeout 4

            label IgaveHerPrivatesPrivacy:
                scene alr225
                with dissolve
            M "(Melissa should be on her way soon. With her here she might open up some more.)"

            scene alr226
            with dissolve
            play music "Follow_The_Shadows.ogg" fadein 5

            "" "While you were lost in thought, Alison was making her way towards you."

            "" "And for the first time in years... You used the words."

            scene alr227

            M "Sweet baby Jesus."

            A "I hope you don't mind me wearing these."

            "" "Mentally slapping yourself back to reality, you replied."

            M "No, I don't mind at all. I'm glad you decided to use them to be honest."

            scene alr228

            A "I'm sorry I took so long in the shower, I won't do it again, I promise."

            M "What? No, no... It's not like that. I wasn't upset over the shower duration."

            M "I was worried about you is all."

            M "And I'm sorry for coming in like that... I don't usually have people in the house with me."

            scene alr229
            pause(.2)
            scene alr228

            A "It's okay, I'm used to it."

            scene alr229
            pause(.2)
            scene alr228

            M "(Used to it?) Okay, I'll just leave it at that for now."

            scene alr230
            with dissolve

            A "Thank you for being so considerate and for not asking."

            M "(Well, I do still remember a thing or two about women, you know?)"

            M "You're welcome. Now how about some food?"

            jump LetseatbaconNEGgS
        "I think I'll give her some privacy.":


            scene alr221

            M "Alison, are you done in there?"

            A "Oh, yes, sorry!"

            M "Your breakfast's going to get cold, you've been in there almost half an hour."

            A "Okay, sorry, I'm coming."
            jump IgaveHerPrivatesPrivacy

label LetseatbaconNEGgS:
    scene alr231
    with dissolve

    A "Yes, I'm starving!"

    A "Is that bacon?!"

    scene alr232
    with dissolve

    M "(Well, what do you know?)"

    M "(She likes bacon as well... Heh, fate is such a cruel mistress.)"
    scene alr233
    with dissolve

    M "You're looking at me and I'm trying to figure out why?"

    M "(Is she waiting for me to eat?)"

    scene alr234
    with dissolve

    A "Can I eat?"

    M "(Okay, that did just happen... Now keep calm and focus on her for now.)"

    M "I don't know what customs you had at your home, and I don't want to know right now."

    scene alr235
    with dissolve

    M "But here, you can eat as much as you want, whenever you want."

    scene alr236
    with dissolve

    M "Now here's your fork."

    A "Um... Is this really all mine?"

    M "(Oh my fucking god... Is she for real? Yeah, her shaky hand says she is.)"

    M "Alison, no one will punish you for eating, or for not eating."

    M "It's all yours. Eat as slow or as fast as you like."

    scene alr237
    with dissolve

    M "My friend, you know the one who called to warn us?"
    stop music fadeout 3

    A "Yes?"

    M "Well, she's coming over sometime today."

    M "Don't get nervous, she is, as I've told you, a really good person and a close friend."

    play sound "doorbell.ogg"

    M "That's probably her now."

    M "She will not turn you in or hurt you. She just wants to help you."

    A "Okay."

    M "I'll clean this up and go get that."

    scene black
    with dissolve
    play sound "doorbell.ogg"

    A "I'll come with you."
    scene alr238
    with dissolve

    M "She is so impatient. Ugh!"

    M "I'm coming!"
    scene alr239
    with dissolve
    play music "Summertime.mp3" fadein 4


    Mls "I've got a key, you know?!"

    Mls "(What the hell were they doing in there?)"

    scene alr240
    with dissolve

    M "Then why did you keep ringing?!"

    scene alr241
    with dissolve

    A "I think I'll stay here."

    M "Sure."

    scene alr242
    with dissolve

    Mls "(So that's her, is it?)"

    M "Hello?"

    scene alr243
    with hpunch

    Mls "Think fast old man!"

    M "Too slow."

    A "*Gasp*"

    scene alr244
    with dissolve

    A "Why is she trying to hurt you?!"

    M "See what you've done now?"

    M "She is just being silly, Alison."

    Mls "Silly, moi? I am hurt."

    scene alr245
    with dissolve

    M "She's not trying to hurt me. Are you, silly [Mls]?"

    Mls "Well, technically I was trying to kick you in the face."

    A "Um... She just admitted to wanting to hurt you."

    scene alr246
    with dissolve

    M "Quit being cute and stop confusing her."

    M "She acts like this most of the time, Alison."

    M "She is having a hard time getting over the fact that she can never land a hit on me."

    M "Ever. Isn't that so, rookie?"

    scene alr247
    with dissolve

    Mls "We shall see about that, Dorkface, and I'm not a rookie anymore!"

    A "A rookie?"

    M "Yeah."

    M "Imagine a silly red-headed girl, wanting to become a cop."

    M "That's [Mls], the rookie."

    Mls "Hey, don't ignore me!"

    scene alr248
    with dissolve

    M "Just sit down already, and get serious."

    A "(So, she doesn't want to hurt him. She is just playing... I think I get it now.)"

    scene alr249
    with dissolve

    Mls "(He is trying to act all cool, but I can tell something is different since the last time we spoke.)"

    M "So, are you just going to sit there, or are you going to tell me what is going on?"

    A "(I hope this doesn't mean she is here to take me away.)"

    scene alr250
    with dissolve

    Mls "Things are much worse than I thought. But, we need to talk alone."

    M "Why?"
    scene alr251
    pause(.2)
    scene alr250
    pause(.2)

    Mls "Because."

    scene alr252
    with dissolve

    M "Fine."

    Mls "Hey, Alison. I'm sorry, but can you please go to the other room for now?"

    A "Oh, okay."

    scene alr253
    with dissolve

    M "I'm not going anywhere, so don't look so worried."

    M "She just needs to talk to me about police business, that's all, okay?"

    A "Okay."

    scene alr254
    with dissolve

    A "(Please don't send me away.)"

    Mls "(Interesting... She barely knows him, but she obeys him without hesitation.)"


    scene alr255
    with dissolve

    A "(He promised. Will he keep his word?)"

    scene alr256
    with dissolve

    Mls "(Yikes. He looks like he wants to choke me or something.)"

    scene alr257
    with dissolve

    Mls "(I guess he really does see something of her in that girl.)"

    Mls "(This is going to be harder than I thought.)"

    M "What?!"
    stop music fadeout 4

    scene alr258
    with dissolve

    Mls "I'm just worried about you, is all."

    M "Worried about me? What for?"

    Mls "Let's see."

    scene alr259
    with dissolve

    Mls "You are being blamed for murdering your partner."

    scene alr262
    with dissolve

    A "(But he didn't do it! I was there... I saw that evil man shoot him.)"

    Mls "Kidnapping the daughter of someone who can buy NYC, literally, mind you."

    scene alr263
    pause(.2)
    scene alr262
    pause(.2)

    A "(He didn't kidnap me... He saved me. She is telling him lies!)"

    A "(Why would his friend lie to him? Is she saying my father told them this?)"

    scene alr263
    pause(.2)
    scene alr262
    pause(.2)

    M "That is bullshit, and you know it."

    scene alr260
    with dissolve

    Mls "Well, maybe so..."

    Mls "However, the rumored bounty that he just put on your head, is going to get people looking hard."

    Mls "Also, she is apparently carrying a military grade top secret weapon, that is so dangerous..."

    Mls "... it can cripple the entire country, if she were to be captured by another nation."

    scene alr261
    pause(.2)
    scene alr260
    pause(.2)

    A "(What?! What weapon?! I didn't steal nothing!)"

    M "(Hmmm. She was very quiet and did not want to talk about anything at all.)"

    M "(Could this really be something a girl like her could be hiding?)"

    M "You saw her. Did she look like some evil mastermind out to bring down the country to you?"

    scene alr259
    with dissolve

    M "Like someone who was hiding a lethal weapon in her pocket?"

    Mls "All I saw was a frightened young girl, who is using you as her bodyguard."

    Mls "I'm not blaming her at all. Just pointing out the obvious."

    scene alr258
    with dissolve

    M "Are you upset that I've decided to help this girl?"

    M "Or do you truly believe all the bullshit her rich father is selling?"

    Mls "I am not upset, [mc]. I am concerned. Concerned about you."

    scene alr260
    with dissolve

    Mls "I remember what you went through after Jessica."

    M "Please, don't."

    Mls "So, you know something I don't know then?"

    scene alr261
    pause(.2)
    scene alr260
    pause(.2)

    M "Yes."

    scene alr259
    with dissolve

    Mls "I'm all ears."

    M "I believe that she needs our help. Regardless of what you may feel or think..."

    M "I am convinced that she is truly scared, and for a very good reason."

    scene alr258
    with dissolve

    M "I have seen fear in her eyes, the likes you only see when one has been faced with death, or worse."

    M "I don't really know what scares her so much, but while she was here, that fear was all but gone..."

    M "Until you showed up."

    scene alr260
    with dissolve

    Mls "Please tell me you at least had second thoughts."

    M "I had seconds, and thirds, but that girl is being honest about one thing..."

    scene alr259
    with dissolve

    M "... she is terrified of being sent back to her father."

    M "She sleeps on the floor, she has nightmares, and she speaks of cages..."

    Mls "Cages?"

    scene alr260
    with dissolve

    M "Yes. The kind you lock slaves and or animals in."

    Mls "Well, he is a rich and very powerful man, who knows what his kind does for fun."

    M "Now, Is there anything I should know, besides your concern and his bullshit?"

    scene alr260
    with dissolve

    Mls "*Sighs* He's the kind of rich and powerful that can end your life as well as mine in the middle of the day [mc]."

    M "I heard you the first time. I don't give a fuck about how rich and or powerful he thinks he is..."

    scene alr261
    pause(.2)
    scene alr260
    pause(.2)

    M "If she says she won't go back, she doesn't have to go back."

    M "You don't have to get involved in this at all, you know?"

    Mls "And what if she is just a spoiled princess who ran away from home, because daddy wouldn't buy her a sky-rise?"

    scene alr262
    with dissolve

    A "*Sad face* (I am not spoiled.)"

    A "(He believes me... He really does believe me! But what if she convinces him otherwise?)"

    scene alr263
    pause(.2)
    scene alr262
    pause(.2)

    M "I am certain that is not the case."

    Mls "Certain? Enough to risk your life, and mine?"

    Mls "Because I'm not staying out of this, and you know it."

    scene alr258
    with dissolve

    M "Yes."

    Mls "*Sighs deeply* [mc]... Are you sure that you are not letting the memory of Jes-"

    M "Don't. Don't you dare ask me that. Not you."

    scene alr260
    with dissolve

    Mls "Fuck! Okay."

    Mls "I'm sorry, okay?"

    Mls "I just don't want you to throw away everything we have worked so hard to build all of these years."

    scene alr261
    pause(.2)
    scene alr260
    pause(.2)

    M "As am I. I didn't mean to get angry with you. You know how much you mean to me."

    Mls "I know, I know. Why do you think I am here?"

    Mls "Can I at least have a go at her? I promise to be as gentle as I can."

    scene alr260
    pause(.2)
    scene alr261
    pause(.2)

    M "Fine. But I'm stepping in, the second I feel you've gone too far, or she has had enough."

    Mls "Such a softie. That will be the end of you one day, you know that don't you, old man?"

    scene alr260
    with dissolve

    M "Heh. I'm soft only where necessary, you are living proof of that, after all."

    Mls "*Smirks*"

    scene alr262
    with dissolve

    A "(Is she coming to talk to me? I should get out of here.)"

    Mls "Okay. I'll try to go easy on her, I promise."

    scene alr264
    with dissolve

    Mls "I need to see what you see in her, for myself."

    scene alr265
    with dissolve

    M "(I guess she heard everything, didn't she? I'm sorry Alison.)"

    M "([Mls] is going to be a big help in keeping you safe, so please convince her.)"

    scene alr266
    with dissolve

    A "(He is risking everything to help me... Maybe I should just tell her to take me back?)"

    A "(I can't put him through this for someone like me.)"

    scene alr267
    with dissolve

    Mls "(I fucking hate this job at times like this. I'm sorry, Alison.)"

    scene alr268
    with dissolve

    Mls "(I promise I'll make it up to you.)"

    scene alr269
    with dissolve

    A "(I'll just go back. I don't want him to get hurt because of me.)"

    scene alr270
    with dissolve

    Mls "I need to ask you a few questions, so be honest with me."

    A "I heard you."

    scene alr271
    with dissolve

    Mls "(Good. Then this will be a lot easier.)"

    scene alr272
    with dissolve

    Mls "Did you run away from home and got yourself in trouble afterwards?"

    scene alr273
    with dissolve

    A "Yes."

    Mls "Did you steal something from your father before leaving?"

    scene alr274
    pause(.2)
    scene alr273
    pause(.2)

    A "Yes."

    scene alr275
    with dissolve

    Mls "(What the hell is she doing?! Why is she lying to me?)"

    Mls "(Hold on a minute... Is she doing this because... Oh, you poor thing.)"

    A "Just take me back to my father. I am sorry for all the trouble."

    scene alr277
    pause(.2)
    scene alr275
    pause(.2)

    Mls "So you admit that you ran away from home, stole something important, got into trouble..."

    Mls "... and then got rescued by my friend, who was at the time on patrol in the area?"

    A "Yes. Also, he didn't kill his partner and he didn't kidnap me, I asked him to take me."

    scene alr278
    with dissolve

    Mls "Are you willing to testify on everything you have told me?"

    A "If it means [mc] will not be in trouble, yes."

    scene alr279
    pause(.2)
    scene alr278
    pause(.2)

    Mls "You wouldn't be telling lies just to protect him, would you?"

    scene alr280
    with dissolve

    A "(Yes I would.)"

    Mls "(I just want to hug you. You sweet little thing...)"

    Mls "(Barely know him, and already willing to lie for him.)"

    Mls "(I suppose time to take this all the way, and see how he reacts.)"

    Mls "Stop lying to me! I'll just take you to your father right this minute!"

    scene alr281
    with dissolve

    A "I'm not! He didn't kill his partner, and he did not kidnap me!"

    A "He has been nothing but nice to me, unlike you!"

    M "That's enough!"

    scene alr282
    with dissolve

    Mls "(Just as I feared.)"

    Mls "(Eeeeek! He looks really mad though, did I overdo it?)"

    scene alr283
    with dissolve

    M "This interrogation, is over. You are done, Melissa."

    Mls "Yes, okay!"

    A "*Sniffles*"

    scene alr284
    with vpunch

    Mls "Ouch! (She sure is a big girl, ooow my poor toes.)"

    play music "goodgirl.mp3" fadein 5

    scene alr285
    with dissolve

    M "Hey."

    A "I'm sorry!"

    Mls "Ow, ow, ow."

    scene alr286
    with hpunch

    M "(What is going on with her?)"

    Mls "(D-awwww. I'm so sorry.)"

    scene alr287
    with dissolve

    A "I'm sorry! I'm sorry!"

    A "I didn't want to lie, but she was saying you did all those terrible things!"

    A "This is all my fault! Please just send me back... I don't want you to get hurt. *Sniffle*"

    scene alr288
    with dissolve

    Mls "*Sniffles* (This is more than just a scared girl falling for her saviour...)"

    Mls "(I don't know why exactly, but she clearly feels safe around him.)"

    Mls "(I'm still confused but I am, at least, convinced that she's not some spoiled princess.)"

    M "(What the fuck just happened?)"

    scene alr289
    with dissolve

    Mls "(I've not seen him look so confused since our first year together.)"

    Mls "(I guess he's still rescuing lost causes.)"

    Mls "(You'll never change, will you [mc]?)"

    M "Hey, Alison?"

    A "*Sobs*"

    M "Shhhh. You don't have to worry about me or the mean lady, okay?"

    scene alr290
    with dissolve

    Mls "Hmmph!"

    M "She was just trying to get to know who you are, that's how she does things."

    M "She wanted to make sure you were not just a spoiled rich girl causing problems for fun."

    scene alr291
    with dissolve

    M "She won't take you away, and she will never again question you like that."

    M "Because now, she knows I was telling her the truth about you."

    M "You are a good girl, who needs our help."

    scene alr292
    pause(.2)
    scene alr291
    pause(.2)

    A "*Sniffles* So, can I stay with you, please?"

    M "Sure... If that's what you want."

    M "But if you want to go somewhere else, she will get you there, safely."

    A "No, no!"

    scene alr293
    with dissolve

    Mls "*Points and laughs* (Nice try. She's already attached to you. Like a lost little puppy.)"

    Mls "*Whispers* Good luck, you're gonna need it."

    M "(Is she already seeing me as her only safe harbor?)"

    M "You can stay with me until we figure out a permanent solution, okay?"

    A "Okay."

    scene alr294
    with dissolve

    M "There, there. Shhhh. You don't need to worry about anything anymore."

    M "I promise, I will make sure that you are safe, no matter what."

    "" "She hugs you even tighter as you speak the words."

    M "How about we send the evil lady on her way?"

    A "Okay!"

    Mls "Hahahaha! Fine!"

    scene black
    with dissolve

    "" "A few seconds later."

    scene alr295
    with dissolve

    Mls "*Whispers* So, she was totally telling me lies, apparently she overheard us."

    Mls "I think you know what this means, don't you?"

    M "I think I have a pretty good idea, yes."

    scene alr296
    with dissolve

    Mls "Well, let me spell it out for you. She's attached to you now, genius."

    Mls "Which means, she is not going to feel safe anywhere unless you are there."

    Mls "Do you understand me? I've seen this before and it's not easy to deal with."

    scene alr295
    with dissolve

    M "I'll be fine. You know all too well that I can't entrust her to anyone else at this point."

    Mls "*Growls* Yeah, I wonder why?! Oh, right."

    M "Quit being a smart-ass and be careful out there, I may have put you in danger."

    scene alr297
    with dissolve

    Mls "Hah! Danger is my middle name! [Mls] Danger Marconi!"

    Mls "Bye, Alison pouty face! I'll bring you lots and lots of ice cream next time, I promise!"

    M "Oh, brother."

    A "Ice cream?!"

    scene alr298
    with dissolve

    A "*Pouts*"

    Mls "A-ha! I knew it!"

    M "(I can't tell which one of them is older at this point.)"

    scene alr299
    with dissolve

    M "So, you were ready to break your silence for some ice cream?"

    A "*Blushes* Umm."

    Mls "Hahahaha! [Mls] wins again!"

    scene alr300
    with dissolve

    M "You little traitor."

    A "*Chuckles* Sorry?"

    M "Hahaha. Lets go relax for a while, you've earned a break after putting up with that ginger monster."

    scene black
    with dissolve

    "" "10 minutes later a few blocks away."


    scene alr301
    with dissolve

    Mls "(What an incredible girl.)"

    Mls "(At least I saw what makes him so insistent on helping her now.)"

    scene alr302
    with dissolve

    Mls "(That pure heart and innocence that will get her killed within minutes in NYC.)"

    Mls "(Yet she was willing to sacrifice her own freedom for him.)"

    Mls "*Sighs deeply* (He really is a magnet for broken things. I should know.)"

    scene alr303
    with dissolve

    "" "Looking back, perhaps at herself in her early days... She chuckles heartily."

    Mls "(I'll always be there for you, [mc].)"

    scene alr304
    with fade

    r "(Found you my little piggy.)"

    r "(The Boss has some serious connections if he can track even cop cars.)"

    scene alr305
    with fade

    r "(All I have to do now is follow this cute little piggy home and blow her house down.)"

    r "(She will tell me where he lives fast or she will die slow.)"

    scene alr306
    with dissolve

    r "Boss? I found her, just as you said."

    r "Yes sir. I'll follow her home and grab her when she is alone."

    scene alr307
    with dissolve

    r "You want me to bring her to you alive?"

    r "(What the fuck is he talking about now!?)"

    scene alr308
    with dissolve

    r "Whatever you say Boss. I won't kill her, I'll just have some fun-"

    r "Seriously?! Fine! I'll bring her in unharmed."

    r "What the fuck is that all about? This is bullshit but I don't care."

    r "I just want to gut the pig bastard who killed Kenny."

    scene black
    with fade

    "" "Back at the current casa de [mc]."

    scene alr309
    with dissolve

    M "So, your sister... She's unaware of this?"

    scene alr310
    with dissolve

    A "Knowing how evil he can be, he probably blamed everything on me or someone else."

    scene alr311
    pause(.2)
    scene alr310
    pause(.2)

    A "By now, she probably thinks you kidnaped me and took me by force."

    scene alr312
    with dissolve

    M "Well, you won't have to worry about her situation for long."

    scene alr313
    pause(.2)
    scene alr312
    pause(.2)

    M "I know just the person to help us with that."

    scene alr314
    with dissolve

    A "Do you mean you are going to help me rescue my little sister?!"

    M "You know something? You look very cute when you get all excited like that."

    scene alr315
    with dissolve

    "" "She looks down, embarrassed, as she blushes slightly."

    M "I'm sorry, I didn't mean to embarrass you."

    scene alr316
    with dissolve

    A "(I can't help it.)"

    scene alr317
    with dissolve

    A "It's okay. I'm just not used to someone being so nice and willing to help me."

    A "Would you tell me the truth if I were to ask why you are so nice to me?"

    M "I'll tell you, but you need to promise to keep it a secret."

    scene alr318
    with dissolve

    "" "She looks at you curiously."

    M "I want to help you because you're a very pretty girl who asked me for help."

    scene alr314
    with dissolve

    A "Me, pretty?!"

    "" "You laughed out loud at her reaction."

    scene alr320
    with dissolve

    A "(Ouww! He is teasing me again.)"

    "" "She blushes once again."

    M "Sorry, you make it really easy for me to tease you."

    M "But I wasn't entirely joking, you know?"

    scene alr321
    with dissolve

    M "You are very pretty, and I want to help you for many reasons."

    M "Most importantly, I want to help you because you clearly need help and because you asked."

    scene alr322
    pause(.2)
    scene alr321
    pause(.2)

    M "Also, because you remind me of someone very important to me."

    A "(Must be the Jessica they were talking about before.)"

    scene alr320
    with dissolve

    M "I bet you have questions, but they will have to wait."

    M "I need to make a few phone calls about your sister."

    A "Okay, thank you [mc]."
    stop music fadeout 3

    scene black
    with fade

    "" "Meanwhile."

    scene alr323
    with dissolve

    Mls "(I need a bath!)"
    play music "Under_the_Gun.mp3" fadein 5

    show meliwalk
    pause(5)

    scene alr324
    with dissolve

    r "(This is too easy.)"

    scene alr325
    with dissolve

    r "Stop right there!"

    Mls "(Could this be?)"

    scene alr326
    with dissolve

    Mls "Easy now."

    r "Don't fucking move, bitch."

    r "You are going to tell me where that pig partner of yours is hiding..."

    r "Then you are coming with me. Someone wants you alive and unharmed it would seem."

    scene alr327
    with dissolve

    r "I said don't fucking move!"

    Mls "I'm just not used to talking to people this way, you know?"

    Mls "You clearly don't want me dead, so let's just talk this out?"

    scene alr328
    with dissolve

    Mls "You must be the one who got away. Ronny, was it?"

    r "You know my name, do you?"

    Mls "Oh, yes. Everyone knows your name by now. You and your brother are infamous."

    r "Hahaha. Kenny would've loved to hear you say that... But he's dead!"

    r "That fucking pig! He killed Kenny, and for that, I'm gonna make him pay."

    scene alr329
    with dissolve

    "Neighbor" "M-Melissa?"

    r "Huh?!"

    Mls "Stay inside!"

    scene alr330
    with dissolve

    r "You stupid bitch!"

    scene alr331
    play sound "9mmglock.ogg"
    with hpunch
    pause(1)
    scene alr332
    with vpunch

    r "Kyeeew!"

    scene alr333
    with hpunch

    r "Ow!"

    scene alr334
    with dissolve

    r "I'm going to enjoy killing you now."

    scene alr335
    with vpunch

    pause(.5)

    scene alr336
    with dissolve

    r "You are going to die in screaming, bitch."

    scene alr337
    with dissolve

    r "Any last words?"

    Mls "As a matter of fact."

    Mls "Were you not loved by your mother as a child? Is that why you're like this?"

    r "Huh?! Are you making fun of me?!"

    scene alr338
    with dissolve

    Mls "Oh, no! That was already done to you before you were born, you poor thing..."

    Mls "Must have been rough growing up with a face not even a mother could love."

    r "Are you saying that's why Momma left me?!"

    scene alr339
    with hpunch

    r "Die!"

    Mls "So much anger... yet you're so small, I can't help but pity you."

    r "I'll ki-"

    scene alr340
    with hpunch

    Mls "Careful, these floors are..."

    scene alr341
    with dissolve
    pause(.5)

    scene alr342
    with vpunch

    Mls "... slippery."

    r "Ow! You stupid bitch!"

    Mls "Can you please stop calling me that?"

    r "Or what, bitch? Are you going to make me?!"

    scene alr343
    with fade

    Mls "Or I may forget that I'm a good person and shoot you."

    r "Wait, wait!"

    scene alr344
    with dissolve

    Mls "Say it one more time, come on... Please?"

    r "Are you fucking crazy or what?"

    Mls "There's only one way to find out."

    Mls "Turn around, and assume the position."

    scene alr345
    with dissolve

    Mls "Try anything and I will drop you where you stand."

    r "Heh. Why would I?"

    r "I'll be out before you dumbasses could even process me, hahahaha."

    r "The people I work for make you look like a little pussycat."

    scene alr346
    with vpunch

    Mls "This little pussy just kicked your ass, little man."

    Mls "You have the right-"

    r "Shut the hell up! I know my rights."

    r "I have the right to be set free before you can spell my name if your report."

    r "Hahahaha!"

    Mls "I bet it would take longer if you were the one trying to spell your name during booking."

    r "You've got jokes, do you?"

    r "We'll see how funny you are when the Boss gets his hands on you."

    scene alr347
    with dissolve

    Mls "Why not just tell me who it is that you work for and I let you walk?"

    Mls "You know, like nothing ever happened."

    Mls "No? Okay, I have a better idea."

    Mls "I'm going to take you to see that pig you've been dying to meet instead of jail."

    scene alr348
    with dissolve

    r "What?! You can't do that! You're a cop! No! He'll kill me!"

    Mls "Oh, kill you is an understatement. You killed a rookie on his watch."

    scene alr347
    with dissolve

    Mls "He is going to kill you so slow... You will near death by old age first."

    Mls "Ever heard of death by a thousand cuts?"

    r "Wait, wait! I'll tell you everything I know but you have to promise to take me in."

    scene alr348
    with dissolve

    Mls "Okay. You better tell me everything you know before we get to the station."

    Mls "Otherwise, I fear your life will be even shorter than you are."

    scene alr347
    with dissolve

    r "Just take me in already you stupid b-"

    scene alr348
    with vpunch

    r "Ouch!"

    Mls "Yes?"

    r "Big fat-ass cop."

    Mls "*Chuckles* Just move!"

    scene black
    with dissolve

    "" "15 minutes later."
    play music "Rocker.ogg" fadein 5

    scene alr349
    with dissolve

    "Beat-cop 1" "Stop running around naked, you little cumstain!"

    "Naked weirdo" "That's Mr. Cumstain to you!"

    scene alr350
    with dissolve

    "Pizza delivery guy" "Why are you arresting me man? I am just here to deliver what was ordered!"

    "Bearded anti-pineapple on pizza cop" "How many times have I told you to stop delivering pineapple pizza to my desk?!"

    "Pizza delivery guy" "I don't know what's inside the box! I only deliver what you guys order!"

    scene alr351
    with dissolve

    "Beat-cop 1" "Oh, you're going down, punk."

    "Naked weirdo" "Oh, my. You sure do work out a lot."

    "Front desk girl" "What brings you to this fine establishment [Mls]?"

    scene alr352
    with dissolve

    "Suicidal cop" "(Someone shoot me.)"

    "Old lady" "When are you people going to do something about finding my dog?"

    "Suicidal cop" "*Mumbles* Ms. Smith... I have told you a thousand times..."

    "Suicidal cop" "We're not going to be able to find your dog."

    "Ms. Smith" "Can't you people do something useful for once? You're just being lazy."

    "Suicidal cop" "Fine Mrs Smith, when did you last see your dog?"

    "Ms. Smith" "It's been 84 years."

    "Suicidal cop" "(Kill me now.)"

    Mls "Give me a hand, will you?"

    scene alr353
    with dissolve

    Lo "*Giggles* Poor Tim."

    scene alr354
    with dissolve

    Lo "Timothy! Can you-"

    scene alr355
    with dissolve

    Tim "Me, I'll do it, I volunteer all of my time!"

    Lo "(Poor Tim, he'll do anything to get away from that crazy old lady.)"

    scene alr356
    with dissolve

    Tim "(Oh, thank god!)"

    scene alr357
    with dissolve

    stop music fadeout 4

    Tim "I owe you lunch."

    Lo "Oh, you better be ready to pay, Tim."

    Mls "I'll be leaving you in good hands, little man."

    r "Uncuff me and say that to my face, bitch!"

    scene alr358
    with dissolve

    Mls "Don't forget to write me, smoochies."

    Lo "[Mls] can be so cruel. God, I love her."

    Tim "Oh, I almost forgot. The Captain wants to see you right away, [Mls]."

    Tim "Let's go. Your new home awaits."

    scene alr359
    with vpunch

    r "What are you smiling at you ugly bitch?!"

    Tim "I think you need a lesson in manners."

    Lo "So sweet. Don't worry about him Tim."

    Lo "Dealing with little peckers like him is in our job description."

    Mls "(What does he want?)"

    scene alr360
    with dissolve

    play sound "ringtone.ogg"

    M "Hmmm. I guess it's her calling."

    scene alr361
    with dissolve
    pause(.3)
    stop sound

    show mcall
    pause(5)

    scene alr362
    with dissolve

    Mls "I got him [mc]. Before you freak out, I'm perfectly okay."

    Mls "Think he followed me from the parking garage, I had a suspicion that someone was there."

    scene alr363
    with dissolve

    M "That mother fucker! Did he lay a hand on you?!"

    Mls "He tried. But it looks you have nothing to worry about, old man, you have taught me well."

    scene alr364
    with dissolve

    "" "Exhales relieved."

    M "I'm sorry, [Mls]."

    Mls "Oh, stop it. You always do the right thing, no matter the cost, and that's what I love about you."

    scene alr365
    with dissolve

    M "I knew you were in love with me all along, it's about time the truth came out."

    Mls "*Chuckles* You sure know how to make a girl smile. Thanks, it's been a rough day."

    M "I doubt it will get easier but I've already made some calls."

    Mls "Good! I also have some news. I got him to talk [mc]."

    scene alr367
    with dissolve

    M "You what?"

    Mls "He told me everything he knew."

    Mls "Well, I had to convince him that it was in his best interest to do so."

    M "Did you threaten to bring him to me?"

    Mls "Hey, if it ain't broke don't fix it, right?"

    scene alr366
    pause(.2)
    scene alr367
    pause(.2)

    M "I can't believe that I have been such a negative influence on you."

    Mls "Oh, shut up already! This is NYC, if we do everything by the book, we won't see tomorrow."

    scene alr366
    pause(.2)
    scene alr367
    pause(.2)

    M "You've grown into another me, haven't you rookie?"

    Mls "I've been trying to tell you that I am not a rookie anymore, you know?"

    M "Yes, I know, partner."

    Mls "*Chuckles*"

    Mls "So... He didn't know much, but he did say that his Boss is so well connected he can track cop cars."

    scene alr363
    with dissolve

    M "In other words, he has someone working for him on the inside."

    Mls "Yup. I know I can trust Tim and Lola, but that's about it, really."

    M "I know you don't want to believe this, but I bet it's that scumbag."

    Mls "This again... I hope you're wrong, I still do."

    scene alr364
    pause(.2)
    scene alr363
    pause(.2)

    M "Anyhow, you will figure it out eventually."

    M "As for those two, they are both good cops, I trust them as well."

    scene alr364
    pause(.2)
    scene alr363
    pause(.2)

    M "However, it's probably best we don't involve them."

    M "You know what will happen if we do, don't you?"

    scene alr365
    with dissolve

    Mls "*Sighs* Yes."

    M "Hey, there's still time for you to walk away from this, you know?"

    Mls "Nu-uh. You can't get rid of me that easily, old man."

    Mls "I mean... I- you know."

    scene alr367
    with dissolve

    M "My goodness. [Mls] Marconi, are you really about to confess your love for me over the phone?"

    Mls "*Scoffs* Fuck you! I have to go, the Captain wanted to see me and he's shouting already."

    scene alr366
    pause(.2)
    scene alr367
    pause(.2)

    M "Be careful, okay? You can't trust anyone else with our location."

    Mls "Don't worry, I know. As far as I can tell nobody else knows about that place anyway."

    Mls "I'll call you back once I get home, just don't go falling in love with her overnight, okay?"

    scene alr366
    pause(.2)
    scene alr367
    pause(.2)

    M "I make no promises, so you better step up your game."

    Mls "*Chuckles heartily* You are such a dick!"

    scene alr366
    pause(.2)
    scene alr367
    pause(.2)

    M "Stay safe, please. I don't know what I'd be capable of doing if something happened to you."

    Mls "Ha! I have some idea but I gotta go for now [mc]. I'll call you as soon as I get home, I promise."

    "" "She hangs up."

    M "Alison?!"

    A "I'm coming!"

    show aliwalk
    pause(4.3)

    scene alr368
    with fade

    A "Did you need me for something?"

    M "I have some good news."

    scene alr369
    with dissolve

    A "Good news?"

    M "[Mls] caught that ugly piece of... Ronny."

    scene alr370
    with dissolve

    A "Really?!"

    M "Yes. He is going to spend some serious time in jail after she's done with him."

    M "And you-"

    scene alr371
    with vpunch

    M "(Sweet baby Jesus. She really is like a big kitten when she gets excited.)"

    M "I knew you would be happy but I had no idea you would pounce like a kitten."

    scene alr372
    with dissolve

    M "And here it comes. Yup! You're blushing again."

    M "I can't even begin to describe just how adorable you look right now, you know?"

    scene alr373
    with dissolve

    A "(You idiot! Why did you just jump on him like that?!)"

    A "I'm so sorry."

    scene alr374
    with dissolve

    M "No need for that."

    scene alr375
    with dissolve

    M "If that's how you express yourself, then you continue doing whatever works for you."

    show kittypat

    M "After all, I am a sucker for kittens, you know?"

    A "(He is so good to me, I can't even control my emotions.)"

    scene alr376
    with dissolve

    M "I guess I'll stop. I don't want you to be frozen in place, speechless."

    scene alr377
    with dissolve

    M "What's this? Kitty wants more?"

    scene alr378
    with dissolve

    "" "She decided to respond without words."

    scene alr379
    with dissolve

    M "I see how it is."

    A "*Chuckles softly*"

    M "Okay... Why don't we sit down and have a little chat, kitty?"

    A "Okay."

    scene black
    with fade

    "Meanwhile."

    scene alr380
    with dissolve

    r "Where is my fucking lawyer!"

    r "(What is taking so long? I should be out by now.)"

    Tim "You'll have to ask him where he has been once he gets here, meanwhile, shut it!"

    scene alr381
    with dissolve

    play music "Stranger_Things.mp3" fadein 5

    Mls "You wanted to see me, sir?"

    "Captain" "Yes, but I wanted to see you as soon as you arrived."

    "Captain" "You like to make me wait, ummm?"

    scene alr382
    with dissolve

    Mls "I had to book someone who had a gun to my head, so I hope that didn't interrupt your lunch."

    Mls "I am so very sorry."

    "Captain" "Sarcasm, is it? Ummm? I see."

    scene alr383
    with dissolve

    Mls "You know something?! My partner is innocent! And that piece of trash in holding can prove it!"

    Mls "So don't you sit there looking at me like I'm some rookie who was called in here to be scolded!"

    "Captain" "Huhuhuhu. That fire in your eyes is the pride of this precinct you know, ummm?"

    scene alr384
    with dissolve

    Mls "(Oh, no.)"

    "Captain" "I simply called you here to share the good news... detective."

    "Captain" "Huhuhu. I am proud to inform you that your exemplary work has not gone unnoticed."

    scene alr385
    with dissolve

    "Captain" "*Texting* (I can only stall her for so long, hurry it up!)"

    "Captain" "However, I can't have my brightest star, now a detective no less..."

    "Captain" "... working a case that involves her previous partner now, can I, ummm?"

    Mls "(You fucking weasel... I knew that would come back to bite me, but not this soon.)"

    Mls "(He must have pulled some strings to fast track me just so I'm off the case.)"

    scene alr386
    with dissolve

    Mls "Detective or not, I will get to the bottom of this, sir!"

    "Captain" "Huhuhu. I am not asking you not to do your job, my shining star!"

    "Captain" "I am simply..."

    scene alr386
    with dissolve


    r "Hey! Where the fuck is my lawyer, dick-heads?"

    r "I have rights, you know?! I'll sue you!"

    scene alr387
    with dissolve

    "Cop?" "Yes, you have the right to remain silent, forever."

    "Cop?" "The Boss sends his condolences for your brother, he wishes for you to join him."

    "Totally not a cop." "Have a safe trip, Ronny."

    r "What the fuck?! Hel-"

    scene alr387
    with flash
    pause(.3)

    scene alr388
    with vpunch

    "Totally not a cop" "(It's done, I'm on my way out.)"

    scene alr389
    with dissolve

    "Captain" "So, you see..."

    "Captain" "If you continue to insist, I will have no choice but to remove you from active duty, ummm?"

    scene alr389
    with dissolve

    Mls "*Mumbles angrily* I'll get you one day, you dirty prick."

    scene alr390
    with dissolve

    "Captain" "Ummmm? Did you say something, detective?"

    Mls "I said!"

    "Captain" "Yes, ummm?"

    Mls "Thank you, sir!"

    "Captain" "Good, good."

    "Captain" "Leave your gun and badge here for now. Pick up your new toys on the way home."

    "Captain" "Congratulations on the promotion, you are dismissed."

    scene alr391
    with dissolve

    "Captain" "(If only she weren't so popular around here, I'd love to take that for a spin. *drools*)"

    "Captain" "Huhuhu."

    Mls "(You dirty fucking rat! I had my suspicions, but [mc] fucking knew, I should have listened.)"

    scene alr392
    with dissolve

    "Captain" "It is done. The attack dog is off the case."

    "Captain" "Kill her? Have you lost your mind, dear brother? Office has made you soft in the head I see."

    scene alr393
    with dissolve

    "Captain" "You fool! She is very popular in this precinct! Even the dirtiest cops on your pay roll wouldn't touch her!"

    "Captain" "Yes. She is very popular and well loved here. No one would back you if you were to harm that woman."

    scene alr394
    pause(.2)
    scene alr393
    pause(.2)

    "Captain" "You seem to forget that her old partner is on the run to keep her out of harms way."

    "Captain" "If we kill her there is no doubt in my mind that the only place you and I would be safe..."

    "Captain" "Is a nuclear bunker, sealed shut from the inside, permanently."

    scene alr394
    pause(.2)
    scene alr393
    pause(.2)

    "Captain" "No, I am not suggesting that I am afraid of him, I'm outright saying that I am."

    "Captain" "I am also saying that you should learn to fear him too, before it is too late."

    "Captain" "If you harm her he will find out and kill us both."

    scene alr394
    pause(.2)
    scene alr393
    pause(.2)

    "Captain" "Coward? Perhaps."

    "Captain" "I'd like to return home after work, wouldn't you brother?"

    scene alr395
    with dissolve

    "Captain" "Right now, what we have is him on the run and us on the right side of the law."

    "Captain" "Leave her out of this, please. She will be the end of you if you insist on taking her."

    scene alr396
    with dissolve

    Mls "(I'll get him to tell me everything. I'm not officially a detective yet.)"

    "Totally not a cop" "Detective."

    Mls "*Growls*"

    "Totally not a cop" "(Good thing she didn't see my face, I get the feeling she's trouble.)"

    scene alr397
    with dissolve

    "Ms. Smith" "He was wearing a red collar."

    Mls "Ungh! (Not now.)"


    stop music fadeout 3

    scene alr398
    with dissolve

    Mls "Hey assh-"

    Mls "Is he dead?!"

    scene alr399
    with dissolve

    Mls "Somebody call the paramedics and get me some help in here!"

    Mls "(Who killed him here, and why now?)"

    scene black
    with fade

    "" "Back home."

    scene alr400
    with dissolve

    A "So, that's why you called me Jessica."

    M "Yeah... When I saw you wearing those Pj's I couldn't tell you apart."

    scene alr401
    with dissolve

    A "You were happy and it didn't bother me."

    A "I was just a little confused."

    scene alr402
    with dissolve

    show kittyblink

    A "You must really love her."

    M "I do but I'm not so sure it matters anymore."

    A "Why do you say that? Did she go somewhere while you were in the military?"

    M "You could say that. I was going out there for the last time."

    M "I planned to return and marry her..."

    M "We were going to travel the world, see new places, do new things."

    M "But when I returned it was too late for any of that."

    scene alr402
    with dissolve

    A "What happened to her [mc]? Did she leave you?"

    M "They told me that both she and the child she was carrying were dead."

    A "D-dead?!"

    M "That's what they told me. She was carrying my... Our child at the time."

    scene alr403
    with dissolve

    A "No. That can't be true... Please, tell me that's not true?!"

    play music "Touching_Moment.mp3" fadein 5

    show kittytears
    pause(1)

    scene alr404
    with dissolve

    A "*Sniffles* That's terrible!"

    A "I am so sorry... I had no idea. You must have been devastated."

    A "Please forgive me."

    scene alr405
    with dissolve
    pause(.5)

    scene alr406
    with dissolve

    M "There is no need for that, kitten. Like I said, they told me she was dead."

    M "I never said I believed them. I still believe she is alive, somewhere."

    scene alr407
    with dissolve

    A "*Sobs softly*"

    M "That's a good girl. If you cry, then I'll think she really is dead."

    M "So please, don't cry anymore, okay?"

    scene alr408
    with dissolve

    A "(He really believes she's not dead...)"

    A "(I need to believe that as well and be strong like he is.)"

    scene alr409
    with dissolve

    M "Let me see that smile."

    M "That's not a smile."

    scene alr410
    with dissolve

    A "You are going to find them, right?"

    M "Yes, kitten. I'll find them, no matter how long it takes me."

    A "Okay! If you believe they are alive, then I will believe it with you, [mc]."

    scene alr411
    pause(.4)
    scene alr412
    with dissolve

    M "Thank you Alison. That really makes me happy."

    scene alr413
    pause(.3)
    scene alr414
    pause(.3)
    scene alr415

    A "Would you have helped me if I looked different, [mc]?"

    M "Haha. Of course, silly! At that point, I already considered you my reponsibility."

    M "All part of the job."

    scene alr416
    pause(.2)
    scene alr417
    pause(.2)

    M "A lot of people seem to believe that we are all crooked and mean..."

    M "The truth is, there are more good cops wearing those uniforms in this world than there are bad ones."

    scene alr416
    pause(.2)
    scene alr417
    pause(.2)

    A "I don't really know anything about any of that, I just wanted to hear you say it, is all."

    M "And now that you have heard me say it?"

    scene alr401
    with dissolve

    A "It's a secret! *Giggles*"

    M "Is that so?"

    A "Mhm."

    stop music fadeout 4

    M "Okay. I'm sure you will tell me when you feel it's the right time."

    A "Yes, I will."

    play sound "ringtone.ogg"

    M "That must be [Mls] again. I'll need to take that."

    A "Okay."

    stop sound

    scene alr418
    with dissolve
    play music "Hey_Girl.mp3" fadein 4

    M "Got home okay?"

    Mls "You could say that."

    scene alr419
    with dissolve

    M "What's wrong? You sound upset."

    Mls "They killed him [mc]. They fucking killed him inside the holding cell."

    M "I can't say that I'm surprised, or even sorry... But I understand why you would be upset."
    label galleryScene27:
    scene alr420
    with dissolve

    Mls "It gets better."

    M "Oh, yeah? Do tell."

    Mls "The Captain \"promoted\" me out of the case."

    scene alr421
    with dissolve

    Mls "And you better not say I told you so!"

    M "Well, I did tell you so."

    Mls "Oh, shut it! That ugly little troll likely stalled me so I wouldn't question him further."

    scene alr422
    with dissolve

    Mls "I planned to have him brought into the interrogation room and squeeze everything out of him."

    M "The Captain knows how capable you are, [Mls]. Of course he would stall you if he is dirty."

    Mls "At least now we know what we are up against."

    scene alr423
    with dissolve

    M "Did you make sure to lock the door?"

    Mls "I'm not scared, [mc]. I'm taking a relaxing bath... You could come over and watch me."

    Mls "You know... Make sure I'm all clean?"

    Mls "Keep me nice and safe? I'm a pretty girl, all wet, naked and alone, you know?"

    scene alr424
    with dissolve

    M "You know, one of these days, I'll take you up on that and the joke will be on you."

    scene alr425
    with dissolve

    Mls "(I'm not joking, you fool.)"

    M "Also, if I did come over now, I'd have to bring Alison as well."

    scene alr424
    pause(.2)
    scene alr425
    pause(.2)

    M "I have a feeling that the three of us would not fit inside your tub."

    scene alr426
    with dissolve

    Mls "I guess you really did forget how big this thing is, didn't you?"

    M "Oh, stop it! You're giving me ideas now."

    Mls "Hahaha. Okay, okay. Just make sure to stock the ice cream I asked for."

    scene alr427
    pause(.2)
    scene alr426
    pause(.2)

    M "I am way ahead of you. I ran downstairs while Alison was taking a shower."

    Mls "You are so sweet to that girl. Why can't you be sweet like that with me?"

    scene alr427
    pause(.2)
    scene alr426
    pause(.2)

    M "Because you are dangerous... She is just an innocent girl who wouldn't know what to do with me."

    Mls "You noticed that as well, huh?"

    M "Yeah, I did."

    scene alr427
    pause(.2)
    scene alr426
    pause(.2)

    Mls "Well, she may be innocent but she does not appear to be slow."

    Mls "Do not understimate her."

    Mls "After all, she does have you all wrapped up around her little pinky in less than 48 hours."

    scene alr427
    pause(.2)
    scene alr426
    pause(.2)

    M "Do you really think so?"

    Mls "Are you seriously asking me?"

    M "Well, yeah."

    scene alr425
    with dissolve

    Mls "(Oh, god. Please help me with this one!)"

    scene alr423
    with dissolve

    Mls "[mc]... That girl was willing to go back to the nightmares and cages you spoke of."

    Mls "No one does that out of the kindness of their heart alone."

    Mls "She sees you as her light at the end of a very long and dark tunnel."

    M "Talk about pressure."

    scene alr426
    with dissolve

    Mls "That's what you signed up for!"

    Mls "And if by some chance you have changed your mind?"

    scene alr427
    pause(.2)
    scene alr426
    pause(.2)

    Mls "I will turn you in myself."

    Mls "She can't handle being betrayed by you of all people right now."

    Mls "It would crush her and she would never recover again."

    scene alr427
    pause(.2)
    scene alr426
    pause(.2)

    M "Ouch. You would really do that?"

    Mls "I guess we will never find out, will we?"

    scene alr427
    pause(.2)
    scene alr426
    pause(.2)

    Mls "I know you don't have it in you to look into those pretty blues..."

    Mls "...and tell her I'm sorry, but you gotta go now."

    M "Meh, you're no fun. Why do you always have to make sense?"

    scene alr427
    pause(.2)
    scene alr426
    pause(.2)

    Mls "D-awww. One of us has to be the adult, you know?"

    M "Hey!"

    Mls "Now now. Little [mc] needs to hang up, mommy [Mls] needs to finish her bath."

    scene alr427
    pause(.2)
    scene alr426
    pause(.2)

    Mls "Tell Alison I'll be over later, okay?"

    M "Yeah, okay. When you get here, I'll go meet up with the little lady."

    Mls "Oh! If that means you're going to see Aiko, tell her [Mls] sends her lots of kisses."

    scene alr427
    pause(.2)
    scene alr426
    pause(.2)

    M "Uh... Okay? You pervert."

    Mls "I'm naked, inside my tub, my nipples are hard *Moans*"

    M "Okay! Message received! I guess I'm the pervert now, Jesus!"

    scene alr427
    pause(.2)
    scene alr426
    pause(.2)

    Mls "*Giggles* Mwuah, laters, you big perv!"

    M "Alison?!"

    Mls "Ouch, hang up first!"

    stop music fadeout 3
    $ renpy.end_replay()
    scene black
    with fade

    A "Coming!"

    scene alr428
    with dissolve

    M "Mel's is coming over shortly and she'll stay with you."

    M "I think I've already explained to you that she is someone I trust with my life."

    scene alr429
    with dissolve

    A "(I guess she can't be a bad person if he trusts her that much, can she?)"

    M "Are you going to be okay?"

    scene alr430
    with dissolve

    A "Um. Will you be gone for long?"

    M "No. I'll just go meet a friend of mine."

    M "She's the one who will help us with your sister and a lot more in the future."

    scene alr429
    with dissolve

    M "You are going to be safe here, kitten."

    A "I don't want to be away from you, but I understand."

    A "I will wait here, with the mean lady."

    M "Hahaha."

    play sound "doorbell.ogg"

    scene alr430
    with dissolve

    M "That'll be Mel now."

    stop sound

    A "How can you be so sure?!"

    M "Don't worry, nobody else knows about this place."

    M "Back in a minute."

    scene alr431
    with dissolve

    "" "You look at her from top to bottom and let out a satisfied long sigh."

    M "Sweet-baby-Jesus."

    Mls "That good, huh?"

    scene alr432
    with dissolve

    A "*Pouts*"

    A "(I don't care!)"

    scene alr433
    with dissolve

    Mls "Now wipe the drool from your chin and tell me how's she doing?"

    scene alr434
    with dissolve

    M "She is still a little annoyed at you for earlier, but nothing you can't handle, I'm sure."

    M "Also..."

    "" "You lean in and whisper in her ear."

    M "You look gorgeous in that outfit, I mean... Phew! I wish I didn't have to go, right now."

    scene alr435
    with dissolve

    Mls "Are you fucking with me? You better not be messing with me, dickhead."

    M "And then you wonder why I rarely compliment you on your appearance."

    Mls "(Shit! I can't ever tell when he is messing with me and when he is seriously flirting with me.)"

    scene alr436
    with dissolve

    M "Bah. Laters, knucklehead."

    Mls "Bite me."

    Mls "Hey, pouty girl."

    scene alr437
    with dissolve

    Mls "I don't know if you've heard, but we are going to spend some time together."

    Mls "I would really like a chance to make up for being so cruel to you earlier."

    scene alr438
    with dissolve

    Mls "Oh well. I guess I'll just go to the kitchen by myself."

    scene alr439
    with dissolve

    Mls "I'll take a look inside that freezer... And maybe find me some ice cream for my sorrows."

    scene alr440
    with dissolve

    A "(Did she say ice cream?!)"



    scene alr441
    with flash

    A "Wait! [Mls]! I want to come with you!"

    "" "[Mls], can be heard laughing out loud from the kitchen."

    Mls "Oh, yeah?! You better hurry, this ice cream is looking very delicious!"

    Mls "It might disappear fast."

    stop music fadeout 3

    scene black
    with fade

    "" "Meanwhile, at the Whiskey-Tango-Foxtrot."

    play music "That One Bar Scene.mp3" fadein 5

    scene alr442
    with dissolve

    "Depressed girl" "Why can't I have some more cock-ala-creme?!"

    "Timid girl" "Honey, we talked about this! You can't have any more because you're an addict!"

    "Timid girl" "You don't know when to stop..."

    "Timid girl" "The last guy was carried to the hospital. You drained him completely."

    scene alr443
    with dissolve

    "Depressed girl" "Not my fault he only had 3 hours worth in him, is it?!"

    "Sushi loving guy" "I love this place!"

    "Sushi loving guy" "I can't wait to eat you out, my tasty little sushi girl."

    "Sushi girl" "*Giggles* It's all you can eat today, sir."

    "Waitress" "Do you need anything else, sir?"

    M "I'm good, thanks."

    "Waitress" "Well, if you change your mind, let me know."

    "Waitress" "We just received a fresh delivery of sushi girls, and young cock-ala-creme."

    "Waitress" "They are waiting to be ordered as we speak."

    scene alr444
    with dissolve

    M "I brought my own sushi, she's on her way."

    "Waitress" "Oh, how wonderful. I'm so happy or you."

    "Waitress" "Let me know if she needs any freshly milked cream, will you?"

    M "Uh-huh."

    M "(Sigh. I guess she picked this place for a reason.)"

    M "(This ass-ylum is certainly a place no one would look for me.)"

    stop music fadeout 4

    scene black
    with fade

    "" "Don't look at me. I'm just the narrator."

    "" "Ahem. Back home with the girls."

    scene alr445
    with dissolve

    play music "Good Times.mp3" fadein 5

    Mls "Before you can have this mountain of ice cream, you'll need to talk to me."

    A "Ouu! Okay."

    Mls "Tell me why are you willing to give your freedom up for [mc]?"

    scene alr446
    with dissolve

    A "Um."

    Mls "(She is blushing. I guess I'll get a lot more from what she can't tell me.)"

    A "I just didn't want him to get hurt because of me. I'm not worth that."

    scene alr447
    with dissolve

    Mls "So that's what you think."

    Mls "If I were you, I would never mention that around him."

    Mls "You see, he has decided to invest everything in helping and keeping you safe."

    scene alr449
    with dissolve

    Mls "Which means you are more important than you think to him right now."

    Mls "Has he told you about Jessica?"

    A "Yes. He explained to me, earlier today."

    Mls "(He really must care for her.)"

    Mls "Listen, Alison... I was like you once."

    scene alr448
    with dissolve

    A "Really?"

    Mls "(Look at her! Oh, my god! She is like a little puppy!)"

    Mls "Really. (Well, not exactly like you, you are bigger all around!)"

    Mls "I don't know how much he has told you about me but he's very important to me."

    scene alr446
    with dissolve

    A "He told me that you were the best thing that ever happened to him, after Jessica went missing."

    A "Without you, he would have been lost, he said."

    Mls "(Did he now? That bastard... Why can't he say those things to me?)"

    scene alr448
    with dissolve

    Mls "Thank you for telling me that, Alison."

    Mls "When I first met him, he was a good cop, but he always liked to work alone when possible."

    scene alr445
    with dissolve

    A "Why?"

    Mls "That was not that long after he had lost Jessica, and I was new on the force."

    Mls "Anyway. He met me inside the locker room one day, after the shift was over."

    scene alr449
    with dissolve

    Mls "I was upset and waiting for someone to come pick me up for a party."

    Mls "Long story short!"

    Mls "He scolded me for being so dependent on others, and insisted I join him at another party."

    scene alr448
    with dissolve

    A "Did you go?!"

    Mls "Hahaha. Yes."

    Mls "I was a little upset that he got bossy with me, but I knew that it wasn't how he meant it."

    scene alr450
    with dissolve

    Mls "At the time, all I had heard about him were rumors."

    Mls "All the busts he had made, the countless lives he had saved and helped save."

    Mls "I was not aware of how much he had lost, or how heavy that loss was weighing on him."

    scene alr451
    with dissolve

    "" "She pauses, and sighs deeply."

    Mls "Despite all the pain and suffering, he reached out and turned my entire life around."

    scene alr450
    with dissolve

    Mls "He never, not once! Stopped to complain about his troubles, or even mention them."

    Mls "He devoted all of his free time into making me the cop I am today..."

    scene alr451
    pause(.2)
    scene alr450
    pause(.2)

    Mls "So you see, I had no choice but to be cruel with you, earlier."

    Mls "I will not allow anyone to hurt him or take advantage of his, kind to a fault, heart."

    scene alr452
    with dissolve

    A "Wow... You are so cool!"

    Mls "You think?"

    A "Yeah! You were just trying to make sure he wasn't going to get hurt, just like I was!"

    scene alr446
    with dissolve

    Mls "(She is adorable, and highly intelligent, despite her clear lack of life experience.)"

    Mls "(I think I finally understand you, [mc].)"

    Mls "(If this gives your life purpose once again, then I'll gladly help you.)"

    scene alr450
    with dissolve

    Mls "That ice cream is going to melt, so one last question."

    A "Okay."

    Mls "Will you promise me that you will make sure he feels loved and appreciated?"

    A "Huh?!"

    scene alr452
    with dissolve

    Mls "Don't look so shocked. I didn't ask you to have sex with him."

    scene alr446
    with dissolve


    A "W-what?!"

    Mls "(Oh, my god... Don't tell me.)"

    scene alr447
    with dissolve

    Mls "So, have you ever had a boyfriend?"

    Mls "We're both girls you know? I'm only curious, I promise to keep your secret."

    Mls "I'll go first!"

    Mls "I have fooled around with some girls, and some toys, but I've never had sex either."

    scene alr449
    with dissolve

    A "Really?!"

    Mls "Stop sounding so surprised! It happens, you know?!"

    A "But, girls?"

    scene alr450
    with dissolve

    Mls "Oh, right... That's a subject for another time, I'm afraid."

    Mls "I have a busy life and the only guy I was really ever interested in is thick as a tree!"

    scene alr451
    pause(.2)
    scene alr450
    pause(.2)

    Mls "In the head, at least. I wouldn't know about any other parts..."

    A "Other parts?"

    Mls "Oh, I'll just shut up now."

    scene alr451
    pause(.2)
    scene alr450
    pause(.2)

    Mls "Your turn now, and you better hurry it up, the ice cream is melting!"

    A "No!"

    Mls "No?"

    scene alr451
    pause(.2)
    scene alr450
    pause(.2)

    A "Yes."

    Mls "Huh?"

    A "I mean the answer is no! I have never had a boyfriend."

    scene alr451
    pause(.2)
    scene alr450
    pause(.2)

    A "I have never had a chance to have anything."

    A "It's hard to have anything inside a cage."

    scene alr451
    pause(.2)
    scene alr450
    pause(.2)

    A "Now, can we please talk about something else?"

    scene alr452
    with dissolve

    Mls "Yes, sweetheart."

    Mls "You can have all the ice cream you can handle, just don't get sick on me, okay?"

    scene alr453
    with flash

    Mls "Woah!"

    scene alr454
    with dissolve
    Mls "It's not going anywhere."

    Mls "(What on earth was that?! That kind of speed can't be possible!)"

    Mls "Hahahahaha!"

    Mls "Eat up before he gets back, otherwise, he might scold me for giving you a sugar overload."

    stop music fadeout 3

    scene black
    with fade

    "" "Back at the Whiskey-Tango-Foxtrot."

    play music "That One Bar Scene.mp3" fadein 5

    scene alr455
    with dissolve

    Sh "So I did some digging as you asked, and it turns out he is a real piece of work."

    Sh "Rumor has it, he had been working on something really big for the military around 20 years back..."

    Sh "But he went dark on them after the project had started."

    scene alr456
    with dissolve

    M "When was this, exactly?"

    Sh "There is no exact date, but it is rumored to be somewhere around 2 years after the project had started."

    M "Hmmm. (Alison is what, 18? 20?)"

    Sh "I know what you're thinking... I thought the same thing, but that girl has a real mother."

    M "Are you and your ass going to sit down, or do you intend to talk out of your ass, all day?"

    scene alr457
    with dissolve

    Sh "Want me to blend in, do you? I could reach down those pants and give you a creamy finish?"

    M "You know, I keep reminding you that you need to be careful with that mouth of yours."

    M "But, it would seem that my words keep falling on deaf ears. So, how about..."

    scene alr458
    with dissolve

    M "You go the extra mile and blend in properly, with that mouth wrapped around it, instead?"

    Sh "Seriously? Do you really mean that, or are you just fucking with me, again?!"

    scene alr459
    with dissolve

    M "It would seem that the only way for you to find out for sure..."

    M "...is to first find the courage to try it out."

    "" "You chuckle as you look into her eyes, shining bright with anticipation."

    Sh "You are such a tease. Why do you always do this to me?"

    scene alr457
    with dissolve

    M "You make it too easy, that's why."

    M "Now, enough about your fantasies, get back to work."

    Sh "(One of these days, I'll just get it done, and we will see who has the last laugh.)"

    Sh "I'll see what else I can find on that project and why she is so important to him."

    stop music fadeout 3

    scene black
    with fade

    "" "Back home with the girls."

    scene alr460
    with dissolve

    play music "Good Times.mp3" fadein 5

    Mls "I have never seen anyone eat so much ice cream and not get sick."

    A "Maybe because they have had it often enough."

    scene alr461
    with dissolve

    A "This was only my second time."

    A "I had almost forgotten what it tasted like."

    Mls "You don't have to worry about going back to that horrible life, sweetheart."

    scene alr461
    with dissolve

    Mls "Believe me, there is barely a handful of people in this entire city..."

    Mls "...that are better suited at keeping you safe, than [mc]."

    A "(She really seems to believe he can keep me safe from him.)"

    A "(Maybe he really can? It would be nice to live like a normal person for once.)"

    scene alr460
    with dissolve

    Mls "What's on your mind, sweetheart?"

    A "I was just thinking to myself about what you said."

    Mls "Share?"

    A "Well, you make it sound like he can keep me safe, but you don't know how evil my father can be."

    scene alr461
    with dissolve

    Mls "I can see where you're coming from, but as well as you might know your father..."

    Mls "I know [mc]. He will stop at nothing if it means he will find justice at the end of the road."

    Mls "The military was all he had, growing up. Then he met Jessica, and she changed him."

    scene alr462
    with dissolve

    Mls "However, once she was gone... He went back to what he knows best."

    Mls "Please don't tell him I told you this, but [mc], has a very strong sense of justice."

    Mls "He doesn't care if you are rich, poor, or famous."

    Mls "If you have done unforgivable things, he will make you pay, no matter the cost."

    Mls "It's scary at times, but at least as a cop he did it within the law."

    scene alr463
    with dissolve

    Mls "I'm scared to think of what he might do now that he is no longer a cop."

    M "Hey, girls."

    Mls "Shhhh."

    scene alr464
    with dissolve

    A "[mc]!"

    Mls "*Chuckles* Look at you all perked up as soon as he enters!"

    scene alr465
    with dissolve

    A "*Embarrassed* (So, what? I'm just happy he is back.)"

    Mls "Hey, big man. How did it go?"

    M "Hey little red."

    scene alr466
    with dissolve

    Mls "(Look at her go. She gets all shy, and embarrassed when I mention it but she still goes to him!)"

    Mls "(And he smiles at her, of course!)"

    scene alr467
    with dissolve

    Mls "*Whispers* I told you so."

    "" "You give her that 'I didn't do nothing' look."

    M "Hey girl, missed me already?"

    scene alr468
    with dissolve

    A "Mhm."

    M "Well, I'm glad I came home soon then."

    scene alr469
    with dissolve

    "" "[Mls] looks at the two of you envious, and wanting."

    M "So, did the mean lady treat you well, while I was gone?"

    A "She is not mean. She is very nice, you know?"

    M "Oh, is that so? Does this mean, I should give her a hug as well?"

    A "Yes."

    scene alr470
    with dissolve

    Mls "(I'll take it!)"

    M "Come here you, big bully!"

    Mls "Oh, bite me!"

    scene alr471
    with dissolve

    Mls "(Of course, for me he uses the sisterly hug!)"

    M "Thanks for coming over."

    "" "You kiss her cheek, gently."

    scene alr472
    with dissolve

    Mls "*Exhales deeply* (That's the first time he has ever shown me such affection.)"

    Mls "(This girl may have brought some life into him after all. Good girl, Alison.)"

    M "So, are you staying, or are you headed home?"

    scene alr473
    with dissolve

    Mls "[mc]? What has gotten into you? You're asking me to stay over?!"

    Mls "My goodness, she has really made you soft, hasn't she?"

    M "Oh, man... Here we go again. I suppose, this is what I get for trying to be nice."

    scene alr474
    with dissolve

    "" "Melissa lets out a hearty laugh."

    M "You can be such a pain, but you are welcome to stay if you want."

    scene alr475
    with dissolve

    M "I'm sure Alison would like the company, wouldn't you?"

    A "Yes."

    Mls "D-awww, you two! I really want to stay now!"

    Mls "I can't though. I'm concerned about the way they tracked me before."

    Mls "I parked far enough away but I don't want them to find out she is here, you know?"

    scene alr476
    with dissolve

    Mls "If I don't go home I have a feeling they'll be watching me even more closely."

    Mls "I'll get my stuff and get going but don't worry Alison..."

    Mls "I'll be back again soon."

    A "Okay."

    M "So, I noticed the whole stock of ice cream is gone."

    M "You wouldn't know anything about that, would you?"

    scene alr477
    with dissolve

    A "Um."

    Mls "Alison ate most of it, she is the ice cream monster, [mc]."

    Mls "Bye!"

    A "*Chuckles* I'm not a monster."

    scene alr478
    with dissolve

    A "Bye [Mls]. Thank you for everything and please be safe."

    Mls "Bye sweetheart, but don't worry about me, I kick ass and carry a gun."

    scene alr479
    with dissolve

    M "(She is really starting to open up. Good girl, Alison.)"

    M "You're not going to give me the I didn't do it look now, are you?"

    scene alr480
    with dissolve

    A "I did it and it was delicious!"

    "" "You laughed out loud as she proudly admitted to destroying that ice cream."

    scene alr481
    with dissolve

    M "So, you like ice cream, do you?"

    A "Yes, I really liked it."

    M "I bet there are a ton of things you haven't tried yet, aren't there?"

    M "Hold that thought. Let me get rid of this jacket first."

    scene alr482
    with dissolve

    M "So, where were we? Oh, right. Stuff you haven't tried yet."

    M "How about watching some shows? You know anime?"

    scene alr483
    with dissolve

    A "Anime?"

    M "Oh, you're either going to love them, or hate them."

    M "Care to find out?"

    scene alr484
    with dissolve

    "" "She pauses and gives you a curious look."

    M "Well, I'm going to put one on and let you decide if you like it."

    scene alr483
    with dissolve

    A "Will you watch with me?"

    M "I planned on it, yes."

    A "Okay! Let's watch animu."

    M "Anime, kitten."

    A "That, yes."
    stop music fadeout 3

    scene black
    with fade

    "" "Meanwhile."

    scene alr485
    with dissolve

    "Henchman 145" "Sir!"

    "Fake hair wearing old guy" "Out with it!"

    "henchman 145" "We lost the cop in the metro, sir."

    scene alr486
    with dissolve

    "Fake hair wearing old guy" "*Glare*"

    "Henchman 145" "I'm sorry sir. She knew she was being followed, and gave us the slip."

    "Henchman 145" "Also, that man is trying to reach you, sir."

    "Fake hair wearing old guy" "You're fired! Now, get out!"

    "Henchman 145" "(God damn it, not again! This is the fifth time this month.)"

    play sound "ringtone.ogg" fadein 6

    "Fake hair wearing old guy" "He wants to talk to me, does he?"

    scene alr487
    with dissolve

    stop sound

    "Fake hair wearing old guy" "Who is it?!"

    "Voice on the phone" "You know who it is."

    "Fake hair wearing old guy" "Of course I know who it is, you nincompoop!"

    "Fake hair wearing old guy" "This is my phone, how can I not know who is calling me?"

    "Voice on the phone" "Then, why did you ask who is it?"

    scene alr488
    with dissolve

    "Fake hair wearing old guy" "I ask the questions here!"

    "Fake hair wearing old guy" "And when I ask, you answer!"

    "Fake hair wearing old guy" "Why did you call me?"

    "Voice on the phone" "You have yet to deliver on the promise."

    scene alr489
    with dissolve

    "Fake hair wearing old guy" "Promise? Can you hear me?!"

    "Voice on the phone" "Yes, I think the entire building can hear you."

    scene alr490
    pause(.3)
    scene alr491
    "Fake hair wearing old guy" "Tell me if you can hear this!"

    scene alr492
    with vpunch

    "Fake hair wearing old guy" "Do you hear that?"

    "Voice on the phone" "Yes, I can still hear you."

    scene alr493
    pause(.5)
    scene alr492
    with vpunch
    pause(.5)
    scene alr493
    pause(.5)
    scene alr492
    with vpunch
    pause(.5)
    scene alr493
    pause(.5)
    scene alr492
    with vpunch
    pause(.5)
    scene alr493
    pause(.5)
    scene alr492
    with vpunch
    pause(.5)
    scene alr493
    pause(.5)
    scene alr492
    with vpunch
    pause(.5)

    "Fake hair wearing old guy" "Let's see if you heard that one!"

    "Voice on the phone" "I can still hear you but what's that noise?"

    "Fake hair wearing old guy" "Who the fuck made this phone?!"

    scene alr493
    pause(.3)
    scene alr492
    with vpunch
    pause(.3)
    scene alr493
    pause(.3)
    scene alr492
    with vpunch
    pause(.3)
    scene alr493
    pause(.3)
    scene alr492
    with vpunch
    pause(.3)
    scene alr493
    pause(.3)
    scene alr492
    with vpunch
    pause(.3)
    scene alr493
    pause(.3)
    scene alr492
    with vpunch
    pause(.3)

    "Voice on the phone" "Are you trying to break your phone?"

    scene alr493
    with dissolve

    "Fake hair wearing old guy" "Yes I am! But the fucking thing is not even damaged!"

    "Voice on the phone" "Is it the new eyephone69 with the built in AI blow-job module?"

    "Fake hair wearing old guy" "Yes, how did you know?"

    "Voice on the phone" "I have the same model."

    "Voice on the phone" "I threw it from my 176 stories high office, along with my secretary..."

    "Voice on the phone" "...when it refused to blow me on low battery and it was still fully functional."

    "Voice on the phone" "Not even a scratch on it, and it was still able to finish me off later."

    "Voice on the phone" "You have a better chance at getting your wife to give you a blowjob than breaking that."

    scene alr493
    pause(.3)
    scene alr492
    with vpunch
    pause(.3)
    scene alr493
    pause(.3)
    scene alr492
    with vpunch
    pause(.3)
    scene alr493
    pause(.3)
    scene alr492
    with vpunch
    pause(.3)
    scene alr493
    pause(.3)
    scene alr492
    with vpunch
    pause(.3)
    scene alr493
    pause(.3)
    scene alr492
    with vpunch
    pause(.3)

    "Voice on the phone" "Still here."

    "Fake hair wearing old guy" "Sorry, I have another call coming through..."

    "Fake hair wearing old guy" "You should pass by the office so we can discuss this further."

    "Voice on the phone" "Wait!"

    "Fake hair wearing old guy" "Sorry, the person you are trying to reach, is done giving a fuck."

    "Fake hair wearing old guy" "Please call back never!"

    scene alr494
    with dissolve

    "Fake hair wearing old guy" "Number one!"

    "Number one" "Sir?!"

    "Fake hair wearing old guy" "Find out who makes these phones and destroy the entire company!"

    "Fake hair wearing old guy" "Do it now! I don't care what it costs, destroy them!"

    scene alr495
    with vpunch

    "Number one" "Uh... Yes, sir!"

    "Fake hair wearing old guy" "And get me a breakable phone! A cheap made in China phone!"

    "Number one" "Sir, almost all phones are made in China, which one?"

    "Fake hair wearing old guy" "Just get me a cheap one that can break!"

    scene alr496
    with dissolve

    "Fake hair wearing old guy" "Your life depends on it, Number one."

    "Fake hair wearing old guy" "If you fail to destroy this company and find me a phone that breaks..."

    "Fake hair wearing old guy" "I will fuck your wife, and your sister!"

    "Number one" "I'm not married sir and I only have a brother?"

    scene alr495
    with vpunch

    "Fake hair wearing old guy" "What?! I will force you to get married, you nincompoop!"

    "Fake hair wearing old guy" "Then, I will turn your brother into a sister!"

    "Fake hair wearing old guy" "This is 2038! People can switch genders with an app!"

    scene alr496
    with dissolve

    "Fake hair wearing old guy" "Do not test me!"

    "Number one" "(Holy fuck, he has really lost it.)"

    "Number one" "Understood, sir!"

    "Fake hair wearing old guy" "Now, get going, or your soon to be sister will be mine!"

    scene black
    with dissolve

    "Meanwh-"

    scene alr495
    with vpunch

    "Fake hair wearing old guy" "Who told you I was done!?"

    scene alr496
    with dissolve

    "Fake hair wearing old guy" "I will turn you into a sister, if you don't show me some respect!"

    "" "As I was saying..."

    scene black
    with dissolve

    "Fake hair wearing old guy" "Get back here, you incompetent nincompoop!"

    "Fake hair wearing old guy" "Do you know who I-"

    "Back at the house."

    scene alr497
    with dissolve

    M "(She seems to like it.)"

    scene alr498
    pause(.5)
    scene alr497
    pause(.5)
    scene alr498
    pause(.5)
    scene alr497
    pause(.5)
    scene alr498
    pause(.5)
    scene alr497
    pause(.5)
    scene alr498
    pause(.5)
    scene alr497
    pause(.5)
    scene alr498
    pause(.5)
    scene alr497
    pause(.5)

    scene alr499
    with dissolve

    A "*Gasps*"

    M "You really like that girl, huh?"

    scene alr500
    with dissolve

    A "Oh, wow! She is so strong!"

    M "Yeah, the little ones often turn out to be the equivalent of a tactical nuke."

    scene alr501
    pause(.2)
    scene alr500
    pause(.2)

    A "Is she going to be able to kill that giant?!"

    M "If I tell you how it ends, then there is little point in watching it."

    scene alr501
    pause(.2)
    scene alr500
    pause(.2)

    A "Oh, she did it!"

    scene alr501
    pause(.2)
    scene alr500
    pause(.2)

    "" "You sigh deeply, as you think to yourself."

    scene alr498
    pause(.5)
    scene alr497
    pause(.5)
    scene alr498
    pause(.5)
    scene alr497
    pause(.5)
    M "(Who would treat someone as sweet and innocent as her the way she has been treated?)"
    scene alr498
    pause(.5)
    scene alr497
    pause(.5)
    scene alr498
    pause(.5)
    scene alr497
    M "(She is like a kid who just got her first console.)"
    pause(.5)
    scene alr498
    pause(.5)
    scene alr497
    pause(.5)

    M "(I'll just have to make sure she never experiences that again and spoil her.)"

    M "(What am I saying? Have I already decided to keep her? Fuck, me...)"

    scene alr498
    pause(.5)
    scene alr497
    pause(.5)
    scene alr498
    pause(.5)
    scene alr497

    A "*Giggles* She is so small, and yet she can drop such a big rock from the sky?!"

    M "(Maybe [Mls] was right after all. Maybe she does have me wrapped around her pinky already?)"

    A "Awwww, it's over!"

    scene alr502
    with dissolve

    M "Yes, for now."

    M "There are new episodes, every week, and a lot of different ones to watch."

    scene alr503
    with dissolve

    A "Can we watch another, please?"

    M "As much as I would love to say yes, you need to start sleeping properly."

    A "Awww! But, I'm not tired."

    M "No arguing, Alison. Bedtime, now."

    scene alr504
    with dissolve

    M "Don't be sad."

    M "You can watch tomorrow, after you wake up, okay?"

    scene alr505
    with dissolve

    A "I wasn't sad. I was just surprised that you care so much, is all."

    A "I'm not used to any of this, you know?"

    M "Well, you best get used to it, because I plan to make sure you live a normal life."

    scene alr507
    with dissolve

    A "Thank you, for everything, [mc]."

    A "I have never been happier in my entire life."

    M "If this is all it takes to make you happy then you and I are going to get along really well."

    scene alr508
    with dissolve

    A "(This still feels like a dream, but with every day that passes, It feels a little more real.)"

    M "(Let's hope she sleeps on the bed this time.)"

    scene alr509
    with dissolve

    "" "You walked her to her room, and said your good nights."

    A "Good night [mc]."

    scene alr510
    with dissolve

    M "(Man, I need to decide what I plan on doing with that poor girl.)"

    M "(I can't just ship her out somewhere and I can't make her someone elses problem.)"

    scene alr511
    with dissolve

    M "(Why the fuck am I complicating matters?)"

    M "(I should just tell her that she can stay here with me.)"

    M "(What's wrong with that?)"

    scene alr512
    with dissolve

    M "(Fuck! I wonder if she will freak out or, even worse, accept and get all excited.)"

    M "(I need sleep, fuck this. I'll decide tomorrow.)"

    scene alr513
    with dissolve

    A "(Today was a really good day.)"

    A "(Melissa giving me all that ice cream.)"

    A "(And [mc] is always taking good care of me... we even watched anime.)"

    scene alr514
    with dissolve

    A "(I really like it here. I hope he will not get tired of me and send me somewhere else.)"

    A "(I wish I could be more useful, learn how to do stuff, and help him in return.)"

    A "(Melissa said that if I stayed here with [mc], alone... Things could get complicated?)"

    scene alr515
    with dissolve

    A "(Ouuum! I wish I knew what she meant. I should have just asked her.)"

    A "(I have to remember to ask her the next time she comes to visit.)"

    scene alr516
    with dissolve

    A "(I wish I could sleep with [mc].)"

    A "*Sleepy* (He makes me feel so safe.)"

    scene black
    with dissolve

    "" "She finally drifted away, into the land of dreams."

    "" "However..."

    scene alr517
    with dissolve
    play music "Fear.ogg" fadein 3

    "" "Her dreams were still haunted by the sounds and voices of those who tormented her."

    scene alr518
    with dissolve

    A "(No, no! Let me go! [mc], help me!)"

    "" "Stuck in her nightmare, her real voice, was but a whisper."

    scene alr519
    with dissolve

    A "(Let me go!)"

    scene black
    with vpunch

    A "*Pants* [mc]? I need to get out of here, I don't want to sleep in here."

    "" "Finally awakened from her nightmare, she made her way towards your room."

    scene alr520
    with dissolve

    A "*Whispering* [mc]?"

    "" "Hearing footsteps approach your room..."

    scene alr521
    with dissolve

    "" "Made you reach for your gun, in haste."

    scene alr522
    with dissolve

    M "Don't move!"

    A "[mc]?! I-it's me... A-Alison."

    M "Oh, Alison! Wait, let me get the light."

    stop music fadeout 3

    scene alr523
    with dissolve

    M "I'm sorry if I scared you. I'm still not used to having people stay with me."

    A "N-no. I... Um... I understand."

    "" "Not realizing that you are not wearing your shirt, you notice that she is staring."

    M "Duh! Let me get my shirt, sorry, sorry."

    scene alr524
    with dissolve

    A "Oh, hehe. I didn't even notice, really, it's fine!"

    M "Oh, I believe you."

    scene alr525
    with dissolve

    "" "You decided to tease her a little, in hopes that it will make her forget the gun incident."

    M "Especially when you make a face like that..."

    M "...and don't even get me started on those cheeks turning red."

    A "Stop teasing me, please."

    scene alr526
    with dissolve

    M "Okay. What brings you here, at this hour?"

    A "I'm sorry [mc]. I just couldn't sleep in that room, I-"

    M "Did you have another nightmare?"

    scene alr527
    with dissolve

    A "Mhm."

    M "Did you come here to ask me to come sit by your bedside?"

    scene alr526
    with dissolve

    A "No, no! I... I was thinking maybe I can sleep with you?"

    M "What?!"

    scene alr525
    with dissolve

    "" "Noticing your tone, she shuts her mouth and blushes, once again."

    scene alr526
    with dissolve

    A "I'm sorry! I'll just leave, good night."

    "" "As she was about to bolt out of your room, you spoke."

    scene alr527
    with dissolve

    M "Wait, wait!"

    M "You just surprised me is all. Twice at that."

    M "You can sleep here for the rest of the night."

    scene alr528
    with dissolve

    A "Really?!"

    M "Yes, yes. But, before you get all excited, I said you."

    M "As for me, I'll sit on that chair, and make sure you sleep safely."

    scene alr529
    with dissolve

    A "Thank you [mc]!"

    M "Don't worry about it. It's only a few more hours, anyhow."

    M "Just get changed first. I'll wait outside until you change into something else."

    A "Okay."

    scene black
    with fade

    "" "A few minutes later."

    scene alr530
    with dissolve

    A "Are you sure you don't want to share the bed? It's a big bed, you know?"

    M "(That's a very valid point and great observational skills, but if I sleep there...)"

    M "(Only one of us will be able to sleep, anyhow.)"

    M "Maybe next time."

    scene alr531
    with dissolve

    A "Do you really mean that?!"

    M "(I have never seen anyone more excited to sleep in my bed, with me in it too!)"

    "" "Not sure what the right answer would be, you paused for a few seconds, then replied."

    scene alr532
    with dissolve

    M "Yes?"

    A "Yay!"

    M "(Yay, she says? Dear god, she is clueless, isn't she?)"

    scene alr533
    with dissolve

    M "(That innocence makes this even harder you know?!)"

    A "Good night!"

    M "Good night, kitten."

    scene alr534
    with dissolve

    A "(He is so kind to me... I wish he would sleep in his bed with me, so I wouldn't feel this bad.)"

    "" "She bounces on your bed with excitment for a brief moment, then tries to go to sleep."

    scene alr535
    with dissolve

    A "(It's a big bed! There is plenty of room, why does he like to sit there instead?)"

    A "(Next time, he said, next time.)"

    scene alr536
    with dissolve

    "" "She falls asleep, at last."

    scene alr537
    with dissolve

    M "(I can't believe my eyes...)"

    M "(There is a gorgeous young woman in my bed, and I sit on a chair, watching her.)"

    M "([Mls] was right after all. This girl will be very complicated.)"

    scene black
    with fade

    "" "Thinking to yourself as you watched the big kitten sleep peacefully, at last..."

    "" "You got some shut-eye where you could, and before you knew it morning had arrived."

    scene alr538
    with dissolve

    "" "Having woken up very early, you let her sleep in and moved on with your morning ritual."

    scene alr539
    with dissolve

    play music "Summertime.mp3" fadein 5

    A "(I slept so good! I need to ask him if I can sleep with him, every night, from now on.)"

    scene alr540
    with dissolve

    A "*Yawns*"

    scene alr541
    pause(.5)
    scene alr542
    with dissolve

    A "(This is real.)"

    scene alr543
    with dissolve

    A "(I really am free.)"

    A "(It's all thanks to him.)"

    scene alr544
    with fade

    A "(I need to figure out a way to thank him.)"

    A "(But what can I do? I've never even slept on a real bed until now.)"

    scene alr545
    with dissolve

    A "(I'm sure I'll think of something, especially if I can stay here long enough.)"

    A "(I feel bad for making him get out of bed, but this was the first time I slept without any nightmares.)"

    scene alr546
    with dissolve

    A "(And now I am smiling for no reason.)"

    A "(What is happening to me?)"

    scene alr547
    pause(.2)
    scene alr546
    pause(.2)

    A "(I should probably get up and try some yoga.)"

    scene alr548
    with dissolve

    A "(I don't think [mc], would mind, would he?)"

    scene alr549
    with dissolve

    A "(No. I don't think he would. He said I could do whatever I want inside the house.)"

    A "(Let me see if I still got it, first of all.)"

    scene alr550
    with dissolve

    A "Oh, my god... This feels so good!"

    A "Aaaaah!"

    scene alr551
    with dissolve

    "" "She starts giggling for no apparent reason, as she stretches."

    A "(I'm going to try talking to the house, and play some music while I work out.)"

    A "(It can't be that hard, can it?)"

    stop music fadeout 3

    scene alr552
    with dissolve

    A "[mc]?"

    scene alr553
    with dissolve

    A "(I guess he is busy, elsewhere.)"

    A "(I'll leave him be.)"

    scene alr554
    with dissolve

    A "Ah! What a beautiful day!"

    A "The sun feels so good!"

    scene alr555
    with dissolve

    A "(Oh, I'm so happy I could dance. Oh, I know!)"

    scene alr556
    with dissolve

    A "(I'll just dance to warm up first, he's not here, so I won't be embarrassed.)"

    scene alr555
    pause(.5)
    scene alr556
    pause(.5)
    scene alr555
    pause(.5)
    scene alr556
    pause(.5)
    scene alr555
    pause(.5)
    scene alr556

    A "Aaaah!"

    A "Okay, I can do better than that. Music, please?"

    "Aida" "What would you like me to play?"

    A "Oh, it talked?!"

    A "Um. Dancing music, please?"

    "Aida" "Here is something you might like."

    play music ["Move_Out.ogg", "Unstoppable.mp3", "Eyes_On_You.ogg", "That_Part.ogg"] fadein 4 fadeout 3 fadein 4 fadeout 3 fadein 4 fadeout 3 fadein 4 fadeout 3

    scene alr555
    pause(.5)
    scene alr556
    pause(.5)
    scene alr555
    pause(.5)
    scene alr556
    pause(.5)
    scene alr555
    pause(.5)
    scene alr556

    A "Woohoo!"

    A "I have not had this much space to move around, in... Well, ever!"

    A "Hahahaha!"

    show shakedatbootay

    A "Woooooooooooo!"

    A "This is what freedom must feel like."

    scene alr557
    with dissolve

    A "(I was so loud.)"

    A "*Chuckles* (I hope he didn't hear me.)"

    scene alr558
    with dissolve

    "" "Having heard Alison's voice and the music playing you decide to check it out."

    M "(What is she doing, I wonder?)"

    scene alr559
    with dissolve

    M "(OOF!)"

    M "(I mean, wow!)"

    scene alr560
    with dissolve

    M "(I should probably stop staring and say something, shouldn't I?)"

    "" "Not aware of your presence, she continued with her workout."

    scene alr561
    with dissolve

    M "(Oh, god! I should definitely say something, but why spoil her fun?)"

    M "(Yeah, I should just let her enjoy her workout, then I can talk to her.)"

    "" "Proud of your very sound and logical plan, you decided to remain quiet, and watch."

    M "(She sure is flexible for such a big girl.)"

    scene alr562
    with fade

    M "(I'm in so much trouble... I simply can't stop myself from staring at her ass.)"

    M "(I feel so dirty, but I can't do anything about it right this moment.)"

    show yoga1

    M "(I am impressed.)"

    M "(This explains the great shape she is in, despite how she has lived.)"

    scene alr563
    with dissolve

    M "(You are killing me here, Alison!)"

    show yoga3

    "" "Still oblivious to your backseat commentary, she continues on with the show."

    M "(So, she figured out how to play music, and is already making herself at home?)"

    scene alr564
    with fade

    M "(This girl is really something.)"

    M "(I guess there is no point pretending anymore, is there?)"

    scene alr565
    with dissolve

    A "*Giggles* I see a kitty!"

    M "(What a coincidence, so do I. I see a big kitty.)"

    show yoga2

    M "(I'll just tell her she can stay with me for good, if she wants.)"

    M "(And whatever happens, happens, I suppose.)"

    scene alr566
    with dissolve

    A "That was really good."

    scene alr567
    with dissolve

    M "(Oops!)"

    M "Hey, kitten!"

    scene alr568
    with dissolve

    A "[mc]! Were you watching me do yoga?"

    M "(I don't want to lie to her.)"

    M "Yes, I was. I didn't want to interrupt your fun, I was also curious."

    scene alr569
    with dissolve

    A "So, what did you think of my moves?"

    M "You are one impressive girl, Alison."

    M "But, right now, there is something important we need to talk about."

    scene alr570
    with dissolve

    A "Is something wrong?"

    M "No need to worry, this is actually good news."

    M "Well, it really depends on how you see it, I suppose."

    A "What is it?"

    label FixMuhSavesBruh:
        scene alr570
        menu:
            "*HINT* The game splits in to three different games here. Love is the real, canonical story."
            "The Harem and Dom paths are fun, alternate routes and shouldn't be taken too seriously."
            "Only the prologue has been remastered so far. Everything else is from the original release."
            "Love interest (Relationship)":

                $ MyAngel = True
                jump myangel
            "Roomie (Harem)":


                $ MyRoomie = True
                jump harem
            "Friend with benefits (Dom/Pet)":


                $ MyPet = True
                jump corupt

    label myangel:
        scene alr570
        menu:
            "The shortcut is not for new players, it takes you forward towards the main girl choice much later in the story."
            "Just Play":
                jump LoveBegins
            "Take a Shortcut":
                jump love4start

    scene alr571
    with dissolve

label LoveBegins:

    M "I've decided that you can stay with me as long as you like."

    A "Do you mean stay, as in stay here, in your house, with you?!"

    stop music fadeout 3

    M "Yes. Stay here with me and I'll do everything I can to make sure you never have to worry about anything ever again, kitten."

    M "Would you like that?"

    scene alr5712
    with dissolve
    play music "myangelcomes.ogg" fadein 5

    "" "At a complete loss for words, yet clearly excited... She charges at you."

    M "(Brace for impact, because here she comes.)"

    scene alr572
    with dissolve
    pause(.5)

    scene alr573
    with vpunch

    A "Yes!"

    "" "She lets out a loud and satisfying yes, as she lands in your arms."

    A "Thank you, thank you! *Giggles* Oh, I'm so excited!"

    A "Can we watch anime later, please?!"

    "" "Looking at her react the way she has, has left you completely speechless."

    scene alr574
    with dissolve

    A "I'm sorry. Did I hurt you?"

    "" "You snap back to reality as she asks you."

    M "No! I'm fine... In fact, I have not been better in a very long time, kitten."

    scene alr575
    pause(.2)
    scene alr574
    pause(.2)

    A "Oh, good!"

    scene alr573
    with dissolve

    A "Can I sleep in your bed, please?!"

    A "I also want to watch some anime later, maybe we can have some ice cream after breakfast?"

    "" "Seeing how excited she still is, you can't help but smile from ear to ear and start laughing out loud."

    scene alr574
    with dissolve

    A "Hey. Are you teasing me again?"

    scene alr576
    with dissolve

    "" "You set her down, before replying."

    M "Alison?"

    A "Um?"

    A "(Your hands are so warm!)"

    M "Look at me, kitten."

    scene alr577
    with dissolve

    M "I'm not teasing you. I am just as happy as you are and to be completely honest..."

    M "I wasn't expecting this kind of reaction."

    scene alr578
    with dissolve

    "" "She smiles at you."

    M "You have a very beautiful smile, did you know that?"

    scene alr579
    with dissolve

    A "Thank you for always being so nice to me, [mc]."

    M "It's hard for me to admit this, especially since we barely know each other..."

    M "But being nice to you, comes naturally to me, Alison."

    M "So there is no need to thank me. Also, we can watch all the anime you like. After breakfast!"

    scene alr574
    with vpunch

    "" "She pounces on you once again, as you say that."

    M "(Oh, this is never going to get old.)"

    A "Can we have ice cream too?"

    M "Ice cream? Hmmm. Have you been a good girl?"

    scene alr573
    with dissolve

    A "*Giggles* What kind of question is that?! Of course I have been a good girl!"

    M "Well, in that case, you can have a little after lunch, not before, okay?"

    scene alr574
    with dissolve

    A "Can I sleep in your bed?"

    scene alr575
    pause(.2)
    scene alr574
    pause(.2)

    M "I'm a little concerned about how excited you are about this, you know?"

    A "Why?!"

    M "Um... Look, Alison."

    scene alr575
    pause(.2)
    scene alr574
    pause(.2)

    M "How do I say this, oh god."

    A "What is it?"

    scene alr575
    pause(.2)
    scene alr574
    pause(.2)

    A "Is it really that strange, [mc]?"

    M "No, I don't think it's strange, it's just that I am not so sure you understand what it means, yet."

    scene alr575
    pause(.2)
    scene alr574
    pause(.2)

    A "I just don't want to have nightmares anymore and sleeping in your bed is the only place where I don't get them."

    A "Why is that a bad thing? Am I missing something?"

    M "You know what kitten?"

    scene alr575
    pause(.2)
    scene alr574
    pause(.2)

    A "What?"

    M "You are absolutely right! If you, as an adult, want to sleep in that bed willingly..."

    M "Then I have no objections!"

    scene alr573
    with vpunch

    "" "She bounces up and down with excitment."

    A "Yay! Thank you, [mc]! Now I won't have to feel so guilty about you sitting on that chair."

    M "(Sweet baby Jesus. She is like an oversized baby on a sugar-rush but I love it!)"

    M "You did that for me?"

    scene alr574
    with dissolve

    A "Of course silly! I'm not stupid you know?!"

    A "I know that sleeping in the same bed is for boyfriend and girlfriend, [Mls] told me."

    scene alr575
    pause(.2)
    scene alr574
    pause(.2)

    A "And I don't care about stupid rules, I just don't want you to sit on a chair while I sleep!"

    M "(Okay... She just completely blew my mind, and destroyed any and all of my assumptions.)"

    M "So... You still don't mind sleeping with me, even though she told you?"

    scene alr575
    pause(.2)
    scene alr574
    pause(.2)

    A "Nope! When I am near you, I feel nothing but safe and happy."

    A "That can't be a bad thing, can it?"

    M "Look at you, being all smart."

    scene alr575
    pause(.2)
    scene alr574
    pause(.2)

    M "Come here you!"

    A "*Giggles* Careful, you're going to drop me!"

    scene alr579
    with fade

    M "Not a chance."

    A "*Exhales happily* You feel so snuggly. *Rubs cheek on your chest*"

    M "Hey, hey, now. No time for naps."

    A "Awww. Why not?"

    M "Time for breakfast, come now, let's go."

    "OMVN" "The Alison some of you have played in the past, is getting a major love-path remaster."

    "OMVN" "With that in mind, I ask that you show patience and hopefully your continued support..."

    "OMVN" "As I pick up from here on the next available slot for remaster."

    "OMVN" "Past this point you are playing the OG version, which may not curremtly fit with the current prologue on places."

    "OMVN" "In other words, this is now a work in progress remaster for these parts."

    "OMVN" "They will be remastered/remade to fit the pace and quality of the prologue."




























































































































    stop music fadeout 2

    jump afterchoice



label not18:

    "OneManVN" "No deal... Come back when you are of legal age. *Rekt*"

    $ renpy.quit()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
