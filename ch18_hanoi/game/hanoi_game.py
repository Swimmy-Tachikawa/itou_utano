import time


class TowerOfHanoi:
    def __init__(self, disk_count, renderer):
        self.disk_count = disk_count
        self.move_count = 0
        self.renderer = renderer
        
        # 塔の状態
        self.towers = [[], [], []]

    
    def play(self):
        """ゲームを実行"""  
        print("ハノイの塔を始めます")
        self.renderer.show_message("Start!")

        # ① 実行前の準備
        self.renderer.prepare_site()
        self.renderer.set_triggers()
        self.renderer.build_towers()
        self.renderer.draw_disks(self.towers)
