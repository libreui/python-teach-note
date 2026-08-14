import json
import pygame


class Level:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.level = 1

        self.triggered_events = []
        self.__current_event = None
        self.data = self._load_level_data()

    def _load_level_data(self):
        """加载关数据"""
        with open(f"level/level_{self.level}.json") as f:
            data = json.load(f)
        return data

    def trigger_event(self, timer):
        """触发事件"""
        if timer > self.data['total_time']:
            return

        for index, event in enumerate(self.data['events']):
            if event['time'] <= timer and index not in self.triggered_events:
                self.__current_event = event
                self.triggered_events.append(index)
                break

    # 获取当前要处理的事件
    def get_current_event(self):
        """获取当前要处理的事件"""
        return self.__current_event

    # 完成当前事件处理
    def complete_event(self):
        """完成当前事件"""
        self.__current_event = None
