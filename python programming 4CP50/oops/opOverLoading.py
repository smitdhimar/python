class student:
    student_count=0;
    def __init__(self):
        self.enrollment=None;
        self.name=None;
        self.setData();
        student.student_count+=1;

    def __str__(self):
        return "The student details is \n enrollment number:%d \n name: %s "%(self.enrollment,self.name);

    def setData(self):
        self.enrollment=int(input("Please enter your enrollment number "));
        self.name=input("please enter you name ");

A=student();
B=student();

print(A)
print(B)
print(student.student_count)