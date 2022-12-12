import os
from PIL import Image

for f in os.listdir("./imgs"):
    basewidth = 512
    img = Image.open("./imgs/" + f)
    if img.size[0] == basewidth:
        continue
    wpercent = basewidth / float(img.size[0])
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    img.save("./imgs/" + f)
