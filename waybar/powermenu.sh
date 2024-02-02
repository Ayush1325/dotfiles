#!/bin/sh

shutdown="⏻ Shutdown"
reboot="↺ Reboot"
lock="🔒Lock"

selected_option=$(echo -e "$shutdown\n$reboot\n$lock" | rofi -dmenu -p "Power")

if [ "$selected_option" == "$shutdown" ]
then
	systemctl poweroff
elif [ "$selected_option" == "$reboot" ]
then
	systemctl reboot
elif [ "$selected_option" == "$lock" ]
then
	swaylock
else
	echo "No Match"
fi
