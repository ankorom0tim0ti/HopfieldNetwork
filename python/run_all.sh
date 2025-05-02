#!/bin/bash

for filepath in ../images/*.png; do
    filename=$(basename "$filepath")
    echo "Processing $filename ..."
    python hopfield.py -r -asyn "$filename" image_1~6.npy
done