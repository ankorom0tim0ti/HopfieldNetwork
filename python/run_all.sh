#!/bin/bash

# 入力画像のディレクトリ
input_dir="../inputs"
# 重みファイルのディレクトリ
weights_dir="weights"

# すべてのPNG画像に対して
for image_path in "$input_dir"/*.png; do
    image_file=$(basename "$image_path")
    echo "Processing image: $image_file"

    # 各PNG画像に対して全ての.npyファイルを使って処理
    for weight_path in "$weights_dir"/*.npy; do
        weight_file=$(basename "$weight_path")
        echo "  Using weights: $weight_file"
        python hopfield.py -r -asyn "$image_file" "$weight_file"
    done
done