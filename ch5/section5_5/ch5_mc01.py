"""ch5_m01.py
プレーヤーが迷子(まいご)にならないように、while文を使って1秒おきに、
その場に花を置くプログラムを作ってみましょう。
花を30本置いたら終了です。終了したらチャットに「Finished!」と表示させてください。
（花ブロックのID：38）
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# timeモジュールからsleep関数を読み込む


# 変数flowersに0を代入する


# flowersが30以下ならずっとくり返す

    # mc.player.getTilePos()を使ってプレイヤーの位置情報を取得し、変数posに代入する


    # mc.setBlock()を使って花をその場に置く


    # flowersを1だけ増やす


    # sleep関数を使って1秒停止する


# mc.postToChat()を使ってチャットに"Finished!"と表示する
