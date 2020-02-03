import git

repos = [
    ('https://github.com/zsh-users/zsh-autosuggestions', '/home/ayush/.oh-my-zsh/custom/plugins/zsh-autosuggestions'),
    ('https://github.com/zsh-users/zsh-syntax-highlighting.git', '/home/ayush/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting'),
    ('https://github.com/romkatv/powerlevel10k.git', '/home/ayush/.oh-my-zsh/custom/themes/powerlevel10k')
]

def init():
    for (link, path) in repos:
        git.clone_from(link, path)
