"""ch3_mc03.py
上方向に瞬間移動させる動きを関数にしてみましょう。
関数「jump」を作り、引数に渡した値分だけ上方向に移動させます。
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()


# 関数「jump」を定義する。引数にpowerを用意する。

    # mc.player.getTilePos()を使って、プレイヤーの位置情報を取得し、変数pos に代入する


    # mc.player.setTilePos()を使ってプレイヤーの位置を変更する。y座標を + power すると、power分だけ上に移動する



# 引数を指定してjump関数を実行する
