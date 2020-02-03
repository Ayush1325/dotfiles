import os

apps = [
    ('/home/ayush/dotfiles/qtile', '/home/ayush/.config/qtile'),
    ('/home/ayush/dotfiles/.Xresources', '/home/ayush/.Xresources'),
    ('/home/ayush/dotfiles/.zshrc', '/home/ayush/.zshrc')
]

def create_all(l):
    for (abs, des) in l:
        os.symlink(abs, des)

        
def init():
    create_all(apps)
