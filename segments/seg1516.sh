fastfetch --config /home/river/.config/fastfetch/segments/seg15.jsonc --pipe false| render | rev | cut -c 6- | rev | tr -d '\n' 
python3 /home/river/.config/fastfetch/segments/microterm.py
