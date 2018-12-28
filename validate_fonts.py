# open font file -> produce label and image

import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as mfm

TEST_DIR = 'korean_test'
if not os.path.exists(TEST_DIR):
    os.makedirs(TEST_DIR)

font_list = [fp for fp in mfm.findSystemFonts() if "Library" in fp]

for fp in font_list:
    try:
        font_name = fp.replace("/", "__").replace(".", "--")
        prop = mfm.FontProperties(fname=fp, size=100)
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.text(0.25, 0.25, s="가", fontproperties=prop)
        ax.axis("off")
        fname = os.path.join(TEST_DIR, font_name + ".png")
        print(fname)
        plt.savefig(os.path.join(fname))
        plt.close()

    except:
        pass