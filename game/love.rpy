label relationship:

    scene l1
    with fade

    M "(Oh man, they're both so stubborn. I couldn't hurt their feelings and choose one over the other.)"

    M "(I'm just glad that they're at least peaceful while they sleep.)"

    M "(Well, time to get up and start looking for Melissa again.)"

    M "(Now let's see if I can get out of here without starting a war.)"

    M "(Shadow is pressing her ass so hard against me.)"

    M "(Fucking hell, what have I done to deserve this? This is torture!)"

    scene l2
    with dissolve

    "You manage to very carefully extract yourself from the two beautiful women."

    M "Wait a second... who's in the shower?"

    play music "popstar.ogg" fadein 5

    scene l3
    with fade

    M "(Fuck! I completely forgot about Caroline. Gotta get out of here before she notices me.)"

    M "(Well done, [mc], as if one wasn't enough. Now you have three to deal with.)"

    scene black
    with fade

    M "(I'll go get some coffee while she finishes.)"

    scene l4
    with dissolve

    M "(Damn, I still need to take a piss and of course someone is here again.)"

    M "(Is it her again? Fuck my life, time to go again before she notices.)"

    scene l5
    with fade

    M "(Too late.)"

    C "*Gasp*"

    C "[mc]?"

    M "Sorry Caroline, I didn't know it was occupied, I just really had to go."

    M "I'll be going now. Again, I'm sorry!"

    scene l6
    with dissolve

    C "No, it's okay, [mc], you just surprised me. I didn't expect anyone to be up this early."

    M "Yeah, Shadow and Alison are still asleep. It took an hour to get them to agree on sleeping arrangements."

    C "Haha, well, I guess in the end you lost that fight, didn't you?"

    M "Haha, yes, afraid so. I gave up trying to convince them. I woke up sandwiched between both of them."

    M "(I'm not complaining but she doesn't need to know that.)"

    C "Well I'm glad Alison is still alive and well. And it's thanks to you, I'm told."

    M "In all honesty, all I did that day was my job. So there's no need to thank me."

    C "Alison thinks otherwise. Anyway, I better go get dressed."

    M "Um, yeah. I'll talk to you in a bit. I need to ask you something."

    C "Sure, I'll be downstairs, [mc]."

    M "Okay, see you shortly."

    scene l7
    with fade

    M "(Goddamn it, [mc], you just had to look, didn't you?)"

    stop music fadeout 3

    M "(Well, I am still a guy.)"

    scene l8
    with dissolve

    play music "fantastic.ogg" fadein 3

    C "Hello again, [mc]. Good morning."

    M "Yeah, good morning to you too, Caroline. Did you sleep well?"

    C "Yes, thank you. After those two stopped shouting, that is."

    C "Why were they fighting to begin with?"

    M "(Oh boy, how do I explain this?)"

    menu:
        "Be honest with her":

            $ BeHonest = True
            jump honest
        "Sugar-coated truth":


            $ SugarCoat = True
            jump sugarcoat

label honest:

    M "Well, Alison told me she feels safe sleeping in my bed. After what she's been through she still has nightmares."

    M "I tried to get her to sleep in her own bed, but she couldn't."

    M "So I let her choose where she wants to sleep and now she can't sleep peacefully anywhere else."

    C "In other words, you spoiled her."

    M "Well, when you put it like that... I suppose I did spoil her, yes."

    M "Shadow, on the other hand, whose real name I can't tell you..."

    M "Trust me, it's complicated. She's the only one who decides who knows her real name."

    C "She's quite strange. But, okay, I guess I understand."

    M "She's very competitive, although she may have met her match with Alison."

    M "Alison seems to be really stubborn when it comes to certain things."

    C "I honestly wouldn't know. As strange as this may sound I never really got to know my sister that well."

    M "Believe me, she has told me enough about it to know that it's not strange at all."

    C "I'd like to know more about what happened to her, when you get a chance."

    M "Yeah, that's what I wanted to talk about. You might want to sit down for this, it's not easy to hear."

    C "Okay, but I want some tea first. You want me to bring you anything?"

    M "Sorry, I spaced out for a second there. I'll take a coffee, thanks."

    C "Hehe, well, I'll go get you a coffee then."

    M "Thank you! Cream and two sugars for me please."

    M "(What a sweet girl. They are similar in some ways but still so different, it's unreal.)"

    C "Okay, just take a seat and i'll come join you in a minute."

    jump honestyjump






label sugarcoat:

    M "Well, I don't know exactly why but I it seems to have something to do with them being competitive."

    M "Shadow is very competitive. And Alison can be really stubborn about some things."

    M "A lot of it is my fault, to be honest. I let them have their way too often."

    C "So, does this mean I can sleep in your bed too, if I am stubborn enough?"

    M "Huh?! Well, I uh... N-"

    C "I was only joking, [mc]. I can see why my sister speaks so highly of you and why she likes you."

    C "You're funny and, to be honest, kind of a pushover. I think we'll get along just fine."

    M "(Listen to this girl! She acts so shy but then talks like a grown woman.)"

    C "You said you wanted to talk to me about something?"

    M "Yeah, sorry. I spaced out for a second there. You caught me off-guard and it's early, haven't even had my coffee yet."

    C "Hehe, well, I'll go get myself a tea and you a coffee, how does that sound?"

    M "You would? Well, thank you! Cream and two sugars for me please."

    C "Okay, just take a seat and I'll come join you in a minute."


