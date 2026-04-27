import time
import random


def printr(content):
    """逐字打印"""
    for c in content:
        print(c, end='', flush=True)
        time.sleep(0.1)

    # 游戏名字


__GAME_NAME__ = "笑傲江湖"
# 游戏版本
__VERSION__ = "1.0.0"

# 屏幕的宽度
__WIDTH__ = 40

# 主角最大生命值
__MAX_HP__ = 2000
# 主角最大内力值
__MAX_MP__ = 100
# 经验值列表
__EXP_LIST__ = [100, 200, 300]

# 键名
name = "name"
hp = "hp"
maxHp = "max_hp"
mp = "mp"
maxMp = "max_mp"
exp = "exp"
skills = "skills"
attack = "attack"
aoe = "aoe"
dex = "dex"
level = "level"

# 欢迎界面
print("=" * __WIDTH__)
print(f"{__GAME_NAME__} ver {__VERSION__}")
print("=" * __WIDTH__)

# 欢迎词
print("\n游戏背景:")
print("""
欢迎来到江湖，你是江湖中的一位侠客，
听说有一把传说中的屠龙宝刀藏在某个地方，
你决定踏上寻找屠龙宝刀的道路
......
""")

# 创建主角
# 生命、内力、经验、技能
player = {
    name: "张无忌",
    hp: __MAX_HP__,  # 当前生命值
    maxHp: __MAX_HP__,  # 最大生命值
    mp: __MAX_MP__,  # 当前内力值
    maxMp: __MAX_MP__,  # 最大内力值
    dex: 30,
    exp: 0,  # 经验值
    level: 1, # 等级
    skills: {
        "普通攻击": {attack: 300, mp: 0, aoe: False},
        "华山剑法": {attack: 200, mp: 10, aoe: False},
        "独孤九剑": {attack: 20, mp: 20, aoe: False},
        "葵花宝典": {attack: 3000, mp: 30, aoe: True}
    }
}

# 创建敌人
enemies = [
    {name: "东方不败", hp: 100, attack: 10, exp: 100},
    {name: "岳不群", hp: 100, attack: 20, exp: 100},
    {name: "林平之", hp: 200, attack: 30, exp: 200},
    {name: "左冷禅", hp: 200, attack: 30, exp: 300},
    {name: "任我行", hp: 5000, attack: 30, exp: 500}
]

# 保存玩家是否胜利
winner = False

# 开始游戏
while True:
    # 回复内力与生命
    player[hp] += 10
    player[mp] += 10
    if player[hp] > __MAX_HP__:
        player[hp] = __MAX_HP__
    if player[mp] > __MAX_MP__:
        player[mp] = __MAX_MP__

    # 主角回合
    title = "玩家回合"  # 标题
    print(f"{title:-^40}")
    print(player[name])
    print(f"生命：{player[hp]}/{player[maxHp]}, 内力：{player[mp]}/{player[maxMp]}")
    print(f"经验值：{player[exp]}")
    print("-" * __WIDTH__)

    # 是否跳过回合
    char = input("是否跳过回合(y/n/q):")
    if char == 'q':
        break
    elif char == 'y':
        # TODO 只接受敌人攻击
        continue

    # 展示敌人信息
    title = "敌人信息"
    print(f"{title:-^40}")
    for i in range(len(enemies)):
        enemy = enemies[i]  # enemy:
        print(f"{i}.[{enemy[name]}]:")
        print(f"\t生命:{enemy[hp]}, 攻击力:{enemy[attack]}")
    print("-" * __WIDTH__)

    # 选择敌人
    n = int(input("请选择敌人编号："))
    enemy = enemies[n]  # 保存选择的敌人信息

    # 展示技能
    title = "技能信息"
    print(f"{title:-^40}")
    skillNames = list(player[skills].keys())
    for i in range(len(skillNames)):
        skn = skillNames[i]  # 技能名称
        skill = player[skills][skn]
        print(f"{i}.[{skn}]")
        print(f"\t攻击力:{skill[attack]}, 消耗内力:{skill[mp]}, AOE:{skill[aoe]}")
    print("-" * __WIDTH__)

    n = int(input("选择技能编号:"))
    # 保存选择的技能信息
    skill = player[skills][skillNames[n]]

    # 内力是否足够
    if player[mp] < skill[mp]:
        print("提示：内力不足")
        continue

    # 攻击敌人，减少敌人血量, #经验有Bug
    if skill[aoe]:
        # 群体攻击
        for e in enemies:
            e[hp] -= skill[attack]
            # 攻击结果提示
            print(f"[你攻击了 '{e[name]}', -{skill[attack]}生命！]")
            if e[hp] <= 0:
                e[hp] = 0
                # 增长经验值
                player[exp] += e[exp]
                print(f"{player[name]} +{e[exp]} 经验值")
    else:
        # 单体攻击
        enemy[hp] -= skill[attack]
        # 攻击结果提示
        print(f"\n[你攻击了 '{enemy[name]}', -{skill[attack]}生命！]")
        # 表示敌人死亡
        if enemy[hp] <= 0:
            enemy[hp] = 0
            # 增长经验值
            player[exp] += enemy[exp]
            print(f"{player[name]} +{enemy[exp]} 经验值")


    #  减少内力
    player[mp] -= skill[mp]


    # 所有敌人回击
    for e in enemies:
        # 判断敌人是否预备攻击能力：1.血量
        if e[hp] <= 0:
            continue
        # 是否躲过攻击
        if random.randint(1, 100) <= 30:
            print(f"{player[name]} 躲过了 {e[name]} 的本次攻击")
        else:
            player[hp] -= e[attack]
            print(f"['{e[name]}' 攻击力 '{player[name]}', -{e[attack]} 生命 {player[hp]}]")

    # 玩家血量小于等于零 == 玩家失败 winner=false 跳出循环
    if player[hp] <= 0:
        winner = False
        break
    # 所有敌人血量小于等于零 == 玩家胜利 winner=true 跳出循环
    enemy_hp_sum = 0
    for e in enemies:
        # 直合计还有生命值的敌人血量
        if e[hp] > 0:
            enemy_hp_sum += e[hp]
    if enemy_hp_sum <= 0:
        winner = True
        break
# 判定玩家胜利还是失败
if winner:
    print("胜利")
else:
    print("Game Over")
