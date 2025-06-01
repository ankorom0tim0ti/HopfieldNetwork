import sys
from PIL import Image
import numpy as np

B = 0
W = 255

file_name = ""

if len(sys.argv) != 3:
    print("Usage: python image_create.py output_file_name.png")
    sys.exit(1)

file_name = sys.argv[1]
if file_name[-4:] != ".png":
    print("The output file name must end with the .png extension")
    sys.exit(1)

noise_ratio = sys.argv[2]
try:
     noise_ratio = float(noise_ratio)
except:
     sys.exit()

im = np.array(Image.open(f'../images/{file_name}'))
im_shape = im.shape
im_v = im.reshape(-1)
num_W = int(len(im_v) * noise_ratio)
indices = np.random.choice(len(im_v), num_W, replace=False) 
for i in indices:
        rand_value = np.random.randint(0,2)
        im_v[i] = B if rand_value == B else W



im_noise = im.reshape(im_shape)

image = Image.fromarray(im_noise, mode='L')

image.save(f"../images/{file_name[:-4]}-noise{noise_ratio}.png")