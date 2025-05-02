import sys
from PIL import Image
import numpy as np

B = 0
W = 255
THRESHOLD = 125

if len(sys.argv) != 2:
    print("Usage: python image_create.py input_file_name.png")
    sys.exit(1)

input_file = sys.argv[1]
if input_file[-4:].lower() != ".png":
    print("The input file must be a .png file")
    sys.exit(1)

image = Image.open(f"../images/{input_file}").convert("RGB")
image_np = np.array(image)

luminance = (
    0.299 * image_np[:, :, 0] +
    0.587 * image_np[:, :, 1] +
    0.114 * image_np[:, :, 2]
)

binary_array = np.where(luminance > THRESHOLD, W, B).astype(np.uint8)

output_image = Image.fromarray(binary_array, mode='L')
output_name = f"{input_file[:-4]}-h{binary_array.shape[1]}-w{binary_array.shape[0]}.png"
output_image.save(f"../images/{output_name}")