#!/bin/sh 
picom --config ~/.config/picom/picom.conf &
nitrogen --restore &
pcmanfm -d &
emacs --daemon &
dunst &
/usr/lib/kdeconnectd &
kdeconnect-indicator &
redshift-gtk &
nm-applet &
/usr/bin/lxpolkit &
light-locker --lock-after-screensaver=0 &
