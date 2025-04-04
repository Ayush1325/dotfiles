#!/bin/sh

screenshot_active="Screenshot Active Window"
screenshot_window="Screenshot Window"
screenshot_screen="Screenshot Screen"
screenshot_region="Screenshot Region"

selected_option=$(echo -e "$screenshot_active\n$screenshot_window\n$screenshot_region\n$screenshot_screen" | rofi -dmenu -p "Sceenshot")

time=`date +%Y-%m-%d-%H-%M-%S`
dir="`xdg-user-dir PICTURES`/Screenshots"
mkdir -p $dir
file_name="Screenshot_${time}.png"
file=$dir/$file_name

if [ "$selected_option" == "$screenshot_active" ]
then
	grimshot save active $file
elif [ "$selected_option" == "$screenshot_window" ]
then
	grimshot save window $file
elif [ "$selected_option" == "$screenshot_region" ]
then
	grimshot save area $file
elif [ "$selected_option" == "$screenshot_screen" ]
then
	grimshot save screen $file
else
	echo "No Match"
fi