label honestyjump:
    scene l9
    with fade

    C "How is your coffee, [mc]?"

    M "Best I've had in a while. Thanks, Caroline."

    C "You're welcome. So, what did you want to talk about?"

    M "I wanted to talk about your father and Alison's past if you don't mind."

    C "Well, okay, I suppose but first, tell me what happened to my sister?"

    M "I'm sorry, Caroline, it's probably best that she tells you herself."

    C "Okay, I can respect that."

    M "So, what can you tell me about her childhood, your parents, and their relationship?"

    M "I'm trying to figure out if Alison is suffering from something that may have happened back then."

    C "Well, years ago, my mother told me that before Alison was even born, she was sick."

    C "She sought help until she found my father and he helped Alison survive birth."

    C "Neither one of them would ever tell me any details, so I don’t know a lot about it."

    C "But I do know that she has a rare condition. Sometimes she walks around late at night, for example..."

    C "Exploring the house, as if she has never been there, or worse, asking questions about obvious things."

    C "One night, I caught her and she stared at me. Her eyes... they were... strange..."

    C "They were gentle, but brighter. As if they were glowing. And she's very curious."

    C "I can't really explain the thing with her eyes. My mother told me that’s just part of her condition."

    C "Beyond that, all I know is that they locked her in the basement for her own safety."

    C "She was homeschooled by someone my father arranged. Some old lady he knows."

    C "I wasn't allowed to visit her much. But I would sneak in every once in a while."

    C "I remember one night my father caught me and he got so angry! It terrified me."

    C "The way he was, I started to question a lot of things. So I went back and this time..."

    C "I went all the way down to the basement. There she was, inside a cage."

    C "I was so worried, I started to cry. They had my sister locked in a cage, like an animal."

    C "She told me to leave, and not get caught."

    C "Her exact words were, \"Leave Caroline, please! And don’t come back ever again.\""

    C "To this day, I don't know why she insisted that I leave, but the look in her eyes was heartbreaking."

    C "So, I stopped going down there. Then one day my mother died. Father said someone shot her."

    C "He said that someone came in and kidnapped Alison, killed my mother, and nearly killed him too."

    C "That’s pretty much all I know about it. I hope that was helpful in some way, [mc]."

    M "(This poor girl deserves to know the truth. Alison needs her love more than ever right now.)"

    stop music fadeout 3

    M "I'm going to tell you what I know and what Alison has told me."

    play music "alisonsfailure.ogg" fadein 5

    M "I'll only tell you as much as I can, though. The rest you'll have to ask her."

    M "I don't know exactly why yet, and trust me, I'm trying to figure it out..."

    M "But Alison was caged for some reason that had nothing to do with her safety."

    M "Of that much I am certain."

    scene l10

    C "(Now I'm really starting to worry. What does he mean by that?)"

    M "May I ask if you know what your father's profession was... is... at the moment?"

    C "I think he's a scientist or a researcher of some kind. I'd often hear my parents arguing over things."

    C "I couldn't make out what they were saying at the time but, only a few days before mom died and Alison disappeared..."

    C "I heard my mother clearly say, \"This is the last time, research be damned\"."

    M "Well, that certainly helps to explain some things, I suppose."

    M "But, my guess is that Alison is not really your sister. Is that an accurate assumption?"

    scene l11

    C "What?! Why would you even think something like that?"

    M "Caroline, I realize that this may come as a shock to you. I really do."

    M "But, think about it for a second. What parent would cage their own child?"

    M "And, not only keep her caged for nearly 15 years, but also experiment on her?"

    C "..."

    scene l12

    M "I believe both your parents were sick people who needed help."

    M "Or perhaps scientists in pursuit of \"science at all costs\""

    M "It could also be that your father was the only real lunatic in the family."

    M "(Well, the bait is set, let's see what comes up.)"

    M "What do you think? Would you disagree with what I have said?"

    scene l13
    with fade

    C "You want to know what I think? I think you need to mind your own business!"

    C "You know nothing about my parents, you know nothing about my sister or me!"

    C "Who do you think you are? Alison is my sister, not yours! I don't need you to tell me who she is to me."

    C "She is my big sister and nothing you say, do, or find will ever change that!"

    C "My parents were not perfect, but they loved me, they took great care of me."

    M "And what about Alison?! Did they take great care of her too?! Answer me, what's the matter?"

    C "..."

    C "I don't care about what you say. Alison is my big sister."

    C "Who are you to tell me otherwise? You're just some guy she has known for a few days."

    M "And you've known her for much longer than I have, right?"

    C "..."

    M "Thought so. I'm not trying to upset you. That's not my intention. Look, I'm sorry, Caroline."

    M "Believe it or not, I care about her very much. I'm not angry at you, I'm angry at your parents for the way she was treated."

    M "The reason I pushed you a little, was simply because, well, let's just say-"

    M "I needed real answers, with real emotion behind them, do you understand?"

    M "I pushed you to get a real response. Since, like you said yourself, I don't really know you, nor do I know your parents."

    M "I only know what Alison has told me and I'll take her word over anyone else's."

    C "I..."
    stop music fadeout 2

    scene l14
    with dissolve

    play music "Frank Nora.ogg" fadein 8

    A "Good morning, [mc]! Hey, Sis!"

    M "Good morning kitten, did you sleep well?"

    C "(Kitten? That used to be my nickname! Wait, could he know? Is he trying to piss me off?)"

    C "(Well, I don't want to upset Alison, so I'll go along with his story for now.)"

    C "Morning, Sis!"

    M "*Whispers* Can we agree to disagree for now, so we don't upset Alison?"

    C "*Whispers* Don't you mean your kitten? And yes, I agree."

    M "(What the fuck? Was that jealousy? Way to go, [mc]. Just keep on digging that hole.)"

    scene l15
    with fade

    M "(God, they're so different. I see it now. Caroline is serious and somewhat aggressive.)"

    M "(Hell, I'd even go as far as to say she's confident in herself.)"

    M "(On the other hand, we have that smile to die for, and a body to kill thousands over.)"

    M "(Whoa, okay, [mc], less thinking with your dick, more with your brain.)"

    C "Good morning, Sis. I see you finally managed to get some sleep."

    C "(I can't stand this anymore! What if he is right about all of it?)"

    scene l16
    with dissolve

    C "I'm so sorry, I love you, Alison. Ever since we were little, you were my big sis."

    C "I may not have gotten to spend much time with you growing up, but I promise-"

    C "That will change from now on. I love you so much."

    A "C-Caroline? I love you too, Sis. My little kitten!"

    scene l17
    with fade

    C "(She remembered! I'm so happy. Maybe he's not such a bad guy after all.)"

    C "(I'll have to ask Alison about what really happened. Sure my parents were strict...)"

    C "(Perhaps even weird. But could they have been as cruel to her as he says?)"

    C "(God, I hope not. I'll talk to her later when we get a chance to be alone.)"

    A "Mmm, I love you, Caroline. Please don't cry anymore. Your big sis will protect you."

    A "I'll never leave your side again. I gave mom my word."

    C "You did? *Hugs her sister even tighter* I love you, Sis."

    C "I'm going to get cleaned up, and I'll see you later, Alison. I think we need to talk."

    A "Sure thing, Sis, come find me whenever you're ready. I'll be right here."

    A "*Thank You*"

    M "*Nods head with a smile*"

    scene l19
    with dissolve

    A "(I wonder what they were talking about just now. She seemed really shaken up. I'll have to ask [mc] and see what's up.)"

    A "(But that felt great. I've missed her so much. She has grown so fast.) *Smiles at [mc]*"

    M "(Someone please help me. That smile is going to be the death of me.)"

    M "(God, just looking at her makes me want to pinch myself to make sure I'm awake.)"

    A "You look like you are lost in thought as usual, [mc]."

    A "What's on your mind? And what were you two talking about just now?"

    M "Nothing much really, I wanted to know a little more about your parents as well as your past. Figured I'd ask her about it."

    A "And? Did you get the answers you were looking for?"

    M "Yeah, I guess I did."

    A "She seemed a little upset. What happened, [mc]?"

    M "Look, Alison, you know I really care about you, right? I'm just trying to find out why you were treated so cruelly all these years."

    M "That's all, kitten. I promise you that I'm not trying to upset her."

    scene l85
    with fade

    A "I know you care about me. And that's why I want her to like you as well. So, please tell me everything."

    M "I'll tell you all that matters, okay?"

    A "Okay. *Squeezes a little tighter*"

    M "I wanted to know what your parents did for a living and why you were kept in a cage."

    M "She got upset when I told her what I thought and I got upset too because the thought of you being in that cage still infuriates me."

    M "I can't help it. Trust me, I've tried to let it go. When you and Melissa were kidnapped, I thought I had lost you. I went crazy."

    A "*Whispers* I'm so sorry for putting you through that again."

    M "You have nothing to be sorry for. I'm the one to blame. I should have never left you alone."

    M "I promise you that no matter what happens, you will never be caged again."

    A "*Nuzzles her head against your cheek*"

    A "*Whispers* Thank you for making me feel like a human being again."

    M "(Fuck. I can't take this anymore. It's now or never, [mc].)"

    "" "Overwhelmed with emotions, you decide to..."

    menu:
        "Kiss her":

            $ Kissedher = True
            $ RPa += 1
            jump kiss

