"""ch1_mc05.py
チャットに位置情報を表示してみましょう。
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# mc.player.getTilePos() を使ってプレイヤーの位置情報を取得し、変数posに代入する
pos=mc.player.getTilePos()
# mc.postToChat()で、変数 pos の値を表示するwwd
mc.postToChat(pos)

# mc.postToChat()で、変数 pos.x の値を表示する
mc.postToChat(pos.x)

# mc.postToChat()で、変数 pos.y の値を表示する
mc.postToChat(pos.y)

# mc.postToChat()で、変数 pos.z の値を表示する
mc.postToChat(pos.z)