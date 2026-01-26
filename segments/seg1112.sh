fastfetch --config /home/river/.config/fastfetch/segments/seg11.jsonc --pipe false| render | rev | cut -c 6- | rev | tr -d '\n' 
fastfetch --config /home/river/.config/fastfetch/segments/seg12.jsonc --pipe false| render 
