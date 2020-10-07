from libqtile.config import EzKey, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.log_utils import logger
from typing import List  # noqa: F401
import os
import subprocess

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])

@lazy.function
def float_to_front(qtile):
    logging.info("bring floating windows to front")
    for group in qtile.groups:
        for window in group.windows:
            if window.floating:
                window.cmd_bring_to_front()

@hook.subscribe.client_new
def float_steam(window):
    float_class = [
        ("lxpolkit", "Lxpolkit"),
        ("evelauncher.exe", "steam_app_8500"),
        ("pavucontrol", "Pavucontrol"),
        ("gw2-64.exe", "gw2-64.exe"),
        ("glyphclientapp.exe", "steam_app_743090"),
        ("War Thunder", "War Thunder"),
        ("totono_en.exe", "totono_en.exe"),
        ("launcher.exe", "steam_app_230410"),
        ("saya_en.exe", "saya_en.exe"),
        ("xdman-Main", "xdman-Main"),
    ]
    float_name = [
        "JetBrains Toolbox",
        "Heartache 101 v2.5",
        "Android Emulator - Pixel_3a:5554",
        "Welcome to Android Studio",
        "ActionRPG (DEBUG)",
        "The Fruit of Grisaia Unrated Version",
        "Wine configuration",
        "The Labyrinth of Grisaia Unrated Version",
        "The Eden of Grisaia Unrated Version",
        "Genshin Impact Beta",
        "Android Virtual Device Manager",
    ]
    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    # logger.warning(wm_class)
    # logger.warning(wm_class in float_class)
    # logger.warning(w_name)
    # logger.warning(w_name in float_name)
    if (
        wm_class == ("Steam", "Steam")
        and (
            w_name != "Steam"
            # w_name == "Friends List"
            # or w_name == "Screenshot Uploader"
            # or w_name.startswith("Steam - News")
            or "PMaxSize" in window.window.get_wm_normal_hints().get("flags", ())
        )
    ) or (
        w_name in float_name
    ) or (
        wm_class in float_class
    ) or (
        wm_class == ("Places", "firefox") and w_name == "Library"
    ):
        window.floating = True

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

def init_keys():
    return [
        # Switch between windows in current stack pane
        # EzKey("-b", lazy.layout.down()),
        # EzKey("C-f", lazy.layout.up()),
        EzKey("M-b", lazy.layout.shuffle_down()),
        EzKey("M-f", lazy.layout.shuffle_up()),
        EzKey("M-<space>", lazy.layout.next()),
        EzKey("M-S-f", float_to_front),
        # Swap panes of split stack
        # EzKey("M-S-<space>", lazy.layout.rotate()),
        # Toggle between split and unsplit sides of stack.
        # EzKey("M-S-<Return>", lazy.layout.toggle_split()),
        EzKey("M-<Tab>", lazy.next_layout()),
        EzKey("M-C-r", lazy.restart()),
        EzKey("M-C-q", lazy.shutdown()),
        EzKey("M-w", lazy.window.kill()),
        EzKey("M-m", lazy.window.toggle_maximize()),
        # Sound
        EzKey("<XF86AudioMute>", lazy.spawn("pamixer -t")),
        EzKey("<XF86AudioLowerVolume>", lazy.spawn("pamixer -d 1 -u")),
        EzKey("<XF86AudioRaiseVolume>", lazy.spawn("pamixer -i 1 -u")),
        # Media
        EzKey("<XF86AudioPrev>", lazy.spawn("playerctl previous")),
        EzKey("<XF86AudioPlay>", lazy.spawn("playerctl play-pause")),
        EzKey("<XF86AudioStop>", lazy.spawn("playerctl stop")),
        EzKey("<XF86AudioNext>", lazy.spawn("playerctl next")),
        # Applications
        EzKey("M-r", lazy.spawn("rofi -show drun")),
        EzKey("M-S-w", lazy.spawn("rofi -show window")),
        EzKey("M-<Return>", lazy.spawn(my_term)),
        EzKey("M-C-d", lazy.spawn("pcmanfm")),
        EzKey("M-e", lazy.spawn("emacsclient -nc")),
        EzKey("M-C-i", lazy.spawn("firefox")),
        EzKey("M-S-h", lazy.spawn(my_term + " -e bpytop")),
        # EzKey("M-C-n", lazy.spawn("notion-app")),
        EzKey("M-C-m", lazy.spawn("youtubemusic-nativefier")),
        # Screenshot
        EzKey("M-<Print>", lazy.spawn("flameshot full -p /home/ayush/Pictures/Screenshots")),
    ]

def init_group_names():
    return [
        ("🌐", {"layout": "max"}),
        ("⚓", {"layout": "monadtall"}),
        ("😎", {"layout": "max"}),
        ("📓", {"layout": "monadtall"}),
        ("🎥", {"layout": "max"}),
        ("🎮", {"layout": "max"}),
        ("📁", {"layout": "max"}),
        ("📦", {"layout": "floating"})
    ]

