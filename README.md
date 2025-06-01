# Hopfiled-Network
Hopfield-Networkを実装したpythonコード  
基本的には0/255で2値化された白黒画像を入力として与えて学習、想起させる  
# 導入/実行
## 導入
1. 本リポジトリをクローンする
```
git clone git@github.com:ankorom0tim0ti/HopfieldNetwork.git # via ssh
```
2. pythonの仮想環境を作成する
```
python -m venv <name_of_virtual_environment> # @ Mac and Windows and Linux
```
3. 仮想環境を有効化する
```
source <name_of_virtual_environment>/bin/activate # @ Mac and Linux
./<name_of_virtual_environment>/Scripts/activate # @ Windows
```
4. 必要なライブラリをインストールする
```
pip install -r requirements.txt
```
5. プロジェクトのルートディレクトリに`images`、`weights`、`results`ディレクトリを作成する
```
mkdir images # in HopfieldNetwork direcotry
mkdir weights # in HopfieldNetwork direcotry
mkdir results # in HopfieldNetwork direcotry
```
## 実行
6. 2値化したい画像を`images`ディレクトリに配置する。
7. `python`ディレクトリに移動して以下のコマンドを実行し、2値化した`.png`ファイルを作成する。
```
cd python
python image_binarizer.py image.png # image-hxxx-wxxx.png will be created as a result of the execution at images directory
```
8. `python`ディレクトリで2以下のコマンドを実行して値化した画像にノイズを加える
```
python image_noise_adder.py image-hxxx-wxxx.png 0.1 # image-hxxx-wxxx-noise0.1.png will be created as a result of the execution at images directory
```
9. `python`ディレクトリで以下のコマンドを実行して学習し、その結果として`weights`ディレクトリに得られる重み行列を格納した`.npy`ファイルを出力する。引数として与えられる`-snc`を`-sc`に変えることで自己結合を許容する
```
python hopfield.py -m -snc image-hxxx-wxxx.png image.npy # image.npy will be created as a result of the execution at weights directory
```

10. `python`ディレクトリで以下のコマンドを実行して想起し、その結果として`results`ディレクトリに得られる画像`.png`を出力する。引数として与えられる`-syn`を`-asyn`に変えることで同期更新を非同期更新にすることができる
```
python hopfield.py -r -syn image-hxxx-wxxx-noise0.1.png image.npy # image-hxxx-wxxx-noise0.1-syn-result.png will be created as a result of the execution at results directory
```

11. `python`ディレクトリで以下のコマンドを実行して元の画像と想起された画像の距離(値の違うマスの合計値)をコマンドラインに出力する
```
python calc_image_distance.py image-hxxx-wxxx.png image-hxxx-wxxx-noise0.1-syn-result.png
```