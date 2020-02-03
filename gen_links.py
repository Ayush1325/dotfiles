import os

apps = [('/home/ayush/dotfiles/qtile', '/home/ayush/.config/qtile')]

def create_all(l):
    for (abs, des) in l:
        os.symlink(abs, des)

        
if __name__ == '__main__':
    create_all(apps)
