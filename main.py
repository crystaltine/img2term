import blessed
from PIL import Image
from utils import fcode, cls
from typing import List, Tuple

term = blessed.Terminal()

im = Image.open('img4.png')

PIXEL = "▄"

pixels = list(im.getdata())
width, height = im.size
pixels: List[List[Tuple[int, int, int, int]]] = [pixels[i * width:(i + 1) * width] for i in range(height)]

final_chars = [] # should eventually be a list of lists of strings to be printed

# look through pairs of rows - top row sets the bg color of the pixel (top half), bottom row sets the fg color of the pixel (bottom half)
for i in range(0, len(pixels)-1, 2): # TODO - last row of odd height images is not being processed
    row = pixels[i]
    row2 = pixels[i + 1]
    
    final_row: List[str] = []
    
    for j in range(len(row)):
        top_pixel = row[j]
        bottom_pixel = row2[j]
        final_row.append("\x1b[0m" + fcode(foreground=bottom_pixel[0:3], background=top_pixel[0:3]) + PIXEL)
        
    final_chars.append(final_row)
    
cls()
for row in final_chars:
    print(''.join(row) + '\x1b[0m')
#print(f"\x1b[0msize of img in chars: {len(final_chars)}x{len(final_chars[0])}")