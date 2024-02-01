# General Stuff
setopt inc_append_history

# Variables
export EDITOR=nvim
export VISUAL=nvim
path+=("$HOME/.local/bin")

# Plugins
PLUGINS_PATH=$HOME/.config/zsh/plugins
source $PLUGINS_PATH/zsh-autosuggestions/zsh-autosuggestions.zsh
source $PLUGINS_PATH/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# Theme
source $PLUGINS_PATH/powerlevel10k/powerlevel10k.zsh-theme
