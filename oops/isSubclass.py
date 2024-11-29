class B:
    def __init__(self):
        pass;

class A(B):
    def __init__(self):
        self.name="Class A"
        pass;


print(issubclass(A,B))

a=A();
print(hasattr(a,"name"));
setattr(a,"name","smit");
print(getattr(a,"name"));
delattr(a,"name");
print(hasattr(a,"name"));