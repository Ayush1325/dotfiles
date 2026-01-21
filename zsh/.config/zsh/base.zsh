# General Stuff
setopt inc_append_history
unsetopt nomatch
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

if [ -e /run/.toolboxenv ]
then
	eval "$(direnv hook zsh)"
	alias zola="flatpak-spawn --host flatpak run org.getzola.zola"
	alias flatpak-builder="flatpak-spawn --host flatpak run org.flatpak.Builder"
else
	alias te="toolbox enter"
	alias zola="flatpak run org.getzola.zola"
	alias flatpak-builder="flatpak run org.flatpak.Builder"
fi

# Alias
alias ls='ls --color=auto'
alias ll='ls -la'
