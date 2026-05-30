"""ch8_ex18.py
Minecraftの世界にテキストの図のような配置の壁を作りましょう。
壁の材料は好きなブロック5種類です。
好きなブロックID５つを要素とするリストを作り、それをうまく使いましょう。
x方向：同じ種類のブロックを5つ並べる
y方向：異なる種類のブロックをリストの要素数だけ積み上げる

＜ブロックIDリスト＞
https://www.sai.co.jp/swimmy/blocklist.php
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
