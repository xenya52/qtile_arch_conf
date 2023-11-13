# ██╗    ██╗██╗██████╗  ██████╗ ███████╗████████╗███████╗
# ██║    ██║██║██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝██╔════╝
# ██║ █╗ ██║██║██║  ██║██║  ███╗█████╗     ██║   ███████╗
# ██║███╗██║██║██║  ██║██║   ██║██╔══╝     ██║   ╚════██║
# ╚███╔███╔╝██║██████╔╝╚██████╔╝███████╗   ██║   ███████║
#  ╚══╝╚══╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝
from libqtile import bar, widget, hook, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from Core.Colors import violet1, violet2, violet3, violet4, violet5, violet6, textColor

widget_defaults = dict(
    font="JetBrainsMono",
    fontsize=15,
    padding=6,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        
        wallpaper = "~/.config/qtile/Images/wallpaper.jpg",
        wallpaper_mode = "stretch",

        top=bar.Bar(
            [
                widget.Sep(
                    background=violet1,
                    linewidth=0,
                    padding=6,
                ),
                #Profile Icon
                widget.Image(
                    background=violet1,
                    filename="~/.config/qtile/Images/lucyProfilePicRound.png",
                    scale="true"
                ),
                widget.TextBox(
                    text='',
                    background=violet2,
                    foreground=violet1,
                    padding=0,
                    fontsize=42,
                ),

                #CurrentDate
                widget.Clock(
                    background = violet2,
                    foreground =  textColor,
                    format = " %d/%m/%Y",
                    update_interval = 60.0,
                ),
                widget.TextBox(
                    text='',
                    background=violet3,
                    foreground=violet2,
                    padding=0,
                    fontsize=42,
                ),

                #CurrentClockTime
                widget.Clock(
                    background = violet3,
                    foreground = textColor,
                    format = " %H:%M",
                    update_interval = 60.0,
                ),
                widget.TextBox(
                    text='',
                    background=violet4,
                    foreground=violet3,
                    padding=0,
                    fontsize=42,
                ), 

                #Choosen Layout
                widget.CurrentLayout(
                    background = violet4,
                    foreground = textColor,
                ),
                widget.TextBox(
                    text='',
                    background=violet5,
                    foreground=violet4,
                    padding=0,
                    fontsize=42,
                ), 

                #Groups
                widget.GroupBox(
                    background = violet5,
                    inactive = violet4,
                    active = textColor,
                    rounded=True,
                    highlight_color= violet1,
                    highlight_method="line",
                    borderwidth=0,
                    padding = 0,
                ),
                widget.TextBox(
                    text='',
                    background=violet6,
                    foreground=violet5,
                    padding=0,
                    fontsize=42,
                ), 
                #Interactive Buttons
                widget.TextBox(
                    text='',
                    background=violet6,
                    foreground=violet6,
                    mouse_callbacks= {},
                    padding=0,
                    fontsize=42,
                ),
                widget.TextBox(
                    text='',
                    background=violet6,
                    foreground=violet6,
                    mouse_callbacks= {},
                    padding=0,
                    fontsize=42,
                ), 
                widget.TextBox(
                    text='',
                    background=violet6,
                    foreground=violet6,
                    mouse_callbacks= {},
                    padding=0,
                    fontsize=42,
                ), 
                widget.TextBox(
                    text='',
                    foreground=violet6,
                    padding=0,
                    fontsize=42,
                ), 

                #Prompts
                widget.Spacer(
                ),
                widget.TextBox(
                    text='',
                    foreground=violet6,
                    padding=0,
                    fontsize=42
                ),
                widget.CPU(
                    background=violet6,
                    foreground=textColor,
                    format="󰘚 {load_percent}%",
                ),
                widget.ThermalZone(
                    background=violet6,
                    fgcolor_normal=textColor,
                    fgcolor_high=textColor
                ),
                widget.TextBox(
                    text='',
                    foreground=violet5,
                    background=violet6,
                    padding=0,
                    fontsize=42,
                ),
                widget.Memory(
                    format=" {MemUsed: .0f}{mm}",
                    background=violet5,
                    foreground=textColor,
                    interval=1.0
                ),
                widget.TextBox(
                    text='',
                    background=violet5,
                    foreground=violet4,
                    padding=0,
                    fontsize=42
                ),
                widget.Battery(
                    format="󰁺 {char} {percent:1.0%} ",
                    charge_char="↑",
                    discharge_char="↓",
                    full_char="!",
                    low_foreground="#FF0001",
                    background=violet4,
                    foreground=textColor,
                ),
                widget.TextBox(
                    text='',
                    background=violet4,
                    foreground=violet3,
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text=" ",
                    foreground = textColor,
                    background = violet3,
                ),
                widget.KeyboardLayout(
                    background=violet3,
                    foreground=textColor,
                    configured_keyboards = ['de','us'],
                ),
                widget.TextBox(
                    text='',
                    background=violet3,
                    foreground=violet2,
                    padding=0,
                    fontsize=42,
                ),
                widget.Backlight(
                    backlight_name = "intel_backlight",
                    format="󰍹 {percent:2.0%} ",
                    background = violet2,
                    foreground = textColor,
                    scroll = True,
                ),
                widget.TextBox(
                    text='',
                    background = violet2,
                    foreground = violet1,
                    padding=0,
                    fontsize=42
                ),
                widget.Volume(
                    background = violet1,
                    foreground = textColor,
                    fmt=" {} "
                ),
                widget.Sep(
                    background = violet1,
                    linewidth=0,
                    padding=6,
                ),
            ],
            24,
            background = "#EDA3B1",
            border_width = 2,
            border_color = "fc679e"
            #margin = [10,10,0,10],
            #background_opacity = 0.5,
        ),
        bottom=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=6,
                ),
                widget.Prompt(
                    foreground = "#EDA3B1",
                ),
                widget.Spacer(
                ),
                widget.Systray(
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                ),
            ],
            24,
            background = "#EDA3B100",
            ),
    ),
]
