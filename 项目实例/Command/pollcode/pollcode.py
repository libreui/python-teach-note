import os
import random
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
# 初始化数据
number = "1234567890"
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# 数字、大写字母、小写字母、特殊字符
allis = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
i = 0
randstr = []
fourth = []
fifth = []
randfir = ""
randsec = ""
randthr = ""
strone = ""
strtwo = ""
nextcard = ""
userput = ""
nres_letter = ""


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


while i < 9:
    mainmenu()
    choice = input("\033[1;32;40m请选择菜单：\033[0m")
    if len(choice) != 0:
        choice = int(input_validation(choice))
        if choice == 1:
            # 生成6位数字防伪编码 (213563型)
            scode1(choice)
        if choice == 0:
            i = 10
            print("\033[1;32;40m 欢迎再次使用！ \033[0m")
    else:
        print("\033[1;31;40m 非法输入，请重新输入!! \033[0m")
