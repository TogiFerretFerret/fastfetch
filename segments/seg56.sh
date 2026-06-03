fastfetch --config /home/river/.config/fastfetch/segments/seg5.jsonc --pipe false| python3 ~/.config/fastfetch/segments/microterm.py | rev | cut -c 6- | rev | tr -d '\n'
fastfetch --config /home/river/.config/fastfetch/segments/seg6.jsonc --pipe false| python3 ~/.config/fastfetch/segments/microterm.py
