import pyte
import subprocess
import os
import unicodedata

# 1. Map pyte color names to ANSI numbers
COLORS = {
    'black': 0, 'red': 1, 'green': 2, 'brown': 3, 
    'blue': 4, 'magenta': 5, 'cyan': 6, 'white': 7, 
    'default': 9
}

def render_screen(screen):
    # Iterate over the rows that have data
    for y in range(max(screen.buffer.keys()) + 1):
        line_str = ""
        row = screen.buffer[y]
        max_x = max(row.keys()) if row else 0
        
        skip_next = False
        
        for x in range(max_x + 1):
            # If the previous char was Japanese/Wide, skip this cell to prevent misalignment
            if skip_next:
                skip_next = False
                continue

            # Get char at this position (or default space)
            char = row.get(x, pyte.screens.Char(" ", "default", "default"))
            
            # --- COLOR LOGIC ---
            codes = []
            
            # Reset is simplistic but safest: Reset everything (\033[0m), then re-apply
            # (Optimized renderers diff the state, but this is the "tiny" reliable version)
            codes.append("0") 
            
            if char.bold: codes.append("1")
            if char.italics: codes.append("3")
            if char.underscore: codes.append("4")
            if char.reverse: codes.append("7")
            
            # Map 'red' -> 31, 'default' -> 39
            if char.fg in COLORS: codes.append(f"3{COLORS[char.fg]}")
            if char.bg in COLORS: codes.append(f"4{COLORS[char.bg]}")
            
            # --- WIDTH LOGIC ---
            # Check if Japanese/Wide char
            if unicodedata.east_asian_width(char.data) in ('W', 'F'):
                skip_next = True
            
            # Add ANSI codes + Character to line
            line_str += f"\033[{';'.join(codes)}m{char.data}"

        print(line_str + "\033[0m")

# --- YOUR SETUP CODE ---
env = os.environ.copy()
# Run Fastfetch
p = subprocess.Popen(
    'fastfetch --config /home/river/.config/fastfetch/segments/seg16.jsonc --pipe false',
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, env=env
)
out, err = p.communicate()

# Feed to Pyte
screen = pyte.Screen(80, 50) # Ensure height (50) is enough for your output
stream = pyte.Stream(screen)
stream.feed(out.decode('utf-8'))

# Print result
render_screen(screen)
