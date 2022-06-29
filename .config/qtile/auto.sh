#!/bin/sh

feh --bg-fill ~/.config/qtile/wallpaper.jpg 
dunst -c ~/.config/dunst/dunstrc &
picom &

# Storage
udiskie &
