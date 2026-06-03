import sys
import pyte
import unicodedata

COLORS = {
    'black': 0, 'red': 1, 'green': 2, 'brown': 3,
    'blue': 4, 'magenta': 5, 'cyan': 6, 'white': 7,
    'default': 9
}

def render_screen(screen):
    for y in range(max(screen.buffer.keys()) + 1):
        line_str = ""
        row = screen.buffer[y]
        max_x = max(row.keys()) if row else 0
        skip_next = False
        for x in range(max_x + 1):
            if skip_next:
                skip_next = False
                continue
            char = row.get(x, pyte.screens.Char(" ", "default", "default"))
            codes = ["0"]
            if char.bold: codes.append("1")
            if char.italics: codes.append("3")
            if char.underscore: codes.append("4")
            if char.reverse: codes.append("7")
            fg = char.fg
            if fg in COLORS:
                codes.append(f"3{COLORS[fg]}")
            elif len(fg) == 6 and all(c in '0123456789abcdefABCDEF' for c in fg):
                r, g, b = int(fg[0:2],16), int(fg[2:4],16), int(fg[4:6],16)
                codes.append(f"38;2;{r};{g};{b}")
            bg = char.bg
            if bg in COLORS:
                codes.append(f"4{COLORS[bg]}")
            elif len(bg) == 6 and all(c in '0123456789abcdefABCDEF' for c in bg):
                r, g, b = int(bg[0:2],16), int(bg[2:4],16), int(bg[4:6],16)
                codes.append(f"48;2;{r};{g};{b}")
            if unicodedata.east_asian_width(char.data) in ('W', 'F'):
                skip_next = True
            line_str += f"\033[{';'.join(codes)}m{char.data}"
        print(line_str + "\033[0m")

data = sys.stdin.buffer.read()
screen = pyte.Screen(220, 100)
stream = pyte.Stream(screen)
stream.feed(data.decode('utf-8', errors='replace'))
render_screen(screen)
