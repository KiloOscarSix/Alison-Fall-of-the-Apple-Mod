label endOfVersion:
    "This is the end of version [config.version]."

    "OneManVN" "Thanks for playing."

    "OneManVN" "Updates are too slow? Try supporting me, it ensures better hardware, which equals faster updates."

    "" "Big thanks to McWoodz, Steele, Darth, Oscar, to name a few, as well as the countless others who helped me proofread in my early days."

    "" "Last but not least! To all of my patrons who continue to support me. I appreciate you!"



label credits:
    image splash = Text("{size=50}OneManVN", text_align=0.5, ypos=0.5)
    play music "Forever.mp3"
    image cred = Text(credits_s, text_align=0.5)
    image thanks = Text("{size=40}Thanks for Playing! Please consider supporting my project(s) Fate of Mirador is coming sometime in 2021.", text_align=0.5)
    $ credits_speed = 90
    scene alr63
    with dissolve
    pause(3)
    scene alr64
    with dissolve
    pause(3)
    scene alr65
    with dissolve
    pause(3)
    scene alr66
    with dissolve
    pause(3)
    scene alr127
    with dissolve
    pause(3)
    scene alr170
    with dissolve
    pause(3)
    scene alr173
    with dissolve
    pause(3)
    scene alr191
    with dissolve
    pause(3)
    scene alr405
    with dissolve
    pause(3)
    scene alr407
    with dissolve
    pause(3)
    scene alr428
    with dissolve
    pause(3)
    scene alr551
    with dissolve
    pause(3)
    scene alf108
    with dissolve
    pause(2)
    scene alf147
    with dissolve
    pause(2)
    scene ugf044
    with dissolve
    pause(2)
    scene alenp019
    with dissolve
    pause(3)

    show cred at Move((0.5, 8.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve
    with Pause(5)
    hide theend
    with dissolve
    with Pause(credits_speed - 5)
    show splash
    with dissolve
    with Pause(3)
    hide splash
    with dissolve
    with Pause(1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with dissolve
    return

init python:
    credits = ('Dedicated Supporter', 'Your name here upon request'), ('Dedicated Supporter', '2'), ('Dedicated Supporter', '3'), ('Dedicated Supporter', '4'), ('Dedicated Supporter', '5'), ('Dedicated Supporter', '6'), ('Supporter', '7'), ('Supporter', '8'), ('Supporter', '9'), ('Supporter', '10'), ('Writing', 'OMVN'), ('Programming', 'OMVN'), ('Proof reading', 'McWoodz')
    credits_s = "{size=40}Alison Fall of the Apple\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=30}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=30}" + renpy.version()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
