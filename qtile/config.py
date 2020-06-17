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


# Make steam windows floating
@hook.subscribe.client_new
def float_steam(window):
    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    if (
        wm_class == ("Steam", "Steam")
        and (
            w_name != "Steam"
            # w_name == "Friends List"
            # or w_name == "Screenshot Uploader"
            # or w_name.startswith("Steam - News")
            or "PMaxSize" in window.window.get_wm_normal_hints().get("flags", ())
        )
    ):
        window.floating = True


def init_keys():
    return [
        # Switch between windows in current stack pane
        # EzKey("-b", lazy.layout.down()),
        # EzKey("C-f", lazy.layout.up()),
        # Move windows up or down in current stack
        EzKey("C-S-b", lazy.layout.shuffle_down()),
        EzKey("C-S-f", lazy.layout.shuffle_up()),
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
        EzKey("<XF86AudioLowerVolume>", lazy.spawn("pamixer -d 4 -u")),
        EzKey("<XF86AudioRaiseVolume>", lazy.spawn("pamixer -i 4 -u")),
        # Media
        EzKey("<F1>", lazy.spawn("playerctl previous")),
        EzKey("<F2>", lazy.spawn("playerctl play-pause")),
        EzKey("<F3>", lazy.spawn("playerctl next")),
        # Applications
        EzKey("M-r", lazy.spawn("rofi -show run")),
        EzKey("M-<Return>", lazy.spawn(my_term)),
        EzKey("M-n", lazy.spawn(["sh", "-c", "kill -s USR1 $(pidof deadd-notification-center)"])),
        EzKey("M-S-d", lazy.spawn("pcmanfm")),
        EzKey("M-e", lazy.spawn("emacsclient -nc")),
        EzKey("M-S-i", lazy.spawn("firefox")),
        EzKey("M-S-j", lazy.spawn(my_term + " -e joplin")),
        EzKey("M-S-h", lazy.spawn(my_term + " -e htop")),
        EzKey("M-S-n", lazy.spawn("notion-app")),
    ]


def init_group_names():
    return [
        ("WEB", {"layout": "max"}),
        ("CONF", {"layout": "monadtall"}),
        ("DEV", {"layout": "max"}),
        ("NOTE", {"layout": "max"}),
        ("MEDIA", {"layout": "max"}),
        ("GAME", {"layout": "max"}),
        ("GIT", {"layout": "max"}),
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


def init_layout_theme():
    return {
        "border_width": 3,
        "margin": 5,
        "border_focus": "#7C4DFF",
        "border_normal": "1D2330",
    }


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
                [
                    widget.GroupBox(
                        active=colors["foreground"],
                        inactive=colors["foreground-alt"],
                        highlight_method="line",
                        highlight_color=colors["highlight"],
                        this_current_screen_border=colors["underline"],
                        urgent_border=colors["alert"],
                    ),
                    widget.Spacer(),
                    widget.Image(filename="~/.config/qtile/icons/sound.png",
                                 margin=4,
                                 background=colors["highlight"]),
                    widget.Volume(volume_app="pavucontrol",
                                  padding=4,
                                  fontsize=18,
                                  background=colors["highlight"]),
                    widget.Spacer(length=10),
                    widget.Image(filename="~/.config/qtile/icons/network.png",
                                 margin=4, background=colors["highlight"]),
                    widget.Net(background=colors["highlight"],
                               format="{down} ↓↑ {up}"),
                    widget.Spacer(length=10),
                    widget.Image(filename="~/.config/qtile/icons/memory.png",
                                 margin=4,
                                 background=colors["highlight"]),
                    widget.Memory(format="{MemUsed}M/{MemTotal}M",
                                  background=colors["highlight"]),
                    widget.Spacer(length=10),
                    widget.Image(filename="~/.config/qtile/icons/cpu.png",
                                 margin=4,
                                 background=colors["highlight"]),
                    widget.CPU(format="{freq_current}GHz {load_percent}%",
                               background=colors["highlight"]),
                    widget.Spacer(length=10),
                    widget.Image(filename="~/.config/qtile/icons/temp.png",
                                 margin=4,
                                 background=colors["highlight"]),
                    widget.ThermalSensor(background=colors["highlight"]),
                    widget.Spacer(length=10),
                    widget.CurrentLayoutIcon(background=colors["highlight"],
                                             foreground=colors["underline"],
                                             custom_icon_paths=["~/.config/qtile/icons/layouts/"],
                                             padding=5),
                    widget.Spacer(length=10),
                    widget.Clock(foreground=colors["foreground"],
                                 background=colors["highlight"],
                                 format="%A, %B %d - %H:%M",),
                    widget.Spacer(length=10),
                    widget.Systray(background=colors["highlight"],
                                   icon_size=24, padding=5),
                    widget.Spacer(length=10),
                    widget.Image(filename="~/.config/qtile/icons/notification-resume.png",
                                 margin=2,
                                 background=colors["highlight"],
                                 mouse_callbacks={
                                     "Button1":
                                     lambda _: os.system("notify-send \"DUNST_COMMAND_TOGGLE\"")
                                     }),
                    widget.Image(filename="~/.config/qtile/icons/restart.png",
                                 margin=2,
                                 background=colors["highlight"],
                                 mouse_callbacks={"Button1": lambda _: os.system("sudo reboot")}),
                    widget.Image(filename="~/.config/qtile/icons/suspend.png",
                                 margin=2,
                                 background=colors["highlight"],
                                 mouse_callbacks={"Button1": lambda _: os.system("dm-tool lock")}),
                    widget.Image(filename="~/.config/qtile/icons/shutdown.png",
                                 margin=4,
                                 background=colors["highlight"],
                                 mouse_callbacks={"Button1": lambda _: os.system("sudo shutdown now")}),
                ],
                30,
                background="#1d1f21",
                margin=0,
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
    my_term = "alacritty"
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
    dgroups_app_rules = []  # type: List
    layouts = init_layouts()
    screens = init_screens()
    keys = init_keys()
    groups = init_groups(keys)
    mouse = init_mouse()
