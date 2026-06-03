fastfetch --config /home/river/.config/fastfetch/segments/seg7.jsonc --pipe false| python3 ~/.config/fastfetch/segments/microterm.py | rev | cut -c 6- | rev | tr -d '\n'
fastfetch --config /home/river/.config/fastfetch/segments/seg8.jsonc --pipe false| python3 ~/.config/fastfetch/segments/microterm.py
