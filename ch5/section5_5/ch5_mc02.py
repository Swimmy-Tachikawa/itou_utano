"""ch5_mc02.py
while文を使って、水の上を歩くと、その水を氷に変えてしまう
「雪の女王の靴」プログラムを作ってみましょう。
水ブロックを10個変えたら終了です。終了したらチャットに「Finished!」と表示させてください。
（水ブロックのID：9、氷ブロックのID：79）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# 変数iceに0を代入する


# iceが10以下ならずっとくり返す

    # mc.player.getTilePos()を使ってプレイヤーの位置情報を取得し、変数posに代入する


    # mc.getBlock()を使ってposのブロック情報をblock_idに代入する


    # もし、block_idが9であれば

        # mc.setBlock()で、posと同じ場所に氷ブロックを置く


        # iceを1だけ増やす


# mc.postToChat()を使ってチャットに"Finished!"と表示する