label kiss:
    scene l20
    with dissolve

    A "Umm"

    M "(Fuck it, no matter what happens now, I've already made up my mind.)"

    M "(No regrets.)"

    scene l21
    with vpunch

    A "You!"
    stop music fadeout 2

    M "(Holy fuck!)"

    scene l22

    play music "myangelcomes.ogg" fadein 5


    M "Whoa! Alison?! Had I been a second slower, you could have killed me!"

    M "Okay, I get it. I'm sorry, I shouldn't have kissed you so suddenly."

    M "But I couldn't take it anymore. I'm sorry, okay? I won't do it again."

    M "Not if you try to kill me over it, that is. When the hell did you get those deadly reflexes, anyway?"

    M "(Wait a minute, what the fuck is happening here? What's up with her eyes?)"

    M "Alison? Are you okay?"

    A "Hmmm, So you are the one who keeps troubling her thoughts. *Smiles* Very curious indeed. I am intrigued."

    M "Huh? What are you talking about? What's going on with your eyes?!"

    A "Hmmm, I can certainly see why she is confused. Fit, young, and attractive by human standards."

    M "Human standards? What are you talking about and why are you looking at me as if you don't know who I am!?"

    A "Hmmm, you seem healthy enough for what's required."

    M "What? Hello! Is anybody home? I'm talking to you!"

    A "Shouting is not necessary. My hearing functions are fully operational. I can hear everything within a radius of one-hundred meters clearly."

    M "Oh, you can, can you? Prove it. Where is Caroline? Where is Shadow? What are they doing or saying right now? Come on, smartass."

    A "What a strange creature. If proof will convince you, then I shall prove it. Searching. Shadow, target located."

    A "Currently in what you call the shower. Twelve point five meters from our position speaking to herself about someone named [mc]."

    A "Searching, Caroline, target located. Currently violently attempting to open a can."

    A "Very strange indeed. Do humans always rely on violence to open things?"

    scene l86
    with fade

    Sh "That meanie [mc]. He allows that fat butt to sleep with him without a second thought."

    Sh "It was a battle to get him to say yes to me, though. What does she have that I don't?"

    Sh "Besides her big melons and huge butt, that is. Ungh, she makes me so mad! Why is this stupid water not working?!"

    Sh "Oh, I didn't actually turn it on... That may have something to do with it."

    scene l22
    with fade


    A "You humans are very complicated. Her intelligence readings are superb."

    A "Yet her current behavioral analysis matches that of a teenage human female."

    M "Okay, seeing as there is no way for me to actually confirm or deny any of this."

    M "I'm going to ask one last time. Who or what the fuck are you? You're starting to test my patience now."

    scene l24
    with flash

    A "Your reaction time is surprising for a human. You managed to move, just a few inches, but impressive all the same."

    M "(What the fuck? In the time that I blinked she got so close... What is going on here?)"

    M "(Did my kiss break Alison? How is that even possible? People don't break.)"

    M "(Well, at least not like this, anyway. I think I need to get out of here.)"

    A "You seem distressed. Do not be alarmed, I mean you no harm."

    A "She cares for you and that is all that matters right now. I could not harm you, even if I wished. Do you understand?"

    M "Yes, I think I do. By she, are you referring to Alison?"

    scene l25
    with fade

    A "Hmmm, this is indeed adequate, perhaps more than necessary for her."

    scene l26

    M "Whoa! Hands off the merchandise! And don't get any crazy ideas."

    M "You try to resize that and I don't care who or what you are."

    M "I'll resize you to pieces. You get me, miss glows-a-lot?"

    M "What the fuck are you doing? You can't just grab someone like that."

    A "Interesting. \"Fuck\", you've used it twenty times in the last day alone. Searching..."

    A "Definition... To have sexual intercourse. I see that you are clothed. Perhaps incorrect?"

    A "Curious. Searching... What the fuck - An expression of extreme surprise."

    scene l27

    A "It would seem the act surprised you. Yet your human reproductive organ..."

    A "Seems fully responsive to my touch. It reacted as expected, yet you resist."

    M "No shit, Sherlock. I'm a guy after all. But that doesn't mean you can touch without asking."

    A "I am... amused? Is that the correct word?"

    M "Well, yes, and I'm glad you're amused and all. But I'm not amused."

    A "May I look at and further examine your reproductive organ?"

    M "No! You certainly may not."

    A "*Repeats YOUR words* That doesn't mean you can touch without asking?"

    A "Did I not ask politely enough? May I please look at and further examine your reproductive organ?"

    M "No. I said no. You can't just ask someone you barely know to do that."

    A "Then I shall attempt again when the requirements are fulfilled."

    M "(Why is she so obsessed with my dick? I don't want her to resize it!)"

    M "You still haven't answered my question. Who or what are you? What happened to Alison?"

    A "I... We are one. I am her and she is me. Does that answer your question?"

    M "Not really! Are you Alison?"

    A "Name. I see. You humans identify by name."

    scene l24
    with flash

    A "You may call me Alice. That was the name I was given many years ago."

    M "Fuck! You're fast. (This is kind of scary, but also exciting.)"

    M "I give up, this is too much. Hello, Alice, nice to meet you. My name is [mc], in case you didn't already know."

    A "You are as her stored memories and emotions describe you. I am very curious. I would like to know more about you."

    A "As well as why you do many of the things you do but our time has come to an end."

    A "Alison awakens. I will return again, [mc]."

    M "Wait a minute!"


    scene l28
    with dissolve

    M "Hey! Get back here! I'm not done with you yet!"

    M "Who told you that you could just leave whenever you want? And who said you could come back?!"

    A "Why are you screaming at me, [mc]? My head hurts. What happened?"

    M "Alison, I'm sorry. I didn't mean to upset you."

    A "(Oh my god, it was real. He really did kiss me. Did I black out?!)"

    scene l29
    with fade

    A "*Shy smile* Why you, how could you! You can't just kiss me out of nowhere!"

    M "I'm sorry. I won't do it again, I promise."

    A "That's not what I meant. I don't care if you do it again!"

    A "(God, this is so embarrassing. I'm getting out of here while I still can.)"

    scene l30
    with dissolve

    M "(What the fuck... Was she smiling at me?)"

    M "(Damn. She's killing me right now.)"

    M "(\"I don't care if you do it again\"? Wait, did she mean..?)"

    scene l31
    with fade

    M "(Women... I'll never be able to understand them. But I'll keep trying!)"

    M "(Whatever that thing was, it didn't seem hostile although, it looks like Alison has no idea what happened.)"

    M "(I'll have to find out more about it before I mention it to anyone else.)"

    M "(My first priority right now is finding Melissa.)"

    stop music fadeout 2

    Sh "Hey hey hey!"

    scene l32

    Sh "Watch where you're going, you RHINO!"

    play music "king.ogg"

    A "(That was my very first kiss. Sure, that idiot [mc] surprised me...)"

    A "(But my heart was beating so fast, I think I blacked out from it.)"

    A "(I couldn't even be angry at him. I almost smiled... so embarrassing.)"

    A "(Haha, strangely enough, that felt a lot better than I had ever imagined.)"

    scene l33

    A "(I wonder, will he try to kiss me again?)"

    Sh "Hey, I'm talking to you, fat butt! You'll break the stairs running like that."

    A "(Do I want him to? I think so. I liked it. I'll tell Caroline about it.)"

    A "(See what my sis thinks about it. I wonder if she's ever kissed a boy before?)"


    scene l34
    with fade

    Sh "Grrrr (I'm really considering just shooting her.)"

    Sh "(I could just say I was cleaning my rifle and she pulled the trigger.)"

    Sh "(Sorry, sir! It is indeed a tragedy, but she is gone now. Shame, really!)"

    Sh "*Yawns*"

    Sh "(Ehh... I don't hate her, to be honest. Plus, [mc] would kill me.)"

    Sh "(He knows my guns are never left loaded.)"

    scene l35
    Sh "(I'll have to figure out a way to start getting along with the rhino.)"

    Sh "(If [mc] gets mad at me, it'll ruin everything.)"

    Sh "(Her younger sister is cute and seems more mature. I bet she will be easier to get along with.)"

    scene l36
    with fade

