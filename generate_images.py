# open font file -> produce label and image

import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as mfm
import glob

VALID_DIR = 'korean_test'
valid_font_names = [x.split(".png")[0] for x in os.listdir(VALID_DIR) if ".png" in x]

valid_font_paths = [font_name.replace("__", "/").replace("--", ".") for font_name in valid_font_names]

print(valid_font_paths)

DATA_DIR = "korean_images"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

cls_list = ['가', '나', '다', '라', '마', '바', '사', '아', '자', '차', '카', '타', '파', '하']

for cls in cls_list:

    cls_dir = os.path.join(DATA_DIR, cls)
    if not os.path.exists(cls_dir):
        os.makedirs(cls_dir)

    for idx, vfp in enumerate(valid_font_paths):
        prop = mfm.FontProperties(fname=vfp, size=100)

        target_char = cls

        fig, ax = plt.subplots(figsize=(3, 3))
        ax.text(0.25, 0.25, s=target_char, fontproperties=prop)
        ax.axis("off")
        
        fname = os.path.join(cls_dir, "{}_{:04d}.png".format(target_char, idx))
        plt.savefig(os.path.join(fname))
        plt.close()
