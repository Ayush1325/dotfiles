#!/bin/sh 
picom --config ~/.config/picom/picom.conf &
nitrogen --restore &
pcmanfm -d &
emacs --daemon &
dunst &
/usr/lib/kdeconnectd &
