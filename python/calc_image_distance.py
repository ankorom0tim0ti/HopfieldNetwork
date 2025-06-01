import os
import argparse
from PIL import Image
import numpy as np
import pandas as pd

# --- コマンドライン引数の処理 ---
parser = argparse.ArgumentParser(description="Compare image files with result files and output difference counts to Excel.")
parser.add_argument('-i', '--image_keywords', nargs='+', default=[], help='Keywords to filter image files (space-separated).')
parser.add_argument('-r', '--result_keywords', nargs='+', default=[], help='Keywords to filter result files (space-separated).')
args = parser.parse_args()

# --- フィルタ設定 ---
image_include_keywords = args.image_keywords
result_include_keywords = args.result_keywords

# --- フィルタ有効/無効切り替え ---
enable_image_filter = bool(image_include_keywords)
enable_result_filter = bool(result_include_keywords)

# --- ディレクトリ ---
images_dir = "../images"
results_dir = "results"

# --- フィルタ関数定義 ---
def match_keywords(filename, keywords):
    return all(keyword in filename for keyword in keywords)

# --- 対象ファイルリストを取得 ---
image_files = sorted([
    f for f in os.listdir(images_dir)
    if f.endswith(".png")
    and (not enable_image_filter or match_keywords(f, image_include_keywords))
])

result_files = sorted([
    f for f in os.listdir(results_dir)
    if f.endswith(".png")
    and (not enable_result_filter or match_keywords(f, result_include_keywords))
])

# --- 出力ファイル名作成 ---
output_file_name = ""
for i in image_include_keywords:
    output_file_name += i + "_"
for i in result_include_keywords:
    output_file_name += i + "_"
output_file_name = output_file_name.rstrip("_") + ".xlsx"

print(f"出力ファイル名: {output_file_name}")
print(f"対象 image ファイル数: {len(image_files)}")
print(f"対象 result ファイル数: {len(result_files)}")

# --- 距離計算と表作成 ---
distance_matrix = []

for result_file in result_files:
    row = []
    path2 = os.path.join(results_dir, result_file)
    image2 = Image.open(path2).convert("L")
    array2 = np.array(image2)

    for image_file in image_files:
        path1 = os.path.join(images_dir, image_file)
        image1 = Image.open(path1).convert("L")
        array1 = np.array(image1)

        if array1.shape != array2.shape:
            print(f"Skipping (size mismatch): {image_file} vs {result_file}")
            row.append(None)
            continue

        diff_count = np.sum(array1 != array2)
        row.append(diff_count)

    distance_matrix.append(row)

# --- Excelファイルとして保存 ---
df = pd.DataFrame(distance_matrix, columns=image_files, index=result_files)
os.makedirs("excel", exist_ok=True)
df.to_excel("excel/" + output_file_name)
print("出力Excelファイルを保存しました！")