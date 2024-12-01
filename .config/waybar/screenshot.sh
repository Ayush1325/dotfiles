#!/bin/sh
#
# Needs grimshot (part of sway-contrib in archlinux)

GRIMSHOT=/usr/share/sway-contrib/grimshot

screenshot_active="Screenshot Active Window"
screenshot_window="Screenshot Window"
screenshot_screen="Screenshot Screen"
screenshot_region="Screenshot Region"

selected_option=$(echo -e "$screenshot_active\n$screenshot_window\n$screenshot_region\n$screenshot_screen" | fuzzel -d -p "Sceenshot")

time=`date +%Y-%m-%d-%H-%M-%S`
dir="`xdg-user-dir PICTURES`/Screenshots"
file_name="Screenshot_${time}.png"
file=$dir/$file_name

if [ "$selected_option" == "$screenshot_active" ]
then
	$GRIMSHOT save active $file
elif [ "$selected_option" == "$screenshot_window" ]
then
	$GRIMSHOT save window $file
elif [ "$selected_option" == "$screenshot_region" ]
then
	$GRIMSHOT save area $file
elif [ "$selected_option" == "$screenshot_screen" ]
then
	$GRIMSHOT save screen $file
else
	echo "No Match"
fi
