import os
import pickle
from date import Date
from student import Student

DATA_FILE = "students.pkl"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "rb") as f:
        return pickle.load(f)


def save_students(student_list):
    with open(DATA_FILE, "wb") as f:
        pickle.dump(student_list, f)


def find_student_by_name(student_list, name):
    for student in student_list:
        if student.name == name:
            return student
    return None


def main():
    STUDENT_LIST = load_students()
    print("欢迎来到招生记录系统！")

    while True:
        print("\n请选择操作:")
        print("1. 添加学生")
        print("2. 查看某已有学生到达记录")
        print("3. 添加学生到达记录")
        print("4. 删除学生")
        print("5. 查看所有学生")
        print("8. 退出系统")
        choice = input("请输入选项编号：")

        if choice == "1":
            name = input("请输入学生姓名：")
            grade = int(input("请输入学生此刻年级："))
            contact_num = input("请输入学生联系电话：")
            old_school = input("请输入学生原学校：")
            year = int(input("请输入第一次到达年份："))
            month = int(input("请输入第一次到达月份："))
            day = int(input("请输入第一次到达日期："))

            first_arrive_date = Date(year, month, day)
            student = Student(name, grade, contact_num, old_school, first_arrive_date)
            STUDENT_LIST.append(student)
            save_students(STUDENT_LIST)

            print(f"学生 {name} 已添加！")

        elif choice == "2":
            name = input("请输入要查看的学生姓名：")
            student = find_student_by_name(STUDENT_LIST, name)

            if student:
                student.print_stu_arrive_records()
            else:
                print("未找到该学生！")

        elif choice == "3":
            name = input("请输入要添加到达记录的学生姓名：")
            student = find_student_by_name(STUDENT_LIST, name)

            if student:
                year = int(input("请输入到达年份："))
                month = int(input("请输入到达月份："))
                day = int(input("请输入到达日期："))
                date = Date(year, month, day)
                info = input("请输入到达记录信息：")

                student.add_stu_arrive_record(date, info)
                save_students(STUDENT_LIST)

                print("到达记录已添加！")
            else:
                print("未找到该学生！")

        elif choice == "4":
            name = input("请输入要删除的学生姓名：")
            student = find_student_by_name(STUDENT_LIST, name)

            if student:
                STUDENT_LIST.remove(student)
                save_students(STUDENT_LIST)
                print("学生已删除！")
            else:
                print("未找到该学生！")

        elif choice == "5":
            if not STUDENT_LIST:
                print("没有学生记录！")
            else:
                for student in STUDENT_LIST:
                    print(f"学生姓名:{student.name}, 年级:{student.grade}, 联系电话:{student.contact_num}, 原学校:{student.oldschool}")

        elif choice == "8":
            save_students(STUDENT_LIST)
            print("感谢使用招生记录系统，再见！")
            break

        else:
            print("无效的选项，请重新选择！")


if __name__ == "__main__":
    main()
