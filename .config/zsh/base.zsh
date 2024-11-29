# General Stuff
setopt inc_append_history
zstyle ':completion:*' rehash true

# Variables
export EDITOR=nvim
export VISUAL=nvim
path+=("$HOME/.local/bin")

# Plugins
PLUGINS_PATH=$HOME/.config/zsh/plugins
source $PLUGINS_PATH/zsh-autosuggestions/zsh-autosuggestions.zsh
source $PLUGINS_PATH/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source $PLUGINS_PATH/zsh-autoswitch-virtualenv/autoswitch_virtualenv.plugin.zsh

# Theme
source $PLUGINS_PATH/powerlevel10k/powerlevel10k.zsh-theme

eval "$(direnv hook zsh)"

# Alias
# alias zola="flatpak run org.getzola.zola"