label nokissykissy:
    scene l36


    Sh "You seem distracted, sir. Is everything okay?"

    M "I'm just thinking about Melissa and a few things that happened recently."

    Sh "Is there anything I can do to help, sir?"

    M "You can start by not calling me sir anymore. We're no longer in Delta."

    Sh "Just because we're not currently on active duty..."

    Sh "Doesn't mean that you are no longer worthy of my respect, sir."

    M "I forgot how many times I've tried having this conversation with you already."

    M "You are as stubborn as you are loyal, Aiko."

    M "I'm glad to have your skill, something only rivaled by your beauty, on my side."

    scene l41
    with dissolve

    Sh "Pleasure to be of service, sir! You have never called me by my name so casually."

    scene l37

    Sh "It sounds nice coming from you. Thank you, [mc]. There I said it, okay?"

    M "Haha, that's much better. You can call me [mc] or sir, really."

    M "It's your choice. I just figured it would be easier for you."

    Sh "Well I'm no slacker, sir. So I'll stick to what I know best, if you don't mind."

    M "Not at all. In fact, that's what I need from you today."

    scene l38

    Sh "*Stretches and yawns*"

    scene l39
    with fade

    Sh "Sorry, I just finished taking a shower not long ago and I'm still sleepy."

    M "(Damn, that thing wasn't lying about her hearing.)"

    scene l40

    Sh "Then the rhino almost ran me over!"

    M "*Glares* Aiko."

    scene l37

    Sh "Hehe, Alison is what I meant to say, of course!"

    M "Haha, that's better."

    scene l39
    with fade

    Sh "Seriously, though. What was that all about?"

    Sh "She completely ignored my existence! Like I wasn't even there. What happened to her?"

    M "Long story, one that you don't need to concern yourself with."

    Sh "I.. (Grrrr) Yes sir, I understand. So, what did you need from me today, sir?"

    M "I need you to look after the girls. You understand what I mean right?"

    scene l41

    Sh "Absolutely sir! I'll make sure no harm comes to them. You have my word."

    M "That's all I needed to hear. You remember how many times I've doubted you?"

    scene l39
    with fade

    Sh "Umm, zero?"

    M "Correct. And do you know why that is?"

    Sh "Because you know I would never let you down, sir."

    M "I've trusted you with my own life, Aiko, because you are extremely competent."

    Sh "(He called me Aiko again! It's not as bad as I thought it would be.)"

    M "But I need you to be extra careful today. This is not some babysitting job."

    M "I'm serious. I'm sure you have already done some digging on your own."

    scene l41

    Sh "Guilty as charged, sir. I can tell that the girl... Alison, I mean..."

    Sh "She seems to be of high importance to some people with political connections."

    Sh "Looking at her, however, doesn't really convince me. I just don't understand."

    M "There may be something more than meets the eye with her."

    M "Trust me and please do not leave her alone or let her go outside until I return."

    Sh "I'll make sure to follow your instructions, sir."

    M "Alright then, send me all the intel you gathered on Melissa."

    Sh "Will do. I'll be going up to watch the girls now."

    M "You're the best."

    scene l37

    Sh "You know it! They don't call me Shadow for no reason. *smiles happily*"

    Sh "Those girls will be kept safe at any cost. So, you go find your partner."



    scene l41

    Sh "Now if you'll excuse me, sir."

    M "On your way then."

    scene l42
    with dissolve

    M "(Honestly, her beauty is only really surpassed by how dangerous she is.)"

    M "(The last idiot who underestimated her was dead before he could blink twice.)"

    Sh "(He trusts me with his life! Take that, you rhino.)"

    scene l43

    M "(Plenty of foolish people think women are less capable than men.)"

    M "(But I'd put my money on her speed, skill, and aim over anyone else.)"

    M "(She's an expert in four different types of martial arts, as well as being an excellent sniper.)"

    M "(And all of that at such a young age. She really is incredible.)"

    M "(And she is barely older than Alison. Her age does show in some things, though...)"

    M "(Her temper for one. She's extremely competitive.)"

    M "(She's never had a guy make it past the first date. They always feel threatened by her.)"

    Sh "(And, up we go!)"

    scene l44
    with fade

    Sh "(I knew this was a good idea, ever since I decided to shadow him.)"

    Sh "(Well, more like stalk him, if I'm being honest with myself.)"

    Sh "(But he doesn't need to know that! I just want to make sure he is okay.)"

    Sh "(Time to go check on the sisters.)"

    scene l64
    with dissolve

    M "Well, now that the girls are taken care of, it's time to call Chris."

    stop music fadeout 2

    scene l45
    with fade

    play sound "ringtone.ogg"

    K "Who's calling, baby?"

    c "That's a number only [mc] knows, love."

    K "Ah yes, almost forgot about that. Say hello to him for me, will you?"

    c "Will do, sweetheart."
    stop sound

    scene l84

    c "Hey [mc]."

    M "Hey Chris, how are you guys doing?"

    K "*Distant* Hey [mc]!"

    M "Hey Kate."

    c "So what's up, [mc]? I know you wouldn't call this number if it wasn't important."

    M "I'm sorry to bother you, Chris. I need your help... again."

    c "Just tell me what you need, [mc]. No worries."

    M "Melissa, Chris. I still haven't found her. I've sent you her last location."

    M "Someone I know and trust followed her trail there, but it went cold."

    M "Anything you could do would be greatly appreciated."

    c "No problem, [mc], I'll send you a text as soon as I have something."

    M "Thanks, Chris. I'll arrange something once this is all handled, so we can meet."

    c "Sounds good. Kate really wants to meet the girls, haha."

    M "Yeah, well tell her there are four of them, once Melissa is found."

    c "Four? Weren't there just two last time? Busy man as always, I see. It's complicated, I know! Okay, I'll get right on it."

    M "Haha, you know me too well. Bye, Chris."

    scene l64
    with fade

    M "Time for me to head out and meet Chris. I really hope he has good news for me."

    M "I'll never forgive myself if she gets hurt... Or worse. I can't even think of that right now. I refuse to."

    M "She's as tough as I am, probably tougher. I'll just go and bring her ass home."

    scene dungeon1
    with hpunch

    Mls "You old perv, I'll make you regret ever coming that close to me."

    scene black
    with vpunch

    play sound "punching.ogg"

    Jm "Ow, my face! How did you get free?"

    Mls "Did you think your cheap toy cuffs would hold me?!"

    play sound "punching.ogg"

    Jm "Guards! Aide moi!"

    scene l46
    with fade

    Mls "Gaaaaaaah! I am really considering killing them instead of just hurting them."

    Mls "That fucking pervert almost touched me. Disgusting little man."

    Mls "I should have broken his neck."

    "Gelée" "Well, well, looks like you are tougher than we anticipated."

    scene l47

    play music "macaroon5.ogg" fadein 8

    Mls "Bring it on, then!"

    "Cacahuète" "Appel au secours. Zis one looks like trouble."

    "Gelée" "Heh, we don't need to call for help, brother, just watch me."

    "Cacahuète" "You are always so brave, bro. I watch you."

    scene l48
    with fade

    Mls "You just wait, Frenchie. I'll come back for you."

    Mls "You first, tough guy!"

    scene l49

    "Gelée" "Let me show you how it's done, little girl."

    Mls "Grrrr."

    scene l50

    "Gelée" "And kick! Oh no, she jumped over."

    Mls "Say goodnight, little princess!"

    "Cacahuète" "I help you, little bro!"

    scene l51
    with vpunch

    "Gelée" "You idiot! I am only 2 minutes younger than you!"

    "Cacahuète" "Argue less, little brother, fight more!"

    "Gelée" "Ow, my face! Oh, that fucking hurt! I'm going to kill you!"

    "Cacahuète" "Oh no, I missed too."

    scene l52

    Mls "Feeling lonely already, are you? Don't worry I'll reunite you soon enough."

    "Cacahuète" "I am not some cheap American guard! I will kill you, if I have to."

    Mls "If you manage to touch me, you can go ahead and kill me, sweetheart."

    scene l53

    "Cacahuète" "Now you die!"

    Mls "(I'm going to really hurt this one. Hope he doesn't die on me. Looks fragile.)"

    "Cacahuète" "Stupid woman, nowhere to run to. Zat is a wall."

    "Cacahuète" "Prepare to die now!"

    "Gelée" "I'm coming to help you, bro. Get her! Don't let her escape!"

    scene l54

    "Cacahuète" "Oh mon Dieu, look at zat magnificent body. Zose tits are so big!"

    "Gelée" "Hey, you dumbass, stop staring at her tits and get her!"

    scene l55
    with vpunch

    "Cacahuète" "Ow, she is going to crush me! Help me!"

    "Gelée" "Serves you right, you moron. (Oh my god, she is incredible!)"

    scene l56
    with vpunch

    "Cacahuète" "Ow, mon Dieu, my back, my head! You are a useless brother!"

    "Gelée" "(I can't even find the strength to fight her.)"

    Mls "You're next, princess!"

    "Gelée" "(She is like a lioness, so graceful, so vicious. No, like an Amazon queen!)"

    scene l57

    "Gelée" "I'm getting out of here, fuck this."

    "Gelée" "I don't even want to fight you anymore, my beautiful Amazon queen."

    "Gelée" "We barely get paid to begin with, but it was fun."

    Mls "Sweet talking me won't save you, princess."

    Mls "Get back here!"

    scene l58
    with vpunch

    "Cacahuète" "(I am so happy I have my phone with me.)"

    "Cacahuète" "(No one will believe zis amazing body. I take picture quietly.)"

    "Cacahuète" "(Now, time to play dead. Good luck, brother, you coward.)"

    scene l59
    with hpunch

    Mls "You aren't going anywhere! Not until I say so."

    "Gelée" "Ouch, you crazy woman! Are all American women crazy like you?"

    scene l60
    with fade

    "Gelée" "Fuck! You're very fast for such a big girl."

    Mls "Did you just call me fat?! Now you're really going to get it!"

    "Gelée" "Oh no, no, no, no. I mean big, like Amazon goddess, big and beautiful."

    Mls "Keep talking."

    "Gelée" "You are like a dangerous lioness. Brave, graceful, and vicious."

    Mls "Your compliments could use some work. But I'll give you points for trying."

    "Gelée" "Zis mean I can go, yes?"

    Mls "Not so fast, little princess. First, where are my clothes?!"

    "Gelée" "You really need clothes? I mean you look so sexy!"

    Mls "How badly do you want to die?"

    "Gelée" "Your clothes are upstairs! Inside guard room, in a box, maybe."

    "Gelée" "Please, I give you what you want. Can I go now, my beautiful goddess?"

    Mls "Hmmm? Well... You did behave like a good little boy, even if it took you a while. So..."

    menu:
        "Let him go":

            $ LetHimGo = True
            jump goddessapproves
        "Knock him out":


            $ KnockHimOut = True
            jump gotosleep

