#!/bin/sh

shutdown=$'\uF011  Shutdown'   # nf-fa-power_off
reboot=$'\uF021  Reboot'       # nf-fa-refresh
lock=$'\uF023  Lock'           # nf-fa-lock
sleep_opt=$'\uF186  Suspend'   # nf-fa-moon_o

selected_option=$(echo -e "$shutdown\n$sleep_opt\n$reboot\n$lock" | rofi -dmenu -p "Power")

if [ "$selected_option" == "$shutdown" ]
then
	systemctl poweroff
elif [ "$selected_option" == "$reboot" ]
then
	systemctl reboot
elif [ "$selected_option" == "$lock" ]
then
	swaylock
elif [ "$selected_option" == "$sleep_opt" ]
then
	systemctl suspend
else
	echo "No Match"
fi
