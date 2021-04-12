screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

            textbutton _("My Games") action OpenURL("https://www.patreon.com/OnemanVN")

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if main_menu:
            textbutton _("Gallery") action [ui.callsinnewcontext("galleryNameChange"), Show("sceneGalleryMenu")]
        else:
            textbutton _("Stats") action Show("statsMenu")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc"):


            textbutton _("Help") action ShowMenu("help")


            textbutton _("Quit") action Quit(confirm=not main_menu)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
