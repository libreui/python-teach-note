import os
import re

filename = './students.txt'

def insert():
    """录入学生信息"""
    studentList = []
    mark = True
    while mark:
        id = input("请输入ID（如1001）：")
        if not id:
            break
        name = input("请输入名字：")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩："))
            python = int(input("请输入Python成绩："))
            c = int(input("请输入C语言成绩："))
        except:
            print("输入无效，不是整数类型，请重新输入")
            continue
        # 将录入的学生信息保存到字典中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'c': c}
        # 将学生信息添加到列表中
        studentList.append(student)
        inputMark = input("是否继续添加？（y/n）：")
        if inputMark == 'y':
            mark = True
        else:
            mark = False
    # 保存学生信息
    save(studentList)
    print("学生信息录入完毕！")


def search():
    """查找学生信息"""
    mark = True
    student_query = []
    while mark:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input("按ID查找请输入1，按姓名查找请输入2：")
            if mode == '1':
                id = input("请输入学生ID：")
            elif mode == '2':
                name = input("请输入学生姓名：")
            else:
                print("您的输入有误，请重新输入！")
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)  # 将找到的学生信息添加到列表中
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)  # 将找到的学生信息添加到列表中
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            inputMark = input("是否继续查询？（y/n）：")
            if inputMark == 'y':
                mark = True
            else:
                mark = False
        else:
            print("暂未保存数据信息...")
            return


def delete():
    """删除学生信息"""
    mark = True
    while mark:
        student_id = input("请输入要删除的学生ID：")
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            ifdel = False  # 是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            ifdel = True
                    if ifdel:
                        print(f"ID为{student_id}的学生信息已被删除")
                    else:
                        print(f"没有找到ID为{student_id}的学生信息")
            else:
                print("无学生信息")
                break
            show()
            inputMark = input("是否继续删除？（y/n）：")
            if inputMark == 'y':
                mark = True
            else:
                mark = False


def modify():
    """修改学生信息"""
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    studentid = input("请输入要修改的学生ID：")
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == studentid:
                print("找到学生信息，可以修改他的相关信息了！")
                while True:
                    try:
                        d['name'] = input("请输入姓名：")
                        d['english'] = input("请输入英语成绩：")
                        d['python'] = input("请输入Python成绩：")
                        d['c'] = input("请输入C语言成绩：")
                    except:
                        print("您的输入有误，请重新输入：")
                    else:
                        break
                wfile.write(str(d) + '\n')
                print("修改成功！")
            else:
                wfile.write(str(d) + '\n')
    mark = input("是否继续修改其他学生信息？（y/n）：")
    if mark == 'y':
        modify()

def sort():
    """对学生信息排序"""
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc = input("请选择（0升序；1降序）：")
    if asc_or_desc == '0':
        asc_or_desc_bool = False  # 升序
    elif asc_or_desc == '1':
        asc_or_desc_bool = True  # 降序
    else:
        print("您的输入有误，请重新输入！")
        sort()
    mode = input("请选择排序方式（1按英语成绩排序 2按Python成绩排序 3按C语言成绩排序 0按总成绩排序）：")
    if mode == '1':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['c']), reverse=asc_or_desc_bool)
    elif mode == '0':
        student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['c']), reverse=asc_or_desc_bool)
    else:
        print("您的输入有误，请重新输入！")
        sort()
    show_student(student_new)



def total():
    """统计学生信息"""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f"一共有{len(students)}名学生")
            else:
                print("没有学生信息")
    else:
        print("暂未保存数据信息...")


def show_student(lst):
    """显示学生信息"""
    if len(lst) == 0:
        print("没有学生信息")
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format("ID", "姓名", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))  # 显示表头
    # 定义内容显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 str(item.get('english')),
                                 str(item.get('python')),
                                 str(item.get('c')),
                                 int(item.get('english')) + int(item.get('python')) + int(item.get('c'))))  # 显示学生信息


def show():
    """显示所有学生信息"""
    student_new = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_new.append(eval(item))
            if student_new:
                show_student(student_new)
    else:
        print("没有学生信息")


def menu():
    """显示菜单"""
    print('''
    +----------------学生信息管理系统-----------------+
    |                                              |
    |   ================ 功能菜单 ===============   |
    |                                              |
    |   1 录入学生信息                               |
    |   2 查找学生信息                               |
    |   3 删除学生信息                               |
    |   4 修改学生信息                               |
    |   5 D_05_排序                                      |
    |   6 统计学生总人数                             |
    |   7 显示所有学生信息                            |
    |   0 退出系统                                  |
    |  =========================================== |
    |  说明：通过数字选择菜单                         |
    +----------------------------------------------+
    ''')


def save(student):
    """保存学生信息"""
    try:
        students_txt = open(filename, 'a', encoding='utf-8')
    except Exception as e:
        students_txt = open(filename, 'w', encoding='utf-8')
    for info in student:
        students_txt.write(str(info) + '\n')


def main():
    """主函数"""
    ctrl = True  # 是否退出系统
    while ctrl:
        menu()
        option = input("请选择：")
        option_str = re.sub(r'\D', "", option)
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:
                print('您已退出学生信息管理系统！')
                ctrl = False
            elif option_int == 1:
                insert()  # 录入学生信息
            elif option_int == 2:
                search()  # 查找学生信息
            elif option_int == 3:
                delete()  # 删除学生信息
            elif option_int == 4:
                modify()  # 修改学生信息
            elif option_int == 5:
                sort()  # D_05_排序
            elif option_int == 6:
                total()  # 统计学生总人数
            elif option_int == 7:
                show()  # 显示所有学生信息
        else:
            input("数字无效！请输入一个数字：")


if __name__ == "__main__":
    main()