label gotosleep:
    scene l61
    with hpunch

    Mls "Time for you to take a well deserved nap!"

    "Gelée" "Gah!"

    scene black
    with vpunch

    Mls "Okay, now time to check those documents."

    jump choicesdone


label goddessapproves:
    scene l62
    with fade

    Mls "*Rawr* Run for your life!"

    "Gelée" "Aaaaaaaa! (I hate this job! I quit!)"

    Mls "Okay, now time to check those documents."

    stop music fadeout 3



label choicesdone:

    scene l63
    with dissolve

    Mls "Well damn. According to this, it looks like they have about all there is to know about me."

    Mls "This makes it personal. Now I'm going to find out who leaked this info."

    Mls "Time to go get my clothes. I'm so dirty. I need a bath and a hug."

    Mls "Where is that dorkface when I need him? I bet he is going crazy right now."

    Mls "Well, I just hope Alison is okay. I really regret not taking her straight home now."

    Mls "I hope [mc] is not too upset with me... Well, I guess I'll find out soon enough."

    stop music fadeout 2

    scene l65
    with fade

    play music "popstar.ogg" fadein 5

    "" "Alison is playing a mobile game, while Shadow flips through the channels on the TV."

    Sh "Ugh, why don't they ever put a good romance movie on when I want one?"

    C "Do you always scream so much or is this new for you? You know, living with people."

    Sh "I'm babysitting you, we're not living together. You're an assignment. Don't get ahead of yourself, little girl."

    C "Funny, I could have sworn I was taller than you."

    Sh "When you grow up you'll understand that size only matters when it comes to certain things."

    A "Well, no matter how much you grow up, you'll never get any taller."

    scene l66

    A "Please take your foot off my butt."

    Sh "But it's so nice and comfortable, you know? Bigger than a pillow, even."

    A "At least I have one. You need to really search to find yours, don't you?"

    Sh "You know, one of these days I'm going to teach you how to respect your elders."

    A "You'll go find an elder to teach us about respecting them, I take it?"

    A "Because I don't see any elders here."

    Sh "Keep talking, little girl. Keep talking."

    Sh "I'm sorry, are my feet bothering you?"

    scene l67

    C "Whoops, I must have accidentally placed my foot on your hand."

    A "Haha, Caroline, stop that. Shadow isn't all bad."

    A "She's just upset that [mc] lets me sleep in his bed but not her."

    Sh "Well, like it or not, rhino, your precious life is in my hands today."

    Sh "So play nice and don't push your luck. I'm not known for controlling my temper."

    C "Wooo, you sound very scary, miss big soldier lady."

    play sound "ringtone.ogg"

    scene l65
    with dissolve
    stop sound

    A "Hello? [mc], is that you?"

    M "Who else would it be Alison? Only I know this number."

    A "Well, hi! Where are you? And when are you coming back? Shadow is annoying me."

    M "Alison, listen to me and listen well. This goes for all three of you. I need you to get along! Do you hear me?"

    M "This is not a game. Shadow is there to keep you safe. Show her the respect she deserves."

    M "As for you, Shadow, you are supposed to be the adult here. Act like it!"

    Sh "Yes, Sir!"

    M "Don't think I forgot about you, Caroline, you also need to learn to get along."

    C "What did I do? And you're not my father, I don't have to listen to you."

    A "Caroline! Don't be rude!"

    C "*Growls* Sorry, Sis. I understand, [mc]. I'll be good, promise."

    M "Thanks Alison. I'm sorry about earlier, okay?"

    A "[mc]! Just shut up already, before I hang up on you."

    Sh "(I knew something happened between these two when she ran upstairs like that.)"

    M "Okay, well, I've found Melissa. I'm going in right now to get her out and bring her home."

    A "Yes! [mc], please be careful. I'll never forgive you if you don't come home."

    M "Haha, your concern is duly noted, Alison. I'll be home soon, kitten."

    A "*Blushes* Okay, [mc], see you soon and bring Melissa back safe please."

    scene l66
    with fade

    Sh "Well, kitten... What exactly happened this morning between the two of you?"

    C "Hehe, you don't know, do you?"

    A "Caroline, you better keep your mouth shut."

    C "Haha, or what, kitten? You stole my nickname and now I'm gonna tell her!"

    A "Don't you dare!"

    C "[mc] kissed her!"

    Sh "Oh my God!"

    A "Caroline! Why you little..."

    C "*Giggles* Remember what [mc] said, kitten. Get along and be good! You want me to tell him you were threatening a little girl?"

    A "You little brat. I bet you would say that, too, haha."

    C "You know it, Sis."

    Sh "Well, come on then, spill! How was it?"

    A "I guess there is no point hiding it from you anymore. I really don't know, okay? It's not like I have anything to compare it to."

    Sh "So this was your first kiss, Alison?"

    A "Well, this is new. You used my name!"

    Sh "Well, I promised [mc] and when it comes to him, I always keep my promises."

    A "Okay, I'll be nice as well. If you like my butt so much feel free to rest your feet on it."

    scene l67
    with dissolve

    Sh "Honestly, your butt is nice and comfy."

    A "Umm, thanks, I think?"

    C "Does this mean I can rest my foot on your hand without you complaining now?"

    Sh "*Sighs* Sure. Whatever makes you happy, little princess."

    Sh "So, Alison, details! Come on, out of all of us you're the only one who has kissed him."

    C "I don't want to kiss him!"

    Sh "You sure? Because no one actually accused you of wanting to."

    scene l68
    with fade

    C "*Remains quiet*"

    Sh "Haha, I knew it."

    A "Well, like I said before, I don't have another kiss to compare it to but, it felt strange at first."

    A " I was in shock, since that idiot [mc] took me by surprise. Then my heart started to beat really, really fast."

    A "I think I may have blacked out, because I don't remember what happened next."

    A "I came to my senses sometime later and [mc] was screaming at me."

    Sh "I see, so that's why you nearly ran me through the wall."

    A "I did? I'm sorry, I didn't even notice you."

    C "Haha, I guess you're in love, sis. Good luck with that. I hear it's incurable."

    A "And you would know this how, exactly? You haven't even been kissed in virtual reality."

    C "Hey! You didn't have to share that!"

    A "Fair is fair, sis. You burned me, now it's my turn, haha."

    C "You meanie."

    Sh "Well, thanks for sharing, you two."

    C "You're welcome."

    A "Yeah, no problem. Have you ever kissed a guy? Or a maybe a girl?"

    Sh "Not going to answer that."

    C "Haha, I thought you were the adult. I bet you've never kissed anyone either."

    Sh "*Completely ignores her* Why do you ask, Alison? You into girls as well now?"

    A "Well, no, I was asking because I know Melissa said she likes girls."

    C "Oh? Is that the girl [mc] left behind to come to rescue me, Sis?"

    A "Yeah and it's killing him. He shouldn't even be out of bed right now."

    Sh "I know, I tried to tell him to let me go instead but he wouldn't. He's angry at himself for leaving her behind."

    C "I feel so shitty right now. He left his girlfriend behind for me?"

    A "She is not his girlfriend!"

    Sh "*Questions her tone* Hmmm... Jealous much?"

    A "I am not! I just meant she isn't his girlfriend, that's all."

    C "Then why did you have to shout it? My sister is jelly of Melissa."

    C "She must really be something if she makes you jealous, sis."

    Sh "She really is. Even I am jealous of her, to be honest. So you're not alone in that, at least."

    A "Haha, umm, well, okay then. Yeah, I guess I am a little bit jealous of her."

    A "She has an incredible body, she's beautiful, and she's a really nice person."

    C "You have an incredible body as well though, Sis. I don't see the point in being jealous."

    Sh "Caroline is right. You both are very pretty, body and all."

    Sh "Trust me. I gather intel and spot targets, among other things, for a living. I've seen all shapes and sizes."

    A "Well, thank you. You're not bad yourself, you know. Petite, as [mc] calls it."

    Sh "[mc] called me petite?"

    A "Well, what he actually said was \"petite bombshell\". He also said you pack a punch."

    A "And he wasn't joking when he said that part. You must be really tough, eh?"

    Sh "Whoa, he actually called me a bombshell..."

    C "Hey Shadow? Are you in love with [mc] or something?"

    Sh "(Petite bombshell... He said that about me? And earlier he called me Aiko.)"

    Sh "(I'm so happy I can even handle babysitting these two now.)"

    A "Earth to Shadow... Is anyone there?"

    C "Helloooo!"

    Sh "What!? I'm just thinking about plans, that's all."

    A "Mhm, plans involving [mc] I bet. Just don't get any ideas about the bed again."

    C "Oh man, here we go again."

    A "Well, you saw what she did yesterday, didn't you?"

    scene l65
    with dissolve

    C "When you two were arguing over who got to sleep with him?"

    A "Yeah. She pushed me and I landed on his face!"

    Sh "Haha, yeah that was awesome. And it's not as if I landed somewhere better."

    C "Haha, you two are so silly. That was so embarrassing..."

    A "You laugh, Sis, but you didn't stay long enough to see what I saw."

    C "Saw what exactly?"

    Sh "Oh God, that thing was massive. And I think it was still half asleep."

    A "Seriously? If that's true, that's kind of scary."

    Sh "That's what a little girl would say."

    Sh "(I don't shy away from a challenge, even one that intimidating... and big.)"

    C "Hello?! What did you two see, I'm here too, you know?"

    A "I'm not so sure it's a good idea to keep having this conversation."

    Sh "I agree with you for once, Alison. She may have nightmares afterward."

    C "Stop treating me like a child and answer my question!"

    A "No, I will not. It's not something you need to know. Now please behave."
    stop music fadeout 3

    C "*Growls at them*"

    scene l69
    with fade

    play music "fantastic.ogg" fadein 5

    Mls "I'm starting to get tired. I can't believe there were that many guards."

    Mls "It's a good thing they were all deadbeats with zero skill so far."

    Mls "This place looks like the one they initially brought me to last night but the outside isn't the same."

    Mls "They must have many of these spots all around the country."

    scene l70
    with dissolve

    Mls "Well, it's time to find my clothes. Let's hope he wasn't lying."

    Mls "I can't wait to get out of here and see [mc] again. I need a bath, too."

    Mls "Maybe I can even convince him to let me stay over for a while."

    Mls "What with me being in such shock from this ordeal and all, haha."

    Mls "Heck, as guilty as he must be feeling right now, he'll buy it."

    scene l71
    with fade

    Mls "I hope Alison is alright. Honestly, I miss her. Despite our differences and our rivalry, she is a really nice girl."

    Mls "I don't know, maybe [mc] should be with her instead of me."

    Mls "Maybe I'm just too much for him. Maybe it's our partnership. Too many maybes and no real answers, sadly."

    Mls "I'm done playing games. I'm going to behave and let him choose."

    scene l72
    with dissolve

    Mls "Now, let's see, where are my clothes? This isn't mine!"

    Mls "Wow, why would someone hide a dildo in here? Maybe one of the guards gets lonely at night?"

    Mls "Oh my God, why do I care!? Focus, Melissa!"

    Mls "Gotcha! Okay, time to get dressed and check that computer."

    scene l74
    with fade

    Mls "Oh my God. This is a gold mine of information. Why would those morons leave it on during an emergency?"

    Mls "I guess they were overconfident. What with me being such a fragile little girl."

    Mls "Well, this is just what I needed, time for some serious payback."

    Mls "[mc] won't believe this. These are all the locations they keep the girls."

    Mls "Names, age, height, pictures, they have everything!"

    Mls "So this is how they mark the girls. I wonder who feeds them this info, though."

    Mls "Okay, I'll just take this nice USB stick. I'm glad they rely on such simple tech."

    scene l73
    with dissolve

    Mls "With all that's happened, I really can't believe how lucky I am. I honestly owe that dorkface my life right now."

    Mls "If he hadn't insisted on training me so far above police standards I could have easily died here."

    Mls "I'll make sure to thank him while I'm kicking his ass."

    Mls "He's still going to pay for leaving me alone in here for so long."

    Mls "He better have a damn good explanation, that's all I have to say."

    stop music fadeout 2

    scene l75
    with fade





    C "So, I was talking to [mc] this morning."

    A "Yeah, I noticed that when I came down here, you were acting a bit strange."

    A "What happened? He wouldn't tell me when I asked him. Well, not all of it. He only told me parts of the story."

    C "He told me about how you were treated badly all those years in that cage."

    C "He didn't go into detail, but seeing how angry he got when I defended Dad I figured he knew a lot more than he shared with me."

    C "What happened, Sis? Is dad really as bad as [mc] make him sound?"

    A "I love you, Caroline. I think it's best if I don't tell you everything."

    C "Now you too? You are going to treat me like a child as well?"

    A "No, sweetheart, that's not it at all. I just don't have the heart to tell you."

    A "I know he wasn't a terrible father to you. At least, I hope nowhere near as bad."

    A "What he put me through makes me wonder if I'm even his child."

    C "Are you saying he hurt you? Please tell me, Alison. I need to know."



    menu:
        "She deserves the truth":

            $ TruthTeller = True
            jump telltruth
        "Protect her from the truth":


            $ ProtectHer = True
            jump innocence

