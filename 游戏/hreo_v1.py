'''
Author: Libre Gu 
Date: 2023-06-03 08:36:49
LastEditors: Libre Gu 
LastEditTime: 2023-06-03 09:07:35
FilePath: /PythonJupyter/hreo_v1.py
Description: 
Copyright (c) 2023 by Libre, All Rights Reserved. 
'''
## 初始化 BEGIN
# 游戏背景
__GAME_NAME__ = "笑傲江湖"
__GAME_VERSION__ = "1.0.0"
# 分割线宽度
__WIDTH__ = 30

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
      
# 定义字典键名
name = "name"   # 名字键名
hp = "hp"       # 血量键名       
mp = "mp"       # 魔法值键名
attack = "attack"   # 攻击力键名
skills = "skills"   # 技能键名

# 创建主角
my = {
    name: "张无忌",
    hp: 2000,
    mp: 100,
    attack: 10,
    skills: {
        "华山剑法": {'attack': 10, 'mp': 10},
        "独孤九剑": {'attack': 20, 'mp': 20},
        "葵花宝典": {'attack': 30, 'mp': 30}
    }
}

# 测试主角
# print('---测试主角--------------------------')
# print("名字：%s\t" % my[name])
# print("血量：%d\t" % my[hp])
# print("魔法: %d\t" % my[mp])
# print("攻击力：%d \t" % my[attack])
# print("技能：")
# for k,v in my[skills].items():
#     print("\t%s：%s" % (k, v))
# print("-----------------------------------")


# 定义NPC敌人

# NPC列表
enemys = [
    {name: "东方不败",hp: 100,attack: 10},
    {name: "岳不群",hp: 100,attack: 20},
    {name: "任我行",hp: 100,attack: 30}
]

# 测试代码
# print("---测试敌人-------------------------")
# for i in range(len(enemys)):
#     print("{1}.{0[name]}: 生命:{0[hp]}, 攻击力:{0[attack]}".format(enemys[i], i))
# print("----------------------------------")

## 初始化 END

# 开始游戏回合
# 游戏结束的条件：我方生命0或者敌人生命之和为0
while True:
    ## 每一个回合代码

    # 展示主角基本信息
    print("{0:-^30}".format(my[name]+'信息'))
    print("生命：{0}, 魔法：{1}".format(my[hp], my[mp]))
    print("-" * __WIDTH__)

    # 展示敌人信息
    print("{:-^30}".format('敌人信息'))
    for i in range(len(enemys)):
        print("{1}.{0[name]}: 生命:{0[hp]}, 攻击力:{0[attack]}".format(enemys[i], i))
    print("-" * __WIDTH__)

    # 选择要攻击的敌人编号
    enemy_num = 0 # 储存选择的敌人编号
    enemy_num = int(input('请选择敌人编号：')) % len(enemys)
    print(enemy_num)
    

    #TODO 展示技能

    #TODO 选择技能

    #TODO 用选择好的技能攻击选中的敌人

    #TODO 敌人回击

    # 判断游戏结束
    enemy_hp_sum = 0
    # 获取敌人hp总和
    for enemy in enemys:
        enemy_hp_sum += enemy[hp]
    
    if my[hp] <= 0 or enemy_hp_sum <= 0:
        break;

# 判断游戏胜利或者失败
if my[hp] > 0 and enemy_hp_sum <= 0:
    print("主角胜利")
else:
    print("敌人胜利")
