class Student ():

    def __init__(self, name, roll_no, standard, student_marks):
        self.name = name
        self.roll_no = roll_no
        self.standard = standard
        self.student_marks = student_marks


    def get_subject_marks(self,english,maths,physics,chemistry,biology):
        subjects={"English" : english , "Maths": maths, "Physics" : physics , "Chemistry":chemistry, "Biology":biology}
        return subjects

    def get_student_details( self, name, roll_no, standard, student_marks):
        student_details = {"name":name , "roll_no" :roll_no, "standard" : standard, "Student_Marks":student_marks} 
        return student_details

    def get_total_marks(self,student_marks):
        total_marks = []
        for value in student_marks.values():
            total_marks.append(value)
            for elements in total_marks:
                sum_total_marks = sum(total_marks)
         
        print("The total marks acquired by the Student is :  " )
        return sum_total_marks

    def get_average_marks (self, student_total_marks, student_marks):
        
        subject_count = 0
        for value in student_marks:
            subject_count += 1
            # print(subject_count)

            average_marks = student_total_marks / subject_count
        print("The Average mark of the Student is :")
        return average_marks

    def get_total_subjects(self, student_marks):
        subject_count = 0
        for value in student_marks:
            subject_count += 1
        return subject_count



    def check_pass_or_fail(self, student_total_marks):
        
        out_of_total = total_subjects * 100
        if (student_total_marks /out_of_total) * 100  > 50 :
            print("The Student has passed the Examination ")
        else:
            print(" The Student has failed the Examination ")



s1 = Student( "Naruto", 7, 12,0)
student_marks = s1.get_subject_marks(55,98,75,89,96)
# print(student_marks)
print(" The Student's Details are : ")
student_details = s1.get_student_details("Naruto", 7, 12 ,student_marks)
print(student_details)

total_subjects = s1.get_total_subjects(student_marks)

print(" Condition ---> If student acquires 50% ... or more he passes the examination ...and if He scores less than that he fails.")

student_total_marks = s1.get_total_marks(student_marks)
print(student_total_marks)

student_average_marks = s1.get_average_marks(student_total_marks, student_marks)
print(student_average_marks)
 
pass_or_fail = s1.check_pass_or_fail(student_total_marks)
print(pass_or_fail)







