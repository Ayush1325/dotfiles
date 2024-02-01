#!/bin/sh

shutdown="⏻ Shutdown"
reboot="↺ Reboot"

selected_option=$(echo -e "$shutdown\n$reboot" | rofi -dmenu -p "Power")

if [ "$selected_option" == "$shutdown" ]
then
	systemctl poweroff
elif [ "$selected_option" == "$reboot" ]
then
	systemctl reboot
else
	echo "No Match"
fi
