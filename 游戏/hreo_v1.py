'''
Author: Libre Gu 
Date: 2023-06-03 08:36:49
LastEditors: Libre Gu 
LastEditTime: 2023-06-03 09:07:35
FilePath: /PythonJupyter/hreo_v1.py
Description: 
Copyright (c) 2023 by Libre, All Rights Reserved. 
'''
# 初始化 BEGIN
# 游戏背景
__GAME_NAME__ = "笑傲江湖"
__GAME_VERSION__ = "1.0.0"

print("=====================")
print("{0} v{1}".format(__GAME_NAME__, __GAME_VERSION__))
print("=====================")
print("游戏背景：")
print("""
欢迎来到江湖，你是江湖中的一位侠客，
听说有一把传说中的屠龙宝刀藏在某个地方，
你决定踏上寻找屠龙宝刀的道路
......
""")
      
# 创建主角
my = {
    "name": "张无忌",
    'hp': 200,
    'mp': 100,
    'attack': 10,
    'skills': {
        "华山剑法": {'attack': 10, 'mp': 10},
        "独孤九剑": {'attack': 20, 'mp': 20},
        "葵花宝典": {'attack': 30, 'mp': 30}
    }
}

# 测试主角
print('---测试主角--------------------------')
print("名字：%s\t" % my["name"])
print("血量：%d\t" % my["hp"])
print("魔法: %d\t" % my["mp"])
print("攻击力：%d \t" % my["attack"])
print("技能：")
for k,v in my["skills"].items():
    print("\t%s：%s" % (k, v))
print("-----------------------------------")

# 初始化 END