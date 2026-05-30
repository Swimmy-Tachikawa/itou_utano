"""ch3_mc02.py
プレイヤーを現在位置から20ブロック分、上方向に移動させてみましょう。
移動したあと、プレイヤーはどんな動きになるでしょうか。
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# mc.player.getTilePos()を使って、プレイヤーの位置情報を取得し、変数pos に代入する


# mc.player.setTilePos()を使ってプレイヤーの位置を変更する。y座標を+20すると、今いる場所の20ブロック分上に移動する


# プラスα: 右クリックでブロックを19個積み上げ、mc.player.setTilePos() でその上に瞬間移動させる
