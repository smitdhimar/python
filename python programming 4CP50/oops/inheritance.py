class vehicle:
    def __init___(self):
        self.reg_no=None;
        self.model=None;
        self.color=None;
    def setdata(self):
        self.reg_no=int(input("enter reg_no :"));
        self.model=input("enter model ");
        self.color=input("enter color ");
    def getdata(self):
        print("reg no: %d\nmodel: %s\ncolor: %s\n"%(self.reg_no,self.model,self.color));

class passengerVehical(vehicle):
    def __init__(self):
        self.maxi=None;
        self.setdata();
    def setdata(self):
        self.maxi=int(input("enter max capacity: "));
        super().setdata()
    def getdata(self):
        print("maximum capacity: %d"%(self.maxi));
        super().getdata()

class commercialVehical(vehicle):
    def __init__(self):
        self.setdata();
    def setdata(self):
        super().setdata()
    def getdata(self):
        super().getdata()

pv=passengerVehical();
cv=commercialVehical();

pv.getdata();
cv.getdata();