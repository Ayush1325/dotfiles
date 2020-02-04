import os

apps = [
    ("/dotfiles/qtile", "/.config/qtile"),
    ("/dotfiles/.Xresources", "/.Xresources"),
    ("/dotfiles/.zshrc", "/.zshrc"),
    ("/dotfiles/picom", "/.config/picom"),
    ("/dotfiles/ranger", "/.config/ranger"),
    ("/dotfiles/.emacs.d", "/.emacs.d"),
]


def create_all(l):
    for (a, d) in l:
        home = os.path.expanduser("~")
        os.symlink(home + a, home + d)


def init():
    create_all(apps)
