class student:
    def __init__(self):
        self.rollno=7;
        self.name="asd";
        self.age=78;
        self.marks=45;
    def __eq__(self,other):
        if(self.marks==other.marks):
            print("%s and %s are having same marks %d"%(self.name,other.name,self.marks));
            return 1;
        return 0;

A=student();
B=student();
A==B