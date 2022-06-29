# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import subprocess
import os
from datetime import datetime

from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, ScratchPad, Screen, DropDown
from libqtile.lazy import lazy



mod = "mod4"
terminal = "termite" 
browser = "brave"


#def ok():
#    now = datetime.now()
#    current_time = now.strftime("%d|%b|%Y|%H:%M:%S")
#    lazy.spawn("maim Pictures/Screenshots/"+current_time+".png")

# For my Cursor
@hook.subscribe.startup
def runner():
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/auto.sh'])
 

keys = [
    
    # =====APPLICATIONS======
        
    Key([mod], "w",         lazy.spawn(browser)),
    Key([mod, "shift"], "Return",    lazy.spawn(terminal)),


 
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "control"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restarts"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("dmenu_run -h 28"), desc="Spawn a command using a prompt widget"),
    Key([mod, "control"], "p", lazy.spawn("rofi -show run")),
    Key([mod], "o", lazy.spawn("maim Pictures/Screenshots/ok.png"))


]

#groups = [Group(i) for i in "123456789"]

groups= [


    Group("1",
          label="",
          ),

    Group("2",
          label="",
          ),

    Group("3",
          label="",
          ),

    Group("4",
          label="",
          ),

    Group("0",
          label=""),

]

#keys.extend([ 
#    Key([], 'F11', lazy.group['scratchpad'].dropdown_toggle('nnn'))
#    ])

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

groups.append( ScratchPad('scratchpad', [ 
        DropDown('ranger', 'termite -e ranger', width=0.5, height = 0.5, x=0.25, y=0.2),
        DropDown('removables', 'termite --exec="ranger /run/media/sakaar"', width=0.5, height = 0.5, x=0.25, y=0.2),
        DropDown('alsa', 'termite -e alsamixer', width=0.5, height = 0.5, x=0.25, y=0.2),
        DropDown('terminal', 'termite', width=0.5, height = 0.5, x=0.25, y=0.2),
    ]) )

scratchkeys = [ 
        Key(['control'], '1', lazy.group['scratchpad'].dropdown_toggle('terminal')),
        Key(['control'], '2', lazy.group['scratchpad'].dropdown_toggle('alsa')),
        Key(['control'], '3', lazy.group['scratchpad'].dropdown_toggle('ranger')),
        Key(['control'], '0', lazy.group['scratchpad'].dropdown_toggle('removables')),
        ]

keys.extend(scratchkeys)

colors = ['#010206', '#F1EDEE', '#7A6563', '#36C9C6', '#56667A']

layouts = [
    layout.Columns(
        margin=[6,6,6,6],
        border_focus = '#F1EDEE',
        border_width = 2,
        border_on_single = True,

        border_normal = colors[4]
        ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(),
    layout.Floating(
        border_focus = '#F1EDEE',
        border_normal = colors[4],
        border_width = 2,
        ),
    layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
        font = "Iosevka Nerd Font",
        fontsize = 14,
        padding = 3
)
extension_defaults = widget_defaults.copy()

col = {'active':"#010206", 'inactive': "#7A6563"}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(

                    center_aligned = True,
                    background = "#010206",
                    font = "NotoSans Nerd Font",
                    fontsize = 13,
                    padding = 5,
                    highlight_method = 'line',
                    this_current_screen_border = '#F1EDEE',
                    highlight_color = ['#F1EDEE', '#F1EDEE'],
                    active = '#F1EDEE',
                    inactive = col['inactive'],
                    hide_unused = False,
                    margin_x = 10,
                    block_highlight_text_color = col['active']

                    ),

                widget.Spacer(),

                widget.Mpris2(
                    name = 'spotify',
                    objname = 'org.mpris.MediaPlayer2.spotify',
                    display_metadata = ['xesam:title'],
                    foreground = colors[1],
                    
                    font = "Iosevka Nerd Font",
                    fontsize = 16,
                    padding = 3,
                    ),

                widget.Spacer(),
                
                widget.CurrentLayout(
                    background = colors[1],
                    foreground = colors[0],
                    padding = 10,
                    font = "Iosevka Nerd Font",
                    fontsize = 14
                    ),
                

                widget.Net(
                    font = 'Iosevka Nerd Font',
                    fontsize = 13,
                    padding = 12,
                    background = '#CE6A85',
                    format = '{down}',
                    prefix = 'M'
                    ),

                widget.Clock(
                        fontsize = 14,
                        background = '#5FA8D3',
                        padding = 12,
                        format = '  %d %b,%H:%M'
                        )

                # widget.Cmus(),
                #                widget.Mpris2()


            ],
            28,
            background = '#010206'
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
#        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"), # GPG key password entry
    ],


    border_focus = '#F1EDEE',
    border_normal = colors[4],
    border_width = 2


)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
