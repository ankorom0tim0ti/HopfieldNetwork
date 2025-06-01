#!/bin/bash


input_dir="../inputs"

weights_dir="weights"

for image_path in "$input_dir"/*.png; do
    image_file=$(basename "$image_path")
    echo "Processing image: $image_file"

    for weight_path in "$weights_dir"/*.npy; do
        weight_file=$(basename "$weight_path")
        echo "  Using weights: $weight_file"
        python hopfield.py -r -asyn "$image_file" "$weight_file"
    done
done