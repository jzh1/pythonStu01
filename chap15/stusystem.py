# -*- coding:utf-8 -*-
# @Time : 2021/12/29 9:31 PM
# @Author: jonas.jiang
# @File : stusystem.py
import os

file_name = 'student.txt'


def main():
    while True:
        menu()
        chose = int(input("请选择功能: "))
        if chose in [0, 1, 2, 3, 4, 5, 6, 7]:
            if chose == 0:
                answer = input("确定要退出系统吗 y/n ？")
                if answer == 'y' or answer == 'Y':
                    print('thanks !!!! ')
                    break
                else:
                    continue
            elif chose == 1:
                insert()
            elif chose == 2:
                search()
            elif chose == 3:
                delete()
            elif chose == 4:
                modify()
            elif chose == 5:
                sort()
            elif chose == 6:
                total()
            elif chose == 7:
                show()


def insert():
    student_list = []
    while True:
        id = int(input("place input id:"))
        if not id:
            break
        name = str(input("place input name:"))
        if not name:
            break

        try:
            english = int(input('place input english:'))
            python = int(input('place input python:'))
            java = int(input('place input java:'))
        except:
            print('input error ,place reinput')
            continue

        # 信息保存字典
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('continue add y/n?')
        if answer == 'y' or answer == 'Y':
            print('--------------- continue add   ----------------')
            continue
        else:
            print('--------------- input end   ----------------')
            break
    # 保存信息
    save(student_list)


def save(lst):
    try:
        stu_txt = open(file_name, 'a', encoding='utf-8')
    except:
        stu_txt = open(file_name, 'w', encoding='utf-8')

    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def show_student(lst):
    if len(lst) == 0:
        print('student is null ')
        return

    print(lst)


def search():
    while True:
        student_lst = []
        student_no = int(input('place input student num:'))
        if student_no != '':
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as files:
                    student_old = files.readlines()
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] == student_no:
                            student_lst.append(d)
            else:
                print('student data is null')
                break
        show_student(student_lst)
        student_lst.clear()
        answer = input('place continue search y/n?')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break


def delete():
    while True:
        student_num = int(input('place input delete student number:'))
        if student_num != '':
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as files:
                    student_old = files.readlines()
            else:
                student_old = []

            flag = False
            if student_old:
                with open(file_name, 'w', encoding='utf-8') as wfile:
                    # d = {}
                    for item in student_old:
                        # 字符串转换为字典
                        d = dict(eval(item))
                        if d['id'] != student_num:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True

                    if flag:
                        print(f'id is {student_num} is delete!')
                    else:
                        print(f'student id  {student_num}  is empty !')
            # 删除之后重新显示学生信息
            show()
            answer = input('is continue delete y/n ?')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('student is not,place input num')
            continue


def modify():
    show()
    while True:
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as files:
                student_old = files.readlines()
        else:
            student_old = []

        student_num = int(input('place input update student number:'))
        if student_old:
            with open(file_name, 'w', encoding='utf-8') as wfile:
                for item in student_old:
                    # 字符串转换为字典
                    d = dict(eval(item))
                    if d['id'] == student_num:
                        while True:
                            try:
                                d['english'] = int(input('place input english:'))
                                d['python'] = int(input('place input python:'))
                                d['java'] = int(input('place input java:'))
                                break
                            except:
                                print('input error place reinput!')
                        wfile.write(str(d) + '\n')

                        print('update success ')
                    else:
                        wfile.write(str(d) + '\n')
        else:
            print(f'{student_num} is not exit,place reinput!')

        answer = input('is continue update y/n ?')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break


def sort():
    student_lst = []
    sort_type = int(input('place chose sort 1/0 ?'))
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as files:
            student_old = files.readlines()
            for item in student_old:
                d = dict(eval(item))
                student_lst.append(d)

    student_lst.sort(key=lambda x: int(x['java']), reverse=True)
    print(student_lst)


def total():
    total_num = 0
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as files:
            student_old = files.readlines()
            total_num = len(student_old)
    print('total:' + str(total_num))


def show():
    student_old = []
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as files:
            student_old = files.readlines()

    show_student(student_old)


def menu():
    print('===========================  学生管理系统  ===========================')
    print('---------------------------    功能菜单   ---------------------------')
    print('\t\t\t\t\t\t 1 录入学生信息')
    print('\t\t\t\t\t\t 2 查找学生信息')
    print('\t\t\t\t\t\t 3 删除学生信息')
    print('\t\t\t\t\t\t 4 修改学生信息')
    print('\t\t\t\t\t\t 5 排序学生信息')
    print('\t\t\t\t\t\t 6 统计学生信息')
    print('\t\t\t\t\t\t 7 显示所有学生信息')
    print('\t\t\t\t\t\t 0 退出系统')
    print('---------------------------    功能菜单   ---------------------------')


if __name__ == '__main__':
    main()
