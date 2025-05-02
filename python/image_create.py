import sys
from PIL import Image
import numpy as np

B = 0
W = 255

file_name = ""

if len(sys.argv) != 2:
    print("Usage: python image_create.py output_file_name.png")
    sys.exit(1)

file_name = sys.argv[1]
if file_name[-4:] != ".png":
    print("The output file name must end with the .png extension")
    sys.exit(1)


image_array = np.array([
    [B, B, B, B, B, B, B, B, W, W, W, W, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, W, W, W, W, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, W, W, W, W, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, W, W, W, W, B, B, B, B, B, B, B, B],
    [B, B, B, B, W, W, W, W, W, W, W, W, W, W, W, W, B, B, B, B],
    [B, B, B, B, W, W, W, W, W, W, W, W, W, W, W, W, B, B, B, B],
    [B, B, B, B, W, W, W, W, W, W, W, W, W, W, W, W, B, B, B, B],
    [B, B, B, B, W, W, W, W, W, W, W, W, W, W, W, W, B, B, B, B],
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [B, B, B, B, W, W, W, W, W, W, W, W, W, W, W, W, B, B, B, B],
    [B, B, B, B, W, W, W, W, W, W, W, W, W, W, W, W, B, B, B, B],
    [B, B, B, B, W, W, W, W, W, W, W, W, W, W, W, W, B, B, B, B],
    [B, B, B, B, W, W, W, W, W, W, W, W, W, W, W, W, B, B, B, B],
    [B, B, B, B, B, B, B, B, W, W, W, W, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, W, W, W, W, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, W, W, W, W, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, W, W, W, W, B, B, B, B, B, B, B, B],
], dtype=np.uint8)

image = Image.fromarray(image_array, mode='L')

image.save(f"{file_name[:-4]}-h{len(image_array[0])}-w{len(image_array)}.png")