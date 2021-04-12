

default book = False
style purple_button:
    background "#800080"
    insensitive_background "#D3D3D3"
    hover_background "#9400D3"

screen script_imagemap:
    imagemap:
        ground "corruption/d4.webp"
        hover "corruption/d4white.webp"

        hotspot (900,471,161,82) action Jump("clickablebooty")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
