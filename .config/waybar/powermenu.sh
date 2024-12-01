#!/bin/sh

shutdown="⏻ Shutdown"
reboot="↺ Reboot"
lock="🔒Lock"
sleep_opt="⏾ Suspend"

selected_option=$(echo -e "$shutdown\n$sleep_opt\n$reboot\n$lock" | fuzzel -d -p "Power")

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
