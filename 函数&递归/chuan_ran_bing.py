# 当天患者 = 前一天患者 + 新进入患者 - 治愈患者
def chuan_ran_bing(n):
    qian_fu_zhe = [0] * (n + 5)
    chuan_ran_zhe = [0] * (n + 5)
    quan_bu = [0] * (n + 5)

    # 赋值
    qian_fu_zhe[1] = 1
    quan_bu[1] = 1

    # 计算
    for day in range(2, n + 1):
        # 当日潜伏期患者来源？
        if day > 5:
            chuan_ran_zhe[day] = qian_fu_zhe[day - 5]

        # 新患者来源
        new_qian_fu_zhe =sum(chuan_ran_zhe[max(1, day - 4):day + 1]) * 3
        qian_fu_zhe[day] = new_qian_fu_zhe
        # 治愈者人数
        zhi_yu_zhe = chuan_ran_zhe[day - 5] if day > 10 else 0
        # 当日患者数
        quan_bu[day] = quan_bu[day-1] + new_qian_fu_zhe - zhi_yu_zhe
    return quan_bu


print(chuan_ran_bing(11))