def init_groups(ks):
    group_names = init_group_names()
    groups = [Group(name, **kwargs) for name, kwargs in group_names]
    for i, (name, _) in enumerate(group_names, 1):
        ks.extend(
            [
                EzKey("M-" + str(i), lazy.group[name].toscreen()),
                EzKey("M-S-" + str(i), lazy.window.togroup(name)),
            ]
        )
    return groups

def init_layouts():
    return [
        layout.MonadTall(**layout_theme),
        layout.TreeTab(**layout_theme),
        layout.Max(**layout_theme),
        layout.Floating(**layout_theme),
    ]

def init_layout_theme():
    return {
        "border_width": 3,
        "margin": 5,
        "border_focus": "#7C4DFF",
        "border_normal": "1D2330",
    }

def playerctl_control(icon, name):
    return widget.Image(filename=icon, margin=2,
                 mouse_callbacks={"Button1": lambda _: subprocess.Popen(f"playerctl --player={name} play-pause", shell=True)})

def system_action(icon, cmd):
    return widget.Image(filename=icon,
                        margin=2,
                        mouse_callbacks={
                            "Button1":
                            lambda _: subprocess.Popen(cmd, shell=True)
                        })

def bar_widgets(colors):
    seperator = widget.Sep(linewidth=3, padding=4, foreground=colors["foreground"])
    return [
        widget.GroupBox(
            active=colors["foreground"],
            inactive=colors["foreground-alt"],
            highlight_method="line",
            highlight_color=colors["highlight"],
            this_current_screen_border=colors["underline"],
            urgent_border=colors["alert"],
        ),
        widget.Spacer(),
        seperator,
        playerctl_control("~/.config/qtile/icons/firefox.png", "firefox"),
        playerctl_control("~/.config/qtile/icons/youtubemusic.png", "chromium"),
        seperator,
        widget.Image(filename="~/.config/qtile/icons/sound.png", margin=4),
        widget.PulseVolume(volume_app="pavucontrol", padding=4, fontsize=18),
        seperator,
        widget.Image(filename="~/.config/qtile/icons/network.png", margin=4),
        widget.Net(format="{down} ↓↑ {up}"),
        seperator,
        widget.Image(filename="~/.config/qtile/icons/memory.png", margin=4),
        widget.Memory(format="{MemUsed}M/{MemTotal}M"),
        seperator,
        widget.Image(filename="~/.config/qtile/icons/cpu.png", margin=4),
        widget.CPU(format="{freq_current}GHz {load_percent}%"),
        seperator,
        widget.Image(filename="~/.config/qtile/icons/temp.png", margin=4),
        widget.ThermalSensor(),
        seperator,
        widget.CurrentLayoutIcon(foreground=colors["underline"],
                                 custom_icon_paths=["~/.config/qtile/icons/layouts/"],
                                 padding=5),
        seperator,
        widget.Clock(foreground=colors["foreground"], format="%A, %B %d - %H:%M",),
        seperator,
        widget.Systray(icon_size=24, padding=5),
        seperator,
        system_action("~/.config/qtile/icons/notification-resume.png", "notify-send \"DUNST_COMMAND_TOGGLE\""),
        system_action("~/.config/qtile/icons/restart.png", "systemctl reboot"),
        system_action("~/.config/qtile/icons/suspend.png", "dm-tool lock"),
        system_action("~/.config/qtile/icons/shutdown.png", "systemctl poweroff"),
    ]

def init_screens():
    colors = {
        "foreground": "#d8dee9",
        "foreground-alt": "#555555",
        "highlight": "#444444",
        "underline": "#268bd2",
        "alert": "#ed0b0b",
    }
    return [
        Screen(
            top=bar.Bar(
                bar_widgets(colors),
                30,
                background="#1d1f21",
                margin=0,
                opacity=0.95,
            ),
        ),
    ]

if __name__ in ["config", "__main__"]:
    wmname = "LG3D"
    auto_fullscreen = True
    focus_on_window_activation = "smart"
    follow_mouse_focus = True
    bring_front_click = False
    cursor_warp = False
    main = None
    my_term = "alacritty"
#    my_term = "emacsclient -nce (vterm)"
    modifier_keys = {
        "M": "mod4",
        "A": "mod1",
        "S": "shift",
        "C": "control",
    }
    mod = "mod4"
    widget_defaults = dict(font="Ubuntu Bold", fontsize=16, padding=5,)
    extension_defaults = widget_defaults.copy()
    layout_theme = init_layout_theme()
    dgroups_key_binder = None
    dgroups_app_rules = []
    layouts = init_layouts()
    screens = init_screens()
    keys = init_keys()
    groups = init_groups(keys)
    mouse = init_mouse()
