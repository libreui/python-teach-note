import random

## 初始化 BEGIN
# 游戏背景
__GAME_NAME__ = "笑傲江湖"
__GAME_VERSION__ = "2.0.0"
# 分割线宽度
__WIDTH__ = 30

# 最大MP
__MAX_MP__ = 100
# 最大HP
__MAX_HP__ = 2000

#TODO 升级的逻辑代码

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
eva = "eva"     # 闪避值键名
attack = "attack"   # 攻击力键名
skills = "skills"   # 技能键名

# 创建主角
my = {
    name: "张无忌",
    hp: __MAX_HP__,
    eva: 50,
    mp: __MAX_MP__,
    skills: {
        "普通攻击": {'attack': 10, 'mp': 0},
        "华山剑法": {'attack': 200, 'mp': 10},
        "独孤九剑": {'attack': 20, 'mp': 20},
        "葵花宝典": {'attack': 30, 'mp': 30}
    }
}

all_skills = my[skills].keys()
for i in range(len(all_skills)):
   skill_name =  all_skills[i]
   print(my[skills][skill_name])


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

    ### 每回合初始化操作 ###

    # 回复生命
    my[hp] += 10
    if my[hp] > __MAX_HP__:
        my[hp] = __MAX_HP__
    
    # 回复魔法值
    my[mp] += 5
    if my[mp] > __MAX_MP__:
        my[mp] = __MAX_MP__

    ### 每回合初始化操作 ###

    # 展示主角基本信息
    print("\n{0:-^30}".format(my[name]+'信息'))
    print("生命：{0}, 魔法：{1}".format(my[hp], my[mp]))
    print("-" * __WIDTH__)

    # 展示敌人信息
    print("\n{:-^30}".format('敌人信息'))
    for i in range(len(enemys)):
        enemy_hp = enemys[i][hp]
        # 如果敌人血量小于0判断
        if enemy_hp < 0:
            enemy_hp = 0
        print("{1}.[{0[name]}]: \n    生命:{2}, 攻击力:{0[attack]}".format(enemys[i], i, enemy_hp))
    print("-" * __WIDTH__)

    # 选择要攻击的敌人编号
    enemy_num = 0 # 储存选择的敌人编号
    enemy_num = int(input('请选择敌人编号：')) % len(enemys)
    
    # 展示技能
    all_skills = list(my[skills].keys())
    print("\n{:-^30}".format('选择技能'))
    for snum in range(len(all_skills)):
        skill_key = all_skills[snum] # 技能字典的键
        skill_attack = my[skills][skill_key][attack] #技能攻击力
        skill_mp = my[skills][skill_key][mp] # 技能消耗的mp
        print("%s.[%s] \n    攻击力 %s 消耗魔法 %s" % (snum, skill_key, skill_attack, skill_mp))
    print('-'*__WIDTH__)

    # 选择技能编号
    chice_snum = int(input("请选择技能：")) % len(all_skills)
    chice_skill = my[skills][all_skills[chice_snum]]

    # 判断主角剩余魔法值是否够本次技能施展
    if my[mp] < chice_skill[mp]:
        print("\n{:*^30}".format(' 错误 '))
        print("魔法值不足！")
        print('*'*__WIDTH__)
        continue

    # 用选择好的技能攻击选中的敌人
    attack_enemy = enemys[enemy_num] #被选择敌人的字典信息
    skill_attack = chice_skill[attack]
    attack_enemy[hp] -= skill_attack

    # 技能消耗MP值
    my[mp] -= chice_skill[mp]

    # 当前目标死亡标识
    dead = ""
    if attack_enemy[hp] <= 0:
        dead = "死亡"
    # 攻击旁白
    print("\n「你攻击了 {0}, -{1} 生命! {2}」\n".format(attack_enemy[name], skill_attack, dead))

    # 敌人回击(逐个回击)
    for enemy in enemys:
        # 如果敌人死亡则不攻击
        if enemy[hp] <= 0:
            continue
        # 回避率的判断
        if random.randint(1, 100) < my[eva]:
            print("\n「躲过了 {0} 的攻击」".format(enemy[name]))
        else:
            # 殴打主角
            my[hp] -= enemy[attack]

            # 旁白
            template = "\n「{0} 攻击了 {1}, -{2} 生命 {3}」"
            print(template.format(enemy[name], my[name], enemy[attack], my[hp]))

    # 判断游戏结束
    enemy_hp_sum = 0
    # 获取敌人hp总和
    for enemy in enemys:
        enemy_hp_sum += enemy[attack]
    
    if my[hp] <= 0 or enemy_hp_sum <= 0:
        break;

# 判断游戏胜利或者失败
if my[hp] > 0 and enemy_hp_sum <= 0:
    print("主角胜利")
else:
    print("敌人胜利")
