"""ch4_mc03.py
雪の上、または水の中にいるときに実行すると、Minecraftのチャットに"Cold!"と表示し、
それ以外の場合は"Nice temp!"と表示するプログラムを作ってみましょう。
（雪ブロックのID：78、水ブロックのID：9）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# mc.player.getTilePos()を使ってプレイヤーの位置情報を取得し、変数posに代入する


# mc.getBlock()を使って、ブロック情報を取得し、変数block_idに代入する


# もし、block_idが78、または9なら

    # mc.postToChat()を使って"Cold!"と表示する

# でなければ

    # mc.postToChat()を使って"Nice temp!"と表示する
