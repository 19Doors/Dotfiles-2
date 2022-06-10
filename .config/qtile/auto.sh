#!/bin/sh

timedatectl set-ntp true &
feh --bg-fill wallpaper.jpg &
dunst -c ~/.config/dunst/dunstrc &
picom &
