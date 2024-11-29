class shape:
    def __init__(self):
        # self.area=0;
        pass
    
    def get_area(self):
        return 0;

class square(shape):
    def __init__(self, length):
        # super.init()
        self.length=length;
        self.area=length*length;
    def get_area(self):
        return self.area;

sq= square(4);
area=sq.get_area();
print(area);