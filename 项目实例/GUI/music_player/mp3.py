import win32com.client
import time

class AudioController:
    def __init__(self):
        # 创建 Windows Media Player 对象
        self.wmp = win32com.client.Dispatch("WMPlayer.OCX")
        self.player = None

    def play(self, audio_path):
        """播放音频文件"""
        self.player = self.wmp.newMedia(audio_path)
        self.wmp.currentPlaylist.appendItem(self.player)
        self.wmp.controls.play()
        print(f"开始播放音频文件: {audio_path}")

    def pause(self):
        """暂停播放"""
        if self.player and self.wmp.playState == 3:  # 3 表示正在播放
            self.wmp.controls.pause()
            print("播放已暂停")

    def stop(self):
        """停止播放"""
        if self.player:
            self.wmp.controls.stop()
            print("播放已停止")

    def get_progress(self):
        """获取播放进度"""
        if self.player and self.wmp.playState == 3:
            current_position = self.wmp.controls.currentPosition
            duration = self.player.duration
            if duration > 0:
                progress = (current_position / duration) * 100
                return progress
        return 0

    def next(self, path):
        self.stop()
        self.play(path)

    def prev(self, path):
        self.stop()
        self.play(path)

# 使用示例
if __name__ == "__main__":
    audio_path = "your_audio_file.mp3"
    controller = AudioController()
    controller.play(audio_path)

    try:
        while True:
            progress = controller.get_progress()
            print(f"播放进度: {progress:.2f}%")
            time.sleep(1)
    except KeyboardInterrupt:
        controller.stop()
        print("程序已停止")