label telltruth:

    play music  "sadness.ogg" fadein 10
    A "Well, I suppose you deserve to know what really happened. When I was locked in that cage, he would come downstairs and do things."

    A "Things that I can't share with you no matter how big you think you are."

    A "They would haunt you for the rest of your life. So please don't ask."

    C "I think I understand enough, Sis. I will hear only what you're willing to share."

    A "He would touch me like no parent should, you know?"

    C "*Sobs* Yeah, I know. He came out of the basement one day. He was angry. He saw me listening in..."

    C "Or trying to, I should say, because the door was closed. I saw him fixing his pants up. He smiled at me and touched me."

    A "He what?!"

    C "He only ran his fingers over my lips, Sis, but it creeped me out."

    A "I tried to protect you, I swear. I tried my best."

    C "If what [mc] was hinting is true, then you suffered because of me?"

    scene l76
    with fade
    with hpunch



    A "No! Don't you ever think like that again! You are my sister!"

    A "I did what any big sister would do. I'm just sorry I wasn't there for you."

    C "I'm so sorry that you had to go through whatever you did to protect me."

    A "*Crying* I'd do it all over again if I had to. I love you, Caroline."

    C "*Sobs* I really can't believe dad was capable of something like that."

    C "I don't even understand how could he be so cold to you and yet not to me."

    A "I intend to find out, when I get my hands on him next time."

    A "Believe me, he will answer all of my questions. Before I kill him, that is."

    C "You would?! You would kill our father?"

    A "You may consider him a father, Caroline but to me, he is nothing more than a nightmare."

    A "A cruel, cold hearted piece of shit!"

    A "I'm sorry, Sis. I don't mean to upset you. I hate him so much, I don't know what I'll do, okay?"

    C "I understand, or at least I'm trying to."

    C "Maybe [mc] is right, maybe he isn't really our father, or not your father at least."

    C "I would like to find out the truth but no matter what that truth may be..."

    C "You will always be my big sister. Do you understand that, Alison?"

    A "*Hugs her tighter* Yes, and I love you, Caroline. Thank you, little kitten."

    C "Haha, careful now, [mc] might confuse his kittens if you keep calling me that."

    A "Caroline! You better not even be thinking about stuff like that."

    C "Too late for that now, Sis!"

    A "I suppose I'll just have to watch you closely from now on!"

    C "I love you, Sis."

    A "I love you more, Baby Sis."
    stop music fadeout 2

    C "I know."

    jump endofsisterlylove



