import urllib.request
import os


# /////////////////////////////////////////////////////////////////////
# ここを書き換えてね
# タイル番号は以下を参照
# https://maps.gsi.go.jp/development/tileCoordCheck.html

z = 17
x_min = 116496
y_min = 49549
width = 10
# /////////////////////////////////////////////////////////////////////


x_max = x_min + width
y_max = y_min + width

tile_count = 0
tile_count_max = ((x_max + 1) - x_min) * ((y_max + 1) - y_min)


for x in range(x_min, x_max + 1):
    for y in range(y_min, y_max + 1):
        tile_count += 1

        try:
            data = urllib.request.urlopen(f'https://cyberjapandata.gsi.go.jp/xyz/seamlessphoto/{z}/{x}/{y}.jpg').read()
            os.makedirs(f'./{z}/{x}', exist_ok=True)
            print(f'[{tile_count}/{tile_count_max}]できた {z}/{x}/{y}')
            with open(f'./{z}/{x}/{y}.png', mode="wb") as f:
                f.write(data)
        except urllib.error.HTTPError:
            print(f'[{tile_count}/{tile_count_max}]えらー {z}/{x}/{y}')

print('おわり')
