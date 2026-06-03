fastfetch --config /home/river/.config/fastfetch/segments/seg13.jsonc --pipe false| python3 ~/.config/fastfetch/segments/microterm.py | rev | cut -c 6- | rev | tr -d '\n' 
fastfetch --config /home/river/.config/fastfetch/segments/seg14.jsonc --pipe false| python3 ~/.config/fastfetch/segments/microterm.py 
