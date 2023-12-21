screens = [
    Screen(
        wallpaper = "~/.config/qtile/Images/wallpaperPixel.jpg",
        wallpaper_mode = "stretch",

        top=bar.Bar(
            [
                widget.Sep(
                    background=violet1,
                    linewidth=0,
                    padding=6,
                ),

                #CurrentDate
                widget.Clock(
                    background = violet1,
                    foreground =  textColor_dark,
                    format = "%d-%m-%Y/%H:%M",
                    update_interval = 60.0,
                    mouse_callbacks={"Button1":lazy.spawn("obsidian"),}
                ),
                widget.TextBox(
                    text='',
                    background=violet2,
                    foreground=violet1,
                    padding=0,
                    fontsize=20,
                ), 
                #Weather
                widget.OpenWeather(
                    background=violet2,
                    foreground=textColor_dark,
                    location='Regensburg', 
                    format='{icon}{main_temp}°{units_temperature} {humidity}%',
                    mouse_callbacks={"Button1":lazy.spawn("kitty curl wttr.in/Regensburg sleep 10")}
                ),
                widget.TextBox(
                    text='',
                    background=violet3,
                    foreground=violet2,
                    padding=0,
                    fontsize=20,
                ), 
                #Memory
                widget.Memory(
                    format="{MemUsed: .0f}{mm}",
                    background=violet3,
                    foreground=textColor_dark,
                    interval=1.0,
                    mouse_callbacks={"Button1":lazy.spawn("kitty ncdu /"),}
                ),
                
                widget.TextBox(
                    text='',
                    background=violet4,
                    foreground=violet3,
                    padding=0,
                    fontsize=20,
                ), 

                widget.CPU(
                    background=violet4,
                    foreground=textColor_dark,
                    format="󰘚 {load_percent}%",
                    mouse_callbacks={"Button1":lazy.spawn("kitty bpytop"),}
                ),
                widget.ThermalZone(
                    background=violet4,
                    fgcolor_normal=textColor_dark,
                    fgcolor_high=textColor_dark
                ),
                
                widget.TextBox(
                    text='',
                    foreground=violet4,
                    padding=0,
                    fontsize=20,
                ),

                widget.Spacer(),

                widget.Systray(),

                widget.TextBox(
                    text='',
                    foreground=violet4,
                    padding=0,
                    fontsize=20
                ),
                #Choosen Layout
                widget.CurrentLayout(
                    background = violet4,
                    foreground = textColor_dark,
                ),
                
                widget.TextBox(
                    text='',
                    foreground=violet3,
                    background=violet4,
                    padding=0,
                    fontsize=20,
                ),
                #Groups
                widget.GroupBox(
                    background = violet3,
                    inactive = violet2,
                    active = textColor_dark,
                    rounded=True,
                    highlight_color= violet1,
                    highlight_method="line",
                    borderwidth=0,
                    padding = 0,
                ),
                widget.TextBox(
                    text='',
                    background=violet3,
                    foreground=violet2,
                    padding=0,
                    fontsize=20
                ),
                widget.TextBox(
                    text=" ",
                    foreground = textColor_dark,
                    background = violet2,
                ),
                widget.KeyboardLayout(
                    background=violet2,
                    foreground=textColor_dark,
                    configured_keyboards = ['de','us'],
                ),
                widget.TextBox(
                    text='',
                    background=violet2,
                    foreground=violet1,
                    padding=0,
                    fontsize=20,
                ),
                widget.Volume(
                    background = violet1,
                    foreground = textColor_dark,
                    fmt=" {} "
                ),
                widget.Sep(
                    background = violet1,
                    linewidth=0,
                    padding=6,
                ),
            ],
            22,
            background = "aa698b",
            #border_width = [0,0,2,0],
            #border_color = violet1,
            #margin = [5,5,0,5],
            #background_opacity = 0.5,
        ),
    ),

    Screen(
        wallpaper = "~/.config/qtile/Images/wallpaperPixel.jpg",
        wallpaper_mode = "fill",

        top=bar.Bar(
            [
                widget.Sep(
                    background=violet1,
                    linewidth=0,
                    padding=6,
                ),

                #CurrentDate
                widget.Clock(
                    background = violet1,
                    foreground =  textColor_dark,
                    format = "%d-%m-%Y/%H:%M",
                    update_interval = 60.0,
                    mouse_callbacks={"Button1":lazy.spawn("obsidian"),}
                ),
                widget.TextBox(
                    text='',
                    background=violet2,
                    foreground=violet1,
                    padding=0,
                    fontsize=20,
                ), 
                #Weather
                widget.OpenWeather(
                    background=violet2,
                    foreground=textColor_dark,
                    location='Regensburg', 
                    format='{icon}{main_temp}°{units_temperature} {humidity}%',
                    mouse_callbacks={"Button1":lazy.spawn("kitty curl wttr.in/Regensburg sleep 10")}
                ),
                widget.TextBox(
                    text='',
                    background=violet3,
                    foreground=violet2,
                    padding=0,
                    fontsize=20,
                ), 
                #Memory
                widget.Memory(
                    format="{MemUsed: .0f}{mm}",
                    background=violet3,
                    foreground=textColor_dark,
                    interval=1.0,
                    mouse_callbacks={"Button1":lazy.spawn("kitty ncdu /"),}
                ),
                
                widget.TextBox(
                    text='',
                    background=violet4,
                    foreground=violet3,
                    padding=0,
                    fontsize=20,
                ), 

                widget.CPU(
                    background=violet4,
                    foreground=textColor_dark,
                    format="󰘚 {load_percent}%",
                    mouse_callbacks={"Button1":lazy.spawn("kitty bpytop"),}
                ),
                widget.ThermalZone(
                    background=violet4,
                    fgcolor_normal=textColor_dark,
                    fgcolor_high=textColor_dark
                ),
                
                widget.TextBox(
                    text='',
                    foreground=violet4,
                    padding=0,
                    fontsize=20,
                ),

                widget.Spacer(),

                widget.TextBox(
                    text='',
                    foreground=violet4,
                    padding=0,
                    fontsize=20
                ),
                #Choosen Layout
                widget.CurrentLayout(
                    background = violet4,
                    foreground = textColor_dark,
                ),
                
                widget.TextBox(
                    text='',
                    foreground=violet3,
                    background=violet4,
                    padding=0,
                    fontsize=20,
                ),
                #Groups
                widget.GroupBox(
                    background = violet3,
                    inactive = violet2,
                    active = textColor_dark,
                    rounded=True,
                    highlight_color= violet1,
                    highlight_method="line",
                    borderwidth=0,
                    padding = 0,
                ),
                widget.TextBox(
                    text='',
                    background=violet3,
                    foreground=violet2,
                    padding=0,
                    fontsize=20
                ),
                widget.TextBox(
                    text=" ",
                    foreground = textColor_dark,
                    background = violet2,
                ),
                widget.KeyboardLayout(
                    background=violet2,
                    foreground=textColor_dark,
                    configured_keyboards = ['de','us'],
                ),
                widget.TextBox(
                    text='',
                    background=violet2,
                    foreground=violet1,
                    padding=0,
                    fontsize=20,
                ),
                widget.Volume(
                    background = violet1,
                    foreground = textColor_dark,
                    fmt=" {} "
                ),
                widget.Sep(
                    background = violet1,
                    linewidth=0,
                    padding=6,
                ),
            ],
            22,
            background = "aa698b",
            #border_width = [0,0,2,0],
            #border_color = violet1,
            #margin = [5,5,0,5],
            #background_opacity = 0.5,
        ),
    ),
]