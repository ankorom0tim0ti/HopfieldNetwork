from PIL import Image
import numpy as np
import sys

if len(sys.argv) != 3:
    print("Usage: python compare_images.py image1.png@images image2.png@results")
    sys.exit(1)

image1 = Image.open(f"../images/{sys.argv[1]}").convert("L")
image2 = Image.open(f"results/{sys.argv[2]}").convert("L")

array1 = np.array(image1)
array2 = np.array(image2)

if array1.shape != array2.shape:
    print("Error: The two images must be the same size.")
    sys.exit(1)

diff_count = np.sum(array1 != array2)

print(f"Number of different pixels: {diff_count}")