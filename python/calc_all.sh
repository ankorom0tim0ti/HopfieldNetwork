
image_keyword="image_1-h5-w5."

noise_list=(
  "image_1-h5-w5-noise0.05"
  "image_1-h5-w5-noise0.1-"
  "image_1-h5-w5-noise0.15"
  "image_1-h5-w5-noise0.2"
  "image_1-h5-w5-noise0.3"
  "image_1-h5-w5-noise0.4"
  "image_1-h5-w5-noise0.5"
  "image_1-h5-w5-noise0.6"
  "image_1-h5-w5-noise0.7"
  "image_1-h5-w5-noise0.8"
  "image_1-h5-w5-noise0.9"
  "image_1-h5-w5-noise1.0"
)

async_list=(
  "image_1-asyn"
  "image_1~2-asyn"
  "image_1~4-asyn"
  "image_1~6-asyn"
)

for noise in "${noise_list[@]}"; do
  for async in "${async_list[@]}"; do
    echo "Running: -i ${image_keyword} -r ${noise} ${async}"
    python calc_image_distance.py -i "$image_keyword" -r "$noise" "$async"
  done
done