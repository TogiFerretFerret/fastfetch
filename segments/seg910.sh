fastfetch --config /home/river/.config/fastfetch/segments/seg9.jsonc --pipe false| render | rev | cut -c 6- | rev | tr -d '\n'
fastfetch --config /home/river/.config/fastfetch/segments/seg10.jsonc --pipe false| render
