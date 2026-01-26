fastfetch --config /home/river/.config/fastfetch/segments/seg15.jsonc --pipe false| render | rev | cut -c 6- | rev | tr -d '\n' 
fastfetch --config /home/river/.config/fastfetch/segments/seg16.jsonc --pipe false| render 
