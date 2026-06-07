"""ch1_mc02.py
テキストのコードを打ち込んで実行してください。
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# 自分の誕生日データを代入する
birthday="2017-04-21"

# チャットに誕生日データを表示する
mc.postToChat(birthday)