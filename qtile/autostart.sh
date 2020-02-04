#!/bin/sh 
picom --config ~/.config/picom/picom.conf &
nitrogen --restore &
urxvtd -q -o -f &
pcmanfm -d &
