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


def search():
    pass


def delete():
    while True:
        student_num = int(input('place input delete student number:'))
        if student_num != '':
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as files:
                    student_old = files.readlines()
            else:
                student_old = []
            print(student_old)

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
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


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
