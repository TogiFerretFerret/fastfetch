fastfetch --config /home/river/.config/fastfetch/segments/seg1.jsonc --pipe false| python3 ~/.config/fastfetch/segments/microterm.py | rev | cut -c 6- | rev | tr -d '\n' | sed 's/AM)/AM) ▌   /g'
fastfetch --config /home/river/.config/fastfetch/segments/seg2.jsonc --pipe false| python3 ~/.config/fastfetch/segments/microterm.py |sed 's/ST     /ST     ▌   /g'