label innocence:
    scene l76
    with dissolve

    play music "fantastic.ogg" fadein 5

    A "Listen, Caroline. He was not a good person and an even worse father to me."

    A "He did things. He put me through things that no child should go through."

    A "He forced Mom to do as he said through ways that I can't even explain."

    A "And he threatened to do the same or worse to you if I didn't obey him."

    C "I am so sorry. I tried, you know? I really, really tried to come to see you."

    C "But you made me promise to never come back, so I stayed away as you said."

    A "I'm happy that you did, Caroline. You being safe was all I cared about."

    C "I love you, Alison, and I promise you that I'll never stay away again. *Sobs* I don't care what you say!"

    A "*Shhh* I'm here now, Sis. And I'll never leave your side again."


    stop music fadeout 3
label endofsisterlylove:
    scene l77
    with dissolve

    play music "fantastic.ogg" fadein 5

    "Security Guard" "Sir, that strange man is back again."

    E "Johnson?"

    "Security Guard" " Yes sir."

    E "Well, send him in then."

    scene l78

    E "I wonder what brings him back so soon. I don't like this at all."

    E "I think it's time I insist on some answers."

    scene l79
    with fade

    E "Ah, Mr. Johnson. Welcome back once again. What brings you here today?"

    J "Thank you, Eric. I need to speak to you privately."

    scene l77


    E "Then you've come to the right place, my friend. This office is secure."

    J "Good to hear. Because what I'm about to tell you could get us both killed."

    scene l79

    E "Now I'm really interested."

    scene l77
    E "Please, carry on. I'm all ears and at your disposal, John."

    J "The girl, you remember the one we had a deal on?"

    E "How could I forget, she cost me a few of my men and a lot of money."

    J "Men and money are easily replaced, Eric. This girl is so valuable..."

    J "People would start wars over her. Do I have your attention now?"

    E "You most certainly do, my friend."

    J "I owe you an apology, but that will have to wait until later."

    J "We need to find her and we need to do it soon. She is special, Eric."

    J "She is the one and only surviving subject of a lifelong scientific experiment."

    E "So you're telling me that you've known this, the entire time..."

    scene l80
    with fade

    E "And yet you wait until now to tell me?! You imbecile!"

    J "I understand your anger, Mr. Mayor, and I deserve it."

    J "But we need to act now, sir! If we don't, that man will figure it out."

    scene l81
    with dissolve

    E "And are you referring to that pesky [mc] character?"

    J "Correct Eric, he is a very skilled and dangerous individual. On top of that, I believe he has outside help."

    E "That is indeed something we need to deal with, and soon. Hmmm, tell me more."

    J "I believe he has someone who is skilled at hacking encrypted servers."

    J "These are not some cheap servers either. We're talking about military grade encryption."

    scene l78

    E "Hmmm, fine! What is there for him to find on these servers?"

    J "I was part of a group of scientists researching ways to enhance infants."

    J "Most of the others, with the exception of myself and one other who got away, are now deceased."

    J "I had them all killed over this information I'm about to share."

    E "I see, so this is indeed something worth killing for."

    J "Correct, sir. Imagine being able to live forever..."

    E "Okay, that's more than enough for me, Johnson. Consider the entire weight of this office at your disposal."

    E "We will start to gather any and all information on this [mc] Wanzer."

    J "Thank you, Eric. We need to act fast, though. The girl is not aware of what she is."

    J "However, I noticed something during our last encounter. Something that should not have been possible without my permission."

    E "Huh? Speak plainly, man."

    J "She activated her defense systems and I am concerned. I fear that she may have done so in reaction to me causing him pain."

    J "I shot him, and I believe that was the trigger for her activation."

    scene l81
    with fade

    E "Alright. It's time you and I renegotiate our business agreement."

    E "And it's time I hear the whole story. Meanwhile, I'll send my men out."

    J "Thank you. I'm really concerned, let's tell them as little as possible."
    scene l79

    E "Not to worry. I'll just have my men gather everything on him and his friends."

    E "It's about time the gloves came off, wouldn't you agree?"

    J "Absolutely. This is the most important decision you'll ever make, Eric."

    stop music fadeout 3

    scene black
    centered "Meanwhile..."

    scene l82
    with dissolve

    Mls "Well, it's time to get out of this cage once and for all."

    Mls "I can't wait to see [mc]. Being in this place really made me realize how much he means to me."

    Mls "Although it may be a losing battle, I won't quit."

    Mls "I know he loves Alison, but I love him too."

    Mls "I have to at least tell him how I feel. Then, whatever he decides, I can live with."

    scene l83
    with fade

    Mls "(Oh shit!)"

    scene l83

    Mls "([mc], I'm sorry...)"

    play sound "9mmglock.ogg"

    scene black
    with hpunch

    stop sound

label end:

    if renpy.loadable('love2.rpyc') and renpy.loadable('/images/love2/lp1.webp'):

        jump loveII
    else:
        jump endOfVersion
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
