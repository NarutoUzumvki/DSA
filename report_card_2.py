class Student:

    PASS_PERCENT = 33  # Class_attribute
    # counter = 0

    def __init__(self, roll_no, name, subjects):
        self.name = name
        self.roll_no = roll_no
        self.subjects = subjects
        self.total_marks = 0
        self.average = 0
        self.status = None
        # Student.counter += 1  


    def calculate_total_marks (self):
        total_marks = 0

        for marks in self.subjects.values():
            total_marks = total_marks +  marks
        self.total_marks = total_marks
        return self.total_marks

    def calculate_avg(self):
        average = self.total_marks / len(self.subjects)
        self.average = average
        return self.average

    def pass_or_fail(self):
        if self.average >= Student.PASS_PERCENT:
            self.status = "Pass"
        else:
            self.status = "Fail"
        return self.status

         

    def generate_result(self):
        output = " \n The Calculated Total Marks of the Student is --> {} .\n The Average Marks of the Student is --> {} .\n The Pass or Fail Status of the Student is --> {} ." 
        ttl_marks = self.calculate_total_marks()
        avg_marks = self.calculate_avg()
        p_f_status = self.pass_or_fail()
        print(output.format(ttl_marks, avg_marks, p_f_status))
        return "Final-Report"



    def __str__(self):

        return  str(self.roll_no) + " " + str(self.name) + " " + str(self.subjects)

students_collection = {"1":{"name":"vijay", "subjects":{"english":95, "maths":80, "physics":87}},
                       "2":{"name":"uzumaki", "subjects":{"english":85, "maths":87, "physics":83}},
                       "3":{"name":"luffy", "subjects":{"english":92, "maths":85, "physics":80}}}


# students_collection = {"1":{ "subjects":{"english":95, "maths":80, "physics":87}},
#                        "2":{  "subjects":{"english":85, "maths":87, "physics":83}},
#                        "3":{  "subjects":{"english":92, "maths":85, "physics":80}}}


students = []
for roll_no, student in students_collection.items() :
    student_object = Student(  roll_no=roll_no, name=student["name"], subjects=student["subjects"])
    students.append(student_object)
    # print(student_object)
    # print(Student.counter)  

# for student in students:
#     print(student)
#     print(Student.counter)

# print([student for student in students])

# s1 = students[0]
# print(s1)

s1 = students[1]
# stud = student_object.generate_result()
stud = s1.generate_result()
print(stud)

 



 
                  