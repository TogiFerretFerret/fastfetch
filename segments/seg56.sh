fastfetch --config /home/river/.config/fastfetch/segments/seg5.jsonc --pipe false| render | rev | cut -c 6- | rev | tr -d '\n'
fastfetch --config /home/river/.config/fastfetch/segments/seg6.jsonc --pipe false| render
