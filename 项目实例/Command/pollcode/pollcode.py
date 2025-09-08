import os
import random
import tkinter
from tkinter import messagebox
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()
# 初始化数据
number = "1234567890"
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# 数字、大写字母、小写字母、特殊字符
allis = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
i = 0
randstr = []
fourth = []
fifth = []


# randfir = ""
# randsec = ""
# randthr = ""
# strone = ""
# strtwo = ""
# nextcard = ""
# userput = ""
# nres_letter = ""


def mkdir(path):
    """创建文件夹"""
    isexists = os.path.exists(path)
    if not isexists:
        os.makedirs(path)


def openfile(filename):
    """打开文件"""
    f = open(filename)
    fllist = f.read()
    f.close()
    return fllist


def inputbox(showstr, showorder, length):
    """输入框"""
    instr = input(showstr)
    if len(instr) != 0:
        # 分成三种情况: 1: 数字，不限位 2: 字幕；3.数字且有位数有要求
        if showorder == 1:
            if instr.isdigit():
                if instr == '0':
                    print("\033[1;31;40m 输入为零，请重新输入!! \033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m 输入非法，请重新输入!! \033[0m")
                return "0"
        if showorder == 2:
            if instr.isalpha():
                if len(instr) != length:
                    print("\033[1;31;40m必须输入" + str(length) + "个字幕, 请重新输入!!\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m 输入非法，请重新输入!! \033[0m")
                return "0"
        if showorder == 3:
            if instr.isdigit():
                if len(instr) != length:
                    print("\033[1;31;40m必须输入" + str(length) + "个数字, 请重新输入!!\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m 输入非法，请重新输入!! \033[0m")
                return "0"
    else:
        print("\033[1;31;40m 输入为空，请重新输入!! \033[0m")
        return "0"


def wfile(sstr, sfile, typeis, smsg, datapath):
    """写入文件"""
    mkdir(datapath)
    datafile = datapath + "/" + sfile
    print(datafile)
    file = open(datafile, "w")
    wrlist = sstr
    pdata = ""
    wdata = ""
    for i in range(len(wrlist)):
        # 去掉字符中的括号
        wdata = str(wrlist[i].replace("[", "").replace("]", ""))
        # 去掉字符中的引号
        wdata = wdata.replace("'", "")
        file.write(str(wdata))
        pdata = pdata + wdata
    file.close()
    print("\033[1;32;40m" + pdata + "\033[0m")
    print(datafile)
    # 是否显示提示框，no不显示
    # if typeis != "no":
    #     tkinter.messagebox.showinfo("提示", smsg + str(len(randstr)) + "\n 防伪码文件存放位置：" + datafile)
    #     root.withdraw()


def input_validation(insel):
    if str.isdigit(insel):
        if insel == 0:
            print("\033[1;31;40m 输入非法，请重新输入!! \033[0m")
            return 0
        else:
            return insel
    else:
        print("\033[1;31;40m 输入非法，请重新输入!! \033[0m")
        return 0


def mainmenu():
    print("""\033[1;32;40m
    +--------------------- 防伪码生成系统 ---------------------+
    |                                                        |
    |   ================ 功能菜单 =================           |
    |                                                        |
    |   1 生成6位数字防伪编码 (213563型)                        |
    |   2 生成9位系列产品数字防伪编码 (879-335439型)             |
    |   3 生成25位混合产品序列号 (xxxx-xxxx-xxxx-xxxx-xxxx)     |
    |   4 生成含数据分析功能的防伪编码 (5A61M0583D2)             |
    |   5 智能批量生成带数据分析功能的防伪码                      |
    |   6 后续补加生成防伪码 (5A61M0583D2)                     |
    |   7 EAN-13条形码批量生成                                 |
    |   8 二维码批量输出                                       |
    |   9 企业粉丝防伪码抽奖                                    |
    |   0 退出系统                                            |
    +--------------------------------------------------------+
    |   说明：通过数字键来选择菜单                               |
    +--------------------------------------------------------+
    \033[0m""")


