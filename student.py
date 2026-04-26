from arrive_record import Arrive_Record

class Student:
    def __init__(self, name, grade, contact_num, old_school, first_arrive_date):
        self.name = name
        self.grade = grade
        self.contact_num = contact_num
        self.oldschool = old_school
        self.student_arrive_records = [Arrive_Record(first_arrive_date, "First arrival")]

    def add_stu_arrive_record(self, date, info):
        self.student_arrive_records.append(Arrive_Record(date, info))
    
    def print_stu_all_records(self):
        print(f"学生 {self.name} 的到达记录：")
        for record in self.student_arrive_records:
            record.print_arrive_record()

