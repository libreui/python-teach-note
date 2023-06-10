'''
Author: Libre Gu 
Date: 2023-05-27 20:41:16
LastEditors: Libre Gu 
LastEditTime: 2023-05-27 20:45:30
FilePath: /PythonJupyter/武侠游戏.py
Description: 
Copyright (c) 2023 by Libre, All Rights Reserved. 
'''
import random

# 游戏背景
print("欢迎来到江湖，你是江湖中的一位侠客，听说有一把传说中的屠龙宝刀藏在某个地方，你决定踏上寻找屠龙宝刀的道路。")

# 定义主角
player = {
    "name": "令狐冲",
    "hp": 100,
    "attack": 10,
    "dodge": 30,
    "skills": {
        "华山剑法": 10,
        "独孤九剑": 20,
        "葵花宝典": 30
    }
}

# 定义敌人
enemies = [
    {
        "name": "岳不群",
        "hp": 50,
        "attack": 8,
        "dodge": 30
    },
    {
        "name": "林平之",
        "hp": 60,
        "attack": 10,
        "dodge": 30
    },
    {
        "name": "任我行",
        "hp": 70,
        "attack": 12,
        "dodge": 30
    }
]

# 游戏主循环
while len(enemies) > 0 and player["hp"] > 0:
    # 打印当前场景
    print("\n当前场景：")
    print("你面前有以下敌人：")
    for i, enemy in enumerate(enemies):
        print(i+1, enemy["name"], "（生命值：", enemy["hp"], "，攻击力：", enemy["attack"], "）")
    print("你的生命值：", player["hp"])
    
    # 玩家回合
    print("\n轮到你了！请选择你的行动：")
    print("1. 华山剑法")
    print("2. 独孤九剑")
    print("3. 葵花宝典")
    choice = input()
    if choice == "1":
        # 华山剑法
        print("你发动了华山剑法！")
        target = random.choice(enemies)
        damage = player["skills"]["华山剑法"] - target["attack"]
        if damage < 0:
            damage = 0
        target["hp"] -= damage
        print("你对", target["name"], "造成了", damage, "点伤害！")
    elif choice == "2":
        # 独孤九剑
        print("你发动了独孤九剑！")
        target = random.choice(enemies)
        damage = player["skills"]["独孤九剑"] - target["attack"]
        if damage < 0:
            damage = 0
        target["hp"] -= damage
        print("你对", target["name"], "造成了", damage, "点伤害！")
    elif choice == "3":
        # 葵花宝典
        print("你发动了葵花宝典！")
        target = random.choice(enemies)
        damage = player["skills"]["葵花宝典"] - target["attack"]
        if damage < 0:
            damage = 0
        target["hp"] -= damage
        print("你对", target["name"], "造成了", damage, "点伤害！")

    # 敌人回合
    print("\n敌人的回合：")
    for enemy in enemies:
        if random.randint(1, 100) <= enemy["dodge"]:
            print(enemy["name"], "闪避了你的攻击！")
        else:
            damage = enemy["attack"]
            player["hp"] -= damage
            print(enemy["name"], "对你造成了", damage, "点伤害！")
            if player["hp"] <= 0:
                break

    # 移除已被击败的敌人
    enemies = [enemy for enemy in enemies if enemy["hp"] > 0]

# 判断胜负
print("\n游戏结束，根据主角的生命值判断胜负：")
if player["hp"] <= 0:
    print("你被击败了，江湖再无你的传说。")
else:
    print("恭喜你击败了所有敌人，你成功地找到了屠龙宝刀，成为了江湖中的传奇人物！")

