from PIL import Image, ImageFile
from pathlib import Path
import os

# 元画像が入ったディレクトリ
INPUT_PATH='static/photos'
OUTPUT_PATH='static/photos/thumbnail'
p = Path(INPUT_PATH)
src_img_list = list(p.glob('*.png'))

def crop_thumbnail(src_img:str)->ImageFile:
    # 画像読み込み
    img = Image.open(src_img)

    # 中心座標を計算
    center_x = int(img.width / 2)
    center_y = int(img.height / 2)

    if img.width > img.height:
        new_size = img.height
    else:
        new_size = img.width

    # トリミング
    _crop_img = img.crop((center_x - new_size / 2, center_y - new_size / 2, center_x + new_size / 2, center_y + new_size / 2))
    return _crop_img.resize((400, 400)) 


for i, src_img in enumerate(src_img_list):

    # トリミング
    img_crop = crop_thumbnail(src_img)

    # トリミングした画像を保存
    img_crop.save(os.path.join(OUTPUT_PATH, src_img.name), 'PNG', quality=100, optimize=True)

