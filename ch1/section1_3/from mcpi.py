from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getTilePos()

for i in range(100):
    for j in range(100):
        mc.setBlock(pos.x+i,pos.y+j,pos.z,46,1)