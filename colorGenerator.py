import PIL
import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO 
import sys

imageList = []
response = requests.get(sys.argv[1])
image2 = PIL.Image.open(BytesIO(response.content))

imageColors = []
image2.size
rgb = image2.convert('RGB')
for x in range(image2.size[0]):
    for y in range(image2.size[1]):
        imageColors.append(str(rgb.getpixel((x, y))))
imageColors = set(imageColors)

df = pd.DataFrame(imageColors)
df = df[0].value_counts().reset_index(name='Count')
df = df.sort_values("Count", ascending=False)

listy = df["index"][0:10]
parsedListy = []
for i in listy:
    parsedListy.append(tuple([int(i2) for i2 in i[1:-1].split(", ")]))

listy = ["#"+'%02x%02x%02x' % i for i in parsedListy]
listy = ", ".join(listy)
print(listy, flush=True)


fig, ax = plt.subplots(10)
fig.subplots_adjust(left=None, bottom=0.0, right=None, top=2.0, wspace=0.0, hspace=2.0)
for i in range(len(parsedListy)):
    ax[i].set_facecolor("#"+'%02x%02x%02x' % parsedListy[i])
    ax[i].axes.xaxis.set_ticklabels([])
    ax[i].axes.yaxis.set_ticklabels([])
    ax[i].set_xlabel("#"+'%02x%02x%02x' % parsedListy[i])
 
    ax[i].plot(111)
fig.savefig("colors.png")