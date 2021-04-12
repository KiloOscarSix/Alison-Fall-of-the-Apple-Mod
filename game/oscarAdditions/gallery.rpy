init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, pageNum, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = pageNum
            self.label = label
            if scope is None:
                scope = {}
            self.scope = scope
            self.thumbnail = os.path.join("/images/", "{}".format(thumbnail))
            galleryItems.append(self)

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

default galleryPageNumber = 1
default scopeDict = {}

define galleryMenu = [
    ["Alice/Alison", "images/prologue/alr12.jpg"],
    ["Melissa", "images/saturday/melissa2.webp"],
    ["Nadia", "images/haremV/hv117.jpg"],
    ["Winter", "images/haremV/w005.jpg"],
    ["Shadow", "images/love2/lp37.webp"],
    ["Tiffa", "images/corruptionII/da47.webp"],
    ["Others", "images/saturday/boss4.webp"],
]

define AliceAlison = GalleryItem("Alice/Alison", 1, "galleryScene8", "prologue/alr98.jpg")
define AliceAlison = GalleryItem("Alice/Alison", 1, "galleryScene9", "prologue/alr220.jpg")
define AliceAlison = GalleryItem("Alice/Alison", 1, "galleryScene1", "love3/ls53.webp")
define AliceAlison = GalleryItem("Alice/Alison", 1, "galleryScene2", "love3/ls70.webp")
define AliceAlison = GalleryItem("Alice/Alison", 1, "galleryScene3", "love4/l057.webp")
define AliceAlison = GalleryItem("Alice/Alison", 1, "SexwithAABedroom", "love5/fcl050.jpg")
define AliceAlison = GalleryItem("Alice/Alison", 1, "corupt", "corruption/d5.webp")
define AliceAlison = GalleryItem("Alice/Alison", 1, "LetMeWatch", "corruptionII/af7.webp")
define AliceAlison = GalleryItem("Alice/Alison", 2, "galleryScene4", "corruptionII/da40.webp")
define AliceAlison = GalleryItem("Alice/Alison", 2, "galleryScene5", "haremIII/hs31.webp")
define AliceAlison = GalleryItem("Alice/Alison", 2, "galleryScene6", "haremV/h6016.jpg")
define AliceAlison = GalleryItem("Alice/Alison", 2, "galleryScene7", "haremV/ack074.jpg")
define AlisonMelissa = GalleryItem("Alice/Alison", 2, "galleryScene11", "corruptionII/da122.webp")
define AlisonWinter = GalleryItem("Alice/Alison", 2, "galleryScene12", "haremV/ack048.jpg")

define Melissa = GalleryItem("Melissa", 1, "galleryScene27", "prologue/alr423.jpg")
define Melissa = GalleryItem("Melissa", 1, "galleryScene15", "harem/h51.webp")
define Melissa = GalleryItem("Melissa", 1, "harem2", "haremII/hr12.webp")
define Melissa = GalleryItem("Melissa", 1, "galleryScene16", "haremII/hr33.webp")
define Melissa = GalleryItem("Melissa", 1, "galleryScene17", "haremIII/hs13.webp")
define Melissa = GalleryItem("Melissa", 1, "galleryScene18", "haremV/hv195.jpg")
define Melissa = GalleryItem("Melissa", 1, "galleryScene19", "love5/fcml035.jpg")
define AlisonMelissa = GalleryItem("Melissa", 1, "galleryScene11", "corruptionII/da122.webp")
define MelissaAvaline = GalleryItem("Melissa", 2, "galleryScene10", "corruptionII/da175.webp")
define GenevieveMelissa = GalleryItem("Melissa", 2, "galleryScene13", "love4/ml004.webp")

define Nadia = GalleryItem("Nadia", 1, "haremIV", "haremIV/hc20.webp")
define Nadia = GalleryItem("Nadia", 1, "galleryScene20", "haremIV/hc95.webp")
define Nadia = GalleryItem("Nadia", 1, "knockedOnDoor", "haremV/hv110.jpg")
define Nadia = GalleryItem("Nadia", 1, "NadiasRoomVI", "haremV/h6066.jpg")

define Winter = GalleryItem("Winter", 1, "galleryScene22", "haremIV/hc115.webp")
define Winter = GalleryItem("Winter", 1, "bathroom", "haremV/w014.jpg")
define AlisonWinter = GalleryItem("Winter", 1, "galleryScene12", "haremV/ack048.jpg")

define Shadow = GalleryItem("Shadow", 1, "ChoseToNailShadow", "corruptionIV/creampie1.jpg")
define Shadow = GalleryItem("Shadow", 1, "LookingforMel6", "haremV/sh017.jpg")

define Tiffa = GalleryItem("Tiffa", 1, "galleryScene21", "corruptionII/da62.webp")
define Tiffa = GalleryItem("Tiffa", 1, "TiffThebuttslut", "corruptionIV/tr32.jpg")

define Genevieve = GalleryItem("Others", 1, "galleryScene23", "haremII/hr81.webp")


define Unknown = GalleryItem("Others", 1, "KekekeStrikesAgain", "love5/jfs004.jpg")
define Kate = GalleryItem("Others", 1, "galleryScene24", "haremIV/hc124.webp")
define Jessica = GalleryItem("Others", 1, "galleryScene14", "prologue/alr184.jpg")



label galleryNameChange:
    default persistent.mc = ""
    if persistent.mc == "":
        $ persistent.mc = renpy.input("What is your name?", default="Micael").strip() or "Michael"

    $ scopeDict = {"mc":persistent.mc}

screen sceneGalleryMenu():

    modal True tag menu
    add "/oscarAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "Scene Gallery":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
            idle "/oscarAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/oscarAdditions/images/backButton.png", im.matrix.brightness(0.2)))

    fixed:
        xysize (1875, 789)
        pos (19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for i in galleryMenu:
                vbox:
                    imagebutton:
                        action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                        idle Transform(i[1], zoom=0.2)
                        hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                    text i[0]:
                        style "modTextBody"
                        xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="None"):

    modal True tag menu
    add "/oscarAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            if galleryPageNumber == 1:
                action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
            else:
                action Function(galleryDecreasePageNumber)
            idle "/oscarAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/oscarAdditions/images/backButton.png", im.matrix.brightness(0.2)))

        if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
            imagebutton:
                action Function(galleryIncreasePageNumber)
                idle "/oscarAdditions/images/nextButton.png"
                hover im.MatrixColor("/oscarAdditions/images/nextButton.png", im.matrix.brightness(0.2))

    fixed:
        xysize (1875, 789)
        pos (19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for galleryItem in galleryItems:
                if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                    imagebutton:
                        action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                        idle Transform(galleryItem.thumbnail, zoom=0.2)
                        hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
                        insensitive Transform(im.Blur(galleryItem.thumbnail, 15), zoom=0.2)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
