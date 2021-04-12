screen statsMenu():
    modal True
    add "/oscarAdditions/images/statsbioBackground.png"

    default character = ""

    python:
        global statsDict
        statsDict = {
            "Menu": [
                mc,
                "Alison",
                "Melissa",
                "Nadia"
            ],
            mc: {
                "RPa": RPa,
                "Trust": trust,
                "Obedience": obedience,
                "Affection": affection,
                "Corruption": corruption,
                "Pregnancy": pregnancy,
                "AssMan": assman,
                "NadiasBitch": NadiasBitch,
            },
            "Alison": {
                "Trust": trust,
            },
            "Melissa": {
                "Trust": trust,
            },
            "Nadia": {
                "Trust": trust,
            },
        }

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        hbox:
            align (0.5, 0.5)
            spacing 50

            for i in statsDict["Menu"]:
                textbutton i:
                    action [Show("characterStats", character=i), SetScreenVariable("character", i)]
                    selected i == character
                    text_style "modTextButtonHeader"

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            action [Hide("statsMenu"), Hide("characterStats")]
            idle "/oscarAdditions/images/backButton.png"
            hover im.MatrixColor("/oscarAdditions/images/backButton.png", im.matrix.brightness(0.2))


screen characterStats(character):
    fixed:
        xysize (1875, 789)
        pos (19, 115)

        vpgrid:
            cols 2
            xspacing 200
            yspacing 50
            align (0.5, 0.5)

            for k, v in statsDict[character].iteritems():
                hbox:
                    spacing 10

                    text "{}:".format(k) style "modTextHeader"
                    text "{}".format(v) style "modTextHeader"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
