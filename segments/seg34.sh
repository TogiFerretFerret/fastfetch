fastfetch --config /home/river/.config/fastfetch/segments/seg3.jsonc --pipe false| render | rev | cut -c 6- | rev | tr -d '\n'
fastfetch --config /home/river/.config/fastfetch/segments/seg4.jsonc --pipe false| render 
