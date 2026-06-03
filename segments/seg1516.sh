fastfetch --config /home/river/.config/fastfetch/segments/seg15.jsonc --pipe false| python3 ~/.config/fastfetch/segments/microterm.py | rev | cut -c 6- | rev | tr -d '\n' 
fastfetch --config /home/river/.config/fastfetch/segments/seg16.jsonc | python3 ~/.config/fastfetch/segments/microterm.py
