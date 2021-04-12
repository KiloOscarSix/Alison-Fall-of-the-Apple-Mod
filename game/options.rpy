













define config.name = _("Alison Fall of the Apple Love-Final.")





define gui.show_name = True




define config.version = "1.0"





define gui.about = _p("""
""")






define build.name = "AlisonFalloftheApple"







define config.has_sound = True
define config.has_music = True
define config.has_voice = False













define config.main_menu_music = "alison.ogg"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 25





default preferences.afm_time = 15
















define config.save_directory = "Alison Fall of the Apple-1542421046"






define config.window_icon = "gui/window_icon.png"










define config.developer = "auto"

init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.bk', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**/desktop.ini', None)
    build.classify('game/**.rpy', None)
    build.classify('game/saves/**', None)
    build.classify('game/cache/**', None)
    build.classify('.git/**', None)
    build.classify('.gitattributes', None)
    build.classify('.gitignore', None)
    build.classify('README.md', None)


    build.archive("scripts", "all")
    build.archive("audio", "all")
    build.archive("prologue", "all")
    build.archive("lovepath", "all")
    build.archive("harem", "all")
    build.archive("love", "all")
    build.archive("love2", "all")
    build.archive("love3", "all")
    build.archive("love4", "all")
    build.archive("love5", "all")
    build.archive("haremII", "all")
    build.archive("corruption", "all")
    build.archive("haremIII", "all")
    build.archive("haremIV", "all")
    build.archive("corruptionII", "all")
    build.archive("haremV", "all")
    build.archive("corruptionIII", "all")
    build.archive("corruptionIV", "all")
    build.archive("saturday", "all")





    build.classify('game/audio/**.ogg', 'audio')
    build.classify('game/audio/**.mp3', 'audio')



    build.classify("game/*.rpyc", "scripts")



    build.documentation('*.html')
    build.documentation('*.txt')




    build.classify('game/images/prologue/**.png', 'prologue')
    build.classify('game/images/prologue/**.jpg', 'prologue')
    build.classify('game/images/prologue/**.webp', 'prologue')

    build.classify('game/images/saturday/**.png', 'saturday')
    build.classify('game/images/saturday/**.jpg', 'saturday')
    build.classify('game/images/saturday/**.webp', 'saturday')


    build.classify('game/images/harem/**.png', 'harem')
    build.classify('game/images/harem/**.jpg', 'harem')
    build.classify('game/images/harem/**.webp', 'harem')

    build.classify('game/images/love/**.png', 'love')
    build.classify('game/images/love/**.jpg', 'love')
    build.classify('game/images/love/**.webp', 'love')

    build.classify('game/images/love2/**.png', 'love2')
    build.classify('game/images/love2/**.jpg', 'love2')
    build.classify('game/images/love2/**.webp', 'love2')

    build.classify('game/images/love3/**.png', 'love3')
    build.classify('game/images/love3/**.jpg', 'love3')
    build.classify('game/images/love3/**.webp', 'love3')

    build.classify('game/images/love4/**.png', 'love4')
    build.classify('game/images/love4/**.jpg', 'love4')
    build.classify('game/images/love4/**.webp', 'love4')

    build.classify('game/images/love5/**.png', 'love5')
    build.classify('game/images/love5/**.jpg', 'love5')
    build.classify('game/images/love5/**.webp', 'love5')



    build.classify('game/images/haremII/**.png', 'haremII')
    build.classify('game/images/haremII/**.jpg', 'haremII')
    build.classify('game/images/haremII/**.webp', 'haremII')

    build.classify('game/images/corruption/**.png', 'corruption')
    build.classify('game/images/corruption/**.jpg', 'corruption')
    build.classify('game/images/corruption/**.webp', 'corruption')

    build.classify('game/images/corruptionII/**.png', 'corruptionII')
    build.classify('game/images/corruptionII/**.jpg', 'corruptionII')
    build.classify('game/images/corruptionII/**.webp', 'corruptionII')

    build.classify('game/images/haremIII/**.png', 'haremIII')
    build.classify('game/images/haremIII/**.jpg', 'haremIII')
    build.classify('game/images/haremIII/**.webp', 'haremIII')

    build.classify('game/images/haremIV/**.png', 'haremIV')
    build.classify('game/images/haremIV/**.jpg', 'haremIV')
    build.classify('game/images/haremIV/**.webp', 'haremIV')

    build.classify('game/images/haremV/**.png', 'haremV')
    build.classify('game/images/haremV/**.jpg', 'haremV')
    build.classify('game/images/haremV/**.webp', 'haremV')

    build.classify('game/images/corruptionIII/**.png', 'corruptionIII')
    build.classify('game/images/corruptionIII/**.jpg', 'corruptionIII')
    build.classify('game/images/corruptionIII/**.webp', 'corruptionIII')

    build.classify('game/images/corruptionIV/**.png', 'corruptionIV')
    build.classify('game/images/corruptionIV/**.jpg', 'corruptionIV')
    build.classify('game/images/corruptionIV/**.webp', 'corruptionIV')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
