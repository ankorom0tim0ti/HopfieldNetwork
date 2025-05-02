import sys
import time
from PIL import Image
import numpy as np
import random

# Constants
W = 255

MAX_LOOP = 3000

OPERATION_MODES = [
    "-m", # Memoraize
    "-r" # Recall
]

MEMORIZE_MODES = [
    "-sc", # self-connected
    "-snc" # self-not-connected
]

RECALL_MODES = [
    "-syn", # sync
    "-asyn" # async
]

THRESHOLD = 1.0e-10

THETA_VALUE = 0
# Constatns

# Valiables

operation_mode = None

self_connection_flag = False

input_files = []
# Valiables


# Functions 
def memorize(input_files, self_connection_flag, output_file_name):
    im = np.array(Image.open(f'../images/{input_files[0]}'))
    im_b = im//W
    im_b_v = im_b.reshape(-1)
    size_data = len(im_b_v)
    x = np.ndarray((len(input_files), size_data))
    # Load image file from images directory as nadarray
    for i in range(0, len(input_files)):
        im = np.array(Image.open(f'../images/{input_files[i]}'))
        im_b = im//W
        im_b_v = im_b.reshape(-1)
        im_b_v = np.where(im_b_v> 0, 1, -1)
        x[i] = np.where(im_b_v> 0, 1, -1)
        
    weight = x.T @ x / len(input_files)
    if not self_connection_flag:
        for i in range(0, size_data):
            weight[i][i] = 0
    np.savetxt(f'weights/{output_file_name}', weight, fmt='%.3f')

def recall(input_file, sync_flag, input_weight_file, output_file_name):
    energy = -1 * np.inf
    im = np.array(Image.open(f'../images/{input_file}'))
    im_b = im//W
    im_shape = im_b.shape
    im_b_v = im_b.reshape(-1, 1)
    x = np.where(im_b_v> 0, 1, -1)
    size_data = len(im_b_v)
    weight = np.loadtxt(f'weights/{input_weight_file}')
    theta = np.ones((size_data, 1)) * THETA_VALUE
    tmp_energy = np.inf
    loop = 0
    if sync_flag:
        while abs(tmp_energy - energy) > THRESHOLD:
            energy = tmp_energy
            loop += 1
            if sync_flag:
                # y = weight @ x
                y = np.dot(weight, x).copy()
                x = np.where(y - theta >= 0, 1, -1)
            tmp_energy = (-0.5 * np.dot(x.T, np.dot(weight, x)) + np.dot(theta.T, x)).item()
            print(np.max(weight))
            print(np.min(weight))
            print(f"ENERGY: {energy} TMP_ENERGY: {tmp_energy} @ {loop}")
    else:
        while loop < MAX_LOOP:
            loop += 1
            rand_value = random.randint(0, size_data-1)
            tmp_value = np.dot(weight[rand_value], x)
            if tmp_value > theta[rand_value]:
                x[rand_value] = 1
            else:
                x[rand_value] = -1
            energy = (-0.5 * np.dot(x.T, np.dot(weight, x)) + np.dot(theta.T, x)).item()
            print(f"ENERGY: {energy} TMP_ENERGY: {tmp_energy} @ {loop}")
    x = x.reshape(im_shape)
    x_img = np.where(x > 0, 255, 0).astype(np.uint8)
    image = Image.fromarray(x_img, mode='L')
    image.save(f"results/{output_file_name}")
# Functions

# Main function
def main():
    if len(sys.argv) <= 3:
        print("Lacking argument")
        sys.exit(1)
    operation_mode = sys.argv[1]
    if operation_mode not in OPERATION_MODES:
        print("Please select operation mode within \"-m\" and \"-r\"")
        sys.exit(1)
    if operation_mode == "-m":
        memorize_mode = sys.argv[2]
        if memorize_mode not in MEMORIZE_MODES:
            sys.exit()
        input_files = sys.argv[3:-1]
        output_file = sys.argv[-1]
        for file in input_files:
            if file[-4:] != ".png":
                print("The input file name must end with the .png extension")
                sys.exit(1)
        if memorize_mode == "-sc": # Self connected
            memorize(input_files, True, output_file)
        else: # memorize_mode: "-snc" (Self not connected)
            memorize(input_files, False, output_file)
    else: # operation_mode : "-r" (Recall)
        recall_mode = sys.argv[2]
        if recall_mode not in RECALL_MODES:
            sys.exit()
        input_file = sys.argv[3]
        weight_file = sys.argv[4]
        sync_mode = sys.argv[2]
        if sync_mode == "-syn": # Sync
            recall(input_file, True, weight_file, f"{input_file[:-4]}-{weight_file[:-4]}{sync_mode}-result-{time.strftime('%Y-%m-%d_%H-%M-%S')}.png")
        else: # sync_mode: "-asyn" (Async)
            recall(input_file, False, weight_file, f"{input_file[:-4]}-{weight_file[:-4]}{sync_mode}-result-{time.strftime('%Y-%m-%d_%H-%M-%S')}.png")

if __name__ == '__main__':
    main()