def scode1(schoice):
    """生成6位数字防伪编码 (213563型)"""
    incount = inputbox("\033[1;32;40m请输入需要生成的防伪码数量：\033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32;40m请输入需要生成的防伪码数量：\033[0m", 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        randfir = ""
        for i in range(6):
            randfir = randfir + random.choice(number)
        randfir = randfir + "\n"
        randstr.append(randfir)
    wfile(randstr, "scode" + str(schoice) + '.txt', "", "已生成6位防伪码共计：", "./codepath")


def scode2(schoice):
    """生成9位系列产品数字防伪编码 (879-335439型)"""
    ordstart = inputbox("\033[1;32;40m请输入系列产品的数字起始号：\033[0m", 3, 3)
    while int(ordstart) == 0:
        ordstart = inputbox("\033[1;32;40m请输入系列产品的数字起始号：\033[0m", 3, 3)
    ordcount = inputbox("\033[1;32;40m请输入产品系列的数量：\033[0m", 1, 0)
    while int(ordcount) == 0:
        ordcount = inputbox("\033[1;32;40m请输入产品系列的数量：\033[0m", 1, 0)
    incount = inputbox("\033[1;32;40m请输入每个系列产品防伪码的数量：\033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32;40m请输入每个系列产品防伪码的数量：\033[0m", 1, 0)
    randstr.clear()
    for m in range(int(ordcount)):
        for j in range(int(incount)):
            randfir = ""
            for _ in range(6):
                randfir = randfir + random.choice(number)
            randstr.append(str(int(ordstart) + m) + randfir + "\n")
    wfile(randstr, "scode" + str(schoice) + '.txt', "", "已生成9位系列产品防伪码共计：", "./codepath")


def scode3(schoice):
    incount = inputbox("\033[1;32;40m请输入25位混合产品序列号数量：\033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32;40m请输入25位混合产品序列号数量：\033[0m", 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        strone = ""
        for _ in range(25):
            strone = strone + random.choice(letter)
        strtwo = strone[:5] + "-" + strone[5:10] + "-" + strone[10:15] + "-" + strone[15:20] + "-" + strone[20:25]
        randstr.append(strtwo + "\n")
    wfile(randstr, "scode" + str(schoice) + '.txt', "", "已生成25位混合产品序列号共计：", "./codepath")


def ffcode(scount, typestr, ismessage, schoice):
    randstr.clear()
    # 按数量批量生成带有数据分析功能的防伪码
    for j in range(int(scount)):
        str_pro = typestr[0].upper()
        str_type = typestr[1].upper()
        str_class = typestr[2].upper()
        rand_fir = random.sample(number, 3)
        rand_sec = sorted(rand_fir)
        str_one = ""
        for _ in range(9):
            str_one = str_one + random.choice(number)
        # 将3个字母按rand_sec中数字的位置添加到数字防伪码中
        sim = str(str_one[0:int(rand_sec[0])] + str_pro +
                  str_one[int(rand_sec[0]):int(rand_sec[1])] + str_type +
                  str_one[int(rand_sec[1]):int(rand_sec[2])] + str_class +
                  str_one[int(rand_sec[2]):9])
        randstr.append(sim + "\n")
    wfile(randstr, "scode" + str(schoice) + '.txt', ismessage, "已生成" + str(scount) + "条带有数据分析功能的防伪码：",
          "./codepath")


def scode4(schoice):
    intype = inputbox("\033[1;32;40m 请输入数据分析编号(3位字母)： \033[0m", 2, 3)
    print(intype.isalpha(), len(intype))
    while not intype.isalpha() or len(intype) != 3:
        intype = inputbox("\033[1;32;40m 请输入数据分析编号(3位字母)： \033[0m", 2, 3)
    incount = inputbox("\033[1;32;40m 请输入要生成带数据分析功能的防伪码数量： \033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32;40m 请输入要生成带数据分析功能的防伪码数量： \033[0m", 1, 0)

    ffcode(incount, intype, "no", schoice)


def scode5(schoice):
    default_dir = r"./codeauto.mri"
    file_path = tkinter.filedialog.askopenfilename(initialdir=default_dir, title="请选择智能批处理文件",
                                                   filetypes=[("文本文件", "*.mri")])
    code_list = openfile(file_path)
    code_list = code_list.split("\n")
    # print(code_list)
    for code in code_list:
        code = code.split(",")
        ffcode(code[1], code[0], "no", code[0] + str(schoice))


def scode6(schoice):
    """补充生成带分析功能的防伪码"""
    default_dir = "./codeauto.mri"
    file_path = tkinter.filedialog.askopenfilename(initialdir=default_dir, title="请选择智能批处理文件",
                                                   filetypes=[("文本文件", "*.mri"), ("文本", "*.txt")])
    code_list = openfile(file_path)
    code_list = code_list.split("\n")
    first = code_list[0]
    remove_digits = first.maketrans("", "", number)
    res_letter = first.translate(remove_digits)
    res_letter = list(res_letter)
    # 去除地区、系列等信息
    str_pro = res_letter[0]
    str_type = res_letter[1]
    str_class = res_letter[2]

    # 去重
    card = set(code_list)
    tkinter.messagebox.showinfo("提示", "之前的访问吗共计：" + str(len(card)))
    root.withdraw()

    incount = inputbox("\033[1;32;40m 请输入要补充防伪码数量： \033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32;40m 请输入要补充防伪码数量： \033[0m", 1, 0)
    # 最大值按输入数量的两倍生成
    for j in range(int(incount) * 2):
        rand_fir = random.sample(number, 3)
        rand_sec = sorted(rand_fir)
        after_total = len(card)
        str_one = ""
        randstr.clear()
        for _ in range(9):
            str_one = str_one + random.choice(number)
        sim = str(str_one[0:int(rand_sec[0])] + str_pro +
                  str_one[int(rand_sec[0]):int(rand_sec[1])] + str_type +
                  str_one[int(rand_sec[1]):int(rand_sec[2])] + str_class +
                  str_one[int(rand_sec[2]):9])
        card.add(sim)
        if len(card) > after_total:
            randstr.append(sim + "\n")
            after_total = len(card)
        if len(randstr) == int(incount):
            print(len(randstr))
            break
    res_letter = "".join(res_letter)
    wfile(randstr,
          res_letter + "ncode" + str(schoice) + '.txt',
          res_letter,
          "已补充" + str(incount) + "条防伪码：", "./codepath")


while i < 9:
    mainmenu()
    choice = input("\033[1;32;40m请选择菜单：\033[0m")
    if len(choice) != 0:
        choice = int(input_validation(choice))
        if choice == 1:
            # 生成6位数字防伪编码 (213563型)
            scode1(choice)
        if choice == 2:
            # 生成9位系列产品数字防伪编码 (879-335439型)
            scode2(choice)
        if choice == 3:
            # 生成25位混合产品序列号 (            # 生成25位混合产品序列号 (xxxx-xxxx-xxxx-xxxx-xxxx)
            scode3(choice)
        if choice == 4:
            # 生成含数据分析功能的防伪编码 (            # 生成含数据分析功能的防伪编码 (5A61M0583D2)
            scode4(choice)
        if choice == 5:
            # 智能批量生成带数据分析功能的防伪码
            scode5(choice)
        if choice == 6:
            # 补充生成带分析功能的防伪码
            scode6(choice)

        if choice == 0:
            i = 10
            print("\033[1;32;40m 欢迎再次使用！ \033[0m")
    else:
        print("\033[1;31;40m 非法输入，请重新输入!! \033[0m")
