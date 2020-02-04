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

from libqtile.config import EzKey, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401
import os
import subprocess

# STARTUP APPLICATIONS
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


def init_keys():
    return [
        # Switch between windows in current stack pane
        EzKey("M-b", lazy.layout.down()),
        EzKey("M-f", lazy.layout.up()),
        # Move windows up or down in current stack
        EzKey("M-S-b", lazy.layout.shuffle_down()),
        EzKey("M-S-f", lazy.layout.shuffle_up()),
        # Switch window focus to other pane(s) of stack
        EzKey("M-<space>", lazy.layout.next()),
        # Swap panes of split stack
        EzKey("M-S-<space>", lazy.layout.rotate()),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        EzKey("M-S-<Return>", lazy.layout.toggle_split()),
        # Toggle between different layouts as defined below
        EzKey("M-<Tab>", lazy.next_layout()),
        EzKey("M-C-r", lazy.restart()),
        EzKey("M-C-q", lazy.shutdown()),
        # Window Stuff
        EzKey("M-w", lazy.window.kill()),
        EzKey("M-m", lazy.layout.maximize()),
        # Sound
        EzKey("<XF86AudioMute>", lazy.spawn("pamixer -t")),
        EzKey("<XF86AudioLowerVolume>", lazy.spawn("pamixer -d 2 -u")),
        EzKey("<XF86AudioRaiseVolume>", lazy.spawn("pamixer -i 2 -u")),
        # Applications
        EzKey("M-r", lazy.spawn("rofi -show run")),
        EzKey("M-<Return>", lazy.spawn(my_term)),
        EzKey("M-d", lazy.spawn(my_term + " -e ranger")),
        EzKey("M-e", lazy.spawn("emacsclient -nc")),
        EzKey("M-i", lazy.spawn("firefox")),
        EzKey("M-h", lazy.spawn(my_term + " -e htop")),
    ]


def init_group_names():
    return [
        ("DEF", {"layout": "monadtall"}),
        ("WEB", {"layout": "max"}),
        ("CONF", {"layout": "monadtall"}),
        ("MEDIA", {"layout": "max"}),
        ("GIMP", {"layout": "floating"}),
    ]


def init_groups(ks):
    group_names = init_group_names()
    groups = [Group(name, **kwargs) for name, kwargs in group_names]
    for i, (name, _) in enumerate(group_names, 1):
        ks.extend(
            [
                # mod1 + letter of group = switch to group
                EzKey("M-" + str(i), lazy.group[name].toscreen()),
                # mod1 + shift + letter of group = switch to & move focused window to group
                EzKey("M-S-" + str(i), lazy.window.togroup(name)),
            ]
        )
    return groups


def init_layout_theme():
    return {
        "border_width": 3,
        "margin": 5,
        "border_focus": "#7C4DFF",
        "border_normal": "1D2330",
    }


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                [
                    widget.GroupBox(
                        margin_y=0,
                        margin_x=0,
                        borderwidth=1,
                        active="#AA00FF",
                        inactive="#4A148C",
                        rounded=True,
                        highlight_method="block",
                        foreground="#4A148C",
                        this_screen_border="#4A148C",
                        this_current_screen_border="#EA80FC",
                    ),
                    widget.WindowName(fontsize=14, foreground="#64FFDA",),
                    widget.Systray(),
                    widget.Sep(),
                    widget.Pacman(
                        foreground="#76FF03", execute=my_term + " -e sudo pacman -Syu",
                    ),
                    widget.Sep(),
                    widget.CurrentLayout(foreground="#2962FF",),
                    widget.Sep(),
                    widget.TextBox(text=" 🕒 ", foreground="#D50000",),
                    widget.Clock(foreground="#D32F2F", format="%A, %B %d - %H:%M",),
                ],
                28,
            ),
        ),
    ]


# Drag floating layouts.
def init_mouse():
    return [
        Drag(
            [mod],
            "Button1",
            lazy.window.set_position_floating(),
            start=lazy.window.get_position(),
        ),
        Drag(
            [mod],
            "Button3",
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
        Click([mod], "Button2", lazy.window.bring_to_front()),
    ]


def init_layouts():
    return [
        layout.MonadTall(**layout_theme),
        layout.Max(**layout_theme),
        layout.Floating(**layout_theme),
    ]


if __name__ in ["config", "__main__"]:
    wmname = "LG3D"
    auto_fullscreen = True
    focus_on_window_activation = "smart"
    follow_mouse_focus = True
    bring_front_click = False
    cursor_warp = False
    main = None
    my_term = "urxvtc"
    modifier_keys = {
        "M": "mod4",
        "A": "mod1",
        "S": "shift",
        "C": "control",
    }
    mod = "mod4"
    widget_defaults = dict(font="Ubuntu Bold", fontsize=16, padding=3,)
    extension_defaults = widget_defaults.copy()
    layout_theme = init_layout_theme()
    dgroups_key_binder = None
    dgroups_app_rules = []  # type: List
    layouts = init_layouts()
    screens = init_screens()
    keys = init_keys()
    groups = init_groups(keys)
    mouse = init_mouse()
