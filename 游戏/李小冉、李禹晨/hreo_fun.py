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
__EXP_LIST__ = [0, 100, 200, 300]

import sys

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
    level: 0,  # 等级
    skills: [
        {name: "普通攻击", attack: 300, mp: 0, aoe: False},
        {name: "华山剑法", attack: 200, mp: 10, aoe: False},
        {name: "独孤九剑", attack: 20, mp: 20, aoe: False},
        {name: "葵花宝典", attack: 3000, mp: 30, aoe: True}
    ]
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
player_win = False


# 游戏逻辑
def showCaption():
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


def show_player_info():
    """显示玩家信息"""
    print(player[name])
    print(f"生命: {player[hp]}/{player[maxHp]}, "
          f"内力: {player[mp]}/{player[maxMp]}")
    print(f"经验值:{player[exp]}")
    pass


def player_turn():
    """玩家回合"""
    print(f"{'玩家回合':-^37}")
    # 显示玩家信息
    show_player_info()
    print(f"-" * __WIDTH__)


def add_exp(enemy):
    """增加经验值"""
    if enemy[hp] <= 0:
        player[exp] += enemy[exp]
        print(f"{player[name]} +{enemy[exp]} 经验值")

    level_up()


def level_up():
    """升级"""
    _level = -1
    # 根据经验值列表来升级
    for _exp in __EXP_LIST__:
        if player[exp] >= _exp:
            _level += 1
        else:
            break

    if player[level] < _level:
        print(f"{player[name]} 升级到了 {_level} 级")
        player[level] = _level


def repeat_attack_player():
    """敌人攻击玩家"""
    for enemy in enemies:
        # 判断敌人是否预备攻击能力：1.血量
        if enemy[hp] <= 0:
            continue
        # 减去玩家血量
        player[hp] -= enemy[attack]
        print(f"['{enemy[name]}' 攻击了 '{player[name]}', -{enemy[attack]} 生命 {player[hp]}]")


def enemies_turn():
    """敌人回合"""
    # TODO 回击玩家
    repeat_attack_player()


def check_winner():
    """玩家是否胜利"""
    return player_win


def show_enemies_info():
    print(f"{'敌人信息':-^37}")
    for i, enemy in enumerate(enemies):
        print(f"{i}.[{enemy[name]}]")
        print(f"\t生命:{enemy[hp]}, 攻击力:{enemy[attack]}")
    print(f"-" * __WIDTH__)


def get_enemy_id() -> int:
    eid = input("选择敌人编号:")

    while True:
        if not eid.isdigit():
            print("输入错误，请输入整数！")
            eid = input("选择敌人编号:")
        elif abs(int(eid)) > len(enemies):
            print("没有此敌人！")
            eid = input("选择敌人编号:")
        else:
            break

    return abs(int(eid))


def get_skill_id():
    skill_id = input("选择技能编号:")
    while True:
        if not skill_id.isdigit():
            print("输入错误，请输入整数！")
            skill_id = input("选择技能编号:")
            continue
        elif int(skill_id) > len(player['skills']):
            print("没有此技能！")
            skill_id = input("选择技能编号:")
        else:
            break
    return int(skill_id)


def show_skills_info():
    print(f"{'选择技能':-^37}")
    for i, skill in enumerate(player[skills]):
        print(f"{i}.[{skill[name]}]")
        print(f"\t攻击力:{get_attack_value(skill)}, 消耗内力:{skill[mp]}, AOE:{skill[aoe]}")
    print(f"-" * __WIDTH__)


def get_attack_value(skill):
    """获取攻击力的值"""
    return skill[attack] * (player[level] + 1)


def attack_enemy(enemy_id, skill_id):
    """攻击敌人"""
    enemy = enemies[enemy_id]
    skill = player[skills][skill_id]
    enemy[hp] -= get_attack_value(skill)
    print(f"[你攻击了 '{enemy[name]}', -{skill[attack]}生命！]")

    # 增加经验
    add_exp(enemy)


def main():
    """程序的主入口"""
    # 显示标题
    showCaption()

    while True:  # 游戏的主循环
        player_turn()  # 玩家回合

        # 问，是否要过回合或者退出游戏
        # y: 跳过 n: 不跳过 q: 退出
        command = input("是否跳过回合(y/[n]/q):")
        if command == 'y':
            continue
        elif command == 'q':
            break

        # 显示敌人信息
        show_enemies_info()

        # 选择敌人编号
        enemy_id = get_enemy_id()
        # 展示技能信息
        show_skills_info()
        # 选择技能编号
        skill_id = get_skill_id()

        # 攻击敌人
        attack_enemy(enemy_id, skill_id)

        # TODO 回击

        enemies_turn()  # 敌人回合

        # 判断游戏结果
        if check_winner():
            break

        # 测试用
        break


if __name__ == "__main__":
    main()
