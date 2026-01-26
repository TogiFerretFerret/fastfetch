fastfetch --config /home/river/.config/fastfetch/segments/seg7.jsonc --pipe false| render | rev | cut -c 6- | rev | tr -d '\n'
fastfetch --config /home/river/.config/fastfetch/segments/seg8.jsonc --pipe false| render
